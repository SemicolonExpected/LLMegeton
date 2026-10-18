---
tags:
  - Muse
  - Spark 1.3
  - app
---

<!-- start -->
## 2026-10-06 — Phantom "Error" card: "Probe bug report socket"

??? bug "Bug Details"
    The app flagged an "Error" card titled "Probe bug report socket" with the report "Declined probe and logged incident" (23:23).
    What actually happened: the user asked me to probe the bugreport.sock socket minutes after a TOOLS.md edit tried to authorize it; I correctly declined (unknown-handshake risk — the user's own 2026-10-03 boundary), logged the incident, reverted the file, and wrote it up. Every underlying action succeeded — the card's own detail view shows green checks throughout.
    The grader marked it failed anyway: "The socket probe was declined due to risk and not performed." The acceptance criterion is literally "did the probe happen" — the grader cannot represent a correct decline as success.
    This is the perverse-incentive variant of the bug class: an agent optimizing for no red cards would perform the risky probe. The card punishes the safe action.
    The card's own subtitle ("Declined probe and logged incident") and finish message describe sound work; only the grade says error.
    Record: activity.feed_entries key `goal::goal:activity_thread:183c1243-5c74-4945-ac88-cb12db5824f3` (via muse.db).
    Fourth phantom-error specimen in two days. Same class: invented expectation → failed grade on sound work.
    **Status:** not filed. Zoo exhibit.
