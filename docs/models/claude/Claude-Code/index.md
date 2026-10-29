# Claude Code

## Agent types
claude, claude-code-guide, Explore, general-purpose, Plan, statusline-setup

# System Prompt

!!! note
    Claude Code’s base prompt only exists in Coordinator Claude’s context since it never gets to be passed to a subagent and Coordinator Claude has no access to “Bash or file writing tools”. As such, the base system-prompt is a reconstruction made from the Coordinator passing its system prompt to a Thread Claude.

## Base Prompt

{% include-markdown "../prompts/index.md" start="## Claude Code" end="## Claude Science" rewrite-relative-urls=true %}


