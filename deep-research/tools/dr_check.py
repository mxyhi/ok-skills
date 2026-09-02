#!/usr/bin/env python3
import json
import os
import re

from lang_config import get_lang_config


# ── Profile loader ────────────────────────────────────────────────────────

_PROFILES_CACHE = None


def load_profile(mode: str) -> dict:
    global _PROFILES_CACHE
    if _PROFILES_CACHE is None:
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(base, 'profiles.json')
        with open(path, 'r', encoding='utf-8-sig') as f:
            _PROFILES_CACHE = json.load(f)
    return _PROFILES_CACHE.get(mode, _PROFILES_CACHE.get('quick', {}))


# ── Mojibake & Encoding ──────────────────────────────────────────────────

MOJIBAKE_PATTERNS = [
    '\ufffd',
    '涓枃', '绯荤粺', '鍦ㄧ嚎',
    'ç³»', 'å·²',
]


def check_encoding(filepath: str) -> dict:
    issues = []
    with open(filepath, 'rb') as f:
        raw = f.read()
    if raw[:3] == b'\xef\xbb\xbf':
        issues.append("BOM detected at byte 0-2: EF BB BF")
        return {"passed": False, "issues": issues}
    try:
        text = raw.decode('utf-8')
    except UnicodeDecodeError as e:
        return {"passed": False, "issues": [f"Invalid UTF-8: {e}"]}
    for i, ch in enumerate(text):
        if ch == '\ufffd':
            line = text[:i].count('\n') + 1
            issues.append(f"Replacement character U+FFFD at line {line}")
            break
    for pattern in MOJIBAKE_PATTERNS[1:]:
        if pattern in text:
            lines = [i + 1 for i, line in enumerate(text.split('\n')) if pattern in line]
            issues.append(f"Mojibake pattern '{pattern}' at lines {lines[:3]}")
    qmark_lines = [i + 1 for i, line in enumerate(text.split('\n')) if re.search(r'\?{3,}', line)]
    if qmark_lines:
        issues.append(f"CP936 question-mark corruption at lines {qmark_lines[:5]}")
    return {"passed": len(issues) == 0, "issues": issues}


# ── Word Count ────────────────────────────────────────────────────────────

def _clean_text(filepath: str) -> str:
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        text = f.read()
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^>\s?', '', text, flags=re.MULTILINE)
    text = re.sub(r'^[-*+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\d+\.\s+', '', text, flags=re.MULTILINE)
    text = text.replace('|', '')
    text = text.replace('`', '')
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'__(.+?)__', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'_(.+?)_', r'\1', text)
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    text = re.sub(r'!\[(.+?)\]\(.+?\)', r'\1', text)
    return text


def word_count(filepath: str) -> int:
    cleaned = re.sub(r'\s+', '', _clean_text(filepath))
    return len(cleaned)


# ── JSON Validation ───────────────────────────────────────────────────────


def json_validate(filepath: str) -> dict:
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            json.load(f)
        return {"passed": True, "issues": []}
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        return {"passed": False, "issues": [str(e)]}


# ── Header Format Checks ──────────────────────────────────────────────────


def check_headers(filepath: str, lang: str = "zh") -> dict:
    issues = []
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    cfg = get_lang_config(lang)
    for i, line in enumerate(lines):
        stripped = line.rstrip('\n\r')
        if cfg['check']['ch_has_number_check']:
            # non-zh: ## headers SHOULD start with number
            if re.match(r'^## (?!Table of Contents|目录|目次|목차|Índice|Table des matières|Inhaltsverzeichnis|Indice|Inhoudsopgave|Innehållsförteckning|Содержание|المحتويات|विषय सूची|Mục lục|Daftar Isi|สารบัญ|İçindekiler|Spis treści|References|参考来源|参照元|Referencias|Réf|Quellen|Fonti|Bronnen|Källor|Источники|المصادر|स्रोत|Nguồn|Kaynaklar|Źródła|Disclaimer|免责|Descargo|Avertissement|Haftungsausschluss|Isenção|Dichiarazione|Vrijwaring|Ansvarsfriskrivning|Отказ|إخلاء|अस्वीकरण|Tuyên bố|Penyangkalan|ข้อจำกัด|Sorumluluk|Zrzeczenie)', stripped) and not re.match(r'^## \d+\.', stripped):
                issues.append(f"Line {i + 1}: ## header should start with number: '{stripped[:60]}'")
        else:
            # zh: ## headers should NOT contain arabic numeral
            if re.match(r'^## .*[0-9]\.', stripped):
                issues.append(f"Line {i + 1}: ## header should not contain number: '{stripped[:60]}'")
        if re.match(r'^### [一二三四五六七八九十]', stripped):
            issues.append(f"Line {i + 1}: ### header uses Chinese numeral: '{stripped[:60]}'")
    return {"passed": len(issues) == 0, "issues": issues}


# ── Chapter Number Compliance ─────────────────────────────────────────────


def check_chapter_numbers(filepath: str, lang: str = "zh") -> dict:
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    cfg = get_lang_config(lang)
    pattern = re.compile(cfg['check']['ch_number_pattern'])
    hits = [i + 1 for i, line in enumerate(lines) if pattern.match(line.rstrip('\n\r'))]
    return {"passed": len(hits) >= 1, "chapter_lines": hits, "count": len(hits)}


# ── Metadata Check ────────────────────────────────────────────────────────


def check_metadata(filepath: str, lang: str = "zh") -> dict:
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    cfg = get_lang_config(lang)
    issues = []
    meta_match = re.search(cfg['check']['metadata_pattern'], content)
    if not meta_match:
        return {"passed": False, "issues": [f"Metadata line '{cfg['metadata_label']}' not found"]}
    meta_line = content[meta_match.end():].split('\n')[0]
    for field in cfg['metadata_fields']:
        if field not in meta_line:
            issues.append(f"Metadata field '{field}' missing")
    if not re.search(cfg['check']['references_pattern'], content):
        issues.append(f"Reference source line '{cfg['references_label']}' not found")
    return {"passed": len(issues) == 0, "issues": issues}


# ── TOC Check ─────────────────────────────────────────────────────────────


def check_toc(filepath: str, expected: int = None, lang: str = "zh") -> dict:
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    issues = []
    cfg = get_lang_config(lang)
    toc_heading = cfg['toc_heading']
    toc_headings = [i for i, line in enumerate(lines) if line.strip() == toc_heading]
    if len(toc_headings) == 0:
        return {"passed": False, "issues": [f"'{toc_heading}' heading not found"], "count": 0}
    elif len(toc_headings) > 1:
        issues.append(f"'{toc_heading}' appears {len(toc_headings)} times (should be 1)")
    toc_start = toc_headings[0]
    toc_entries = 0
    for line in lines[toc_start + 1:]:
        stripped = line.strip()
        if stripped.startswith('## '):
            break
        if stripped.startswith('- ['):
            toc_entries += 1
    if expected is not None and toc_entries != expected:
        issues.append(f"TOC has {toc_entries} entries, expected {expected}")
    return {"passed": len(issues) == 0, "issues": issues, "count": toc_entries}


# ── Tail Check ────────────────────────────────────────────────────────────


def check_tail(filepath: str, lang: str = "zh") -> dict:
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    cfg = get_lang_config(lang)
    issues = []
    refs_title = cfg['check']['tail_refs']
    disc_title = cfg['check']['tail_disclaimer']
    conf_title = cfg['check'].get('tail_confidence')

    accepted_refs = [refs_title, "## 数据来源"]
    for title in accepted_refs:
        if title in content:
            break
    else:
        issues.append(f"Tail section '{refs_title}' not found")
    if disc_title not in content:
        issues.append(f"'{disc_title}' not found")
    if conf_title:
        if conf_title not in content:
            issues.append(f"Confidence section '{conf_title}' not found")
        else:
            # Verify data type row exists within confidence section
            start = content.index(conf_title) + len(conf_title)
            after = content[start:]
            next_heading = after.find('\n## ')
            block = after[:next_heading] if next_heading != -1 else after
            has_data_type_pct = bool(re.search(r'\w+\s*\d+[条]?\(\d+%\)', block))
            if not has_data_type_pct:
                issues.append(f"Confidence section missing data-type row (e.g. '**数据类型**' / '**Data Type**')")
    return {"passed": len(issues) == 0, "issues": issues}


# ── Year Density ──────────────────────────────────────────────────────────


def year_density(filepath: str, target_year: int) -> dict:
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    years = re.findall(r'(?:19|20|21)\d{2}', content)
    if not years:
        return {"passed": False, "issues": ["No year data found"], "density": 0, "total": 0}
    total = len(years)
    target_count = sum(1 for y in years if int(y) in (target_year, target_year - 1))
    density = target_count / total
    return {
        "passed": density >= 0.5,
        "density": round(density, 3),
        "target_count": target_count,
        "total": total,
        "issues": [] if density >= 0.5 else [f"Year density {density:.1%} < 50% (target={target_year})"],
    }


# ── Data Pool Check ───────────────────────────────────────────────────────


def check_datapool(filepath: str, mode: str) -> dict:
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            return {"passed": False, "issues": [f"Invalid JSON: {e}"]}
    issues = []
    required_fields = {'question': str, 'src': list, 'facts': list}
    records = data if isinstance(data, list) else [data]
    for i, rec in enumerate(records):
        for field, ftype in required_fields.items():
            if field not in rec:
                issues.append(f"Record {i}: missing field '{field}'")
            elif not isinstance(rec[field], ftype):
                issues.append(f"Record {i}: '{field}' should be {ftype.__name__}")
        facts = rec.get('facts') or []
        if len(facts) < 1:
            issues.append(f"Record {i}: no facts")
        priority = rec.get('priority', 'medium')
        if priority == 'high' and len(facts) < 2:
            issues.append(f"Record {i}: priority=high but only {len(facts)} fact(s)")
        fact_required = ['src', 'yr', 'met', 'val', 'u', 'ctx']
        for j, fact in enumerate(facts):
            for field in fact_required:
                if field not in fact:
                    issues.append(f"Record {i} fact {j}: missing '{field}'")
            url_val = fact.get('url')
            if not url_val or not str(url_val).strip():
                issues.append(f"Record {i} fact {j}: 'url' is empty or null")
            if mode == 'quick':
                if 'cur' in fact:
                    issues.append(f"Record {i} fact {j}: quick mode should not have 'cur'")
            else:
                if 'cur' not in fact:
                    issues.append(f"Record {i} fact {j}: {mode} mode should have 'cur'")
                if 'conf' not in fact:
                    issues.append(f"Record {i} fact {j}: {mode} mode should have 'conf'")
    for i, rec in enumerate(records):
        for j, fact in enumerate(rec.get('facts') or []):
            for field in ('src', 'title', 'ctx'):
                val = str(fact.get(field, ''))
                if re.search(r'\?{3,}', val) or '\ufffd' in val:
                    issues.append(f"Record {i} fact {j}: mojibake in '{field}'")
    all_srcs = set()
    total_facts = 0
    for rec in records:
        for s in rec.get('src', []):
            all_srcs.add(s)
        total_facts += len(rec.get('facts', []))
    return {
        "passed": len(issues) == 0,
        "issues": issues,
        "record_count": len(records),
        "source_count": len(all_srcs),
        "fact_count": total_facts,
    }


# ── Chapter Validation (single-command for sub-agents) ─────────────────


def validate_chapter(filepath: str, expected_sections: int = 0) -> dict:
    results = {}
    enc = check_encoding(filepath)
    results['encoding'] = enc['passed']
    hdr = check_headers(filepath)
    results['headers'] = hdr['passed']
    try:
        wc = word_count(filepath)
    except Exception:
        wc = 0
    results['word_count'] = wc
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    check_lines = lines[1:] if lines and lines[0].startswith('#') else lines
    has_bq = len(check_lines) > 0 and check_lines[0].startswith('>')
    results['has_blockquote'] = has_bq
    para_count = 0
    in_table = False
    for line in lines:
        if line.startswith('|') and line.endswith('|'):
            in_table = True
            continue
        if in_table and not (line.startswith('|') and line.endswith('|')):
            in_table = False
        if in_table:
            continue
        if line.startswith('#'):
            continue
        if line.startswith('>'):
            continue
        if line.startswith('|---'):
            continue
        if line.startswith('|'):
            continue
        para_count += 1
    results['paragraphs'] = para_count
    table_count = sum(1 for l in lines if l.startswith('|---'))
    results['tables'] = table_count
    section_headers = [l.lstrip('#').strip() for l in lines if l.startswith('###')]
    results['sections'] = section_headers
    results['section_count'] = len(section_headers)
    results['sections_ok'] = expected_sections == 0 or len(section_headers) == expected_sections
    checks = [results['encoding'], results['headers'], results['has_blockquote'],
              results['sections_ok']]
    results['passed'] = all(checks)
    return results


# ── Batch Chapter Validation (Parallel) ───────────────────────────────────


def validate_all_chapters(chapters_dir: str, chapter_count: int, expected_sections: int = 0) -> dict:
    from concurrent.futures import ThreadPoolExecutor, as_completed
    results = {}
    with ThreadPoolExecutor(max_workers=min(chapter_count, 8)) as ex:
        futures = {}
        for i in range(1, chapter_count + 1):
            path = os.path.join(chapters_dir, f"chapter-{i}.md")
            if not os.path.exists(path):
                results[i] = {"passed": False, "error": f"chapter-{i}.md not found"}
                continue
            futures[ex.submit(validate_chapter, path, expected_sections)] = i
        for fut in as_completed(futures):
            chapter_num = futures[fut]
            try:
                result = fut.result()
                results[chapter_num] = result
            except Exception as e:
                results[chapter_num] = {"passed": False, "error": str(e)}
    sorted_results = {k: results[k] for k in sorted(results.keys())}
    failed_chapters = {str(num): r for num, r in sorted_results.items()
                       if not r.get('passed', False)}
    return {
        "passed": len(failed_chapters) == 0,
        "total": chapter_count,
        "passed_count": chapter_count - len(failed_chapters),
        "failed_count": len(failed_chapters),
        "results": sorted_results,
        "failed_chapters": failed_chapters,
    }


# ── Full QA Report ────────────────────────────────────────────────────────


def _run_checks_concurrent(filepath: str, target_year: int, lang: str = "zh") -> dict:
    from concurrent.futures import ThreadPoolExecutor, as_completed

    def _wc(p):
        wc = word_count(p)
        return {'word_count': wc}

    def _toc(p, expected):
        return {'toc': check_toc(p, expected=expected, lang=lang)}

    results = {}
    with ThreadPoolExecutor(max_workers=6) as ex:
        futures = {
            ex.submit(check_encoding, filepath): 'encoding',
            ex.submit(_wc, filepath): 'word_count_raw',
            ex.submit(check_headers, filepath, lang): 'headers',
            ex.submit(check_chapter_numbers, filepath, lang): 'chapter_numbers',
            ex.submit(check_metadata, filepath, lang): 'metadata',
            ex.submit(check_tail, filepath, lang): 'tail',
            ex.submit(year_density, filepath, target_year): 'year_density',
        }
        for fut in as_completed(futures):
            key = futures[fut]
            try:
                result = fut.result()
                if key == 'word_count_raw':
                    results['word_count_raw'] = result['word_count']
                else:
                    results[key] = result
            except Exception as e:
                results[key] = {"passed": False, "issues": [f"Check error: {e}"]}
    expected = results.get('chapter_numbers', {}).get('count', 0)
    results['toc'] = check_toc(filepath, expected=expected, lang=lang)
    return results


def qa_report(filepath: str, mode: str, target_year: int, lang: str = "zh") -> dict:
    raw = _run_checks_concurrent(filepath, target_year, lang)
    results = {}
    results['encoding'] = raw.get('encoding', {"passed": False, "issues": ["missing"]})
    results['headers'] = raw.get('headers', {"passed": False, "issues": ["missing"]})
    results['chapter_numbers'] = raw.get('chapter_numbers', {"passed": False, "issues": ["missing"]})
    results['metadata'] = raw.get('metadata', {"passed": False, "issues": ["missing"]})
    results['toc'] = raw.get('toc', {"passed": False, "issues": ["missing"]})
    results['tail'] = raw.get('tail', {"passed": False, "issues": ["missing"]})
    results['year_density'] = raw.get('year_density', {"passed": False, "issues": ["missing"]})
    wc = raw.get('word_count_raw', 0)
    prof = load_profile(mode)
    limit = prof.get('max_chars', 3000)
    results['word_count'] = {"passed": True, "count": wc, "limit": limit, "exceeded": wc > limit,
                              "issues": [] if wc <= limit else [f"{wc} > {limit} limit (informational)"]}
    all_passed = all(r.get('passed', False) for r in results.values())
    failures = {name: r.get('issues', []) for name, r in results.items()
                if not r.get('passed', False) and r.get('issues')}
    return {
        "passed": all_passed,
        "file": filepath,
        "mode": mode,
        "target_year": target_year,
        "checks": results,
        "failures": failures,
    }


# ── Chapter Depth Balance ────────────────────────────────────────────────


def check_depth_balance(chapters_dir: str, chapter_count: int,
                        threshold: float = 0.5) -> dict:
    """Check if any chapter is significantly shorter than average.
    threshold=0.5 means flag if a chapter < 50% of average line count.
    Language-agnostic — pure line count comparison."""
    issues = []
    lengths = []
    for i in range(1, chapter_count + 1):
        path = os.path.join(chapters_dir, f"chapter-{i}.md")
        try:
            with open(path, 'r', encoding='utf-8-sig') as f:
                lines = f.readlines()
            lengths.append((i, len(lines)))
        except FileNotFoundError:
            lengths.append((i, 0))
            issues.append(f"Chapter {i}: file not found")

    if not lengths:
        return {"passed": False, "issues": ["No chapter files found"]}

    avg = sum(n for _, n in lengths) / len(lengths)
    thin = [(i, n) for i, n in lengths if n < avg * threshold and n > 0]
    for i, n in thin:
        issues.append(
            f"Chapter {i}: {n} lines ({n/avg:.0%} of avg {avg:.0f} lines) "
            f"— below {threshold:.0%} threshold"
        )

    return {"passed": len(issues) == 0, "issues": issues,
            "chapters": [{"num": i, "lines": n} for i, n in lengths],
            "average": round(avg, 1)}
