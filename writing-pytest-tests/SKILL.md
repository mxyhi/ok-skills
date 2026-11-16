---
name: writing-pytest-tests
description: Write or extend pytest tests for existing Python code. Use when the user asks to add tests, raise coverage, write a regression test, or fix or clean up a pytest suite (fixtures, parametrize, mocking, flaky tests) in a Python project. For test-first feature work use tdd; for finding a bug's cause use diagnosing-bugs.
compatibility: Requires Python and pytest (examples checked with pytest 9.2). pytest-cov and numpy are optional and only needed for the coverage and array sections.
---

# Writing pytest Tests

Use this skill to add tests to Python code that already exists, in the project's own pytest style. It covers the pytest mechanics: layout, fixtures, parametrize, mocking, numbers, flakiness, and running.

**Boundary with other skills**

- Building a feature or fix test-first (red → green, agreeing seams up front): use `tdd`. Come back here for the pytest details.
- A bug whose cause is unknown: use `diagnosing-bugs` to build the loop and find the cause. Use this skill to turn the minimised repro into a regression test.
- This skill does not change production code. If a test exposes a likely bug, stop and report it (or pin it with a strict `xfail`, below) instead of quietly "fixing" the code to make tests pass.

## 1. Discover the project first

Before writing a test, find out what already exists:

- Config: `pyproject.toml` (`[tool.pytest]` or `[tool.pytest.ini_options]`), `pytest.toml`, `pytest.ini`, `tox.ini`, `setup.cfg`. Note `testpaths`, `addopts`, `markers`, `strict*` options and the import mode.
- `conftest.py` files: shared fixtures live here. Reuse them before writing new ones.
- Plugins in use (`pytest-cov`, `pytest-mock`, `pytest-asyncio`, `hypothesis`, `pytest-xdist`): check the dev dependencies. Don't add a new plugin when the existing ones or core pytest can do the job.
- Existing tests: copy their layout, naming, fixture style and assert style. Consistency beats your own preferences.
- How tests are run: `Makefile`, `tox.ini`, `noxfile.py`, CI config. Run the suite once before changing anything so you know the baseline (and which tests already fail).

## 2. Layout and naming

- Default discovery: files named `test_*.py` or `*_test.py`; functions whose names start with `test`; and `test`-prefixed methods inside `Test`-prefixed classes that have no `__init__`.
- Mirror the source tree: `src/pkg/pricing.py` → `tests/test_pricing.py`. Keep one behaviour per test and name it after that behaviour: `test_discount_above_100_percent_is_rejected`, not `test_discount_2`.
- Test the public interface. Don't import private helpers (`_name`) or assert on internal state when the return value or a public side effect shows the behaviour.
- Expected values come from an independent source (a worked example, the spec, a known-good literal), never from re-running the same formula the code uses.
- For new projects the pytest docs recommend `--import-mode=importlib`. In an existing project, keep whatever it already uses.

## 3. Asserts

Use plain `assert`; pytest rewrites it to show both sides on failure. Compare whole values when you can, so a failure shows the full diff:

```python
from shop.pricing import apply_discount, cart_total

def test_cart_total_sums_line_items():
    assert cart_total([("apple", 2, 0.5), ("pear", 1, 1.25)]) == 2.25

def test_discount_rounds_to_cents():
    assert apply_discount(19.99, 15) == 16.99
```

Exceptions and warnings:

```python
import pytest
from shop.pricing import apply_discount, legacy_price

def test_discount_over_100_is_rejected():
    with pytest.raises(ValueError, match=r"between 0 and 100") as excinfo:
        apply_discount(10.0, 150)
    assert excinfo.value.args[0].startswith("percent")

def test_legacy_price_warns():
    with pytest.warns(DeprecationWarning, match="use cart_total"):
        legacy_price(3.0)
```

`match` is a regex checked with `re.search`, so escape special characters (`re.escape(msg)`). Keep only the call that should raise inside the `with` block.

## 4. Fixtures

```python
import json
import pytest
from shop.store import Store

@pytest.fixture
def store(tmp_path):
    db = tmp_path / "store.json"
    db.write_text(json.dumps({"apple": 3}))
    s = Store(db)
    yield s          # test runs here
    s.close()        # teardown runs even if the test fails

def test_restock_adds_quantity(store):
    store.restock("apple", 2)
    assert store.quantity("apple") == 5
```

- Default scope is `function` (fresh per test). Use `module` or `session` only for expensive, read-only setup; shared mutable state is the classic cause of order-dependent tests.
- Put fixtures used by several files in the nearest `conftest.py`; no import needed.
- Built-ins worth knowing: `tmp_path` (unique `pathlib.Path` per test), `monkeypatch` (env vars, attributes, cwd; undone after the test), `capsys` (stdout/stderr), `caplog` (logging), `request` (params, markers, test info).
- Factory fixtures (a fixture that returns a function) beat many near-duplicate fixtures.

```python
import logging

def test_report_prints_summary(capsys):
    print("3 items")
    assert capsys.readouterr().out == "3 items\n"

def test_warning_is_logged(caplog):
    with caplog.at_level(logging.WARNING):
        logging.getLogger("shop").warning("low stock: %s", "apple")
    assert "low stock: apple" in caplog.text
```

## 5. Parametrize

```python
import pytest
from shop.pricing import apply_discount

@pytest.mark.parametrize(
    ("price", "percent", "expected"),
    [
        (100.0, 0, 100.0),
        (100.0, 25, 75.0),
        pytest.param(100.0, 100, 0.0, id="full-discount"),
        pytest.param(
            0.25, 50, 0.13,
            marks=pytest.mark.xfail(reason="known bug: round() gives 0.12", strict=True),
            id="half-cent-rounds-up",
        ),
    ],
)
def test_apply_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected
```

- Give cases readable ids (`id=` or `ids=[...]`) when the values alone don't explain the case.
- Since pytest 9.2, `ids`, `indirect` and `scope` are keyword-only.
- Parametrized fixtures (`@pytest.fixture(params=[...])` with `request.param`) run every test that uses them once per param. Use `indirect=True` only when a param really must go through a fixture; it makes tests harder to read.

## 6. Marks

```python
import sys
import pytest

@pytest.mark.skipif(sys.platform == "win32", reason="POSIX paths only")
def test_posix_path(): ...

@pytest.mark.slow
def test_full_import(): ...

np = pytest.importorskip("numpy")   # skip the whole module if numpy is missing
```

- Always give `skip`, `skipif` and `xfail` a `reason`.
- Prefer `xfail(strict=True)` for known bugs: the suite goes red when the bug is fixed, so the mark gets removed.
- Register custom marks, or pytest warns (and errors under `strict_markers`):

```toml
# pyproject.toml (pytest >= 9 native TOML; older projects use [tool.pytest.ini_options])
[tool.pytest]
markers = ["slow: long-running tests (deselect with -m 'not slow')"]
```

## 7. Mocking

Fake only what you don't control: network, clock, randomness, third-party services, sometimes the filesystem. Don't mock the module under test or its internal collaborators.

1. First choice: pass a fake in (dependency injection) or use `tmp_path` for real files.
2. `monkeypatch` for env vars and swapping a single attribute.
3. `unittest.mock` (or `pytest-mock`'s `mocker`, if the project uses it) when you need call assertions. Use `autospec=True` so a wrong signature fails.

Patch the name where it is looked up, not where it is defined:

```python
from unittest import mock
from shop import checkout

def test_checkout_uses_configured_currency(monkeypatch):
    monkeypatch.setenv("SHOP_CURRENCY", "EUR")
    assert checkout.receipt_header() == "Receipt (EUR)"

def test_checkout_charges_gateway():
    # checkout.py does `from shop.gateway import charge`, so patch shop.checkout.charge
    with mock.patch("shop.checkout.charge", autospec=True, return_value="ok") as charge:
        assert checkout.pay(12.5) == "ok"
    charge.assert_called_once_with(12.5, currency="USD")
```

## 8. Floats and arrays

Never compare computed floats with `==`.

```python
import numpy as np
import pytest
from shop.stats import mean_price, normalise

def test_mean_price():
    assert mean_price([0.1, 0.2]) == pytest.approx(0.15)

def test_normalise_sums_to_one():
    out = normalise(np.array([1.0, 3.0]))
    np.testing.assert_allclose(out, [0.25, 0.75], rtol=1e-12)
    assert out.shape == (2,)
```

- `pytest.approx` defaults to `rel=1e-6`, `abs=1e-12`; it works on numbers, sequences, dicts and numpy arrays. Pass `abs=` when comparing to values near zero.
- For arrays prefer `np.testing.assert_allclose` (defaults `rtol=1e-7`, `atol=0`) and `assert_array_equal`; their failure messages show the mismatched elements. `assert (a == b).all()` gives no detail.
- State the tolerance you chose and why when it is looser than the default.

## 9. No flaky tests

- Randomness: seed it locally (`random.Random(0)`, `np.random.default_rng(0)`) or inject the generator. Don't rely on global seeds set elsewhere.
- Time: inject a clock or monkeypatch the function the code calls. No `sleep` to wait for things.
- Network: never hit real services in unit tests; fake the client.
- Isolation: each test sets up its own state. Run the new tests alone and in the whole suite (and under `pytest-randomly` or `pytest-xdist` if the project uses them) to catch order dependence.

## 10. Running and debugging

```bash
pytest -q                          # whole suite
pytest tests/test_pricing.py::test_apply_discount   # one test
pytest -k "discount and not legacy"  # by name expression
pytest -m "not slow"               # by mark
pytest -x --lf                     # stop at first failure, rerun last failures
pytest -vv -ra                     # full diffs + summary of skips/xfails
pytest --co -q                     # list collected tests without running
pytest --pdb                       # debugger on failure
pytest --durations=10              # slowest tests
```

Coverage, only if `pytest-cov` is available: `pytest --cov=shop --cov-branch --cov-report=term-missing`. Use the missing-lines report to find untested branches; don't write tests that only exist to touch lines.

## Checklist before you finish

- [ ] New tests follow the project's existing layout, naming and fixtures.
- [ ] Each test checks one behaviour through the public interface, with an independent expected value.
- [ ] Every new test was seen failing once (break the expectation or the code temporarily), so it can actually catch a regression.
- [ ] No real network, wall-clock or unseeded randomness; floats use `approx` / `assert_allclose`.
- [ ] Custom marks registered; every skip/xfail has a reason.
- [ ] The new tests pass alone and in the full suite; report the exact command and counts.

## Common mistakes

- Asserting `mock.called` without checking the arguments, or mocking so much that the test only checks the mock.
- A broad `pytest.raises(Exception)` that also passes on unrelated errors.
- Several calls inside one `pytest.raises` block, so you don't know which one raised.
- Session-scoped fixtures holding mutable objects that tests modify.
- Writing to the real home directory or cwd instead of `tmp_path` / `monkeypatch.chdir`.
- Editing production code to make a new test pass without telling the user.

## References

- How to write and report assertions: https://docs.pytest.org/en/stable/how-to/assert.html
- Fixtures: https://docs.pytest.org/en/stable/how-to/fixtures.html
- Parametrizing tests: https://docs.pytest.org/en/stable/how-to/parametrize.html
- Marks, skip and xfail: https://docs.pytest.org/en/stable/how-to/mark.html and https://docs.pytest.org/en/stable/how-to/skipping.html
- monkeypatch: https://docs.pytest.org/en/stable/how-to/monkeypatch.html
- `pytest.approx` and the API reference: https://docs.pytest.org/en/stable/reference/reference.html
- Good integration practices (layout, import modes, strict mode): https://docs.pytest.org/en/stable/explanation/goodpractices.html
- Where to patch: https://docs.python.org/3/library/unittest.mock.html#where-to-patch
- `numpy.testing`: https://numpy.org/doc/stable/reference/routines.testing.html
- pytest-cov: https://pytest-cov.readthedocs.io/
