---
tags:
  - Muse
  - Spark 1.3
  - app
---

<!-- start -->
## 2026-10-06 — Phantom "Error" card: "Check log for requested turns"

??? bug "Bug Details"
    The app flagged an "Error" card titled "Check log for requested turns" with the report "Checked logs but no turns returned."
    "No turns returned" was the correct outcome, not a failure: the activity log records work (tool calls, tasks), not conversation prose, and the turn data is withheld by the security barrier by design. There was nothing to return and nothing was supposed to be returned.
    The grader treats an empty-but-correct result as an error. Same bug class as the [app name redacted] phantom error (2026-10-06) and the activity-feed false error (2026-10-05): the app invents a failure where the work was sound.
    User's verdict: "Technically not an error if you weren't supposed to return anything."
    **Status:** not filed. Zoo exhibit.
