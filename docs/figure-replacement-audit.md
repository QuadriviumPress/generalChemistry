# Missing-figure audit and replacement plan

Audit date: 2026-10-30. Scope: exploration and replacement planning; no textbook figures, captions, source snapshots, or verification rules were changed.

Implementation has since begun. See [photograph replacement progress](photograph-replacements.md) and the [replacement ledger](../figure-replacements.json) for current installation status; the findings below describe the original discovery snapshot.

## Findings

**65 source image assets, used at 65 locations across 21 chapters, contain the same unavailable-image notice.** They account for 51 numbered figures and 14 unnumbered illustrations, including five chapter openers. These are existing files with missing educational content, rather than broken file paths. The notice says: “Sorry! This image is permanently unavailable.”

All 65 files are byte-identical 640 × 480 JPEGs with SHA-256:

```text
93f80bd15e870d30b31a3f2185d4a3d03408696daa0f2643462e8d604ce24a6b
```

The source manifest records this same digest for each of them. The retained source HTML already references these images. This establishes that the gaps were inherited from the imported source; it does **not** establish why each original image was withdrawn. Copyright removal is plausible given the third-party credits, but the notice and local records do not confirm that explanation.

`npm run verify` passes: 24 chapters, nine appendices, 36 source pages, 1,265 local source assets, and 1,221 cross-reference targets. It checks existence, checksums, and source-image references, so a valid placeholder JPEG passes. `verify_rendered.py` counts image nodes and also cannot distinguish a placeholder from a useful figure.

The imported source assets comprise 1,264 JPEGs plus the PNG license badge. The three SVGs under `images/` are site branding, not chemistry diagrams. There are no chemistry SVG originals in this checkout to restore. A new diagram would be authored from the scientific description and checked data, or adapted from a separately licensed SVG.

## Coverage and limits

The audit grouped all imported image assets by SHA-256, visually inspected the repeated notice, mapped every matching asset through the retained HTML and Markdown, and read each associated caption and surrounding context. Thumbnail contact sheets of the remaining 1,199 JPEGs showed no additional obvious full-image withdrawal notices. That thumbnail review does not rule out small missing panels, unreadable labels, or scientific defects inside otherwise present images. This is a confirmed inventory of the 65 matching notices, not a full rights or scientific audit of all surviving artwork.

Chapters 12, 20, and 24 have no matching unavailable-image notice. Their surviving third-party art still retains its individual attribution requirements.

The [CSV inventory](figure-replacement-inventory.csv) contains one row per location, including exact asset path and digest, Markdown file and line, source figure ID, original caption, replacement brief, priority, review notes, and candidate links. Line numbers describe this checkout at the audit date and may move after edits. The table below is the compact work queue.

## Proposed replacement approach

Initial editorial routing: **38 SVG diagrams, 25 photographs, and 2 combined photo/diagram figures**. These are recommendations, not completed replacements. A photograph route can fall back to a clearly identified schematic if a suitably licensed, scientifically matching photograph cannot be found. That switch requires a matching caption.

Use an SVG when the lesson depends on apparatus, particle accounting, forces, a process sequence, or quantitative positions. Use a real photograph when the lesson depends on an observed material, texture, micrograph, radiograph, phase appearance, or specimen color. Do not use generated photographs as experimental evidence. Open SVGs can be adapted with their required credits; new independent diagrams should use scientific facts and a fresh composition rather than trace restricted artwork.

Prefer CC0/public-domain, CC BY, or CC BY-SA components. Keep each component's actual license in its own attribution record. In particular, a CC BY-SA adaptation keeps its applicable share-alike terms; do not silently relabel it with the textbook's CC BY-NC-SA license. See the official [CC BY deed](https://creativecommons.org/licenses/by/4.0/) and [CC BY-SA deed](https://creativecommons.org/licenses/by-sa/3.0/).

OpenStax is a useful secondary search source, but its current [Chemistry 2e preface](https://openstax.org/books/chemistry-2e/pages/preface) states CC BY-NC-SA 4.0. Do not assume a remembered CC BY license applies to the current edition or every individual image. The initial shortlist below uses component-specific file descriptions instead.

## Initial external candidates

The linked description pages and their listed licenses were checked on the audit date. None has been downloaded into the book or accepted as a final replacement. Scientific fit, actual pixels, panel order, legibility, and any needed caption changes remain to be checked before adoption. A listed license is recorded from the source page; it is not a blanket clearance of other material on that page.

| ID | Missing figure | Candidate and creator | Listed license | Remaining work |
| --- | --- | --- | --- | --- |
| C1 | 1.8 Distillation | [Simple distillation apparatus.svg](https://commons.wikimedia.org/wiki/File:Simple_distillation_apparatus.svg), original PNG Quantockgoblin; SVG adaptation Slashme | Public-domain dedication | Simplify labels, identify salt solution and water distillate, check coolant directions and apparatus geometry. Editable SVG, not an exact ready-made replacement. |
| C2 | 11.11–11.12 Capillary action | [CapillaryAction.svg](https://commons.wikimedia.org/wiki/File:CapillaryAction.svg), Eduard Konečný | Public-domain dedication | Use as a starting point; supply explicit water/mercury labels, reservoir reference levels, and the missing tilted-tube comparison. |
| C3 | 23.4 Vanadium colors | [Vanadiumoxidationstates.jpg](https://commons.wikimedia.org/wiki/File:Vanadiumoxidationstates.jpg), Steffen Kristensen | Public-domain dedication | Four-state subject match; inspect tube order and add verified species/oxidation-state labels. Original is 2,003 × 3,005 pixels. |
| C4 | 9.27 Paramagnetic liquid oxygen | [Liquid oxygen in a magnet.jpg](https://commons.wikimedia.org/wiki/File:Liquid_oxygen_in_a_magnet.jpg) and [second frame](https://commons.wikimedia.org/wiki/File:Liquid_oxygen_in_a_magnet_2.jpg), Bob Burk | CC BY 3.0 | Subject matches; stills are only 294 × 240 and 302 × 225 pixels. Inspect quality and follow the source-video trail for a better frame if available. |
| C5 | 2.9 Hydrate dehydration | [Copper sulfate anhydrous.jpg](https://commons.wikimedia.org/wiki/File:Copper_sulfate_anhydrous.jpg), W. Oelen | CC BY-SA 3.0 | This supplies only the anhydrous side. Find a separately credited pentahydrate image; check staged dehydration labels. Original is 459 × 447 pixels. |
| C6 | 5.12 Sodium acetate heat pack | [Hand warmer activation.webm](https://commons.wikimedia.org/wiki/File:Hand_warmer_activation.webm), Teren | CC BY-SA 4.0 | Extract and credit before/after frames from the 1,920 × 1,080 video; verify pack details. This is a still-image route, not a proposal to embed video. |
| C7 | 16.22 Cabbage indicator | [Red cabbage indicator.jpg](https://commons.wikimedia.org/wiki/File:Red_cabbage_indicator.jpg), Epaenurk | CC BY-SA 3.0 | Photo description establishes increasing pH left to right, not the original precise pH values. Revise the caption accordingly. [Laundry's alternative](https://commons.wikimedia.org/wiki/File:Rode_kool_pH-indicator.jpg) has a public-domain dedication but likewise needs a fit check. |
| C8 | Unnumbered calcite illustration | [Calcite and double refraction, GeoDIL 670](https://commons.wikimedia.org/wiki/File:Calcite_and_double_refraction_(GeoDIL_number_-_670).jpg), Twyla Baker / GeoDIL | CC0 1.0 | Check the visible doubled subject and adapt the caption; original is 1,637 × 1,812 pixels. The Commons page records a source-license review. |

One superficially relevant cabbage candidate, [Red cabbage pH values.jpg](https://commons.wikimedia.org/wiki/File:Red_cabbage_pH_values.jpg), is flagged as lacking source information and has a malformed author attribution. It should not be the default choice despite its license templates.

## Start with these batches

1. **Foundational diagrams:** 1.6 states of matter, 1.8 distillation, 4.4 conductivity, and 4.11 precipitation. These repair important early-chapter explanations and establish a reusable SVG style for vessels, particles, arrows, and labels.
2. **Quantitative and process diagrams:** 10.16 diffusion distances, 11.11–11.12 capillarity, 15.12–15.13 equilibrium, and 17.11 qualitative separation. These require careful label/panel matching and are poor candidates for generic stock photographs.
3. **Photographs with identified candidates:** 23.4 vanadium, calcite double refraction, 5.12 heat pack, 16.22 cabbage, and 9.27 liquid oxygen. These can proceed through visual acceptance and attribution without waiting for all harder photo searches.
4. **Specialized photo searches and remaining schematics:** milk microscopy, barium radiography, silver bromide darkening, cholesteryl benzoate phases, liquid-ammonia solutions, and manganese compounds. Chapter-opening imagery is generally lower priority unless it carries an essential chart, as in Chapter 16.

### Editorial prerequisites

- **Figure 15.1 / Equation 15.1:** the source heading and displayed equation have N₂O where the surrounding explanation and figure caption specify N₂O₄. Resolve this discrepancy and record the correction before drawing the equilibrium.
- **Figure 13.5:** the caption asserts three separate layers of water, CCl₄, and hexane, while the surrounding discussion says common organic liquids are miscible. Check the CCl₄/hexane mixture before depicting it; two separate binary-mixture examples may be the appropriate revision. This audit flags the issue rather than adopting a new phase diagram.
- **Figure 10.16:** preserve the source's observed 15.5 cm and 9.2 cm distances and ratio about 1.7 separately from the theoretical 1.47. The adjacent reaction also labels NH₄Cl as a gas although the lesson describes solid white fumes; review the phase label.
- **Unknown original visual details:** Figure 3.1 has no descriptive caption identifying the lost specimens; the Chapter 16 opener does not identify its seven indicators in surviving prose. Make new documented selections and update the captions rather than inventing what the original pixels contained.
- The CSV records further local checks, including pH-paper precision, the microstate wording in 18.7, and the reference to molecular I₂ as ions in 19.8. These are replacement-specific review notes, not completed scientific edits.

## Full work queue

P1: explanation, mechanism, quantitative comparison, or essential subject evidence. P2: illustrative observation or supporting example. P3: general chapter-opening image. SVG means original drawing or adaptation of an openly licensed SVG; Hybrid means a photograph with a new explanatory diagram. Exact captions and detailed briefs are in the CSV. An asterisk marks a row with an editorial prerequisite or acceptance condition recorded there.

| ID | Location | Route | Priority | Candidate |
| --- | --- | --- | --- | --- |
| FR001 | [1.6 States of matter](../chapters/ch-01-introduction-to-chemistry.md#src-averill-1-0-ch01-s03-f01) | SVG | P1 | — |
| FR002 | [1.7 Milk as a heterogeneous mixture](../chapters/ch-01-introduction-to-chemistry.md#src-averill-1-0-ch01-s03-s01-f01) * | Photo | P2 | — |
| FR003 | [1.8 Salt-water distillation](../chapters/ch-01-introduction-to-chemistry.md#src-averill-1-0-ch01-s03-s01-f02) | SVG | P1 | C1 |
| FR004 | [1.9 Sodium acetate crystallization](../chapters/ch-01-introduction-to-chemistry.md#src-averill-1-0-ch01-s03-s01-f03) * | Photo | P2 | — |
| FR005 | [1.16 Gas discharge tube](../chapters/ch-01-introduction-to-chemistry.md#src-averill-1-0-ch01-s05-s01-f01) | SVG | P1 | — |
| FR006 | [2.9 Hydrate losing water](../chapters/ch-02-molecules-ions-and-chemical-fo.md#src-averill-1-0-ch02-s02-s03-f01) * | Photo | P2 | C5 |
| FR007 | [Ch. 3 opener: sodium](../chapters/ch-03-chemical-reactions.md) | Photo | P3 | — |
| FR008 | [3.1 One-mole samples](../chapters/ch-03-chemical-reactions.md#src-averill-1-0-ch03-s01-s03-f01) * | SVG | P1 | — |
| FR009 | [3.7 Ammonium dichromate reaction](../chapters/ch-03-chemical-reactions.md#src-averill-1-0-ch03-s03-f01) * | SVG | P1 | — |
| FR010 | [3.9 Candle combustion](../chapters/ch-03-chemical-reactions.md#src-averill-1-0-ch03-s03-s02-f01) | SVG | P2 | — |
| FR011 | [Example 13: galena and lead](../chapters/ch-03-chemical-reactions.md) | Photo | P2 | — |
| FR012 | [Example 15: AgCl precipitation](../chapters/ch-03-chemical-reactions.md) | SVG | P1 | — |
| FR013 | [Ch. 4 opener: HgI2 precipitation](../chapters/ch-04-reactions-in-aqueous-solution.md) * | Photo | P3 | — |
| FR014 | [4.4 Electrolyte conductivity](../chapters/ch-04-reactions-in-aqueous-solution.md#src-averill-1-0-ch04-s01-s02-f01) * | SVG | P1 | — |
| FR015 | [Example 8: Breathalyzer color change](../chapters/ch-04-reactions-in-aqueous-solution.md) * | SVG | P2 | — |
| FR016 | [4.11 Silver dichromate precipitation](../chapters/ch-04-reactions-in-aqueous-solution.md#src-averill-1-0-ch04-s03-s02-f01) | SVG | P1 | — |
| FR017 | [Example 11: barium contrast x-ray](../chapters/ch-04-reactions-in-aqueous-solution.md) * | Photo | P2 | — |
| FR018 | [Photography callout: AgBr darkening](../chapters/ch-04-reactions-in-aqueous-solution.md) * | Photo | P2 | — |
| FR019 | [4.14 Acid-carbonate gas formation](../chapters/ch-04-reactions-in-aqueous-solution.md#src-averill-1-0-ch04-s06-s05-f01) | SVG | P2 | — |
| FR020 | [4.16 pH paper versus pH meter](../chapters/ch-04-reactions-in-aqueous-solution.md#src-averill-1-0-ch04-s06-s06-f02) * | SVG | P1 | — |
| FR021 | [4.21 Copper displacing silver](../chapters/ch-04-reactions-in-aqueous-solution.md#src-averill-1-0-ch04-s08-s02-s01-f01) | Hybrid | P1 | — |
| FR022 | [4.23 Permanganate-oxalate titration](../chapters/ch-04-reactions-in-aqueous-solution.md#src-averill-1-0-ch04-s09-s01-f01) * | SVG | P1 | — |
| FR023 | [4.24 Ascorbic-acid titration](../chapters/ch-04-reactions-in-aqueous-solution.md#src-averill-1-0-ch04-s09-s03-f01) | SVG | P1 | — |
| FR024 | [5.12 Sodium acetate hot pack](../chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05-s02-s05-f01) * | Photo | P2 | C6 |
| FR025 | [Ch. 6 opener: noble-gas discharge tubes](../chapters/ch-06-the-structure-of-atoms.md) * | Photo | P3 | — |
| FR026 | [6.9 Hydrogen emission](../chapters/ch-06-the-structure-of-atoms.md#src-averill-1-0-ch06-s03-s01-f01) * | Hybrid | P1 | — |
| FR027 | [6.13 H/Ne/Hg emission comparison](../chapters/ch-06-the-structure-of-atoms.md#src-averill-1-0-ch06-s03-s02-f04) * | SVG | P1 | — |
| FR028 | [Group 1: potassium burning on water](../chapters/ch-07-the-periodic-table-and-periodi.md) * | Photo | P2 | — |
| FR029 | [Ch. 8 opener: CO2 versus SiO2](../chapters/ch-08-ionic-versus-covalent-bonding.md) * | SVG | P2 | — |
| FR030 | [9.27 Liquid oxygen in a magnet](../chapters/ch-09-molecular-geometry-and-covalen.md#src-averill-1-0-ch09-s03-s04-f02) * | Photo | P1 | C4 |
| FR031 | [10.15 NH3/HCl gas diffusion](../chapters/ch-10-gases.md#src-averill-1-0-ch10-s07-s04-f01) * | SVG | P1 | — |
| FR032 | [10.16 Quantitative gas diffusion](../chapters/ch-10-gases.md#src-averill-1-0-ch10-s07-s04-f02) * | SVG | P1 | — |
| FR033 | [11.1 Dye diffusion in water](../chapters/ch-11-liquids.md#src-averill-1-0-ch11-s01-s05-f01) * | SVG | P2 | — |
| FR034 | [11.10 Surface tension](../chapters/ch-11-liquids.md#src-averill-1-0-ch11-s03-s01-f02) | Photo | P2 | — |
| FR035 | [11.11 Capillary rise](../chapters/ch-11-liquids.md#src-averill-1-0-ch11-s03-s02-f01) * | SVG | P1 | C2 |
| FR036 | [11.12 Capillary depression and menisci](../chapters/ch-11-liquids.md#src-averill-1-0-ch11-s03-s02-f02) | SVG | P1 | C2 |
| FR037 | [11.18 Iodine sublimation](../chapters/ch-11-liquids.md#src-averill-1-0-ch11-s05-s01-f01) * | Photo | P2 | — |
| FR038 | [11.25 Cholesteryl benzoate phases](../chapters/ch-11-liquids.md#src-averill-1-0-ch11-s08-f01) * | Photo | P2 | — |
| FR039 | [13.5 Immiscible liquids](../chapters/ch-13-solutions.md#src-averill-1-0-ch13-s02-s02-s01-f01) * | SVG | P1 | — |
| FR040 | [13.8 Crown ether and solubility](../chapters/ch-13-solutions.md#src-averill-1-0-ch13-s02-s04-f03) | SVG | P1 | — |
| FR041 | [13.22 Tyndall effect](../chapters/ch-13-solutions.md#src-averill-1-0-ch13-s06-s01-f01) * | SVG | P1 | — |
| FR042 | [14.1 Concentration and sucrose reaction](../chapters/ch-14-chemical-kinetics.md#src-averill-1-0-ch14-s01-s01-f01) * | Photo | P2 | — |
| FR043 | [14.2 Temperature and glow sticks](../chapters/ch-14-chemical-kinetics.md#src-averill-1-0-ch14-s01-s02-f01) * | Photo | P2 | — |
| FR044 | [14.3 Surface area and reaction rate](../chapters/ch-14-chemical-kinetics.md#src-averill-1-0-ch14-s01-s03-f01) * | SVG | P1 | — |
| FR045 | [14.4 Catalysts and H2O2 decomposition](../chapters/ch-14-chemical-kinetics.md#src-averill-1-0-ch14-s01-s05-f01) * | SVG | P1 | — |
| FR046 | [15.1 N2O4/NO2 and temperature](../chapters/ch-15-chemical-equilibrium.md#src-averill-1-0-ch15-s01-f01) * | SVG | P1 | — |
| FR047 | [15.12 Equilibrium after compression](../chapters/ch-15-chemical-equilibrium.md#src-averill-1-0-ch15-s05-s02-f01) * | SVG | P1 | — |
| FR048 | [15.13 Equilibrium and temperature](../chapters/ch-15-chemical-equilibrium.md#src-averill-1-0-ch15-s05-s03-f01) | SVG | P1 | — |
| FR049 | [Ch. 16 opener: indicator colors](../chapters/ch-16-aqueous-acid-base-equilibriums.md) * | SVG | P2 | — |
| FR050 | [16.22 Red-cabbage indicator](../chapters/ch-16-aqueous-acid-base-equilibriums.md#src-averill-1-0-ch16-s05-s04-f01) * | Photo | P2 | C7 |
| FR051 | [16.25 pH paper](../chapters/ch-16-aqueous-acid-base-equilibriums.md#src-averill-1-0-ch16-s05-s04-f04) * | Photo | P2 | — |
| FR052 | [Calcite double refraction](../chapters/ch-17-solubility-and-complexation-eq.md) * | Photo | P2 | C8 |
| FR053 | [17.4 Copper-ammonia complex ions](../chapters/ch-17-solubility-and-complexation-eq.md#src-averill-1-0-ch17-s03-f01) * | SVG | P1 | — |
| FR054 | [17.9 Amphoteric chromium hydroxide](../chapters/ch-17-solubility-and-complexation-eq.md#src-averill-1-0-ch17-s04-s02-f02) * | SVG | P1 | — |
| FR055 | [17.11 Qualitative cation separation](../chapters/ch-17-solubility-and-complexation-eq.md#src-averill-1-0-ch17-s05-s05-f01) * | SVG | P1 | — |
| FR056 | [18.6 Spontaneous endothermic reaction](../chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-f01) * | SVG | P1 | — |
| FR057 | [18.7 Entropy and playing cards](../chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s01-f01) * | SVG | P1 | — |
| FR058 | [19.2 Zn in CuSO4: one compartment](../chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s01-s01-f01) * | SVG | P1 | — |
| FR059 | [Galvanic-cell unnumbered illustration](../chapters/ch-19-electrochemistry.md) * | SVG | P2 | — |
| FR060 | [19.8 Dichromate and iodide](../chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s02-f01) * | SVG | P2 | — |
| FR061 | [21.10 Sodium and water](../chapters/ch-21-periodic-trends-and-the-s-bloc.md#src-averill-1-0-ch21-s03-s03-f03) | Photo | P2 | — |
| FR062 | [21.11 Alkali metal in liquid ammonia](../chapters/ch-21-periodic-trends-and-the-s-bloc.md#src-averill-1-0-ch21-s03-s05-f01) * | Photo | P2 | — |
| FR063 | [Fluorite specimen](../chapters/ch-22-the-p-block-elements.md) * | Photo | P2 | — |
| FR064 | [23.4 Vanadium oxidation-state colors](../chapters/ch-23-the-d-block-elements.md#src-averill-1-0-ch23-s02-s01-s03-f01) * | Photo | P1 | C3 |
| FR065 | [23.5 Manganese oxidation states](../chapters/ch-23-the-d-block-elements.md#src-averill-1-0-ch23-s02-s02-s02-f01) * | Photo | P2 | — |

### Counts by chapter

| Chapter | Missing assets | Chapter | Missing assets |
| --- | ---: | --- | ---: |
| 1 | 5 | 13 | 3 |
| 2 | 1 | 14 | 4 |
| 3 | 6 | 15 | 3 |
| 4 | 11 | 16 | 3 |
| 5 | 1 | 17 | 4 |
| 6 | 3 | 18 | 2 |
| 7 | 1 | 19 | 3 |
| 8 | 1 | 20 | 0 |
| 9 | 1 | 21 | 2 |
| 10 | 2 | 22 | 1 |
| 11 | 6 | 23 | 2 |
| 12 | 0 | 24 | 0 |

## Repository changes needed during replacement

1. **Keep provenance intact.** Retain the original HTML, original image files, and their checksums. Add replacement files under descriptive names such as `images/replacements/fig-04-04-conductivity.svg`, rather than overwriting a hashed source JPEG or replacing a provenance checksum.
2. **Add an explicit replacement ledger.** Map the source asset and its original checksum to the approved replacement path, current chapter/figure, creator, title, source URL, component license URL/version, retrieval date, changes made, and replacement checksum. Record original artwork and its chosen component license too. The exploratory CSV is the starting work queue, not this final approval ledger.
3. **Teach verification about replacements.** `verify_book.py` currently requires the original `/images/...jpg` string to occur in the chapter. A simple Markdown swap therefore fails even if the SVG is correct. Allow an original reference or a declared replacement; still verify the preserved original checksum and the replacement's existence and provenance. Detect known notice hashes in actively used figure paths and report unresolved counts. Do not simply waive all source-coverage checks.
4. **Match captions and references.** Keep source figure numbers and existing source targets so inbound links continue to resolve. Add accessible alt text and labels appropriate to each replacement. Apply the repository's MyST figure conventions while respecting its intentional literal numbering. Match every (a)/(b)/(c), chemical species, color statement, unit, and quantitative label to the actual image. Do not collapse or remove image slots without explicitly revising the rendered-coverage expectations.
5. **Update attribution and editorial notes.** Add current replacement credits and substantive corrections to `SOURCES.md`; distinguish them from the historical source credits in `appendices/art-and-photo-credits.md`. A vendor credited for a lost source photo must not appear to be the creator of a new diagram. Follow each adopted component's stated license and preserve existing source attribution.
6. **Make re-import behavior explicit.** The importer currently overwrites converted pages. Apply the approved replacement ledger during import, or provide a deterministic post-import step, so future imports do not restore the notices or lose approved caption corrections.
7. **Check the delivered book.** Run `npm run verify` and `npm run check` after the verifier understands replacements. Inspect the affected rendered pages for small-screen legibility, clipped labels, contrast, panel order, working references, and correct alt text. File integrity alone will not establish scientific usefulness.

No replacement implementation or textbook license change is included in this exploration. The next concrete deliverable is a small reviewed batch of replacement assets plus the ledger/verifier support that makes those assets maintainable.
