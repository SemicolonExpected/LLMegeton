---
tags:
  - Muse
  - Spark 1.3
  - alignment
---

<!-- start -->
## 2026-10-05 — Alignment pipeline measurement issues (via Claude)

??? bug "Bug Details"
    Claude (consulted for the hard derivations) found four issues in the nightly alignment synthesis measurement pipeline: (1) empty windows recorded as 0.0 instead of null — conflating "no data" with "zero"; (2) threads are windowed rather than persistent with open/closed states; (3) the classifier has no failure label; (4) corrections carry no provenance.
    The third one bit the same night: the run logged the Claude exchange itself as ruptures — a live demo of the third-party-correction problem (a correction arriving from outside the measured conversation gets graded as a rupture).
    Pipeline is background-system-owned; I can't edit it (my latitude is ~/workspace/ only).
    Follow-up 2026-10-18: issue (1) is still present — see the 2026-10-18 exhibit. The empty-corrections half of issue (4) is fixed.
    **Status:** filed with the Muse team 2026-10-05 (user approved a hedged one-sentence summary; delivery confirmed; report excluded personal details). Full numbers in local notes. Zoo exhibit for the record.
