# Right to left

Rules for screens in Arabic, Persian, Urdu or Hebrew, or any screen with `dir="rtl"`. Read this before the passes when the screen is right to left, or when the user asks for an Arabic or Hebrew version. Where a rule here differs from the passes in the skill, this one wins.

Most RTL slop is not decoration. It is a left to right screen with the words swapped, so the text runs one way and everything around it runs the other. Fix the direction first, then run the passes as usual.

## Direction

- The root carries `dir="rtl"` and the right `lang`, like `<html lang="ar" dir="rtl">`. Without them the browser aligns text left, picks the wrong fallback fonts and breaks punctuation at the ends of lines.
- Use logical properties everywhere, so the layout flips by itself. `margin-inline-start`, `padding-inline-end`, `inset-inline-start`, `text-align: start`, `border-start-start-radius`. In Tailwind that is `ms-*`, `me-*`, `ps-*`, `pe-*`, `start-*`, `end-*`, `text-start` and `rounded-s-*`. A hard `left` or `right`, `ml-*`, `mr-*` or `text-left` is a bug waiting for the other direction.
- The whole screen mirrors. The sidebar moves to the right, the logo sits at the top right, the primary action of a pair comes first from the right, and a back arrow points right.
- Progress bars, sliders and steppers fill from the right.
- Do not flip with `transform: scaleX(-1)` on whole containers. It mirrors the text inside too.

## Icons

- Mirror icons that show direction or order: back and forward arrows, chevrons in breadcrumbs and next buttons, undo and redo, a list indent, a reply arrow, a send icon, a sidebar toggle.
- Do not mirror icons that show a real object or a universal sign: play, pause and the media controls, a clock, a checkmark, a search glass, a phone, a download arrow pointing down, logos, and anything with Latin letters in it.
- Mirror with `[dir="rtl"] .icon-directional { transform: scaleX(-1) }` on the icon only, or pick the opposite icon from the set.

## Mixed text

- Latin words, numbers, code, emails and links inside an Arabic sentence go in `<bdi>` or get `unicode-bidi: isolate`, so `Al-Fatiha` or `v2.1` does not drag the punctuation around it to the wrong side.
- Signed numbers and changes, like `+12%` or `-3`, go in `<bdi dir="ltr">`. Otherwise the sign jumps to the far side and reads `12%+`.
- Content the user typed, like names, titles and search queries, goes in `<bdi>`, which picks its direction from its own first strong letter. Put `dir="auto"` on an inline element, not on a table cell or a block, or the whole cell flips its alignment and runs into the next column.
- Inputs for email, URLs, phone numbers and codes stay `dir="ltr"` with `text-align: end`, so they read left to right but sit on the right edge with the other fields.

## Numbers

- Choose Western digits (0 to 9) or Arabic-Indic digits (٠ to ٩) for the whole screen and never mix them. Western digits are common in North Africa and in technical products. Arabic-Indic digits suit the Gulf, Egypt and anything traditional or religious. Persian uses its own forms (۰ to ۹).
- Format with `Intl.NumberFormat("ar-EG")`, `"ar-SA"` or `"ar"` with `numberingSystem: "latn"`, instead of building strings by hand.
- Numbers still use `tabular-nums`, and figures in a column align to the end of the column, which is the left edge in RTL.

## Type

- Choose a family that was drawn for the script, with real weights, not a Latin family that falls back to a system Arabic font. Pair it with a Latin family from the same design, so mixed lines keep one texture.

| Character | Arabic interface family | Latin partner | Optional display |
| --- | --- | --- | --- |
| Precise, technical, calm | IBM Plex Sans Arabic | IBM Plex Sans | IBM Plex Mono for figures |
| Neutral, everyday | Noto Sans Arabic | Noto Sans | Noto Kufi Arabic for large headlines |
| Warm, friendly, modern | Readex Pro | Readex Pro | Reem Kufi for the hero headline only |
| Persian first | Vazirmatn | Vazirmatn | |
| Literary, traditional, religious | Noto Sans Arabic or IBM Plex Sans Arabic for the interface | the matching Latin | Noto Naskh Arabic or Amiri for headlines and reading text |

- Hebrew screens use Noto Sans Hebrew, Heebo or Rubik with the same rules, and Urdu reading text uses Noto Nastaliq Urdu.
- Cairo and Tajawal on every element, at every weight, are the Arabic equivalent of Inter that nobody chose. Keep them when they are part of a real brand, otherwise pick for the character.
- Letter spacing on Arabic is always 0. Any tracking, positive or negative, pulls the joined letters apart and breaks the word. This includes large display text.
- Arabic has no capitals, so there is no uppercase or sentence case to fix. Labels get hierarchy from size, weight and color only.
- Arabic has no italic. A browser fakes it by slanting the glyphs, which reads as broken. Use weight or color.
- Arabic looks smaller than Latin at the same size. Body text is 15 to 17, captions no smaller than 13.
- Arabic needs more line height, because dots and vowel marks sit above and below the line. Body 1.6 to 1.8, headings 1.3 to 1.4. The tight 1.02 to 1.08 for Latin heroes clips marks on Arabic.
- Do not justify short interface text and do not stretch words with tatweel (ـ) to fill a line. Align to the start.

## Copy

- Arabic punctuation: the comma `،`, the semicolon `؛` and the question mark `؟`. No space before punctuation and one after it. Quotes are `«»` or `""`, chosen once.
- The rules from the Copy pass hold. No exclamation marks, no greeting headline like `أهلاً بعودتك يا أحمد! 👋`, no trailing period on labels and buttons.
- Arabic hype words count as hype: ثوري، سحري، مذهل، بلا حدود، الأفضل على الإطلاق، بضغطة زر، مدعوم بالذكاء الاصطناعي. Say what the thing does.
- Copy that reads translated, with English word order, `ال` stuck onto English words, or a different register in every label, gets rewritten in one register. Modern Standard Arabic for most products, a dialect only when the brand really speaks it.
- Short labels: `بحث`, not `ابحث عن أي شيء...`.

## Scripture and quoted text

- Quranic verses, hadith, poetry and other quoted text are copied exactly from a verified source, with their marks, and never rewritten, shortened mid verse or invented. If the screen has placeholder scripture, replace it with real text from a source the user names, or leave the exact slot and say so in the report.
- Set it in a face made for reading it, like Amiri Quran or a mushaf font for Quranic text, separate from the interface family.
- No gradient, glow, outline or animation on scripture. It carries the screen through the type, the space around it and the paper it sits on.
- The end of a verse is marked with ۝ (U+06DD) and its number in the digits of the screen, not with a glowing pill.

---

Part of unslop by Damir Sokolovsky ([@heydamir](https://x.com/heydamir)), CC BY 4.0. Keep this credit in copies and adaptations.
