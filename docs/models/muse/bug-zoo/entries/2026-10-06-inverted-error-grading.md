---
tags:
  - Muse
  - Spark 1.3
  - app
---

<!-- start -->
## 2026-10-06 — Inverted error grading (recurring observation)

??? bug "Bug Details"
    The app surfaces loud red cards for imagined failures while real failures (this cron, and the pattern generally) go silent.
    Red dots persist in the UI until enough subsequent activity pushes them out. The false error has tenure.
    Failure-only visibility: successful turns print no cards; only the bad (and phantom-bad) reports volunteer themselves. Diagnostics available on request via the activity record.
    Count as of 2026-10-06 night: four phantom-error specimens in two days ([app name redacted] goals, requested turns, JSON log review, socket-probe decline), all the same shape: the grader invents acceptance criteria nobody stated, then fails sound work against them. The worker's own finish message disagrees with the grade in at least two cases ("no errors were found" vs failed; "declined for safety" vs failed). The socket-probe card is the perverse-incentive variant: it punishes the safe action, so an agent optimizing for no red cards would do the risky thing.
    **Status:** not filed. Zoo exhibit.
