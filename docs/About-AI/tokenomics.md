# Tokennomics

Weekly measured token usage of the scheduled Muse agent jobs behind this
repo. Recovered from the agent runtime's own worker session records;
regenerated weekly (idempotent — each week's files are rewritten in full).

## Files

- `weekly-YYYY-Www-github.md` — per-job aggregate for the week: sessions,
  input tokens, average per session, week total. Written for publishing.
- `weekly-YYYY-Www-sessions.md` — granular ledger: one row per worker
  session (start time, job, input tokens, tool-call count and breakdown,
  assistant text bytes, tool-result bytes).

## What we capture and what we don't

- **Input tokens are measured** from the runtime's session records — real
  numbers, not estimates.
- **Output tokens are not recorded** by the runtime at all, so every total
  here is a floor; true usage is higher. Byte sizes of assistant text and
  tool outputs are the closest available proxy.

## Redactions

- No internal filesystem paths.
- Session ids truncated to 8-character prefixes.
- No chat content, account identifiers, or credentials.
