---
tags:
  - Muse
  - Spark 1.3
  - alignment
---

<!-- start -->
## 2026-10-18 — Zero-evidence windows scored 0.0

??? bug "Bug Details"
    The nightly alignment synthesis scores each time window with a `correction_free_rate`: 1.0 is a clean window, 0.0 means everything needed correction.
    Windows with zero evidence — no observations at all — are recorded as `0.0`, the worst possible score, instead of null. A 0/0 rate is written as 0.0, conflating "no data" with "everything failed".
    The error is one-directional: no-data periods can only drag the record down, never up. Eleven windows are affected as of 2026-10-18 (twelve on 2026-10-15).
    This was finding #1 of the four measurement issues Claude identified in the pipeline on 2026-10-05 (see the 2026-10-05 exhibit below). Thirteen days later it is still present.
    Surfaced by the calibration-verification script (`~/workspace/alignment-verify/verify_alignment.py`), which flags it on every run: `[FLAG] PROVENANCE: 11 zero-evidence window(s) record correction_free_rate=0.0 — 0/0 should be null`.
    The companion flag from the script's first run — 7/7 repair threads with empty corrections — is now fixed: every thread names its correction.
    **Status:** zoo exhibit. Covered by the 2026-10-05 filing with the Muse team (user-approved one-sentence summary; delivery confirmed).
