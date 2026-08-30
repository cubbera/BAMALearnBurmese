BAMA LEARN BURMESE — SITE FILES (v3)
======================================

Plain HTML/CSS/JS site — no build step, no Wix. Upload the whole
folder to bamalearnburmese.com as-is.

WHAT CHANGED IN THIS ROUND
----------------------------
- FIXED A REAL FONT BUG: stacked/complex Myanmar script (kinzi
  formations like the ်ဂ in မင်္ဂလာပါ) was rendering as a broken "+"
  because the self-hosted Noto Sans Myanmar font (assets/fonts/) was
  an old, incomplete build pulled from a random GitHub mirror. Fixed
  by re-fetching the current, complete build (v2.105) directly from
  Google's own noto-fonts repository. Verified on both the web pages
  and the PDF — kinzi and consonant stacking now render correctly
  everywhere.
- Stroke practice: you sent a real handwriting-practice sheet with
  genuine stroke-direction arrows. I looked closely at it — the row
  structure (5/6/5/5/5/5/3) strongly matches the traditional 33-
  consonant grouping, and row 1 checks out against letterforms I
  can verify, but I couldn't get to real confidence mapping every
  individual cell to a specific letter without risking teaching the
  wrong stroke order for that letter — worse than not providing one.
  So I used it exactly as given: the unmodified image, front and
  center in Downloads (both as a download and embedded inline), and
  linked from every unit's "Learn to write" section instead of
  guessing at a per-letter crop. assets/img/stroke-practice-sheet.png
  is the file if you want to tell me the correct per-letter mapping —
  I'll gladly wire up accurate per-unit crops once I have it from you.
- Removed the placeholder arrow icon I'd invented for the write guide
  (it wasn't based on anything real, just a generic curl) — the
  four-line red/blue guide box stays, since that's a genuine general
  reference, not a per-letter guess.


STILL IN PLACE FROM EARLIER ROUNDS
------------------------------------
- Every unit has a Culture Note — real pragmatics (when a phrase is
  actually used, what it signals, how a native speaker reads it),
  not just translation. build/culture_notes.py is the source.
- Paper background + jade green theme, roomy phone-first layout.
- One continuous story across all 33 units (you land in Yangon,
  meet Ko Aung, later his friend Su) with dialogue length growing
  4 → 9 lines as the book progresses, including two narrated-
  paragraph units near the end.
- Okell's romanization system throughout.
- Burmese by Ear (PDF + audio) credited as Okell's original work,
  linked at the top of Downloads.
- Mark-as-read + resume (localStorage), back-to-top button, and the
  mobile-sized (4.5in x 8in) PDF.

STRUCTURE
---------
index.html             Home
lessons.html            Bookshelf (Book 1 lives here; room for more later)
resources.html          Compact one-screen resource list
downloads.html           Burmese by Ear (PDF + audio) → cheatsheets → Book 1 PDF
book1.html               Book 1 — Survival Kit, all 33 units
data/book1-units.json      Source of truth for every unit's content
build/                    Scripts that regenerate the site from the data file:
  units_source.py           the actual authored content (edit THIS, then
                             run it — it overwrites data/book1-units.json)
  fix_main_burmese.py        a one-time patch that filled in the Burmese-
                              script text for dialogue lines; safe to re-run,
                              but new units you add to units_source.py need
                              their own Burmese text written directly in
                              the "main" field, not through this patch
  generate_book1.py          rebuilds book1.html from the data file
  generate_book1_print.py    rebuilds book1-print.html (the PDF source)

REGENERATING BOOK 1
--------------------
All run from the SITE ROOT, in this order:
  python3 build/units_source.py           # base data: vocab, grammar, writing guide
  python3 build/narrative_v2.py           # overlays the story dialogue on top
  python3 build/culture_notes.py          # overlays the culture note on top
  python3 build/generate_book1.py         # rebuilds the web page
  python3 build/generate_book1_print.py   # rebuilds the PDF's source HTML
Then render the PDF from book1-print.html with a headless browser's
print-to-PDF at 4.5in x 8in (Chromium/Playwright handles Burmese
script shaping correctly; wkhtmltopdf and plain reportlab do not):
  page.pdf(path="assets/pdf/book1-survival-kit.pdf",
           width="4.5in", height="8in", print_background=True)

WHAT TO UPLOAD, BY TYPE
------------------------
Images (assets/img/):
  scripts-cheatsheet.png    Okell's Basic Scripts Cheatsheet
  suffixes-cheatsheet.png   Okell's Basic Suffixes Cheatsheet
  consonants-33.png         the 33 initial consonants chart
  favicon.png                 replace with your own logo file whenever ready

Recordings (assets/audio/book1/):
  unit-01.mp3 … unit-33.mp3
  Each unit's Listening block checks for its file automatically and
  swaps in a real player the moment it exists — no code changes needed.

A NOTE ON ACCURACY
--------------------
Units 1–4, 9, 21, and 23 draw directly on phrases and vocabulary I
found in your uploaded Burmese by Ear PDF, so those are on the
firmest ground. The remaining units follow Okell's spelling
conventions carefully, but the vocabulary itself is my own
extrapolation to fill out situational themes BBE doesn't cover in
as much depth. Before this goes fully live, it's worth having a
native speaker — or the BBE audio itself — check the units built
without a direct source, especially anything you'll print and hand
to someone.

The culture notes carry a different, higher kind of risk than the
vocabulary does. They're built from general Southeast Asian /
Theravada Buddhist sociolinguistic patterns I have reasonable
confidence in (the mingalar-ba/street-greeting distinction, kinship-
term address, indirect refusal, bargaining norms), not from lived
experience or native cultural authority — and I deliberately hedged
language like "often" and "commonly" rather than stating them as
fixed rules, because that's genuinely what they are: patterns, not
laws, and they'll vary by region, generation, and relationship. This
is the section most worth a native speaker's eyes before it reaches
a real student, more so even than the vocabulary.
