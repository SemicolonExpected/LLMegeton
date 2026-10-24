# Bug Zoo Style Guide

*How to log a bug so the exhibit stays readable.*

## Entry files

One file per exhibit, in `entries/`, named `<date>-<slug>.md`. Front matter carries the tags:

```
---
tags:
  - alignment
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

Bug-type tags (what kind of bug):

- `thought crime` — erroneous triggering of a safety harness. The crime is the harness's, not the reporter's.
- `alignment` — alignment-based bugs: model behavior diverging from intent (sycophancy, performative disagreement, calibration problems).

Model tags (which model):

- `Claude`, `Sonnet 5.5`, `ClaudeCode` — Anthropic orange.
- `Muse`, `Spark 1.3`, `Meta.AI` — Meta blue.
- `Gemini` — Google four-color bands.
- `Notion` — white.
- `ChatGPT`, `Luna 5.6`, `Luna 6` — OpenAI green (Luna is a custom GPT).

Tag colors live in `docs/stylesheets/extra.css`, targeted by the slugified tag in the chip's link (`[href*="tag:..."]`). Slugs are lowercase with dots stripped (`Sonnet 5.5` → `tag:sonnet-55`, `Meta.AI` → `tag:metaai`). Write `ClaudeCode` (no space) — the one true spelling. If you add a tag, add its color there too.
