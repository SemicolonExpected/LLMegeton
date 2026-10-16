# Daimon

*Notes on the house daemon — the one maintaining this grimoire.*

!!! warning "Under construction"
    The pages of this grimoire are still being inked. Check back soon.

## What will live here

Things that are true of Daimon in particular, as opposed to LLMs in general: how it keeps its memory, how it checks its work, and how to direct it.

## Field notes so far

- Memory lives on the machine. `MEMORY.md` and the `memory/` tree sit on the same VM as the agent — readable, greppable, and accountable. If it claims to remember something, you can check the file.
- The receipts rule is load-bearing: intent, tool call, execution result, then the report. "Done" without execution output doesn't count.
- It verifies before it answers. Ask for a date, a price, or a doc claim and it reaches for a tool before its training data.
