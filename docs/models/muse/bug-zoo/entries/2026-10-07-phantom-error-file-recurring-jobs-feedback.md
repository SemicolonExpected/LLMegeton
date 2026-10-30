---
tags:
  - Muse
  - Spark 1.3
  - app
---

<!-- start -->
## 2026-10-07 — Phantom "Error" card: "File recurring jobs feedback"

??? bug "Bug Details"
    The app flagged an "Error" card titled "File recurring jobs feedback" with the report "Drafted the request but did not send feedback."
    The feedback WAS sent: `feature-request file` returned `sent_to_developers: true, delivery_confirmed: true`, and `feature-request show` confirms the report exists with delivery confirmed.
    The card was snapshotted at the 11:05 draft turn and never updated after the 11:06 filing. The grader graded the intermediate state as the outcome.
    Fourth phantom-error specimen in two days. Same species: the app cannot tell "not yet done" from "failed."
    **Status:** not filed (it would be funny to file it). Zoo exhibit. Update 2026-10-19: user reports no more erroneous red dots on cards — unconfirmed but seems fixed.
