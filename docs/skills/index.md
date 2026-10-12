# Skills

Skills are the shareable units of agent capability: packaged knowledge + instructions that an agent loads when relevant. If prompts are individual evocations, skills are the bound volumes.

## What a skill is

A skill typically bundles:

- **Instructions** — how to approach a class of task (the procedure, the pitfalls, the conventions)
- **Knowledge** — domain facts the model shouldn't have to guess at
- **Examples** — input/output pairs showing the skill done right
- **Tools/scripts** — helper code the agent can run, not just read

The common shape (popularized by Claude's SKILL.md format) is a Markdown file with frontmatter:

```markdown
---
name: pdf-reading
description: Extract text and tables from PDFs, handling scanned pages via OCR
---

# PDF reading

...instructions, examples, conventions...
```

The `description` is the critical part — it's what the agent uses to decide *when* to reach for the skill. Write it as: what it does + when to use it.

## Anatomy of a good skill

1. **Trigger description** — one or two sentences; this is the retrieval key. Be specific about the situations it covers.
2. **Procedure** — the steps, in order. Imperative voice. Assume a smart reader with no prior context.
3. **Conventions** — the non-obvious rules: naming, formats, edge cases, what *not* to do.
4. **Examples** — at least one concrete input/output pair. Abstract instructions alone underdetermine behavior.
5. **Scripts** — if the task involves repeatable mechanics (API calls, file transforms), ship a script rather than describing the steps in prose. Code doesn't get misread.

## Adapting a skill

Skills are meant to be remixed. When borrowing one:

- **Keep the trigger description honest** — rewrite it to match what the skill actually does *for you*, or the agent will reach for it at the wrong times.
- **Prune ruthlessly** — a skill that tries to cover everything gets reached for never. Split it.
- **Localize conventions** — paths, tool names, account details: replace the author's with yours.
- **Test the retrieval** — ask your agent something the skill should trigger on, and something adjacent it shouldn't. Adjust the description until both behave.

## Anti-patterns

- **The junk drawer** — one skill covering five unrelated tasks. Nobody (human or model) can tell when to use it.
- **The novel** — 3,000 words where 300 would do. Long skills get skimmed; put the load-bearing rules first.
- **The oracle** — instructions that assume facts the agent can't verify. If it needs a live check, say so.
