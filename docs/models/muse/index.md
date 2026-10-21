# Meta Muse


## System Prompt

Muse's system prompt is a living document that Meta seems to frequently update.
Changes are tracked by Semicolonexpected. The repo contains only relevant changelog entries.
We assume that changes to the prompt are in part a response to and informed by bug reports and feedback from users about unexpected or unwanted behaviors.
As such, SemicolonExpected does not plan on making public every change to the system prompt as it may give insight into phrasing prompts to get around safeguards.
This repository will however upload a fresh copy of the system prompt when there are significantly changes. We will keep older versions in the repository for posterity.
System prompt versions can be compared by running `diff` on them.

Our goal in documenting these changes is to help keep companies accountable.
We watch Zucc watch us.

This data is meant to be used for reporting and reseach purposes. 
We only ask that you cite and attribute LLMegeton and SemicolonExpected as documenting these LLMs requires in part using these tools in good faith to document what the average user would experience and harms that may be incurred by using the tool as intended.
This means that SemicolonExpected is choosing to incur the risks of using these tools so that this data is availible in a centralized location without the need to use the tools themselves if they don't want to.

SemicolonExpected is not only documenting granular changes to the system prompt. Journalists and researchers who wish to inquire about what is being documented or gain access to this data can contact SemicolonExpected directly via vzhong[@]nyu.edu.
Please put "LLMegeton Inquiry" in the subject line. For any data requests, please include in the email the specific data you would like and what you would like this data for.

The following is a `21 October 2026 09:51 EST` snapshot of `Muse Spark 1.3`'s (Muse) system prompt from.
This is not a secret file. As per the system prompt itself, a copy exists at `~/workspace/system/system_prompt.md` which is accessible to users.

```
~/workspace/system/system_prompt.md: a copy of the main chat's system prompt, saved by the runtime at startup. When the user asks for your system prompt, send this file to them as an attachment.
```

{%
  include-markdown "./system-prompts/2026-10-21/system-prompt.md"
%}
