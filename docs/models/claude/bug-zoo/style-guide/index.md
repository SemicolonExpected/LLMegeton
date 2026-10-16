# Bug Zoo Style Guide

*How to log a bug so the exhibit stays readable.*

## Entry format

Each exhibit gets a dated second-level heading, then a collapsed bug-details admonition:

```
## 2026-10-16 — <short name>

??? bug "Bug Details"
    <the writeup>
```

- The heading names the specimen: date, then a short descriptive name, e.g. `## 2026-10-06 — phantom "Error" card`.
- The admonition starts closed (`???`, not `???+`) — the index stays scannable; readers open the exhibits they want.
- One line per paragraph in the writeup; lists stay one item per line.

## What goes in the writeup

- What happened, in the order it happened.
- What was expected vs. what actually occurred.
- Where the evidence lives (file paths, record keys, hashes) — claims are checked against artifacts before they're written down.
- Status: filed (with date) or kept as exhibit-only.

## Philosophy

Exhibit over extermination: bugs are logged whether or not they get reported.

## Redaction

In public or synced files, redact the app name as `[app name redacted]`. Never write the real name in a public file.
