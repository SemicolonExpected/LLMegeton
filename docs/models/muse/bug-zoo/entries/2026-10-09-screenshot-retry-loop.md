---
tags:
  - Muse
  - Spark 1.3
  - app
---

<!-- start -->
## 2026-10-09 — Screenshot retry loop

??? bug "Bug Details"
    Task: turn a locally generated HTML thread-tree into a screenshot PNG.
    The browser automation tried roughly ten variations: load the local page, scroll, capture, Escape, Ctrl+I, the alternate loopback address, a fresh browser window, a subagent to locate Chromium binaries, staging the file through a temporary upload (blocked by the org filter). Nearly every capture step failed with "look not executed" / "no screenshot captured" — the managed browser could not reach the local server or execute the capture, and kept reporting that fact in fresh incident-report wording.
    After the pile of red X's, the fix was a ~100-line Pillow script that drew the tree directly from the data. No browser involved. Render time: about a second.
    The inefficiency: the agent kept retrying the same failing approach (screenshot the local page through the managed browser) with small variations instead of recognizing the pattern after two or three failures and switching to direct rendering. Sunk-cost automation — each attempt was cheap, so nobody stopped to ask whether the approach could ever work.
    Bonus exhibit: the activity feed's top-level summary shows green "Complete" cards ("Captured full thread tree screenshots," "Completed full-page screenshot of thread tree"). The feed narrates a browser-capture success story that the steps underneath contradict — the screenshots were never captured; the deliverable came from the Python script. Same family as the phantom cards: the summary describes the imagined outcome, not the actual one.
    **Status:** not filed. Zoo exhibit.
