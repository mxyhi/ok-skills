#!/usr/bin/env python3
import argparse
import json
import sys

from dr_check import (
    check_encoding, word_count, json_validate,
    check_headers, check_chapter_numbers, check_metadata,
    check_toc, check_tail, year_density, check_datapool,
    validate_chapter, validate_all_chapters, qa_report,
    check_depth_balance,
)
from dr_gen import (
    extract_sources, generate_toc, generate_metadata,
    generate_refs, map_chapters,
    write_json, write_md,
    prepare_chapter, assemble_report, convert_citations,
    generate_confidence_section, escape_currency,
)
from lang_config import get_lang_config


def _exit(result: dict):
    passed = result.get('passed', False)
    issues = result.get('issues', [])
    stats = {k: result[k] for k in ('record_count', 'source_count', 'fact_count') if k in result}
    if stats:
        import json
        print(f"STATS: {json.dumps(stats)}")
    print("PASS" if passed else "FAIL")
    if not passed:
        for issue in issues:
            print(f"  - {issue}")
    sys.exit(0 if passed else 1)


def main():
    for stream in (sys.stdout, sys.stderr):
        enc = getattr(stream, 'encoding', None)
        if enc and enc.upper() not in ('UTF-8', 'UTF8'):
            try:
                stream.reconfigure(encoding='utf-8', errors='replace')
            except Exception:
                pass

    parser = argparse.ArgumentParser(description='Deep Research Tools v3.0 — QA & utilities')
    sub = parser.add_subparsers(dest='command', required=True)

    # Shared --lang for applicable commands
    LANG_ARG = {'flags': ['--lang'], 'default': 'zh',
                'help': 'Report language code (zh/en/ja/ko/es/fr/de/pt/it/nl/ru/ar/hi/vi/id/th/tr/pl/sv)'}

    # ── Check subcommands ──
    p = sub.add_parser('check-encoding', help='Check UTF-8, BOM, Mojibake')
    p.add_argument('file')
    p = sub.add_parser('word-count', help='Count all chars (excl whitespace/markdown)')
    p.add_argument('file')
    p = sub.add_parser('json-validate', help='Validate JSON')
    p.add_argument('file')
    p = sub.add_parser('json-get', help='Read a value from JSON by dot-separated key path')
    p.add_argument('file')
    p.add_argument('key_path', help='e.g. "0.src" or "0.facts.0.src"')
    p = sub.add_parser('check-headers', help='Check ##/### header format')
    p.add_argument('file')
    p.add_argument('--lang', default='zh', help='Language code')
    p = sub.add_parser('check-chapter-numbers', help='Check chapter number format')
    p.add_argument('file')
    p.add_argument('--lang', default='zh', help='Language code')
    p = sub.add_parser('check-metadata', help='Check metadata line completeness')
    p.add_argument('file')
    p.add_argument('--lang', default='zh', help='Language code')
    p = sub.add_parser('check-toc', help='Check TOC existence and count')
    p.add_argument('file')
    p.add_argument('--expected', type=int, default=None)
    p.add_argument('--lang', default='zh', help='Language code')
    p = sub.add_parser('check-tail', help='Check tail sections (refs + disclaimer)')
    p.add_argument('file')
    p.add_argument('--lang', default='zh', help='Language code')
    p = sub.add_parser('year-density', help='Calculate year density')
    p.add_argument('file')
    p.add_argument('--target-year', type=int, required=True)
    p = sub.add_parser('check-datapool', help='Validate data-pool.json structure')
    p.add_argument('file')
    p.add_argument('--mode', choices=['quick', 'standard', 'deep'], required=True)
    p = sub.add_parser('validate-chapter', help='Single-command: all chapter checks at once')
    p.add_argument('file')
    p.add_argument('--expected-sections', type=int, default=0)
    p = sub.add_parser('validate-all-chapters', help='Parallel batch chapter validation')
    p.add_argument('--chapters-dir', required=True)
    p.add_argument('--chapters', type=int, required=True)
    p.add_argument('--expected-sections', type=int, default=0)
    p = sub.add_parser('depth-balance', help='Check chapter depth balance')
    p.add_argument('--chapters-dir', required=True)
    p.add_argument('--chapters', type=int, required=True)
    p.add_argument('--threshold', type=float, default=0.5, help='Min ratio vs average (default: 0.5)')
    p = sub.add_parser('qa-report', help='Full report quality check')
    p.add_argument('file')
    p.add_argument('--mode', choices=['quick', 'standard', 'deep'], required=True)
    p.add_argument('--target-year', type=int, required=True)
    p.add_argument('--lang', default='zh', help='Language code')

    # ── Generate subcommands ──
    p = sub.add_parser('extract-sources', help='Extract unique (来源，年份) from report')
    p.add_argument('file')
    p.add_argument('--format', choices=['text', 'json'], default='text')
    p = sub.add_parser('generate-toc', help='Generate TOC from outline.json')
    p.add_argument('outline')
    p = sub.add_parser('generate-metadata', help='Generate metadata block')
    p.add_argument('--word-count', type=int, required=True)
    p.add_argument('--reading-time', type=int, required=True)
    p.add_argument('--data-until', required=True)
    p.add_argument('--generate-time', required=True)
    p.add_argument('--mode', required=True, choices=['quick', 'standard', 'deep'])
    p.add_argument('--source-count', type=int, required=True)
    p.add_argument('--top-sources', nargs='*', default=[])
    p.add_argument('--version', default='', help='Skill version')
    p.add_argument('--lang', default='zh', help='Language code')
    p = sub.add_parser('map-chapters', help='Map chapters to sub_questions')
    p.add_argument('outline')
    p = sub.add_parser('generate-refs', help='Generate source list with titles')
    p.add_argument('datapool')
    p.add_argument('--numbered', action='store_true', help='Output as (N) numbered list')
    p.add_argument('--lang', default='zh', help='Language code')

    # convert-citations
    p = sub.add_parser('convert-citations', help='Convert [N] → [(N)](#refN) clickable citations')
    p.add_argument('report', help='Path to assembled report')
    p.add_argument('--datapool', required=True, help='Path to data-pool.json')
    p.add_argument('--output', default=None, help='Output path (default: in-place)')
    p.add_argument('--lang', default='zh', help='Language code')

    # ── Write subcommands ──
    p = sub.add_parser('write-json', help='Read JSON from stdin, write UTF-8 no BOM')
    p.add_argument('filepath')
    p = sub.add_parser('write-md', help='Read markdown from stdin, write UTF-8 no BOM')
    p.add_argument('filepath')

    # ── Confidence section ──
    p = sub.add_parser('generate-confidence-section',
                       help='Generate and insert confidence assessment into report')
    p.add_argument('--datapool', required=True)
    p.add_argument('--manifest', required=True)
    p.add_argument('--report', required=True, help='Path to assembled report (in-place update)')
    p.add_argument('--lang', default='zh', help='Language code')

    # ── Currency escaping ──
    p = sub.add_parser('escape-currency', help='Escape dollar signs to prevent LaTeX math mode rendering')
    p.add_argument('report', help='Path to report markdown file')

    # ── Chapter skeleton + Report assembly ──
    p = sub.add_parser('prepare-chapter', help='Generate chapter skeleton with pre-matched facts')
    p.add_argument('--outline', required=True)
    p.add_argument('--datapool', required=True)
    p.add_argument('--chapter', type=int, required=True)
    p.add_argument('--total', type=int, default=1)
    p.add_argument('--mode', choices=['quick', 'standard', 'deep'], default='standard')
    p = sub.add_parser('assemble-report', help='Assemble final report from chapters + metadata')
    p.add_argument('--outline', required=True)
    p.add_argument('--chapters-dir', required=True)
    p.add_argument('--wordcount', default=None, help='Deprecated')
    p.add_argument('--datapool', required=True)
    p.add_argument('--mode', choices=['quick', 'standard', 'deep'], required=True)
    p.add_argument('--target-year', type=int, required=True)
    p.add_argument('--output', default=None,
                   help='Output file path. If omitted, auto-generates from title+date')
    p.add_argument('--lang', default='zh', help='Language code')

    args = parser.parse_args()

    # ── Dispatch: checks ──
    if args.command == 'check-encoding':
        _exit(check_encoding(args.file))
    elif args.command == 'word-count':
        print(word_count(args.file))
        sys.exit(0)
    elif args.command == 'json-validate':
        _exit(json_validate(args.file))
    elif args.command == 'json-get':
        import json as _json
        with open(args.file, 'r', encoding='utf-8-sig') as _f:
            _data = _json.load(_f)
        _val = _data
        for _key in args.key_path.split('.'):
            if isinstance(_val, list):
                _val = _val[int(_key)]
            else:
                _val = _val[_key]
        print(_json.dumps(_val, ensure_ascii=False, indent=2) if not isinstance(_val, (str, int, float, bool)) else _val)
        sys.exit(0)
    elif args.command == 'check-headers':
        _exit(check_headers(args.file, lang=args.lang))
    elif args.command == 'check-chapter-numbers':
        _exit(check_chapter_numbers(args.file, lang=args.lang))
    elif args.command == 'check-metadata':
        _exit(check_metadata(args.file, lang=args.lang))
    elif args.command == 'check-toc':
        _exit(check_toc(args.file, expected=args.expected, lang=args.lang))
    elif args.command == 'check-tail':
        _exit(check_tail(args.file, lang=args.lang))
    elif args.command == 'year-density':
        _exit(year_density(args.file, target_year=args.target_year))
    elif args.command == 'check-datapool':
        _exit(check_datapool(args.file, mode=args.mode))
    elif args.command == 'validate-chapter':
        result = validate_chapter(args.file, expected_sections=args.expected_sections)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(0)
    elif args.command == 'validate-all-chapters':
        result = validate_all_chapters(args.chapters_dir, args.chapters, args.expected_sections)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(0 if result['passed'] else 1)
    elif args.command == 'depth-balance':
        result = check_depth_balance(args.chapters_dir, args.chapters, args.threshold)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(0 if result['passed'] else 1)
    elif args.command == 'qa-report':
        result = qa_report(args.file, mode=args.mode, target_year=args.target_year, lang=args.lang)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(0 if result['passed'] else 1)

    # ── Dispatch: generate ──
    elif args.command == 'extract-sources':
        result = extract_sources(args.file)
        if args.format == 'json':
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            for s in sorted(result['sources']):
                print(s)
        sys.exit(0)
    elif args.command == 'generate-toc':
        print(generate_toc(args.outline)['toc_text'])
        sys.exit(0)
    elif args.command == 'generate-metadata':
        version = args.version
        if not version:
            import os
            vpath = os.path.join(os.path.dirname(__file__), '..', 'VERSION')
            try:
                with open(vpath) as f:
                    version = f.read().strip()
            except Exception:
                pass
        print(generate_metadata(
            word_count=args.word_count, reading_time=args.reading_time,
            data_until=args.data_until, generate_time=args.generate_time,
            depth_mode=args.mode, source_count=args.source_count,
            top_sources=args.top_sources, skill_version=version,
            lang=args.lang)['full_block'])
        sys.exit(0)
    elif args.command == 'map-chapters':
        print(json.dumps(map_chapters(args.outline), ensure_ascii=False, indent=2))
        sys.exit(0)
    elif args.command == 'generate-refs':
        result = generate_refs(args.datapool, numbered=args.numbered, lang=args.lang)
        print(result['ref_text'])
        sys.exit(0)

    elif args.command == 'convert-citations':
        result = convert_citations(args.report, args.datapool, args.output, lang=args.lang)
        _exit(result)

    #     ── Dispatch: write ──
    elif args.command == 'write-json':
        _exit(write_json(args.filepath))
    elif args.command == 'write-md':
        _exit(write_md(args.filepath))

    # ── Dispatch: confidence section ──
    elif args.command == 'generate-confidence-section':
        result = generate_confidence_section(
            datapool_path=args.datapool, manifest_path=args.manifest, lang=args.lang)
        if not result['passed']:
            _exit(result)
        section = result['section']

        report_path = args.report
        try:
            with open(report_path, 'r', encoding='utf-8-sig') as f:
                content = f.read()
        except Exception as e:
            _exit({'passed': False, 'issues': [f"Failed to read report: {e}"]})

        cfg = get_lang_config(args.lang)
        conf_heading = cfg.get('confidence_heading', '## Confidence Assessment')
        refs_marker = cfg['refs_prefix']

        # Skip if confidence section already exists
        if conf_heading in content:
            print(f"Confidence section already present, skipping: {report_path}")
            sys.exit(0)

        # Insert confidence section before the references section
        pos = content.find(f'\n{refs_marker}')
        if pos == -1:
            pos = content.find(refs_marker)
        if pos == -1:
            _exit({'passed': False,
                   'issues': [f"References marker '{refs_marker}' not found in report"]})

        new_content = content[:pos] + '\n\n' + section + '\n\n---\n\n' + content[pos:]

        tmp = report_path + '.tmp'
        try:
            with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
                f.write(new_content)
            import os
            os.replace(tmp, report_path)
        except Exception as e:
            _exit({'passed': False, 'issues': [f"Write failed: {e}"]})

        enc_check = __import__('dr_check', fromlist=['check_encoding']).check_encoding(report_path)
        if not enc_check['passed']:
            _exit(enc_check)

        print(f"Confidence section inserted: {report_path}")

        sumd = result.get('summary', {})
        print(f"CONFIDENCE: coverage={sumd.get('coverage','unknown')}"
              f"|total_facts={sumd.get('total_facts',0)}"
              f"|high_pct={sumd.get('high_pct',0)}"
              f"|medium_pct={sumd.get('medium_pct',0)}"
              f"|low_pct={sumd.get('low_pct',0)}"
              f"|actual_pct={sumd.get('actual_pct',0)}"
              f"|est_pct={sumd.get('est_pct',0)}"
              f"|fct_pct={sumd.get('fct_pct',0)}"
              f"|auth_pct={sumd.get('auth_pct',0)}"
              f"|data_limited={str(sumd.get('data_limited',False)).lower()}"
              f"|controversies={sumd.get('controversies',0)}"
              f"|adequate_subq={sumd.get('adequate_subq',0)}"
              f"|total_subq={sumd.get('total_subq',0)}"
              f"|score={sumd.get('score',0)}"
              f"|verdict={sumd.get('verdict_label','unknown')}")
        sys.exit(0)

    # ── Dispatch: escape-currency ──
    elif args.command == 'escape-currency':
        result = escape_currency(args.report)
        print(f"Escaped {result['changes']} dollar signs in: {args.report}")
        _exit(result)

    # ── Dispatch: skeleton + assembly ──
    elif args.command == 'prepare-chapter':
        result = prepare_chapter(
            outline_path=args.outline, datapool_path=args.datapool,
            chapter_num=args.chapter, total_chapters=args.total, mode=args.mode)
        if result['passed']:
            print(result['skeleton'])
        _exit(result)
    elif args.command == 'assemble-report':
        result = assemble_report(
            outline_path=args.outline, chapters_dir=args.chapters_dir,
            datapool_path=args.datapool,
            mode=args.mode, target_year=args.target_year,
            wordcount_path=args.wordcount,
            output_path=args.output)
        if result['passed']:
            print(f"Report assembled: {result['output_path']} ({result['line_count']} lines, {result['chapter_count']} chapters, {result['word_count']} chars)")
        _exit(result)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"UNEXPECTED ERROR: {e}", file=sys.stderr)
        print(f"Type: {type(e).__name__}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        print("\n---", file=sys.stderr)
        print("Fallback: This script crashed. The LLM can:", file=sys.stderr)
        print("  1. Check Python version: python --version", file=sys.stderr)
        print("  2. Check file existence: os.path.exists(path)", file=sys.stderr)
        print("  3. Run with traceback: PYTHONTRACEMALLOC=1", file=sys.stderr)
        print("  4. Use sys.executable to find the correct Python path", file=sys.stderr)
        sys.exit(1)
