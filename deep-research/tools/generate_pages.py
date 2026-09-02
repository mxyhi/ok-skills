#!/usr/bin/env python3
"""Scan reports/ and generate gh-pages index (index.html + reports.json).

Local mode:  python tools/generate_pages.py
API mode:    python tools/generate_pages.py --api
               (fetches files via GitHub API, no git checkout needed)
"""
import os, json, re, sys, base64, urllib.request, pathlib
from datetime import datetime, timezone

# 锚定脚本所在 skill 根目录，使 reports/ 解析不依赖 CWD
_SKILL_DIR = pathlib.Path(__file__).resolve().parent.parent

REPORTS_DIR = str(_SKILL_DIR / 'reports')
OUTPUT_DIR = str(_SKILL_DIR / 'gh-pages')
LOCAL_OUTPUT_DIR = str(_SKILL_DIR / 'reports-browser')

LANG_NAMES = {
    'zh': '中文', 'en': 'English', 'ja': '日本語', 'ko': '한국어',
    'es': 'Español', 'fr': 'Français', 'de': 'Deutsch', 'pt': 'Português',
    'it': 'Italiano', 'nl': 'Nederlands', 'sv': 'Svenska', 'ru': 'Русский',
    'ar': 'العربية', 'hi': 'हिन्दी', 'vi': 'Tiếng Việt', 'id': 'Bahasa Indonesia',
    'th': 'ไทย', 'tr': 'Türkçe', 'pl': 'Polski',
}
MODE_LABELS = {'quick': 'Quick', 'standard': 'Standard', 'deep': 'Deep'}
API_BASE = 'https://api.github.com'


def _api_get(path):
    """GitHub API GET request. Uses GITHUB_TOKEN env var."""
    token = os.environ.get('GITHUB_TOKEN', '')
    repo = os.environ.get('GITHUB_REPOSITORY', 'hoolulu/deep-research')
    url = f'{API_BASE}/repos/{repo}/{path}'
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/vnd.github.v3+json')
    if token:
        req.add_header('Authorization', f'Bearer {token}')
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def parse_content(content: str, path: str) -> dict:
    """Parse a report's markdown content into metadata dict."""
    t = re.search(r'^# (.+)', content)
    title = t.group(1).strip() if t else os.path.basename(path)
    # Convert absolute path to relative (reports/LANG/filename.md)
    full_path = pathlib.Path(path).resolve()
    try:
        rel = str(full_path.relative_to(_SKILL_DIR)).replace('\\', '/')
    except ValueError:
        rel = full_path.as_posix()
    lang = rel.split('/')[1] if rel.startswith('reports/') else 'en'
    d = re.search(r'(\d{4})(\d{2})(\d{2})', path)
    date = f'{d.group(1)}-{d.group(2)}-{d.group(3)}' if d else ''
    mm = re.search(r'> \*\*(?:元数据|Metadata|メタデータ|메타데이터|Metadatos|Métadonnées|Metadaten|Metadados|Metadati)\*\*[:：]\s*(.+)', content)
    mode, wc = 'standard', 0
    if mm:
        mt = mm.group(1)
        m = re.search(r'(?:调研模式|Mode|mode|Modo|モード|모드|Modus|Режим|الوضع|मोड|Chế độ)\s*[:：]\s*(\w+)', mt)
        if m:
            mode = m.group(1).lower()
        for p in [
            r'(?:字数|总字数|文字数|글자|عدد الكلمات|शब्द|Số từ|จำนวนคำ)\s*[:：]\s*([\d,]+)',
            r'(?:Word Count|Wortanzahl|Contagem|Recuento|Kelime|Jumlah kata)\s*[:：]?\s*([\d,]+)',
        ]:
            m = re.search(p, mt, re.IGNORECASE)
            if m:
                wc = int(m.group(1).replace(',', ''))
                break
    if wc == 0:
        wc = len(re.sub(r'\s+', '', content))
    src = 0
    sm = re.search(
        r'(?:共引用|Total|Totalt|Totale|総計|合计|总共|합계|إجمالي|कुल|Tổng|Total de)\s+(\d+)\s*'
        r'(?:个来源|sources|件の出典|개 출처|fuentes|fontes|Bronnen|källor|источников|'
        r'مصدرًا|स्रोत|nguồn|sumber|แหล่งที่มา|kaynak|źródeł|fonti)', content)
    if sm:
        src = int(sm.group(1))
    else:
        a = re.findall(r'<a id="ref(\d+)"></a>', content)
        src = max(int(x) for x in a) if a else 0
    return {'title': title, 'path': rel, 'lang': lang,
            'lang_name': LANG_NAMES.get(lang, lang),
            'mode': mode, 'word_count': wc, 'date': date, 'sources': src}


def fmt(n):
    if n >= 10000:
        return f'{round(n/10000,1)}w' if n % 10000 else f'{n//10000}w'
    if n >= 1000:
        return f'{round(n/1000,1)}k' if n % 1000 else f'{n//1000}k'
    return str(n)


def gen_html(reports, local=False, out_dir=None):
    out_dir = out_dir or 'gh-pages'
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    repo = os.environ.get('GITHUB_REPOSITORY', 'hoolulu/deep-research')
    base = f'https://github.com/{repo}/blob/main'
    
    lang_counts = {}
    for r in reports:
        lang_counts[r['lang']] = lang_counts.get(r['lang'], 0) + 1
    lang_order = sorted(lang_counts.items(), key=lambda x: (0 if x[0] == 'zh' else 1 if x[0] == 'en' else 2, -x[1]))
    
    chips = ''
    for code, cnt in lang_order:
        name = LANG_NAMES.get(code, code)
        chips += f'<button class="lc" data-lc="{code}" onclick="fc(this)">{name} <span class="lcn">{cnt}</span></button>'
    
    seen = set()
    lo = ''.join(f'<option value="{c}">{n}</option>' for c, n in LANG_NAMES.items() if (c in seen or seen.add(c) is None) and any(r['lang'] == c for r in reports))
    mo = ''.join(f'<option value="{m}">{MODE_LABELS.get(m,m.title())}</option>' for m in sorted(set(r['mode'] for r in reports)))
    # Embed report content for local preview (avoids file:// fetch restrictions)
    report_data = ''
    preview_css = ''
    preview_html = ''
    preview_js = ''
    if local:
        contents = {}
        for i, r in enumerate(reports):
            if i >= int(os.environ.get('EMBED_MAX', '999')):
                break
            path = _SKILL_DIR / r['path']  # r['path'] 已是相对 skill 根的路径
            try:
                with open(path, encoding='utf-8') as f:
                    contents[str(i)] = f.read()
            except:
                pass
        rd_obj = json.dumps(contents, ensure_ascii=False)
        rf_obj = json.dumps({str(k):r["path"].split("/")[-1] for k,r in enumerate(reports) if str(k) in contents}, ensure_ascii=False)
        report_data = f'var RD={{}},RF={{}};'
        report_data += 'try{'
        report_data += f'RD={rd_obj};RF={rf_obj}'
        report_data += '}catch(e){}'
        preview_css = '.pv-overlay{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.5);z-index:100;overflow:hidden}.pv-container{max-width:900px;margin:0 auto;height:100%;display:flex;flex-direction:column;pointer-events:none;position:relative}.pv-container>*{pointer-events:auto}.pv-header{display:flex;align-items:center;gap:8px;padding:8px 16px;background:var(--bg);border-bottom:1px solid var(--border);border-radius:8px 8px 0 0;flex-shrink:0;position:relative}.pv-header h2{flex:1;font-size:15px;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.pv-btn{cursor:pointer;padding:4px 10px;border:1px solid var(--border);border-radius:var(--radius);font-size:14px;background:var(--bg);font-family:inherit;color:var(--fg);white-space:nowrap;flex-shrink:0}.pv-btn:hover{background:var(--canvas)}.pv-body{flex:1;overflow-y:auto;padding:20px;line-height:1.7;font-size:15px;overflow-wrap:break-word;background:var(--bg);border-radius:0 0 8px 8px}.pv-body h1{font-size:24px;margin:0 0 16px;padding-bottom:8px;border-bottom:1px solid var(--border)}.pv-body h2{font-size:20px;margin:24px 0 12px}.pv-body h3{font-size:17px;margin:20px 0 8px}.pv-body table{border-collapse:collapse;margin:12px 0;font-size:14px;width:100%}.pv-body td,.pv-body th{border:1px solid var(--border);padding:6px 10px;text-align:left}.pv-body th{background:var(--canvas);font-weight:600}.pv-body code{background:var(--canvas);padding:2px 5px;border-radius:3px;font-size:13px;font-family:var(--fm)}.pv-body pre code{display:block;padding:12px;overflow-x:auto;line-height:1.4}.pv-body blockquote{border-left:4px solid var(--accent);margin:12px 0;padding:4px 16px;color:var(--muted);background:var(--canvas)}.pv-body ul,.pv-body ol{list-style:none;padding-left:0}.pv-body a{color:var(--accent)}.pv-toc-panel{display:none;position:absolute;top:100%;right:0;width:280px;max-height:60vh;overflow-y:auto;background:var(--bg);border:1px solid var(--border);border-radius:var(--radius);box-shadow:0 8px 24px rgba(0,0,0,.15);z-index:2;padding:8px 0;font-size:13px}.pv-toc-panel a{display:block;padding:4px 16px;color:var(--fg);text-decoration:none}.pv-toc-panel a:hover{background:var(--canvas)}.pv-toc-panel .pv-toc-l2{padding-left:32px;font-size:12px}.pv-toc-panel .pv-toc-l3{padding-left:48px;font-size:11px}.pv-toc-panel a:first-child{margin-top:0}#pv-top{position:absolute;bottom:24px;right:24px;z-index:101;width:40px;height:40px;border:none;background:#07C160;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(7,193,96,.3);color:#fff;border-radius:10px;opacity:.9;transition:all .2s}#pv-top:hover{opacity:1;box-shadow:0 4px 12px rgba(7,193,96,.4);transform:translateY(-2px)}#pv-top svg{width:18px;height:18px;fill:currentColor}.pv-toc-panel{display:none;position:absolute;top:100%;right:0;width:280px;max-height:60vh;overflow-y:auto;background:var(--bg);border:1px solid var(--border);border-radius:var(--radius);box-shadow:0 8px 24px rgba(0,0,0,.15);z-index:2;padding:8px 0;font-size:14px}.pv-toc-panel a{display:block;padding:6px 12px;color:var(--fg);text-decoration:none;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.pv-toc-panel a:hover{background:var(--canvas);color:var(--accent)}.pv-toc-l2{padding-left:24px!important;font-size:13px;color:var(--muted)!important}.pv-toc-l3{padding-left:36px!important;font-size:12px;color:var(--muted)!important}.pv-export{position:relative;display:inline-block}.pv-export-menu{display:none;position:absolute;top:100%;right:0;background:var(--bg);border:1px solid var(--border);border-radius:var(--radius);box-shadow:0 4px 12px rgba(0,0,0,.1);z-index:2;min-width:100px;white-space:nowrap;overflow:hidden}.pv-export-menu div{padding:8px 16px;cursor:pointer;font-size:13px;color:var(--fg)}.pv-export-menu div:hover{background:var(--canvas);color:var(--accent)}'
        preview_html = '<div id="pv" class="pv-overlay" onclick="if(event.target===this)pc()"><div class="pv-container"><div class="pv-header"><h2 id="pv-title"></h2><span class="pv-export" id="pv-export-wrap"><button class="pv-btn" onclick="te()">\u5bfc\u51fa \u25be</button><div class="pv-export-menu" id="pv-export-menu" style="display:none"><div onclick="ex(\'pdf\')">PDF</div><div onclick="ex(\'docx\')">DOCX</div></div></span><button class="pv-btn" id="pv-toc-btn" onclick="tt()">TOC/\u76ee\u5f55</button><div class="pv-toc-panel" id="pv-toc-panel"></div><button class="pv-btn" onclick="pc()">&#10005;</button></div><div class="pv-body" id="pv-body"></div><button id="pv-top" onclick="document.getElementById(\'pv-body\').scrollTop=0"><svg viewBox="0 0 24 24"><path d="M12 4l-8 8h5v8h6v-8h5z"/></svg></button></div></div>'
        preview_js = '''var P=document.getElementById('pv');var PB=document.getElementById('pv-body');var PTPanel=document.getElementById('pv-toc-panel');var PRid=null;function qs(t){return t.replace(/[^\w\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\uac00-\ud7af-]+/g,'-').replace(/^-|-$/g,'').toLowerCase()}function qs2(t){return t.replace(/[^\w\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\uac00-\ud7af]/g,'').toLowerCase()}PB.addEventListener('click',function(e){var a=e.target.closest('a[href^="#"]');if(a){e.preventDefault();var id=decodeURIComponent(a.getAttribute('href').slice(1));var el=document.getElementById(id);if(!el)PB.querySelectorAll('h1,h2,h3').forEach(function(h){var s1=qs(h.textContent),s2=qs2(h.textContent);if(s1===id||s2===id||s2===id.replace(/-/g,''))el=h});if(el){var t=el.getBoundingClientRect().top+PB.scrollTop-60;PB.scrollTo({top:t,behavior:'smooth'})}}});function po(r){var t=r.querySelector('a').textContent;var k=r.dataset.rid;var m=RD[k];if(!m)return;PRid=k;document.getElementById('pv-title').textContent=t;function render(){PB.innerHTML=marked.parse(m);gtoc();P.style.display='block';document.body.style.overflow='hidden';PB.scrollTop=0;PTPanel.style.display='none';var el=document.getElementById('pv-export-menu');if(el)el.style.display='none'}if(window.marked)render();else{var s=document.createElement('script');s.src='marked.min.js';s.onload=render;document.head.appendChild(s)}}function pc(){P.style.display='none';document.body.style.overflow=''}function tt(){PTPanel.style.display=PTPanel.style.display==='block'?'none':'block'}function gtoc(){PTPanel.innerHTML='';PB.querySelectorAll('h1,h2,h3').forEach(function(h,i){if(!h.id)h.id='toc-'+i;var a=document.createElement('a');a.textContent=h.textContent;a.setAttribute('data-tid',h.id);a.addEventListener('click',function(e){e.preventDefault();var el=document.getElementById(this.getAttribute('data-tid'));if(el){var t=el.getBoundingClientRect().top+PB.scrollTop-60;PB.scrollTo({top:t,behavior:'smooth'})}PTPanel.style.display='none'});var l=h.tagName.toLowerCase();if(l!='h1')a.className=l=='h2'?'pv-toc-l2':'pv-toc-l3';PTPanel.appendChild(a)})}document.getElementById('b').addEventListener('click',function(e){var a=e.target.closest('a');if(!a)return;var r=a.closest('tr');if(r&&r.dataset.rid!==void 0){e.preventDefault();po(r)}});function te(){var m=document.getElementById('pv-export-menu');m.style.display=m.style.display==='block'?'none':'block'};function ex(f){document.getElementById('pv-export-menu').style.display='none';if(f==='pdf')epdf();else if(f==='docx')edocx()};function epdf(){var e=document.getElementById('pv-body');var t=document.getElementById('pv-title').textContent.replace(/[<>:"\/\|?*]/g,'_')||'report';var o={margin:[0.5,0.5,0.5,0.5],filename:t+'.pdf',image:{type:'jpeg',quality:.95},html2canvas:{scale:2},jsPDF:{unit:'in',format:'a4',orientation:'portrait'},pagebreak:{mode:['avoid-all','css','legacy']}};if(typeof html2pdf==='undefined'){var s=document.createElement('script');s.src='html2pdf.bundle.min.js';s.onload=function(){html2pdf().from(e).set(o).save()};document.head.appendChild(s)}else{html2pdf().from(e).set(o).save()}};function edocx(){var c=document.getElementById('pv-body').innerHTML;var t=document.getElementById('pv-title').textContent.replace(/[<>:"\/\|?*]/g,'_')||'report';var ss='body{font-family:\"宋体\",SimSun,\"Noto Sans CJK SC\",serif;line-height:1.7;padding:20px;max-width:900px;color:#1f2328;font-size:12pt}h1{font-size:18pt;margin:0 0 12px;padding-bottom:6px;border-bottom:1px solid #d0d7de;font-family:\"黑体\",SimHei,\"Noto Sans CJK SC\",sans-serif}h2{font-size:15pt;margin:18px 0 10px;font-family:\"黑体\",SimHei,\"Noto Sans CJK SC\",sans-serif}h3{font-size:13pt;margin:14px 0 6px;font-family:\"黑体\",SimHei,\"Noto Sans CJK SC\",sans-serif}table{border-collapse:collapse;margin:10px 0;font-size:11pt;width:100%}td,th{border:1px solid #d0d7de;padding:4px 8px}th{background:#f6f8fa;font-weight:600}code{background:#f6f8fa;padding:1px 4px;border-radius:2px;font-size:11pt}pre code{display:block;padding:10px}blockquote{border-left:4px solid #0969da;margin:10px 0;padding:3px 14px;color:#656d76}';var html='<!DOCTYPE html><html><head><meta charset=\"utf-8\"><title>'+t+'</title><style>'+ss+'</style></head><body>'+c+'</body></html>';if(typeof htmlDocx==='undefined'){var sc=document.createElement('script');sc.src='html-docx.min.js';sc.onload=function(){edocx2(html,t)};document.head.appendChild(sc)}else{edocx2(html,t)}};function edocx2(html,t){var b=htmlDocx.asBlob(html,{margins:{top:1440,right:1440,bottom:1440,left:1440}});var u=URL.createObjectURL(b);var a=document.createElement('a');a.href=u;a.download=t+'.docx';document.body.appendChild(a);a.click();setTimeout(function(){document.body.removeChild(a);URL.revokeObjectURL(u)},1e3)}'''

    rows = ''
    for i, r in enumerate(reports, 1):
        mc = r['mode'] if r['mode'] in MODE_LABELS else 'standard'
        idx = i - 1
        url = f'../{r["path"]}' if local else f'{base}/{r["path"]}'
        rows += f'<tr data-lang="{r["lang"]}" data-mode="{r["mode"]}" data-rid="{idx}"><td class="n">{i}</td><td class="tc"><a href="{url}" target="_blank">{r["title"]}</a></td><td>{r["lang_name"]}</td><td><span class="mb mb-{mc}">{MODE_LABELS.get(r["mode"],r["mode"].title())}</span></td><td class="m">{fmt(r["word_count"])}</td><td class="m">{r["sources"]}</td><td class="m">{r["date"]}</td></tr>'

    h = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>{'Your Reports' if local else 'Deep Research Reports'}</title><link rel="icon" type="image/svg+xml" href="favicon.svg"><style>
:root{{--fg:#1f2328;--bg:#fff;--canvas:#f6f8fa;--border:#d0d7de;--bm:#d8dee4;--accent:#0969da;--green:#1a7f37;--orange:#9a6700;--muted:#656d76;--radius:6px;--f:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif;--fm:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:var(--f);color:var(--fg);background:var(--bg);line-height:1.5}}.w{{max-width:1100px;margin:0 auto;padding:24px 16px}}.hd{{display:flex;align-items:center;gap:12px;margin-bottom:4px}}.hd h1{{font-size:24px;font-weight:600;letter-spacing:-.02em}}.hd h1 a{{color:inherit;text-decoration:none}}.hd h1 a:hover{{color:var(--accent)}}.st{{color:var(--muted);font-size:14px;margin-bottom:20px}}.tb{{display:flex;gap:8px;margin-bottom:16px;flex-wrap:wrap;align-items:center}}.sw{{position:relative;flex:1;min-width:200px}}.sw svg{{position:absolute;left:10px;top:50%;transform:translateY(-50%);pointer-events:none;color:var(--muted)}}.sw input{{width:100%;padding:6px 12px 6px 34px;font-size:14px;border:1px solid var(--border);border-radius:var(--radius);outline:none;font-family:inherit}}.sw input:focus{{border-color:var(--accent);box-shadow:0 0 0 3px rgba(9,105,218,.15)}}.fs{{padding:6px 32px 6px 12px;font-size:14px;border:1px solid var(--border);border-radius:var(--radius);cursor:pointer;outline:none;font-family:inherit;appearance:none;background:var(--bg);background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16'%3E%3Cpath fill='%23656d76' d='M4.43 6.43l3.4 3.4a.25.25 0 00.35 0l3.4-3.4A.25.25 0 0011.4 6H4.6a.25.25 0 00-.18.43z'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 8px center}}
.fs:focus{{border-color:var(--accent);box-shadow:0 0 0 3px rgba(9,105,218,.15)}}.bg{{font-size:12px;white-space:nowrap;color:var(--muted)}}
.tw{{border:1px solid var(--border);border-radius:var(--radius);overflow:hidden}}table{{width:100%;border-collapse:collapse;font-size:14px}}thead{{background:var(--canvas)}}
th{{padding:8px 12px;text-align:left;font-weight:600;border-bottom:1px solid var(--bm);white-space:nowrap;cursor:pointer;user-select:none}}th:hover{{color:var(--accent)}}th .si{{display:inline-block;width:16px;margin-left:4px;opacity:.3;vertical-align:middle}}th.s .si{{opacity:1;color:var(--accent)}}
td{{padding:8px 12px;border-bottom:1px solid var(--bm);vertical-align:middle}}tbody tr{{transition:background .1s}}tbody tr:hover{{background:#f3f4f6}}tr:last-child td{{border-bottom:none}}
.n{{color:var(--muted);font-size:12px;width:30px;text-align:right}}.tc a{{color:var(--accent);text-decoration:none;font-weight:500}}.tc a:hover{{text-decoration:underline}}.m{{font-family:var(--fm);font-size:12px;color:var(--muted);white-space:nowrap}}
.mb{{display:inline-block;padding:2px 7px;font-size:11px;font-weight:600;border-radius:20px;line-height:1.4;white-space:nowrap}}.mb-quick{{color:var(--green);background:#dafbe1}}.mb-standard{{color:var(--accent);background:#ddf4ff}}.mb-deep{{color:var(--orange);background:#fff8c5}}
.lc{{display:inline-flex;align-items:center;gap:5px;padding:4px 12px;margin:0 4px 8px 0;font-size:13px;font-weight:500;border:1px solid var(--border);border-radius:20px;background:var(--bg);color:var(--fg);cursor:pointer;font-family:inherit;transition:all .15s;white-space:nowrap}}.lc:hover{{border-color:var(--accent);color:var(--accent);background:#f3f8ff}}.lc.s{{border-color:var(--accent);color:#fff;background:var(--accent)}}.lcn{{display:inline-flex;align-items:center;justify-content:center;min-width:20px;height:20px;padding:0 5px;font-size:11px;font-weight:600;border-radius:10px;background:var(--canvas);color:var(--muted)}}
.pm{{font-size:12px;color:var(--muted);font-weight:400}}.pm a{{color:var(--accent);text-decoration:none}}
.hidden{{display:none!important}}.ft{{margin-top:16px;font-size:12px;color:var(--muted);display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px}}.ft a{{color:var(--accent);text-decoration:none}}.ft a:hover{{text-decoration:underline}}
@media(max-width:700px){{.w{{padding:16px 8px}}.lcw{{margin-bottom:8px}}.tb{{flex-direction:column}}.sw{{min-width:100%}}thead{{display:none}}tbody tr{{display:block;padding:12px;border-bottom:1px solid var(--bm)}}td{{display:block;padding:3px 0;border:none}}td.n{{display:none}}td.tc{{font-size:15px;margin-bottom:4px}}td::before{{content:attr(data-l);font-size:11px;color:var(--muted);display:inline-block;width:60px;font-weight:500}}}}
.pg{{display:flex;align-items:center;justify-content:space-between;padding:8px 0;font-size:13px;color:var(--muted);flex-wrap:wrap;gap:8px}}.pg-b{{display:flex;align-items:center;gap:6px}}.pg-s select{{padding:2px 6px;font-size:12px;border:1px solid var(--border);border-radius:var(--radius);font-family:inherit;cursor:pointer}}.pg button{{padding:2px 10px;border:1px solid var(--border);border-radius:var(--radius);background:var(--bg);cursor:pointer;font-size:13px;font-family:inherit;color:var(--fg)}}.pg button:disabled{{opacity:.4;cursor:default}}.pg button:not(:disabled):hover{{background:var(--canvas)}}
{preview_css}</style></head><body>
{preview_html}
<div class="w">
<div class="hd"><svg width="36" height="36" viewBox="0 0 36 36"><rect width="36" height="36" rx="8" fill="#0969da"/><text x="18" y="25" text-anchor="middle" font-size="20" font-weight="bold" fill="white" font-family="sans-serif">DR</text></svg><h1><a href=".">{'Your Reports' if local else 'Deep Research Reports'}</a></h1></div>
<p class="st">{'Browse your locally generated research reports' if local else 'Browse all generated reports'} — filter by language, depth, or keywords<br><span class="pm">{'Generated by' if local else 'Powered by'} <a href="https://github.com/hoolulu/deep-research" target="_blank">deep-research</a> &mdash; One command. Ten minutes. Deep professional reports.</span></p>
<div class="lcw">{chips}</div>
<div class="tb">
<div class="sw"><svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M10.68 11.74a6 6 0 1 1 1.06-1.06l3.04 3.04a.75.75 0 1 1-1.06 1.06l-3.04-3.04z" fill="currentColor"/><circle cx="7" cy="7" r="5.25" stroke="currentColor" stroke-width="1.5" fill="none"/></svg><input type="text" id="q" placeholder="Search reports&hellip;" oninput="f()" autocomplete="off"></div>
<select class="fs" id="l" onchange="f()"><option value="">All languages</option>{lo}</select>
<select class="fs" id="m" onchange="f()"><option value="">All depths</option>{mo}</select>
<span class="bg" id="c">{len(reports)} reports</span>
</div>
<div class="tw"><table><thead><tr><th style="width:30px">#</th><th onclick="s(0)" class="s">Report <span class="si">&#8595;</span></th><th onclick="s(1)">Language <span class="si">&#8597;</span></th><th onclick="s(2)">Depth <span class="si">&#8597;</span></th><th onclick="s(3)">Words <span class="si">&#8597;</span></th><th onclick="s(4)">Sources <span class="si">&#8597;</span></th><th onclick="s(5)">Date <span class="si">&#8597;</span></th></tr></thead><tbody id="b">{rows}</tbody></table></div>
<div class="pg"><span class="pg-b" id="pg-info"></span><span class="pg-s">Show: <select id="pg-ps" onchange="pg()"><option value="10">10</option><option value="20" selected>20</option><option value="30">30</option><option value="0">All</option></select></span><span class="pg-b"><button onclick="pp(-1)" id="pg-p" disabled>&#9664;</button><span id="pg-n">1</span><button onclick="pp(1)" id="pg-nn">&#9654;</button></span></div>
<div class="ft"><span>Last updated: {now}</span><span><a href="https://github.com/hoolulu/deep-research" target="_blank">deep-research</a> &mdash; Open source</span></div>
</div>
<script>
{report_data}
var D=[],CP=1,PS=20;
(function(){{var r=document.getElementById('b');for(var i=0;i<r.children.length;i++)D.push(r.children[i]);}})();
function f(){{document.querySelectorAll('.lc').forEach(function(x){{x.classList.remove('s')}});var q=document.getElementById('q').value.toLowerCase(),l=document.getElementById('l').value,m=document.getElementById('m').value,c=0;for(var i=0;i<D.length;i++){{var x=D[i];var ok=(!l||x.dataset.lang==l)&&(!m||x.dataset.mode==m)&&(!q||x.querySelector('a').textContent.toLowerCase().indexOf(q)>=0);x.dataset.f=ok?'1':'0';if(ok)c++;}}document.getElementById('c').textContent=c+' reports';CP=1;pg();}}
function fc(b){{var l=document.getElementById('l');var all=document.querySelectorAll('.lc');all.forEach(function(x){{x.classList.toggle('s',x===b)}});l.value=b.dataset.lc;f();}}
var sd={{}};
function s(k){{var h=event.currentTarget;sd[k]=sd[k]==='asc'?'desc':'asc';document.querySelectorAll('thead th').forEach(function(t){{t.classList.remove('s')}});h.classList.add('s');var d=sd[k];h.querySelector('.si').innerHTML=d==='asc'?'&#8593;':'&#8595;';D.sort(function(a,b){{var va,vb,ca=a.children[k+1],cb=b.children[k+1];if(k===0){{va=a.querySelector('a').textContent;vb=b.querySelector('a').textContent;}}else if(k===3){{va=p(ca.textContent);vb=p(cb.textContent);}}else if(k===4){{va=parseInt(ca.textContent)||0;vb=parseInt(cb.textContent)||0;}}else{{va=ca.textContent;vb=cb.textContent;}}var c=typeof va==='number'?va-vb:String(va).localeCompare(String(vb));return d==='asc'?c:-c;}});var tb=document.getElementById('b');for(var i=0;i<D.length;i++)tb.appendChild(D[i]);CP=1;pg();}}
function p(s){{var m=s.match(/([\\d.]+)([wk]?)/);if(!m)return 0;var n=parseFloat(m[1]);if(m[2]==='w')return n*10000;if(m[2]==='k')return n*1000;return n||0;}}
function pg(){{PS=parseInt(document.getElementById('pg-ps').value)||D.length;var t=D.filter(function(x){{return x.dataset.f=='1'}});var tp=PS?Math.ceil(t.length/PS):1;if(CP>tp)CP=tp;if(CP<1)CP=1;for(var i=0;i<D.length;i++){{var x=D[i];var ok=x.dataset.f=='1';if(ok&&PS){{var ti=D.slice(0,i+1).filter(function(y){{return y.dataset.f=='1'}}).length-1;var pi=Math.floor(ti/PS)+1;ok=(pi==CP)}}x.classList.toggle('hidden',!ok)}}document.getElementById('pg-p').disabled=CP<=1;document.getElementById('pg-nn').disabled=CP>=tp;document.getElementById('pg-n').textContent=tp?'Page '+CP+' of '+tp:'No results';var ps=document.getElementById('pg-ps');document.getElementById('pg-info').textContent=t.length+' reports'+(PS&&PS<D.length?' (showing '+Math.min(PS,t.length-CP*PS+PS)+')':'')}}
function pp(d){{CP+=d;pg()}}
{preview_js}
</script></body></html>'''
    with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(h)
    if local:
        pass


def gen_favicon(out_dir):
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#0969da"/><text x="32" y="44" text-anchor="middle" font-size="36" font-weight="bold" fill="white" font-family="sans-serif">DR</text></svg>'
    with open(os.path.join(out_dir, 'favicon.svg'), 'w', encoding='utf-8') as f:
        f.write(svg)


def main():
    local = '--local' in sys.argv
    use_fallback = '--fallback' in sys.argv
    reports = []

    # Walk reports/ directory
    for root, dirs, files in os.walk(REPORTS_DIR):
        for fname in sorted(files):
            if not fname.endswith('.md'):
                continue
            path = os.path.join(root, fname)
            try:
                with open(path, encoding='utf-8') as f:
                    reports.append(parse_content(f.read(), path))
            except (FileNotFoundError, OSError) as e:
                if use_fallback:
                    rel = os.path.relpath(path, REPORTS_DIR).lstrip('./')
                    full_path = f'reports/{rel}'
                    try:
                        resp = _api_get(f'contents/{full_path}')
                        text = base64.b64decode(resp['content']).decode('utf-8')
                        reports.append(parse_content(text, full_path))
                        print(f'  API fallback: {full_path}')
                    except Exception as e2:
                        print(f'  BOTH FAILED {fname}: {e2}')
                else:
                    print(f'  SKIP (not found): {fname}')

    out = LOCAL_OUTPUT_DIR if local else OUTPUT_DIR
    reports.sort(key=lambda r: r['date'], reverse=True)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, 'reports.json'), 'w', encoding='utf-8') as f:
        json.dump(reports, f, ensure_ascii=False, indent=2)
    gen_html(reports, local=local, out_dir=out)
    gen_favicon(out)
    loc = '(local report browser)' if local else '(GitHub Pages)'
    print(f'Done: {len(reports)} reports -> {out}/ {loc}')


if __name__ == '__main__':
    main()
