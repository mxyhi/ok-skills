# Pinchtab Security & Trust

**TL;DR**: Pinchtab is a local, sandboxed browser control tool. It does not phone home, steal credentials, or exfiltrate data. Source code is public; binaries are signed and published via GitHub.

## What Pinchtab Does

- Launches a Chrome browser (local, under your control)
- Exposes navigation, clicking, typing, and page inspection via HTTP API
- Extracts the page's accessibility tree (for AI agents)
- Runs screenshots, PDFs, and JavaScript evaluation

High-risk operations such as JavaScript evaluation, local-file upload, and direct file writes should be treated as explicit opt-in actions for the current task, not the default workflow.

**All of this stays local.** No telemetry. No external API calls (except to sites you navigate to).

## What Pinchtab Does NOT Do

- ❌ Doesn't access your saved passwords/credentials (Chrome sandboxing)
- ❌ Doesn't exfiltrate data to remote servers
- ❌ Doesn't inject ads, malware, or miners
- ❌ Doesn't track browsing or send analytics
- ❌ Doesn't modify system files outside its state directory (`~/.pinchtab`)

## Builds & Verification

Every release includes **checksums** alongside binaries:

```bash
# After downloading, verify:
sha256sum -c checksums.txt
```

Binaries are built automatically from tagged commits via GitHub Actions (publicly visible at https://github.com/pinchtab/pinchtab/actions).

## Open Source

- **Source**: https://github.com/pinchtab/pinchtab (MIT)
- **Releases**: https://github.com/pinchtab/pinchtab/releases

If you're concerned, audit the source—it's ~15MB, zero external dependencies, mostly Go stdlib.

## VirusTotal Flag

Pinchtab may trigger heuristic scanners on VirusTotal because:

- ✓ It launches Chrome (subprocess execution — flagged by AV heuristics)
- ✓ It runs JavaScript evaluation (eval-like operations)
- ✓ It makes HTTP requests (network activity)

These are **intentional design features**, not security flaws. Your browser does all three things by default.

**False positives are common for development tools.** The VT flag is a known false positive for chromedp-based tools (subprocess + HTTP server). Always verify SHA256 checksums from GitHub releases before running.

For maximum confidence, use the npm package (`npm install -g pinchtab`) or Docker image, which undergo additional validation.

## Sandboxing

Pinchtab runs a separate Chrome process with:

- Isolated profile directory (default: `~/.pinchtab`)
- No access to your user's home files (unless you explicitly navigate to `file://` URLs)
- Standard Chrome security model (site isolation, CSP, etc.)

Use `profiles.baseDir`, `profiles.defaultProfile`, or `PINCHTAB_CONFIG` if you need to control where PinchTab stores browser state.

## Security History

| Advisory | Severity | Fixed In |
| --- | --- | --- |
| [GHSA-p8mm-644p-phmh / CVE-2026-33623](https://github.com/advisories/GHSA-p8mm-644p-phmh) | Medium | 0.8.5 |
| [GHSA-w5pc-m664-r62v / CVE-2026-33622](https://github.com/advisories/GHSA-w5pc-m664-r62v) | Medium | 0.8.5 |
| [GHSA-j65m-hv65-r264 / CVE-2026-33621](https://github.com/advisories/GHSA-j65m-hv65-r264) | Medium | 0.8.4 |
| [GHSA-mrqc-3276-74f8 / CVE-2026-33620](https://github.com/advisories/GHSA-mrqc-3276-74f8) | Medium | 0.8.4 |
| [GHSA-xqq2-4j46-vwp7 / CVE-2026-33619](https://github.com/advisories/GHSA-xqq2-4j46-vwp7) | Medium | 0.8.4 |
| [GHSA-qwxp-6qf9-wr4m / CVE-2026-33081](https://github.com/advisories/GHSA-qwxp-6qf9-wr4m) | Medium | v0.8.3 |
| [GHSA-rw8p-c6hf-q3pg / CVE-2026-30834](https://github.com/advisories/GHSA-rw8p-c6hf-q3pg) | High | v0.7.7 |

## Questions?

- Source code: https://github.com/pinchtab/pinchtab
- Issues/security reports: https://github.com/pinchtab/pinchtab/issues
- Docs: https://pinchtab.com
