# The Hair Rhythm By Tara Rose, landing page

> **DRAFT. Not final, and not approved.** Nothing here has been through the formal
> `/brand-review` gate, the founder has not signed off the copy, and the campaign it belongs
> to still has four things outstanding before launch. Treat every sentence as a proposal.
> Do not send this to a client, an agency or a stylist as finished work.

The junior stylist campaign landing page, built to **Layer 5, The Landing Page Handover**
in the Notion framework, and renamed to **The Hair Rhythm By Tara Rose** on 28 Aug on
Emma-Louise's confirmation. Canonical copy of the framework
now lives in Kate's workspace, teamspace **Junior Stylist Framework**:
<https://app.notion.com/p/88975ef7d53d82deacd4816fb414aaed>

**Renamed 28 Aug 2026.** This is the campaign's fourth name; the previous three, and why
each moved on, are in `docs/BUILD-NOTES.md`, along with the full list of what changed and
why the name moved off the tier.

This is the standalone, source-separated copy: one HTML file, four stylesheets, five small
scripts, nothing inlined. Open `index.html` over a local server and it runs.

Every open decision, every contradiction found in the source, and every deliberate
departure from the spec is written down in **[docs/BUILD-NOTES.md](docs/BUILD-NOTES.md)**.
Read that before changing copy.

---

## Run it

```bash
python -m http.server 8807 --directory "D:/WORK/Claude/claude-cowork-build/the hair rhythm"
```

Then open <http://localhost:8807/>. A server is needed rather than a double-click, because
the fonts are same-origin woff2 and `file://` blocks them.

---

## Layout

```text
the hair rhythm/
├── index.html                  markup only, no inline CSS, no inline JS
├── css/
│   ├── fonts.css               @font-face, same-origin woff2, never a CDN
│   ├── trs-core.css            the TRS design system. Shared, do not edit here
│   ├── trs-blocks.css          shared campaign blocks (hero, press strip, grids,
│   │                           dark bands, FAQ, form, footer, timeline)
│   └── the-hair-rhythm.css         this page only: Hero-B split, the entry cards,
│                               availability band, form selects, sticky bar
├── js/
│   ├── nav-scroll.js           nav shadow once the page moves
│   ├── sticky-cta.js           mobile sticky bar, IntersectionObserver
│   ├── form-prefill.js         entry card sets the reason, "a friend" reveals a field
│   ├── tracking.js             UTM / gclid / fbclid / fbp / touch capture, session
│   │                           ref, and the form POST
│   └── submit-guard.js         submit stays disabled until the form is valid
├── assets/
│   ├── fonts/                  Inter 300, Playfair Display 500 + italic
│   └── img/                    hero placeholder, founder portrait
└── docs/BUILD-NOTES.md         what was built, what is open, what conflicts
```

Load order matters and is fixed in `index.html`: `trs-core.css` carries the tokens, then
`trs-blocks.css`, then `the-hair-rhythm.css` last so page rules win. Scripts are `defer`
and run in listed order; `form-prefill.js` must come before `tracking.js`, because
tracking reads the same `#svc` control.

---

## Editing rules

**Copy.** Anything a client reads goes through `/brand-review` before it ships. The page
carries locked sentences that must not be paraphrased: the Confidence Promise band, and
"That was never yours to work out alone." in the `#column` section.

**Prices.** Seven in the `#start` section and nowhere else, since the fourth revision merged the
two menus: the consultation hour at AED 300, then From 175 / 150 / 240 between visits and
From 380 / 570 / 620 for the bigger visits. **The Tone Reset moved 130 to 175 on 25 Aug**, on
Emma's edited playbook; it is also in the JSON-LD, and her own nine mentions of 130 have not
been changed yet. No percentage, no "save", no strike-through, no
countdown. Anything above `#start` that carries a number is a defect. The one exception is
the hero support line, which carries AED 300 because Layer 5 B option 1 specifies it.
**No course price is published yet**, and the blow-dry bundle's AED 240 does not reconcile
with Emma's single-blow-dry price; see the fifth pass in `docs/BUILD-NOTES.md`.

**The word junior** is out of the campaign name and still on the page, per Kate's 28 Aug
ruling: it stays in the JUNIOR STYLISTS heading, the reframe band, the FAQ and its JSON-LD
twin, the reviews and the capability sentence, and it appears nowhere in the campaign name,
the hero campaign label, the `<title>`, the OG and Twitter titles, or the URL. The page
names the tier plainly where it answers a question, never where it makes the offer.

**Never "fewer years".** Retired 21 Aug: it is factually false of at least one stylist in
the cohort. The locked replacement wording is on the Belief 5 page.

**`trs-core.css` and `trs-blocks.css` are copies of the shared design system** from
`tara-rose-pages-main/_css/`. Fix a token there and re-copy; do not fork them here.

---

## Where this also lives

The same page is built into the live page tree at
`tara-rose-pages-main/the-hair-rhythm/index.html`, where `build.py` inlines the CSS into the
file. **Both copies were revised on 24 Aug and are in sync.** This folder is the readable
source: change it here, then port the markup across and run `python build.py` in that repo.

**The production host is neither of those.** Checked 24 Aug: `tararosesalon.com` answers as
WordPress on LiteSpeed, which is LID's hosting. So this folder is the hand-off package. LID
mounts it at `/en/ae/the-hair-rhythm/`, and the `noindex` flip and any redirects happen there.

The sibling `/menu/` page the footer and `#start` link to is **not built yet**. It is the
next thing, and it inherits every pricing rule above.

**Read `docs/BUILD-NOTES.md` first.** The fifth pass, 25 Aug, checked this page against
Emma's own campaign playbook as well as the framework, fixed four faults, and left six for
Emma and Tara. Two of those six could change what the page leads on.
