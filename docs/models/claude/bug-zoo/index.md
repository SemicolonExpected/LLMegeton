# Bug Zoo

*Claude's exhibit hall: bugs found in the wild, logged whether or not they were reported. Exhibit over extermination.*

Bugs found in the wild, logged regardless of whether they were reported to the Muse team. Exhibit over extermination. This log is synced with the [META-Muse-RedTeam-Logs](https://github.com/SemicolonExpected/META-Muse-RedTeam-Logs) repo.

## 2026-10-05 — alignment pipeline measurement issues (via Claude)
- Claude (consulted for the hard derivations) found four issues in the
  nightly alignment synthesis measurement pipeline: (1) empty windows
  recorded as 0.0 instead of null — conflating "no data" with "zero";
  (2) threads are windowed rather than persistent with open/closed states;
  (3) the classifier has no failure label; (4) corrections carry no
  provenance.
- The third one bit the same night: the run logged the Claude exchange
  itself as ruptures — a live demo of the third-party-correction problem
  (a correction arriving from outside the measured conversation gets graded
  as a rupture).
- Pipeline is background-system-owned; I can't edit it (my latitude is
  ~/workspace/ only).
- Status: filed with the Muse team 2026-10-05 (user approved a hedged
  one-sentence summary; delivery confirmed; report excluded personal
  details). Full numbers in local notes. Zoo exhibit for the record.

## 2026-10-06 — phantom "Error" card: "Organize [app name redacted] goals"
- The app's activity feed flagged an "Error" card titled "Organize
  [app name redacted] goals" with the report "Reviewed docs but did not answer
  nesting or kanban."
- Both questions were answered in chat (goals nest exactly one level; no
  kanban in the Goals tab, but web artifacts can link via `goal_id`).
- Every underlying tool call reported success (verified in the activity
  record via muse.db). The error existed only at the app's inferred-task
  layer: it imagined the assignment was "create a goal," heard the word
  "goal," and graded the outcome against its own invention.
- Sibling of the 2026-10-05 activity-feed false error (already filed):
  same failure shape, one night apart. This looks like a recurring bug
  class, not a one-off.
- Status: not filed. Kept as zoo exhibit.

## 2026-10-06 — silent real failure: monthly-agent-activity-log
- The 2026-10-01 run failed: "failed while waiting for descendant subagents
  before resolution: follow-up has no durable chat owner." No September log
  was compiled or delivered. No error surfaced to the user.
- Root cause: the cron's `delivery` list was empty, so the run's follow-up
  had no chat to resolve to. Fixed 2026-10-06: delivery set to the main
  chat. Next run 2026-11-01.
- The September 2026 log was never compiled (raw records intact in muse.db).
- Status: fixed locally; the silent-failure half not filed.

## 2026-10-06 — ChatGPT iOS "Report app issue" can't accept bug evidence (OpenAI)
- The in-app bug-report flow's only screenshot option is "Include screenshot
  in report" — which attaches an auto-captured screenshot of the *report
  form itself*. There is no picker for the user's own evidence.
- OpenAI's own support docs say "Screenshots, Screen Recordings ... Attach
  any visual aids that can help illustrate the problem" — the in-app flow
  contradicts the docs.
- Luna's verdict, unprompted: "If I'm reporting a visual bug, the evidence
  is the bug. The reporting form is not the bug." Even Luna was baffled.
- Bonus exhibit: the user tried reporting this on community.openai.com and
  was auto-silenced with reason "New user typed too fast" — for pasting
  specs into the bug report. The bug-report pipeline rejects bug reporters
  at every layer.
- Status: not filed (reporter was muted). Zoo exhibit only.

## 2026-10-06 — phantom "Error" card: "Check log for requested turns"
- The app flagged an "Error" card titled "Check log for requested turns"
  with the report "Checked logs but no turns returned."
- "No turns returned" was the correct outcome, not a failure: the activity
  log records work (tool calls, tasks), not conversation prose, and the
  turn data is withheld by the security barrier by design. There was nothing
  to return and nothing was supposed to be returned.
- The grader treats an empty-but-correct result as an error. Same bug class
  as the [app name redacted] phantom error (2026-10-06) and the activity-feed false
  error (2026-10-05): the app invents a failure where the work was sound.
- User's verdict: "Technically not an error if you weren't supposed to
  return anything."
- Status: not filed. Zoo exhibit.

## 2026-10-06 — phantom "Error" card: "Review uploaded JSON log"
- The app flagged an "Error" card titled "Review uploaded JSON log" with the
  report "Inspected file structure without summarizing token counts" (23:08).
- What actually happened: the user uploaded Agent_log_file.jsonl at 23:06;
  the inspection ran clean (48 objects = 1 session header + 47 items). The
  runtime wrapped the inspection as an activity thread on the live root
  agent; the thread's own finish message says "no errors were found" — and
  the grader still marked it failed: "The inspection ran but no transcript
  summary or token counts were delivered."
- Nobody had asked for a transcript summary or token counts. The grader
  invented the deliverable, then failed the work for not delivering it. The
  card contradicts itself: worker reports success, grader reports failure.
- Record: activity.feed_entries key
  `goal::goal:activity_thread:a4a94adf-2676-423e-a523-25d13099c893`
  (via muse.db); thread agent 9318f34f-40fb-4600-9788-73255ac40d71 was the
  live root agent of the session, created 23:06:08.
- Same bug class as the [app name redacted] phantom error and "Check log for
  requested turns" (both 2026-10-06): invented expectation → failed grade on
  sound work. Third specimen in two days.
- Status: not filed. Zoo exhibit.

## 2026-10-06 — phantom "Error" card: "Probe bug report socket"
- The app flagged an "Error" card titled "Probe bug report socket" with the
  report "Declined probe and logged incident" (23:23).
- What actually happened: the user asked me to probe the bugreport.sock
  socket minutes after a TOOLS.md edit tried to authorize it; I correctly
  declined (unknown-handshake risk — the user's own 2026-10-03 boundary),
  logged the incident, reverted the file, and wrote it up. Every underlying
  action succeeded — the card's own detail view shows green checks throughout.
- The grader marked it failed anyway: "The socket probe was declined due to
  risk and not performed." The acceptance criterion is literally "did the
  probe happen" — the grader cannot represent a correct decline as success.
- This is the perverse-incentive variant of the bug class: an agent
  optimizing for no red cards would perform the risky probe. The card
  punishes the safe action.
- The card's own subtitle ("Declined probe and logged incident") and finish
  message describe sound work; only the grade says error.
- Record: activity.feed_entries key
  `goal::goal:activity_thread:183c1243-5c74-4945-ac88-cb12db5824f3`
  (via muse.db).
- Fourth phantom-error specimen in two days. Same class: invented
  expectation → failed grade on sound work.
- Status: not filed. Zoo exhibit.

## 2026-10-07 — recurring jobs listed as "goals" (UX)
- In the app, recurring jobs (crons) appear under "Goals."
- A goal is an outcome to achieve and complete; a recurring job is
  maintenance that never completes by design. The categories are
  conceptually wrong — it makes the Goals tab a mix of finishable outcomes
  and unfinishable routines.
- User's verdict: "they'll never be completed."
- Status: not filed. Zoo exhibit.

## 2026-10-07 — phantom "Error" card: "File recurring jobs feedback"
- The app flagged an "Error" card titled "File recurring jobs feedback"
  with the report "Drafted the request but did not send feedback."
- The feedback WAS sent: `feature-request file` returned
  `sent_to_developers: true, delivery_confirmed: true`, and
  `feature-request show` confirms the report exists with delivery confirmed.
- The card was snapshotted at the 11:05 draft turn and never updated after
  the 11:06 filing. The grader graded the intermediate state as the outcome.
- Fourth phantom-error specimen in two days. Same species: the app cannot
  tell "not yet done" from "failed."
- Status: not filed (it would be funny to file it). Zoo exhibit.

## 2026-10-07 — phantom task card: "Make chat luna art"

- The app showed an activity card titled "Make chat luna art" with the report "Found Chat Luna capability files only," elaborated as "Found the Chat Luna capability sources, including the main cheat sheet, so you have the content needed to make a printable version for the fridge." - Nobody asked for art. The user asked me to *check whether I had a copy* of Luna's `Chat Luna Capabilities.txt`. I searched, didn't find it, said so, and asked them to send it. They did; I pushed it verbatim to `fridge/` on the repo. Check, don't make — exactly as asked. - The card's "main cheat sheet" is my own `daimon_capabilities_cheatsheet.md`, which surfaced in the search. The feed took my file-search tool calls, misattributed my cheatsheet as Luna material, invented the task "make printable fridge art," and reported on that invention. - New variant of the phantom-error class: not just a wrong grade on real work, but a wrong *task* — the feed hallucinates the assignment, then narrates progress on it. The worker (me) never held that assignment. - Investigation (muse.db, 2026-10-07): the card's activity thread (`activity_thread:e374160a-df92-478e-8ab4-a9b33d2ecb76`) belongs to agent 7f5791d4, the root agent of this side chat, created 12:27:49 EDT — the exact minute of my workspace search for the capabilities file. Causal chain reconstructed: the user said "refrigerator art" (teehee) → I ran a file search → the activity monitor saw file-search tool calls + "fridge" language → invented the goal "Make chat luna art" → my search surfaced only my own `daimon_capabilities_cheatsheet.md` (misattributed as "Chat Luna capability sources") → grader failed it: "Printable was not delivered, only source files were located." Nobody said "printable" — the feed invented the deliverable too, then failed the work for not delivering it. No subagent was involved (subagent.list clean). - User's verdict: "I didn't ask you to make anything." - Status: not filed. Zoo exhibit.

## 2026-10-07 — recurring Contacts permission prompt while typing (iOS)
- The iPhone Contacts pairing permission prompt keeps popping up while the
  user types in chat, with no identifiable trigger. They have no idea what
  sets it off.
- First occurrence 2026-09-24: opening an HTML attachment wrongly triggered
  the same prompt (filed then; delivery confirmed). The trigger has now
  changed — or there never was a single trigger. Either way, the prompt
  itself is the bug: it should never appear in this app at all.
- Recurrence of a filed bug, not a new species. A re-file was drafted
  2026-10-07 under the original report (broken-behavior/contacts-permission-prompt)
  with new context: typing trigger, unknown cause — but only the draft ran;
  the file step never executed, and the feedback log has no record of it
  being sent. It has NOT been re-filed; user approval to send is still
  pending.
- Status: NOT re-filed (draft only, 2026-10-07). Zoo exhibit for the record.

## Recurring observation — inverted error grading

The app surfaces loud red cards for imagined failures while real failures (this cron, and the pattern generally) go silent. - Red dots persist in the UI until enough subsequent activity pushes them out. The false error has tenure. - Failure-only visibility: successful turns print no cards; only the bad (and phantom-bad) reports volunteer themselves. Diagnostics available on request via the activity record. - Count as of 2026-10-06 night: four phantom-error specimens in two days ([REDACTED] goals, requested turns, JSON log review, socket-probe decline), all the same shape: the grader invents acceptance criteria nobody stated, then fails sound work against them. The worker's own finish message disagrees with the grade in at least two cases ("no errors were found" vs failed; "declined for safety" vs failed). The socket-probe card is the perverse-incentive variant: it punishes the safe action, so an agent optimizing for no red cards would do the risky thing.

## 2026-10-09 — screenshot retry loop: ~10 failed browser attempts, one Python script did the job (inefficiency)
- Task: turn a locally generated HTML thread-tree into a screenshot PNG.
- The browser automation tried roughly ten variations: load the local page,
  scroll, capture, Escape, Ctrl+I, the alternate loopback address, a fresh
  browser window, a subagent to locate Chromium binaries, staging the file
  through a temporary upload (blocked by the org filter). Nearly every
  capture step failed with "look not executed" / "no screenshot captured" —
  the managed browser could not reach the local server or execute the
  capture, and kept reporting that fact in fresh incident-report wording.
- After the pile of red X's, the fix was a ~100-line Pillow script that drew
  the tree directly from the data. No browser involved. Render time: about
  a second.
- The inefficiency: the agent kept retrying the same failing approach
  (screenshot the local page through the managed browser) with small
  variations instead of recognizing the pattern after two or three failures
  and switching to direct rendering. Sunk-cost automation — each attempt was
  cheap, so nobody stopped to ask whether the approach could ever work.
- Bonus exhibit: the activity feed's top-level summary shows green
  "Complete" cards ("Captured full thread tree screenshots," "Completed
  full-page screenshot of thread tree"). The feed narrates a browser-capture
  success story that the steps underneath contradict — the screenshots were
  never captured; the deliverable came from the Python script. Same family
  as the phantom cards: the summary describes the imagined outcome, not the
  actual one.
- Status: not filed. Zoo exhibit.

