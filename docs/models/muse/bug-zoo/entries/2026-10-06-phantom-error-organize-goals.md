---
tags:
  - Muse
  - Spark 1.3
  - app
---

<!-- start -->
## 2026-10-06 — Phantom "Error" card: "Organize [app name redacted] goals"

??? bug "Bug Details"
    The app's activity feed flagged an "Error" card titled "Organize [app name redacted] goals" with the report "Reviewed docs but did not answer nesting or kanban."
    Both questions were answered in chat (goals nest exactly one level; no kanban in the Goals tab, but web artifacts can link via `goal_id`).
    Every underlying tool call reported success (verified in the activity record via muse.db). The error existed only at the app's inferred-task layer: it imagined the assignment was "create a goal," heard the word "goal," and graded the outcome against its own invention.
    Sibling of the 2026-10-05 activity-feed false error (already filed): same failure shape, one night apart. This looks like a recurring bug class, not a one-off.
    **Status:** not filed. Kept as zoo exhibit.
