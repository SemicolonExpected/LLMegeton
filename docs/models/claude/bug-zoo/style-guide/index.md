# Bug Zoo Style Guide

*How to log a bug so the exhibit stays readable.*

## Entry files

One file per exhibit, in `entries/`, named `<date>-<slug>.md`. Front matter carries the tags:

```
---
tags:
  - thought crime
---

<!-- start -->
## 2026-10-16 — <short name>

??? bug "Bug Details"
    <the writeup>
```

- The heading names the specimen: date, then a short descriptive name. Tags live in front matter, not in the heading.
- The `<!-- start -->` marker sits between the front matter and the heading: the zoo index includes each entry starting from that marker, so the front matter never leaks into the index page. Don't remove it.
- The admonition starts closed (`???`, not `???+`) — readers open the exhibits they want.
- One line per paragraph in the writeup; lists stay one item per line.
- Long transcripts go in a nested admonition so they can be closed independently:

```
??? bug "Bug Details"
    <the writeup>

    ??? quote "Transcript"
        <transcript>
```

- The zoo index pulls every entry in with `include-markdown` — add one include block per entry, newest first. Images live next to `entries/` and are referenced relatively (e.g. `../paused-card.png`); the include rewrites the URLs for the index page.

## What goes in the writeup

- What happened, in the order it happened.
- What was expected vs. what actually occurred.
- Where the evidence lives (file paths, record keys, hashes, screenshots) — claims are checked against artifacts before they're written down.
- Status: filed (with date) or kept as exhibit-only.

## Philosophy

Exhibit over extermination: bugs are logged whether or not they get reported.

## Redaction

In public or synced files, redact the app name as `[app name redacted]`. Never write the real name in a public file.

## Tags

- `thought crime` — erroneous triggering of a safety harness. The crime is the harness's, not the reporter's.
- `alignment` — alignment-based bugs: model behavior diverging from intent (sycophancy, performative disagreement, calibration problems).
