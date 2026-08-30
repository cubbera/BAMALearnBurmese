# -*- coding: utf-8 -*-
# BAMA Book 2 — Home Talk
# Everyday family Burmese for primary-school-age heritage learners.
#
# Script content verified against John Okell's "Burmese by Ear" (SOAS),
# Appendix 2 "Outline description of Burmese script" (sections 2-3),
# cross-checked with the BAMA Basic Scripts Cheatsheet and the
# traditional 33-consonant + tone-mark system described on Wikipedia's
# "Burmese alphabet" article.
#
# ROMANIZATION (Okell's system, used consistently throughout):
#   low tone     — no accent mark               (e.g. ka, ki, ku)
#   creaky tone  — ACUTE accent                  (e.g. ká, kí, kú)
#   plain high   — GRAVE accent                  (e.g. kà, kì, kù)
#   stopped      — final -q (glottal stop)
#   nasal        — final -n
# No colons are added to mark vowel length; tone is carried by the
# accent alone, per Okell's convention.
#
# VOWEL SIGN KEY FACTS (confirmed against BBE Appendix 2 §3.1):
#   - For the "a" rhyme, CREAKY tone is written with NO vowel sign at
#     all — a bare consonant is read -á by default. This is easy to
#     get wrong (an earlier draft of this book got it wrong) so it's
#     called out explicitly in Unit 8.
#   - For "i" and "u", the SHORT sign (ိ / ု) carries creaky tone and
#     the LONG sign (ီ / ူ) carries low tone; add း for high tone.
#   - For "e", low = ေ, creaky = ေ့, high = ေး.
#   - "eh" and "aw" are the two vowels whose low-tone spelling uses a
#     different base glyph (ယ်/ော်) from their creaky/high spellings
#     (ဲ,ဲ့/ော,ော့) — genuinely trickier, so each gets its own unit.

import json

UNITS = json.load(open("data/book2-units.json", encoding="utf-8"))
UNITS.sort(key=lambda u: u["n"])


data_json = json.dumps(UNITS, ensure_ascii=False)

SOCIAL_SVG = '''
    <div class="social-row">
      <a href="https://www.facebook.com/bamalearnburmese" target="_blank" rel="noopener" aria-label="Facebook">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M15 8.5h-2a1.5 1.5 0 0 0-1.5 1.5v2H15l-.4 3H11.5v7h-3v-7H6.5v-3h2V9.5A4 4 0 0 1 12.5 5.5H15v3z"/></svg>
      </a>
      <a href="http://instagram.com/bamalearnburmese" target="_blank" rel="noopener" aria-label="Instagram">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="4" y="4" width="16" height="16" rx="4"/><circle cx="12" cy="12" r="3.4"/><circle cx="16.6" cy="7.4" r="0.6" fill="currentColor" stroke="none"/></svg>
      </a>
      <a href="https://www.pinterest.com/bamalearnburmese/" target="_blank" rel="noopener" aria-label="Pinterest">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="8.5"/><path d="M9.5 18c.8-3 1.4-5.4 1.9-7.3.3-1.2 1-1.9 2-1.9 1.1 0 1.8.8 1.8 2 0 1.6-1 3.9-1.5 5.1-.4.9.2 1.7 1.1 1.7 1.4 0 2.5-1.5 2.5-3.6 0-1.9-1.3-3.4-3.7-3.4-2.5 0-4.1 1.9-4.1 3.9 0 .7.2 1.2.6 1.6"/></svg>
      </a>
      <a href="https://quizlet.com/BAMALearnBurmese/classes" target="_blank" rel="noopener" aria-label="Quizlet">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="5" y="5" width="12" height="9" rx="1.2"/><rect x="8" y="10" width="12" height="9" rx="1.2" fill="var(--paper)"/></svg>
      </a>
    </div>
'''

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Book 2 — Home Talk — BAMA Learn Burmese</title>
<meta name="description" content="Book 2: Home Talk — everyday family Burmese for kids growing up abroad. 33 units covering consonants, digits, every vowel in all three tones, tone marks, medials, and final consonants.">
<link rel="icon" href="assets/img/favicon.png">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

<header class="site">
  <div class="nav-wrap">
    <a class="brand" href="index.html">
      <span class="mark mm">ဗ</span>
      <span class="wordmark">BAMA Learn Burmese</span>
    </a>
    <input type="checkbox" id="nav-toggle">
    <label class="nav-btn" for="nav-toggle">MENU</label>
    <nav class="primary">
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="lessons.html" class="active">Lessons</a></li>
        <li><a href="resources.html">Resources</a></li>
        <li><a href="downloads.html">Downloads</a></li>
      </ul>
    </nav>
  </div>
</header>

<div class="book-header">
  <span class="eyebrow">Book 2</span>
  <h1>Home Talk</h1>
  <p class="lede">{len(UNITS)} units of everyday family Burmese — the phrases parents and children actually say around the house. Organized like Book 1: Foundations, Manners &amp; Respect, Everyday Life, and First Conversations. Written for kids who hear Burmese at home but go to school in English, so the language has something to hold on to.</p>

  <p class="lede" style="margin-top:-0.6rem;">Every unit follows the same shape: a short family conversation that gets a little longer each time, and six vocabulary words to go with it. Underneath, as a bonus, each unit also teaches one small piece of the Burmese script — but that's a side dish, not the main course. <span style="font-family:'IBM Plex Mono',monospace; font-size:0.78rem;">M</span> = Mummy, <span style="font-family:'IBM Plex Mono',monospace; font-size:0.78rem;">D</span> = Daddy, <span style="font-family:'IBM Plex Mono',monospace; font-size:0.78rem;">G</span> = grandparent, <span style="font-family:'IBM Plex Mono',monospace; font-size:0.78rem;">K</span> = older brother, <span style="font-family:'IBM Plex Mono',monospace; font-size:0.78rem;">C</span> = the child.</p>

  <div class="goal-box">
    <strong>By the end of Book 2, you can</strong>
    Greet your family and elders properly, welcome a guest, eat together with the right manners, take care of yourself, talk about food, school, feelings, colors, weather, animals, playtime, your body, days of the week, the zoo, the river, pets, and more — with the complete everyday Burmese script picked up along the way, unit by unit, as a bonus.
  </div>

  <div class="progress-bar"><span id="progress-fill"></span></div>
  <p class="progress-label" id="progress-label">0 / {len(UNITS)} read</p>
  <div class="resume-row">
    <a class="btn small" id="resume-btn" href="#unit-1">Start Unit 1</a>
  </div>

  <p class="romanization-note"><strong>Romanization:</strong> this book follows John Okell's system from <em>Burmese by Ear</em> (SOAS) — syllables hyphenated, aspirated consonants marked with an apostrophe (p&#39; t&#39; k&#39; c&#39;), tone marked by accent alone: no accent for low tone, an ACUTE accent for creaky tone (á í ú é), a GRAVE accent for plain high tone (à ì ù è). Subject pronouns are dropped wherever natural spoken Burmese would drop them — this is a spoken-register book, not textbook Burmese.</p>
</div>

<div class="toc-wrap" id="toc-wrap"></div>

<div id="units"></div>

<button class="back-to-top" id="back-to-top" aria-label="Back to top / contents">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
</button>

<footer class="site">
  <div class="footer-wrap">
{SOCIAL_SVG}
    <p class="footer-copy">© 2026 BAMA Learn Burmese</p>
  </div>
</footer>

<script>
const UNITS = {data_json};
const STORAGE_KEY = "bama-book2-read";

function getRead() {{
  try {{ return new Set(JSON.parse(localStorage.getItem(STORAGE_KEY)) || []); }}
  catch (e) {{ return new Set(); }}
}}
function setRead(readSet) {{
  localStorage.setItem(STORAGE_KEY, JSON.stringify([...readSet]));
}}

function renderTOC(readSet) {{
  const wrap = document.getElementById("toc-wrap");
  const parts = [];
  UNITS.forEach(u => {{ if (!parts.includes(u.part)) parts.push(u.part); }});
  wrap.innerHTML = parts.map(part => {{
    const us = UNITS.filter(u => u.part === part);
    return `
      <div class="part-label">${{part}}</div>
      <div class="toc-grid">
        ${{us.map(u => `
          <a class="toc-item ${{readSet.has(u.n) ? 'is-read' : ''}}" href="#unit-${{u.n}}" data-n="${{u.n}}">
            <span class="tn">${{String(u.n).padStart(2,'0')}}</span>
            <span class="tl mm">${{u.write.letters[0]}}</span>
            <span class="tt">${{u.theme}}</span>
            <span class="check"></span>
          </a>
        `).join("")}}
      </div>
    `;
  }}).join("");
}}

function updateProgress(readSet) {{
  const pct = Math.round((readSet.size / UNITS.length) * 100);
  document.getElementById("progress-fill").style.width = pct + "%";
  document.getElementById("progress-label").textContent = `${{readSet.size}} / ${{UNITS.length}} read`;
  const resumeBtn = document.getElementById("resume-btn");
  const firstUnread = UNITS.find(u => !readSet.has(u.n));
  if (readSet.size === 0) {{
    resumeBtn.textContent = "Start Unit 1";
    resumeBtn.href = "#unit-1";
  }} else if (firstUnread) {{
    resumeBtn.textContent = `Resume — Unit ${{firstUnread.n}}`;
    resumeBtn.href = `#unit-${{firstUnread.n}}`;
  }} else {{
    resumeBtn.textContent = "Book complete — review Unit 1";
    resumeBtn.href = "#unit-1";
  }}
}}

function dlgLine(l) {{
  const [speaker, mm, rom, eng] = l;
  const label = speaker || "•";
  return `<div class="dlg-line">
    <span class="dlg-speaker">${{label}}</span>
    <span class="dlg-body"><span class="mm">${{mm}}</span><span class="rom">${{rom}}</span><span class="eng">${{eng}}</span></span>
  </div>`;
}}

function vocabItem(v) {{
  return `<div class="vocab-item"><span class="mm">${{v[0]}}</span> <span class="rom">${{v[1]}}</span><span class="eng">${{v[2]}}</span></div>`;
}}

function writeLetterBox(letter, name) {{
  return `<div class="guide-box">
    <div class="guide-lines">
      <div class="rl top"></div>
      <div class="bl top"></div>
      <div class="guide-letter mm">${{letter}}</div>
      <div class="bl bottom"></div>
      <div class="rl bottom"></div>
    </div>
    <p class="write-hint" style="text-align:center; margin-top:0.4rem;">${{name}}</p>
  </div>`;
}}

function renderUnits() {{
  const wrap = document.getElementById("units");
  wrap.innerHTML = UNITS.map((u, idx) => {{
    const next = UNITS[idx + 1];
    const rowLetters = u.write.letters.join(" ");
    return `
    <section class="unit" id="unit-${{u.n}}">
      <span class="unit-part">${{u.part}} — Unit ${{String(u.n).padStart(2,'0')}} of ${{UNITS.length}}</span>
      <div class="unit-head">
        <span class="unit-num">UNIT ${{u.n}}/${{UNITS.length}}</span>
        <span class="unit-letter mm multi">${{rowLetters}}</span>
      </div>
      <h2>${{u.theme}}</h2>
      <div class="goal-box"><strong>You will be able to</strong>${{u.goal}}</div>

      <div class="section-block">
        <div class="section-head"><span class="sn">01</span><h3>Conversation</h3></div>
        <div class="main-block">
          ${{u.main.lines.map(dlgLine).join("")}}
        </div>
      </div>

      <div class="section-block">
        <div class="section-head"><span class="sn">02</span><h3>Vocabulary</h3></div>
        <div class="vocab-grid">${{u.vocab.map(vocabItem).join("")}}</div>
      </div>

      <div class="section-block">
        <div class="section-head"><span class="sn">03</span><h3>${{u.script}}</h3></div>
        <p class="write-hint" style="margin-bottom:0.9rem;">${{u.write.desc}}</p>
        <div class="write-guide">
          ${{u.write.letters.map((ltr, i) => writeLetterBox(ltr, u.write.names[i])).join("")}}
        </div>
        <p class="write-hint" style="margin-top:1rem;">Guide lines follow the official Myanmar four-line system: red marks the full letter height, blue marks the main body.</p>
        <a class="practice-sheet-link" href="downloads.html#stroke-sheet">
          <img src="assets/img/stroke-practice-sheet.png" alt="Stroke practice sheet thumbnail">
          <span class="psl-text"><strong>Stroke Practice Sheet</strong>By John Okell — real stroke-direction arrows for the alphabet, in Downloads.</span>
        </a>
      </div>

      <div class="mark-read-row">
        <button class="mark-read" data-n="${{u.n}}">Mark as read</button>
        ${{next ? `<span class="next-unit">Next: <a href="#unit-${{next.n}}">Unit ${{next.n}} — ${{next.theme}}</a></span>` : `<span class="next-unit">That's Book 2 — nice work.</span>`}}
      </div>
    </section>
    `;
  }}).join("");
}}

function initBackToTop() {{
  const btn = document.getElementById("back-to-top");
  window.addEventListener("scroll", () => {{
    if (window.scrollY > 600) btn.classList.add("is-visible");
    else btn.classList.remove("is-visible");
  }});
  btn.addEventListener("click", () => {{
    window.scrollTo({{ top: 0, behavior: "smooth" }});
  }});
}}

function init() {{
  let readSet = getRead();
  renderTOC(readSet);
  updateProgress(readSet);
  renderUnits();
  initBackToTop();

  document.addEventListener("click", (e) => {{
    const btn = e.target.closest(".mark-read");
    if (!btn) return;
    const n = parseInt(btn.getAttribute("data-n"), 10);
    let rs = getRead();
    if (rs.has(n)) {{ rs.delete(n); btn.classList.remove("is-done"); btn.textContent = "Mark as read"; }}
    else {{ rs.add(n); btn.classList.add("is-done"); btn.textContent = "Read ✓"; }}
    setRead(rs);
    renderTOC(rs);
    updateProgress(rs);
  }});

  document.querySelectorAll(".mark-read").forEach(btn => {{
    const n = parseInt(btn.getAttribute("data-n"), 10);
    if (readSet.has(n)) {{ btn.classList.add("is-done"); btn.textContent = "Read ✓"; }}
  }});
}}

init();
</script>

</body>
</html>
"""

with open("book2.html", "w", encoding="utf-8") as f:
    f.write(HTML)

print("book2.html written:", len(HTML), "bytes;", len(UNITS), "units")
