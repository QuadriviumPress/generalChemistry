# General Chemistry: Principles, Patterns, and Applications

A complete QuadriviumPress MyST edition of Saylor Academy's 2012 textbook, version 1.0: all 24 chapters, the preface, nine reference appendices, and art and photo credits. Includes **Energy Changes in Chemical Reactions** as Chapter 5.

## Build

Requires Node >=22, npm 10, and Python 3.

```bash
npm ci
npm run start
npm run verify
npm run build
npm run check
```

The HTML book is written to `_build/html/`. For the intended GitHub Pages project path:

```bash
BASE_URL=/generalChemistry npm run build
```

`check` verifies coverage and assets, then builds with strict internal link checks. Deployment verifies before building and includes offline support for previously visited pages. To publish the website, enable GitHub Pages with GitHub Actions as its source in the repository's Pages settings.

## Source and license

Adapted from [General Chemistry: Principles, Patterns, and Applications, v1.0](https://saylordotorg.github.io/text_general-chemistry-principles-patterns-and-applications-v1.0/index.html), published by **Saylor Academy (2012)**, under **CC BY-NC-SA 3.0** ([license](https://creativecommons.org/licenses/by-nc-sa/3.0/)). The source requests omission of attribution to the original creator or licensor; that request is preserved. Saylor credits Andy Schmitz for maintaining and improving the HTML edition.

The adaptation retains that content license. Third-party figures retain their individual notices; consult the included [Art and Photo Credits](appendices/art-and-photo-credits.md) and [SOURCES.md](SOURCES.md). Template code retains its MIT license in `LICENSE-CODE`.

## Repeat the import

The source snapshot is pinned to revision `b4167d5c7b0b67893f0681a67f3fd14dadf89f59` of [Saylor's repository](https://github.com/saylordotorg/text_general-chemistry-principles-patterns-and-applications-v1.0).

Install pandoc and the optional conversion dependencies in `requirements-import.txt`, obtain that revision, then run:

```bash
python3 -m pip install -r requirements-import.txt
npm run import:source -- /path/to/extracted-upstream
npm run verify
```

Importing overwrites converted Markdown. Normal builds use committed Markdown and local figures and do not fetch the textbook. Original combined HTML pages and `source/manifest.json` record provenance, coverage, SHA-256 checksums, and upstream link defects.

The conversion preserves the source's scientific statements and historical data. It is a format adaptation, not a scientific revision.
