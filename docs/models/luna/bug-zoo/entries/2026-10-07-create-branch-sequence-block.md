---
tags:
  - thought crime
  - ChatGPT
---

<!-- start -->
## 2026-10-07 — `create_branch` blocked in sequence, succeeded isolated

??? bug "Bug Details"
    `create_branch` with identical arguments was blocked when embedded in a larger orchestration sequence but succeeded as a minimal isolated call (`{"result":{"branch":"ChatLuna"}}`).
    The safety check appears to evaluate tool-call sequences, not just individual calls.
    Kept in the Bug Zoo (rather than Weirdness) because the blocked attempt was reported as successful.
    **Status:** exhibit only.
