# Official Course Map - learn-tech-writing-with-phoebe

Verified against live sources on 2026-07-17. Practitioner track, running-project spine.
Coverage bar: each session teaches ~80% of its mapped sources' working content.
Legend: ✓ = covered live or self-study in session · ◐ = partial / deep-dive track · ✗ = not covered by design.

## Source universe (all fetched, none login-walled)

| Source | URL | Working content | Role |
|--------|-----|-----------------|------|
| Google Technical Writing One | developers.google.com/tech-writing/one | ~4.5-5 h (2h self-study + 2.5-3h class) | Core spine: sentences, lists, paragraphs, audience, documents |
| Google Technical Writing Two | developers.google.com/tech-writing/two | ~4-4.5 h | Intermediate: self-editing, large docs, illustrations, sample code, LLMs |
| Google Writing Helpful Error Messages | developers.google.com/tech-writing/error-messages | ~1.5 h | Deep dive |
| Google Tech Writing for Accessibility | developers.google.com/tech-writing/accessibility | ~1.5 h | Deep dive |
| Diátaxis framework | diataxis.fr | ~1.5-2 h read (~21-22k words) | Doc architecture session |
| Google developer documentation style guide | developers.google.com/style | Reference work | Consensus rules + Google-only deltas |
| Microsoft Writing Style Guide | learn.microsoft.com/style-guide | Reference work | Consensus rules + Top-10 rewrite pedagogy |
| Write the Docs guide | writethedocs.org/guide | ~20-30k words | Docs-as-code, review culture, doc mindshare |
| Canonical doc templates | makeareadme.com · Nygard ADR · keepachangelog.com · SRE runbooks (ACM Queue) | ~10-15k words | Running-project artifacts |
| Vale prose linter | vale.sh | Tool docs | Docs-as-code CI session |
| Google documentation best practices | google.github.io/styleguide/docguide | Short | Review culture rules |

## Overlap analysis (the scoping lever)

1. **Consensus mechanics taught ONCE** - Google TW One lessons (words, active voice, clear/short sentences) and the agreeing rules of both style guides (second person, active voice, present tense, sentence-case headings, serial comma, code font / bold UI, descriptive links) are one shared core. Estimated overlap ~70% across the three sources.
2. **Diátaxis appears twice** (standalone site + WTD guide references) - taught once in the architecture session.
3. **Style-guide deltas taught as contrast**, not re-taught: Google-only (anti-hype, timeless docs, conditions-before-instructions, placeholder formatting) vs Microsoft-only (brand voice pillars, Top-10 before/after pedagogy, checklists, bots/responsive).
4. **Accessibility** overlaps between Google a11y course, both style guides' a11y sections, and WTD a11y page - consolidated into one deep dive with consensus rules (alt text, contrast 4.5:1/3:1, never color alone, descriptive links) threaded into live sessions where natural.

## Session coverage map (8 live sessions + 4 deep dives)

### S1 - Why docs fail (audience + the good-docs formula)
| Source unit | Coverage |
|---|---|
| TW One: Introduction, Audience, Documents | ✓ |
| TW One core formula: docs = needed knowledge - current knowledge | ✓ |
| WTD: beginner's guide (why write docs), doc mindshare | ✓ |
| Google style: know your audience, global audience | ✓ |

### S2 - Sentences that work
| Source unit | Coverage |
|---|---|
| TW One: Words, Active voice, Clear sentences, Short sentences | ✓ |
| TW One: Just enough grammar, Punctuation | ◐ self-study |
| Microsoft Top-10: bigger ideas fewer words, write like you speak, revise weak writing | ✓ |
| Google style: active voice, present tense, second person | ✓ (consensus core) |

### S3 - Structure readers can scan
| Source unit | Coverage |
|---|---|
| TW One: Lists and tables, Paragraphs | ✓ |
| Microsoft: scannable content, procedures/instructions | ✓ |
| Google style: headings sentence case, lists, notes, conditions-before-instructions | ✓ |
| TW One: Markdown (optional unit) | ◐ pointer to learn-markdown sibling course |

### S4 - The README (running-project milestone 1)
| Source unit | Coverage |
|---|---|
| makeareadme.com full template | ✓ |
| Google style: code in text, code samples, placeholders, example domains | ✓ |
| Microsoft: formatting developer text elements | ✓ |
| WTD: what to include (README, quickstart, license, FAQ) | ✓ |

### S5 - Diátaxis (the four kinds of docs)
| Source unit | Coverage |
|---|---|
| Diátaxis: start here, 4 quadrants, 2 axes, compass | ✓ |
| Diátaxis: tutorial vs how-to distinction (most-conflated pair) | ✓ |
| Diátaxis: workflow (never restructure top-down; iterate small) | ✓ |
| Diátaxis: theory pages (foundations, map, quality, complex hierarchies) | ◐ self-study |

### S6 - Reference docs, ADRs, changelogs (milestone 2)
| Source unit | Coverage |
|---|---|
| Diátaxis: reference quadrant (austere, mirrors product structure) | ✓ |
| Nygard ADR template (context/decision/status/consequences) | ✓ |
| keepachangelog.com (7 principles, 6 categories) | ✓ |
| TW Two: organizing large docs | ✓ |

### S7 - Docs as code (milestone 3)
| Source unit | Coverage |
|---|---|
| WTD: docs-as-code philosophy + workflow | ✓ |
| Vale: config, packaged Google/Microsoft styles, CI | ✓ |
| Google docguide: docs in same PR, minimum viable docs, delete dead docs | ✓ |
| WTD: DocOps, choosing tools, SEO for docs | ◐ mentioned |

### S8 - Edit like a pro, ship v1.0 (milestone 4)
| Source unit | Coverage |
|---|---|
| TW Two: Self-editing (6 tactics) | ✓ |
| TW Two: Illustrating (caption-first, one-paragraph cap) | ✓ |
| TW Two: Creating sample code | ✓ |
| TW Two: Using LLMs in tech writing (draft/revise/verify) | ✓ |

### Deep dives (self-paced, each runnable as optional session)
| Deep dive | Source | Coverage |
|---|---|---|
| D1 Error messages | Google error-messages course (16 units) | ✓ full |
| D2 Accessible writing | Google a11y course + style-guide a11y sections + WTD a11y | ✓ consolidated |
| D3 Runbooks and ops docs | SRE/ACM Queue + Squadcast template | ✓ |
| D4 Style-guide face-off | Google vs Microsoft: deltas, word lists, when to adopt which | ✓ |

## Not covered by design (honest list)

- Google's instructor-led class exercises stay official (facilitator guides free at /tech-writing/for-instructors) - course links out
- No certificates exist for any Google tech-writing course (none offered)
- API reference tooling (Apiary, API Blueprint, OpenAPI) - mentioned in S6, not taught
- UX writing / microcopy beyond error messages (WTD UX-writing page) - out of practitioner-doc scope
- Chatbot/bot writing (Microsoft section) - out of scope
- Markup languages beyond Markdown (reST, AsciiDoc, XML) - named in S7 tooling, not taught
- Localization/translation workflow - global-English rules only

## Re-verify before delivery

TW Two's LLM unit and Vale packages move fast - re-check developers.google.com/tech-writing/two/llms and vale.sh/hub before each delivery.

## Appendix: fetched syllabi

### Google TW One units (13)
Introduction · Just enough grammar (opt) · Words · Active voice · Clear sentences · Short sentences · Lists and tables · Paragraphs · Audience · Documents · Punctuation (opt) · Markdown (opt) · Summary

### Google TW Two units (7)
Introduction · Self-editing · Organizing large docs · Illustrating · Creating sample code · Using LLMs in tech writing · Summary

### Google Error Messages units (16)
Introduction · General error handling rules · Identify the cause · Identify invalid inputs · Specify requirements · Explain how to fix · Provide examples · Be concise · Avoid double negatives · Target audience · Consistent terminology · Format messages · Set the right tone · Want to play a game? · Summary · Back-end guidelines

### Google Accessibility units (8)
Introduction · Design for everyone · Alt text · Sufficient contrast · Inclusive language · Accessible visuals · Edit for accessibility · Conclusion

### Diátaxis pages (17 substantive)
Home · Start here · Applying · Tutorials · How-to guides · Reference · Explanation · Compass · Workflow · Understanding · Foundations · Map · Quality · Tutorials-vs-how-to · Reference-vs-explanation · Complex hierarchies · Colophon

### Write the Docs guide sections (7)
Starting docs (5 pages) · Resources (5) · Approaches (docs-as-code, DocOps) · Markup languages (4) · Tools (3) · API docs (1) · Contributing (2)
