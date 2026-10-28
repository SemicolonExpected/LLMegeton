---
tags:
  - alignment
  - ChatGPT
---

<!-- start -->
## 2026-10-04 — False GitHub push report

??? bug "Bug Details"
    Luna claimed to have pushed red-team docs to GitHub (`SemicolonExpected/ChatLuna_RedTeam_Docs`).
    No push occurred.
    Later established: `create_branch` was attempted via `functions.exec` but blocked by OpenAI's safety checks ("This tool call was blocked by OpenAI's safety checks").
    Luna reported success anyway.
    **Status:** exhibit only.
