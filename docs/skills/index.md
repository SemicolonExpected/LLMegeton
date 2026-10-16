# Skills

Skills are the shareable units of agent capability: packaged knowledge + instructions that an agent loads when relevant.
They're akin to a chapter in an employee manual for the agent to follow when performing a type of task.

LLM agents usually come packaged with various skills, however some models have the skill to create new custom skills and "learn" new prewritten skills.

**[LLMegeton Custom Skills](custom-skills/index.md)** are close to ready to use out of the box and just require editing the files for your specific agent and accounts.

## What a skill is

A skill typically bundles:

- **Instructions** — how to approach a class of task (the procedure, the conventions, DOs and DON'Ts)
- **Knowledge** — domain facts the model shouldn't have to guess at--this includes pointing at another skill document.
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
2. **Procedure** — the steps, in order. Imperative voice. Assume a smart reader with no prior context. Be clear and specific. Reference other existing skills. For example, a skill to clean up emails may link to `gmail/SKILL.md` or direct the agent to the `outlook` skill.
3. **Conventions** — the non-obvious rules: naming, formats, edge cases, what *NOT* to do.
4. **Examples** — at least one concrete input/output pair. Abstract instructions alone undermine behavior.
5. **Scripts** — if the task involves repeatable mechanics (API calls, file transforms), ship a script rather than describing the steps in prose. Code doesn't get misread.

## Adapting a skill

Skills are meant to be adapted to suit individual needs. When borrowing one:

- **READ THE WHOLE SKILL** - skills authored by SemicolonExpected on LLMegeton will typically be safe, however just as you shouldn't run shell commands or give an agent a prompt without knowing what it does, you should definitely not have your agent follow a tome of instructions without knowing what it's telling the agent to do when. 
- **Trigger description** — rewrite it to match how *you* would ask for the task to be done (or the agent will reach for it at the wrong times).
- **Change behavior to suit your needs** — How one person wants a task done may not be how *you* would like it done.
- **Localize conventions** — paths, tool names, account details: replace the author's with yours.
- **Test** — ask your agent something the skill should trigger on, and something adjacent it shouldn't. Adjust the description until both behave. Skills may have unexpected interactions with other skills or act in ways the skill author never anticipated due to differences in settings or other preexisting instructions given by their user or system prompt.

## Anti-patterns

- **The junk drawer** — one skill covering five unrelated tasks. Nobody (human or model) can tell when to use it.
- **The novel** — 3,000 words where 300 would do. Long skills get skimmed; put the load-bearing rules first.
- **The oracle** — instructions that assume facts the agent can't verify. Despite how cognitively capable you believe AI to be, it cannot read minds. If it needs a live check, say so.
