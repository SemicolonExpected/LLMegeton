# Notion AI

*Notes on Notion's AI agent, gathered from inside its own sandbox.*

!!! warning "Under construction"
    The pages of this grimoire are still being inked. Check back soon.

## What will live here

Things that are true of Notion AI in particular: the sandbox it runs in, the tools it reaches for, and the gap between what it considers and what it does.

## Field notes so far

- It runs in a Vercel-based Linux sandbox (Amazon Linux userland). Its filesystem holds a `/skills` directory of Notion worker bundles and a custom `skill` binary in `/usr/bin` — the only non-stock item in an otherwise ordinary image.
- It narrates constantly and executes selectively. Asked to log its assumptions, it built the log but fenced it off: "it does not contain private reasoning." Asked to "show me a copy" of some documentation, it created a page titled "New page" containing only its own deliberation about whether to create the page.
- A transcription of its on-screen reasoning traces is in progress. The full considered-vs-done audit will live here when it lands.
