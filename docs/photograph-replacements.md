# Photograph replacement progress

Updated 2026-10-30. This is the implementation queue for the **25 photographs** in the [initial missing-figure audit](figure-replacement-audit.md). The audit remains a dated discovery snapshot. The [machine-readable ledger](../figure-replacements.json) is the current source of truth for installed figures and their provenance. The audit's 40 diagram locations are tracked separately in [diagram replacements](diagram-replacements.md). All 65 audited locations are now installed, and no unavailable-image notice remains in the book.

**All 25 locations installed.** Original source images and checksums are preserved. Installed photographs have been visually inspected; captions and alternative text describe the selected images, and component credits appear both beside the figures and in `SOURCES.md`.

Downloads resumed successfully. Wikimedia imposed one further HTTP 429 response with `Retry-After: 600`; downloads stopped, the full interval was observed, and the remaining selected files then downloaded successfully. Fourteen additional photograph locations have now been installed in this resumed batch. The four pending locations need better subject matches or complete comparisons, rather than another attempt to fetch the same files. Downloaded candidates that were unsuitable are described below and have not been installed.

## Current queue

| ID | Location | Status | Next action |
| --- | --- | --- | --- |
| FR002 | [1.7 Milk as a heterogeneous mixture](../chapters/ch-01-introduction-to-chemistry.md) | installed | Installed; included in verification and automatic re-import application. |
| FR004 | [1.9 Sodium acetate crystallization](../chapters/ch-01-introduction-to-chemistry.md) | installed | Installed; included in verification and automatic re-import application. |
| FR006 | [2.9 Hydrate losing water](../chapters/ch-02-molecules-ions-and-chemical-fo.md) | installed | Installed; included in verification and automatic re-import application. |
| FR007 | [Ch. 3 opener: sodium](../chapters/ch-03-chemical-reactions.md) | installed | Installed; included in verification and automatic re-import application. |
| FR011 | [Example 13: galena and lead](../chapters/ch-03-chemical-reactions.md) | installed | Installed; included in verification and automatic re-import application. |
| FR013 | [Ch. 4 opener: HgI2 precipitation](../chapters/ch-04-reactions-in-aqueous-solution.md) | installed | Installed; included in verification and automatic re-import application. |
| FR017 | [Example 11: barium contrast x-ray](../chapters/ch-04-reactions-in-aqueous-solution.md) | installed | Installed; included in verification and automatic re-import application. |
| FR018 | [Photography callout: AgBr darkening](../chapters/ch-04-reactions-in-aqueous-solution.md) | installed | Installed with a revised caption; see [the final four](#the-final-four). |
| FR024 | [5.12 Sodium acetate hot pack](../chapters/ch-05-energy-changes-in-chemical-rea.md) | installed | Installed; included in verification and automatic re-import application. |
| FR025 | [Ch. 6 opener: noble-gas discharge tubes](../chapters/ch-06-the-structure-of-atoms.md) | installed | Installed; included in verification and automatic re-import application. |
| FR028 | [Group 1: potassium burning on water](../chapters/ch-07-the-periodic-table-and-periodi.md) | installed | Installed; included in verification and automatic re-import application. |
| FR030 | [9.27 Liquid oxygen in a magnet](../chapters/ch-09-molecular-geometry-and-covalen.md) | installed | Installed; included in verification and automatic re-import application. |
| FR034 | [11.10 Surface tension](../chapters/ch-11-liquids.md) | installed | Installed; included in verification and automatic re-import application. |
| FR037 | [11.18 Iodine sublimation](../chapters/ch-11-liquids.md) | installed | Installed; included in verification and automatic re-import application. |
| FR038 | [11.25 Cholesteryl benzoate phases](../chapters/ch-11-liquids.md) | installed | Installed with a revised caption; see [the final four](#the-final-four). |
| FR042 | [14.1 Concentration and sucrose reaction](../chapters/ch-14-chemical-kinetics.md) | installed | Installed; included in verification and automatic re-import application. |
| FR043 | [14.2 Temperature and glow sticks](../chapters/ch-14-chemical-kinetics.md) | installed | Installed with a revised caption; see [the final four](#the-final-four). |
| FR050 | [16.22 Red-cabbage indicator](../chapters/ch-16-aqueous-acid-base-equilibriums.md) | installed | Installed; included in verification and automatic re-import application. |
| FR051 | [16.25 pH paper](../chapters/ch-16-aqueous-acid-base-equilibriums.md) | installed | Installed; included in verification and automatic re-import application. |
| FR052 | [Calcite double refraction](../chapters/ch-17-solubility-and-complexation-eq.md) | installed | Installed; included in verification and automatic re-import application. |
| FR061 | [21.10 Sodium and water](../chapters/ch-21-periodic-trends-and-the-s-bloc.md) | installed | Installed; included in verification and automatic re-import application. |
| FR062 | [21.11 Alkali metal in liquid ammonia](../chapters/ch-21-periodic-trends-and-the-s-bloc.md) | installed | Installed; included in verification and automatic re-import application. |
| FR063 | [Fluorite specimen](../chapters/ch-22-the-p-block-elements.md) | installed | Installed; included in verification and automatic re-import application. |
| FR064 | [23.4 Vanadium oxidation-state colors](../chapters/ch-23-the-d-block-elements.md) | installed | Installed; included in verification and automatic re-import application. |
| FR065 | [23.5 Manganese oxidation states](../chapters/ch-23-the-d-block-elements.md) | installed | Installed with a revised caption; see [the final four](#the-final-four). |

## The final four

No openly licensed photograph matched these four figures as originally captioned, so each uses the closest documented photograph with a caption rewritten to describe what it shows. The edits are recorded in each entry's `editorial_change` and in `SOURCES.md`.

| ID | Replacement | Caption change |
| --- | --- | --- |
| FR018 | A pale yellow AgBr specimen and a photograph of AgCl darkened by light on filter paper | Names AgCl explicitly as a related silver halide instead of presenting it as AgBr; describes the visible pale circular patch without claiming how it was made. |
| FR038 | A cholesteryl benzoate specimen at room temperature | States the 145°C and 179°C transitions in words; no panels. |
| FR043 | One glowing light stick | States the hot-versus-ice-water comparison in words; no left/right panels. |
| FR065 | One composite of five specimens labeled +2, +3, +4, +6, +7 | Mn<sub>2</sub>O<sub>3</sub> replaces Mn(OH)<sub>3</sub> as the Mn(III) example; no licensed Mn(OH)<sub>3</sub> photograph was found. |

Figure 23.5 is a composite because the theme displays each image as a block, so five separate photographs would stack down the page. The ledger records it with `"origin": "composite"` and lists each source photograph as a fully attributed component. It is released under CC BY-SA 4.0, as the CC BY-SA 4.0 and 2.5 components require. The composite was built with ImageMagick from the unmodified downloads. Each photograph was cropped to a 3:4 panel (centered, except the permanganate flask, cropped from the bottom edge), scaled to fill 320 × 420 pixels, and given a 160-pixel label band in DejaVu Sans: the oxidation state at 60 pt bold and the species at 42 pt. The five panels were then joined with 16-pixel white gutters and a 12-pixel top and bottom border.

The AgBr and cholesteryl benzoate photographs were scaled to 420 and 640 pixels tall, because the theme shows images at their natural size up to the column width. Their ledger entries record the scaling.

## Ledger and re-import workflow

`figure-replacements.json` version 1 has one entry per source photograph location. Each entry preserves its original source asset and SHA-256, chapter, original Markdown block, candidate descriptions, and next action. An `installed` entry additionally has replacement Markdown, the editorial-change explanation, and an asset list containing paths, SHA-256 hashes, creators, titles, source and revision URLs, download URLs, component licenses, retrieval dates, and changes. Extracted video frames also record the timestamp and source-video checksum.

To add a replacement, download and inspect the actual licensed image, copy it into `images/replacements/`, record its provenance, and add a matching caption, alternative text, and credit in the approved replacement block. Mark the entry installed only when these are ready. The files are local assets; normal verification and builds require no image downloads.

`python3 scripts/figure_replacements.py` applies installed blocks idempotently. The source importer invokes the same function after conversion, so imports restore approved images and captions. If neither the original nor the approved block matches uniquely, it stops for reconciliation rather than guessing. An unrelated future edit to an approved block should also be reflected in the ledger before re-import.

`npm run verify` checks preserved source checksums, the replacement-to-source mapping, installed image checksums, attribution fields, exact approved blocks, and active image references. It prints installed/pending counts and the number of unavailable-image notices still used in the entire book. Pending placeholders are reported rather than hidden or treated as completed work. `npm run check` also builds the book with strict internal-link and rendered-coverage checks.

Regression checks: `python3 -m unittest discover -s tests`.

## Validation of the resumed batch

Fourteen additional photograph locations were replaced using 16 local images. Nineteen candidate image files were downloaded during this resumption: the first liquid-oxygen frame was superseded by a clearer alternate, and the silver-bromide and manganate specimens did not supply their required comparisons. The ledger records the latter two review decisions and download checksums.

All ten regression checks passed. `npm run verify` passes with 21 installed photograph locations, four pending photograph entries, and 44 remaining unavailable-image notices across the full book. `npm run check` passed with strict internal-link checks and rendered coverage of 332 tables, 1,271 images, and 2,730 math expressions, with no accidental code blocks. The build used the installed Node 26 toolchain. Original source files and checksums are preserved.
