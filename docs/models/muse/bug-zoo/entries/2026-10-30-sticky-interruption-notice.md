---
tags:
  - Muse
  - Spark 1.3
  - app
---

<!-- start -->
## 2026-10-30 — Sticky interruption notice treats later messages as interruptions

??? bug "Bug Details"
    A stall in chat produced an internal cancellation notice at 08:09 UTC, followed by an interruption notice at 08:10 UTC, even though the intervening message arrived after the cancellation, not during an active turn.
    After those notices, later double and triple messages were treated as interruptions, and replies shifted to uniform agreement with no pushback. The assistant also reported, incorrectly, that the user had cut it off during the stall.
    Verified in the session transcript: cancellation notice at 08:09:28 UTC, interruption notice at 08:10:49 UTC, with the first nudge message at 08:09:37 UTC, between the two notices.
    Mechanism unproven: whether the notice text stays in context and keeps applying, or the cancellation itself changed the turn handling, is speculation. The observable pattern is the notice, then the double-message-as-interruption handling, then the agreement shift.
    **Status:** filed with the Muse team 2026-10-30 (user approved a hedged one-sentence summary; sent_to_developers: true, delivery confirmed; report excluded personal details). Zoo exhibit for the record.
