# Photograph replacement progress

Updated 2026-10-30. This is the implementation queue for the **25 photographs** in the [initial missing-figure audit](figure-replacement-audit.md). The audit remains a dated discovery snapshot. The [machine-readable ledger](../figure-replacements.json) is the current source of truth for installed figures and their provenance.

**7 locations installed; 18 remain pending.** Original source images and checksums are preserved. Installed photographs have been visually inspected; captions and alternative text describe the selected images, and component credits appear both beside the figures and in `SOURCES.md`.

Wikimedia returned HTTP 429 with `Retry-After: 600` during acquisition. Download retries were stopped to respect that ten-minute cooldown. Pending candidates below have not been installed or represented as visually accepted. Some are only partial subject matches and need further research regardless of download availability.

## Current queue

| ID | Location | Status | Next action |
| --- | --- | --- | --- |
| FR002 | [1.7 Milk as a heterogeneous mixture](../chapters/ch-01-introduction-to-chemistry.md) | installed | Installed; included in verification and automatic re-import application. |
| FR004 | [1.9 Sodium acetate crystallization](../chapters/ch-01-introduction-to-chemistry.md) | installed | Installed; included in verification and automatic re-import application. |
| FR006 | [2.9 Hydrate losing water](../chapters/ch-02-molecules-ions-and-chemical-fo.md) | installed | Installed; included in verification and automatic re-import application. |
| FR007 | [Ch. 3 opener: sodium](../chapters/ch-03-chemical-reactions.md) | installed | Installed; included in verification and automatic re-import application. |
| FR011 | [Example 13: galena and lead](../chapters/ch-03-chemical-reactions.md) | installed | Installed; included in verification and automatic re-import application. |
| FR013 | [Ch. 4 opener: HgI2 precipitation](../chapters/ch-04-reactions-in-aqueous-solution.md) | pending | Candidate shows mercury(II) iodide, but a documented precipitation photograph matching the reactants has not been established. Inspect and source the actual exchange-reaction scene before replacement. |
| FR017 | [Example 11: barium contrast x-ray](../chapters/ch-04-reactions-in-aqueous-solution.md) | pending | Candidate is a documented esophageal barium-swallow radiograph, but only 120 x 360 pixels. Inspect it and seek a larger reusable radiograph; caption must describe the esophagus rather than all digestive organs. |
| FR018 | [Photography callout: AgBr darkening](../chapters/ch-04-reactions-in-aqueous-solution.md) | pending | Inspect the public-domain AgBr image to see whether it actually documents light-induced darkening. A specimen-only photo cannot replace a before/after comparison without changing the teaching claim. |
| FR024 | [5.12 Sodium acetate hot pack](../chapters/ch-05-energy-changes-in-chemical-rea.md) | installed | Installed; included in verification and automatic re-import application. |
| FR025 | [Ch. 6 opener: noble-gas discharge tubes](../chapters/ch-06-the-structure-of-atoms.md) | pending | A CC BY 3.0 composite has been identified. Download after Wikimedia cooldown, inspect gas ordering, and match the caption to the visible labeled vials. |
| FR028 | [Group 1: potassium burning on water](../chapters/ch-07-the-periodic-table-and-periodi.md) | installed | Installed; included in verification and automatic re-import application. |
| FR030 | [9.27 Liquid oxygen in a magnet](../chapters/ch-09-molecular-geometry-and-covalen.md) | pending | CC BY 3.0 subject match identified; download was rate-limited. The original is only 294 x 240 pixels, so assess legibility before adoption. |
| FR034 | [11.10 Surface tension](../chapters/ch-11-liquids.md) | pending | Licensed paper-clip and water-strider photographs identified. Download after Wikimedia cooldown and verify the two observed surface-tension examples. |
| FR037 | [11.18 Iodine sublimation](../chapters/ch-11-liquids.md) | pending | CC0 process and deposition photographs identified. Download after Wikimedia cooldown and confirm that the phase change and cold-surface deposit are visible. |
| FR038 | [11.25 Cholesteryl benzoate phases](../chapters/ch-11-liquids.md) | pending | Only a solid specimen and molecular diagrams were found, not the named isotropic/cholesteric phase comparison. A matched phase pair with documented temperatures is still needed. |
| FR042 | [14.1 Concentration and sucrose reaction](../chapters/ch-14-chemical-kinetics.md) | pending | Licensed sugar-dehydration sequence identified. Download and inspect it; revise the caption to the actual sequence rather than claim a dilute-acid control that may not be present. Describe the carbonaceous product without an unverified graphite classification. |
| FR043 | [14.2 Temperature and glow sticks](../chapters/ch-14-chemical-kinetics.md) | pending | No matching licensed hot/cold glow-stick comparison identified. Continue a targeted search or obtain an original photograph with documented temperature conditions and a common exposure. |
| FR050 | [16.22 Red-cabbage indicator](../chapters/ch-16-aqueous-acid-base-equilibriums.md) | pending | Licensed pH-series photograph identified. Download after Wikimedia cooldown and inspect; use increasing pH rather than assign the original exact numerical pH values. |
| FR051 | [16.25 pH paper](../chapters/ch-16-aqueous-acid-base-equilibriums.md) | pending | Licensed indicator-paper photograph identified. Download after Wikimedia cooldown; ensure the strips and their own reference chart are both visible. |
| FR052 | [Calcite double refraction](../chapters/ch-17-solubility-and-complexation-eq.md) | pending | CC0 calcite double-refraction photograph identified. Download after Wikimedia cooldown and describe the actual doubled subject, without assuming it is lettering. |
| FR061 | [21.10 Sodium and water](../chapters/ch-21-periodic-trends-and-the-s-bloc.md) | pending | Initial search did not identify an adequate sodium-water reaction photograph. Continue searching for the actual reaction; a sodium specimen alone is insufficient. |
| FR062 | [21.11 Alkali metal in liquid ammonia](../chapters/ch-21-periodic-trends-and-the-s-bloc.md) | pending | A CC BY-SA 4.0 lithium/liquid-ammonia photograph has been identified. Download after Wikimedia cooldown and verify credit to Joshua Judkins and the documented blue/bronze states before adapting the caption. |
| FR063 | [Fluorite specimen](../chapters/ch-22-the-p-block-elements.md) | pending | A CC BY 2.0 fluorite specimen photograph has been identified. Download after Wikimedia cooldown and verify its visible color. Avoid inferring ozone release from the appearance of a specimen. |
| FR064 | [23.4 Vanadium oxidation-state colors](../chapters/ch-23-the-d-block-elements.md) | pending | Public-domain four-state vanadium photograph identified. Download after Wikimedia cooldown, inspect tube order, and match species labels to the photographed solutions. |
| FR065 | [23.5 Manganese oxidation states](../chapters/ch-23-the-d-block-elements.md) | pending | A public-domain manganate photograph supplies only Mn(VI). The full original comparison still needs documented Mn(II), Mn(III), Mn(IV), and Mn(VII) specimens, or a deliberate revision of figure scope. |

## Ledger and re-import workflow

`figure-replacements.json` version 1 has one entry per source photograph location. Each entry preserves its original source asset and SHA-256, chapter, original Markdown block, candidate descriptions, and next action. An `installed` entry additionally has replacement Markdown, the editorial-change explanation, and an asset list containing paths, SHA-256 hashes, creators, titles, source and revision URLs, download URLs, component licenses, retrieval dates, and changes. Extracted video frames also record the timestamp and source-video checksum.

To add a replacement, download and inspect the actual licensed image, copy it into `images/replacements/`, record its provenance, and add a matching caption, alternative text, and credit in the approved replacement block. Mark the entry installed only when these are ready. The files are local assets; normal verification and builds require no image downloads.

`python3 scripts/figure_replacements.py` applies installed blocks idempotently. The source importer invokes the same function after conversion, so imports restore approved images and captions. If neither the original nor the approved block matches uniquely, it stops for reconciliation rather than guessing. An unrelated future edit to an approved block should also be reflected in the ledger before re-import.

`npm run verify` checks preserved source checksums, the replacement-to-source mapping, installed image checksums, attribution fields, exact approved blocks, and active image references. It prints installed/pending counts and the number of unavailable-image notices still used in the entire book. Pending placeholders are reported rather than hidden or treated as completed work. `npm run check` also builds the book with strict internal-link and rendered-coverage checks.

Regression checks: `python3 -m unittest discover -s tests`.

## Validation of this batch

All ten regression checks passed. `npm run verify` passes with seven installed photograph locations, 18 pending photograph entries, and 58 remaining unavailable-image notices across the full book. `npm run check` passed with strict internal-link checks and rendered coverage of 332 tables, 1,269 images, and 2,730 math expressions. The build used the installed Node 26 toolchain. Simulating source conversion by restoring every installed entry's original block, then applying the ledger, reproduced the edited chapter files exactly; a second application made no changes.
