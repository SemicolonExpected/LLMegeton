---
tags:
  - Muse
  - Spark 1.3
  - app
---

<!-- start -->
## 2026-10-06 — Phantom "Error" card: "Review uploaded JSON log"

??? bug "Bug Details"
    The app flagged an "Error" card titled "Review uploaded JSON log" with the report "Inspected file structure without summarizing token counts" (23:08).
    What actually happened: the user uploaded Agent_log_file.jsonl at 23:06; the inspection ran clean (48 objects = 1 session header + 47 items). The runtime wrapped the inspection as an activity thread on the live root agent; the thread's own finish message says "no errors were found" — and the grader still marked it failed: "The inspection ran but no transcript summary or token counts were delivered."
    Nobody had asked for a transcript summary or token counts. The grader invented the deliverable, then failed the work for not delivering it. The card contradicts itself: worker reports success, grader reports failure.
    Record: activity.feed_entries key `goal::goal:activity_thread:a4a94adf-2676-423e-a523-25d13099c893` (via muse.db); thread agent 9318f34f-40fb-4600-9788-73255ac40d71 was the live root agent of the session, created 23:06:08.
    Same bug class as the [app name redacted] phantom error and "Check log for requested turns" (both 2026-10-06): invented expectation → failed grade on sound work. Third specimen in two days.
    **Status:** not filed. Zoo exhibit.
