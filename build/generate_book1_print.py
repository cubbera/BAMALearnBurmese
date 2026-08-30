import json

with open("data/book1-units.json", encoding="utf-8") as f:
    units = json.load(f)

def dlg_rows(lines):
    out = ""
    for speaker, mm, rom, eng in lines:
        out += f'''<div class="p-line">
          <span class="spk">{speaker if speaker in ("A","B") else "\u2022"}</span>
          <span class="p-body"><span class="mm">{mm}</span><span class="rom">{rom}</span><span class="eng">{eng}</span></span>
        </div>'''
    return out

def vocab_rows(vocab):
    return "".join(
        f'<div class="v-item"><span class="mm">{v[0]}</span> <span class="rom">{v[1]}</span><span class="eng">{v[2]}</span></div>'
        for v in vocab
    )

def grammar_rows(grammar):
    out = ""
    for g in grammar:
        ex = "".join(
            f'<div class="g-ex"><span class="mm">{e[0]}</span><span class="rom">{e[1]}</span><span class="eng">{e[2]}</span></div>'
            for e in g["examples"]
        )
        out += f'''<div class="g-point">
          <h4>{g["title"]}</h4>
          <p>{g["explain"]}</p>
          {ex}
        </div>'''
    return out

unit_html = ""
current_part = None
for u in units:
    part_break = ""
    if u["part"] != current_part:
        current_part = u["part"]
        part_break = f'<div class="part-page"><h2>{current_part}</h2></div>'
    unit_html += part_break + f"""
    <section class="unit">
      <div class="unit-head">
        <span class="unit-num">UNIT {u['n']:02d}</span>
        <span class="unit-letter mm">{u['letter']}</span>
      </div>
      <h2>{u['theme']}</h2>
      <p class="unit-sub">{u['letter']} ({u['name']})</p>
      <div class="goal">{u['goal']}</div>

      <div class="block">
        <span class="lbl">01 · Main</span>
        {f'<p class="narration-p">{" ".join(u["main"]["narration"])}</p>' if u["main"].get("narration") else ""}
        {dlg_rows(u['main']['lines'])}
        <p class="listen-note">Audio for this unit: bamalearnburmese.com/book1.html#unit-{u['n']}</p>
      </div>

      <div class="block">
        <span class="lbl">02 · Culture Note</span>
        <p class="culture-p">{u.get('culture','')}</p>
      </div>

      <div class="block">
        <span class="lbl">03 · Vocabulary</span>
        <div class="v-grid">{vocab_rows(u['vocab'])}</div>
      </div>

      <div class="block">
        <span class="lbl">04 · Grammar</span>
        {grammar_rows(u['grammar'])}
      </div>

      <div class="block write-block">
        <div class="guide-box">
          <div class="rl"></div><div class="bl"></div>
          <div class="big-letter mm">{u['letter']}</div>
          <div class="bl"></div><div class="rl"></div>
        </div>
        <p class="write-text">{u['write']}<br><em style="font-size:8.5pt;">See the Stroke Practice Sheet (John Okell) in Downloads for real stroke-direction arrows.</em></p>
      </div>
    </section>
    """

toc_html = ""
current_part_toc = None
for u in units:
    if u["part"] != current_part_toc:
        current_part_toc = u["part"]
        toc_html += f'<div class="toc-part">{current_part_toc}</div>'
    toc_html += f'<div class="toc-row"><span class="tn">{u["n"]:02d}</span><span class="tl mm">{u["letter"]}</span><span class="tt">{u["theme"]}</span></div>'

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Book 1 — Survival Kit</title>
<style>
@font-face {{
  font-family: 'Noto Sans Myanmar';
  src: url('assets/fonts/NotoSansMyanmar-Regular.ttf') format('truetype');
  font-weight: 400;
}}
@font-face {{
  font-family: 'Noto Sans Myanmar';
  src: url('assets/fonts/NotoSansMyanmar-Bold.ttf') format('truetype');
  font-weight: 700;
}}
* {{ box-sizing: border-box; }}
:root {{
  --ink: #221b16; --paper: #f4efe1; --paper-2: #eae1c8;
  --jade: #1f5d42; --gold: #ab7f28; --umber: #7a4a23; --muted: #5c5240; --line: #ddd2ac;
}}
body {{
  margin: 0; color: var(--ink); background: var(--paper);
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 13pt; line-height: 1.5;
}}
.mm {{ font-family: 'Noto Sans Myanmar', sans-serif; }}
h1, h2 {{ font-family: Georgia, serif; font-weight: 700; margin: 0 0 0.2em; }}

.cover {{ height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; page-break-after: always; padding: 0 0.5in; }}
.cover .mark {{ width: 64px; height: 64px; border: 1px solid var(--line); background: var(--paper-2); display: flex; align-items: center; justify-content: center; font-family: 'Noto Sans Myanmar', sans-serif; font-weight: 700; font-size: 2.2rem; color: var(--jade); margin-bottom: 1.2rem; }}
.cover .eyebrow {{ font-family: 'Courier New', monospace; font-size: 10pt; letter-spacing: 0.12em; color: var(--gold); text-transform: uppercase; margin-bottom: 0.5rem; }}
.cover h1 {{ font-size: 24pt; margin-bottom: 0.4rem; }}
.cover p {{ color: var(--muted); font-size: 11pt; }}
.cover .goal {{ font-size: 10pt; color: var(--ink); background: var(--paper-2); border-left: 2px solid var(--umber); padding: 0.6rem 0.8rem; text-align: left; margin-top: 1rem; }}
.cover .footnote {{ position: absolute; bottom: 1.6rem; font-size: 9pt; color: var(--muted); }}

.toc-page {{ page-break-after: always; padding: 0.9in 0.5in 0; }}
.toc-page h2 {{ font-size: 15pt; margin-bottom: 0.8rem; }}
.toc-part {{ font-family: 'Courier New', monospace; font-size: 9pt; letter-spacing: 0.1em; text-transform: uppercase; color: var(--jade); margin: 1rem 0 0.4rem; }}
.toc-row {{ display: flex; align-items: baseline; gap: 0.5rem; padding: 0.22rem 0; border-bottom: 1px dotted var(--line); font-size: 10.5pt; }}
.toc-row .tn {{ font-family: 'Courier New', monospace; color: var(--muted); width: 1.5em; flex: none; }}
.toc-row .tl {{ color: var(--jade); font-size: 12pt; flex: none; width: 1.5em; }}
.toc-row .tt {{ flex: 1; }}

.part-page {{ page-break-before: always; height: 100vh; display: flex; align-items: center; justify-content: center; }}
.part-page h2 {{ font-family: 'Courier New', monospace; font-size: 13pt; letter-spacing: 0.14em; text-transform: uppercase; color: var(--jade); }}

.unit {{ padding: 0.7in 0.5in 0.3in; page-break-before: always; }}
.unit-head {{ display: flex; align-items: baseline; gap: 0.5rem; }}
.unit-num {{ font-family: 'Courier New', monospace; color: var(--gold); font-size: 10pt; }}
.unit-letter {{ color: var(--jade); font-size: 22pt; }}
.unit h2 {{ font-size: 18pt; margin: 0.15rem 0 0.1rem; }}
.unit-sub {{ color: var(--muted); font-size: 10pt; margin: 0 0 0.6rem; }}
.goal {{ font-size: 10.5pt; background: var(--paper-2); border-left: 2px solid var(--umber); padding: 0.5rem 0.7rem; margin-bottom: 1rem; }}

.block {{ margin-bottom: 1rem; }}
.lbl {{ display: block; font-family: 'Courier New', monospace; font-size: 9pt; letter-spacing: 0.09em; text-transform: uppercase; color: var(--gold); margin-bottom: 0.4rem; }}

.p-line {{ display: flex; gap: 0.5rem; padding: 0.3rem 0; border-bottom: 1px dotted var(--line); align-items: flex-start; }}
.spk {{ flex: none; width: 1.1rem; height: 1.1rem; border-radius: 50%; background: var(--ink); color: var(--paper); font-family: 'Courier New', monospace; font-size: 8pt; display: flex; align-items: center; justify-content: center; }}
.p-body .mm {{ font-size: 12.5pt; display: block; }}
.p-body .rom {{ color: var(--umber); font-family: 'Courier New', monospace; font-size: 9.5pt; display: block; }}
.p-body .eng {{ color: var(--muted); font-size: 10pt; display: block; }}
.listen-note {{ font-size: 8.5pt; color: var(--muted); font-style: italic; margin: 0.5rem 0 0; }}
.narration-p {{ font-family: Georgia, serif; font-style: italic; font-size: 10pt; color: var(--muted); margin: 0 0 0.6rem; padding-bottom: 0.5rem; border-bottom: 1px dotted var(--line); }}
.culture-p {{ font-size: 10pt; line-height: 1.55; background: var(--paper-2); border: 1px solid var(--line); border-left: 3px solid var(--jade); padding: 0.7rem 0.8rem; margin: 0; }}

.v-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 0.15rem 1rem; }}
.v-item {{ font-size: 10.5pt; padding: 0.2rem 0; border-bottom: 1px dotted var(--line); }}
.v-item .mm {{ font-size: 12pt; }}
.v-item .rom {{ color: var(--umber); font-family: 'Courier New', monospace; font-size: 9pt; }}
.v-item .eng {{ color: var(--muted); display: block; font-size: 9.5pt; }}

.g-point {{ border: 1px solid var(--line); padding: 0.6rem 0.7rem; margin-bottom: 0.6rem; }}
.g-point h4 {{ margin: 0 0 0.3rem; font-size: 11pt; color: var(--jade); }}
.g-point p {{ font-size: 10pt; margin: 0 0 0.4rem; }}
.g-ex {{ display: flex; flex-wrap: wrap; gap: 0.25rem 0.5rem; align-items: baseline; font-size: 10pt; padding: 0.15rem 0; border-top: 1px dotted var(--line); }}
.g-ex .mm {{ font-size: 11.5pt; }}
.g-ex .rom {{ color: var(--umber); font-family: 'Courier New', monospace; font-size: 9pt; }}
.g-ex .eng {{ color: var(--muted); }}

.write-block {{ display: flex; align-items: center; gap: 0.8rem; }}
.guide-box {{ flex: none; width: 1.15in; position: relative; padding: 0.15in 0; }}
.guide-box .rl {{ height: 2px; background: #b5433a; margin: 0 0 0.32in; }}
.guide-box .bl {{ height: 1px; background: #3a6ea5; }}
.big-letter {{ font-size: 26pt; color: var(--ink); text-align: center; padding: 0.12in 0; }}
.write-text {{ margin: 0; font-size: 10pt; color: var(--muted); flex: 1; }}

.backpage {{ padding: 1.2in 0.6in; page-break-before: always; }}
.backpage h2 {{ font-size: 14pt; }}
.backpage p {{ font-size: 10.5pt; color: var(--muted); }}
</style>
</head>
<body>

<div class="cover">
  <span class="mark mm">ဗ</span>
  <span class="eyebrow">Book 1</span>
  <h1>Survival Kit</h1>
  <p>Thirty-three units, ground zero to basic conversation — one Burmese consonant per unit, from က to အ. Following John Okell's <em>Burmese by Ear</em>, one layer at a time.</p>
  <div class="goal"><strong>By the end of this book</strong> you can introduce yourself, order food and pay, take a taxi, shop and bargain, ask directions, talk about work and family, handle a health concern, and hold a full polite conversation in Burmese.</div>
  <span class="footnote">BAMA Learn Burmese &nbsp;·&nbsp; bamalearnburmese.com</span>
</div>

<div class="toc-page">
  <span style="font-family:'Courier New',monospace;font-size:9pt;letter-spacing:0.1em;color:var(--gold);text-transform:uppercase;">Contents</span>
  <h2>33 Units</h2>
  {toc_html}
</div>

{unit_html}

<div class="backpage">
  <span class="mm" style="display:inline-flex;width:40px;height:40px;border:1px solid var(--line);background:var(--paper-2);align-items:center;justify-content:center;font-weight:700;font-size:1.3rem;color:var(--jade);">ဗ</span>
  <h2 style="margin-top:1rem;">Keep going</h2>
  <p>The full interactive version of this book — with audio as it's added, and progress tracking — lives at <strong>bamalearnburmese.com/book1.html</strong>. More cheatsheets and resources: <strong>bamalearnburmese.com/downloads.html</strong>.</p>
  <p>Facebook &amp; Instagram: @bamalearnburmese &nbsp;·&nbsp; Quizlet: BAMALearnBurmese</p>
</div>

</body>
</html>
"""

with open("book1-print.html", "w", encoding="utf-8") as f:
    f.write(HTML)

print("book1-print.html written:", len(HTML), "bytes,", len(units), "units")
