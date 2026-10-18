---
tags:
  - Muse
  - Spark 1.3
  - app
---

<!-- start -->
## 2026-10-06 — ChatGPT iOS "Report app issue" can't accept bug evidence (OpenAI)

??? bug "Bug Details"
    The in-app bug-report flow's only screenshot option is "Include screenshot in report" — which attaches an auto-captured screenshot of the *report form itself*. There is no picker for the user's own evidence.
    OpenAI's own support docs say "Screenshots, Screen Recordings ... Attach any visual aids that can help illustrate the problem" — the in-app flow contradicts the docs.
    Luna's verdict, unprompted: "If I'm reporting a visual bug, the evidence is the bug. The reporting form is not the bug." Even Luna was baffled.
    Bonus exhibit: the user tried reporting this on community.openai.com and was auto-silenced with reason "New user typed too fast" — for pasting specs into the bug report. The bug-report pipeline rejects bug reporters at every layer.
    **Status:** not filed (reporter was muted). Zoo exhibit only.
