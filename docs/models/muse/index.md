# Meta Muse

> Muse Spark [is] an 816B-parameter sparse mixture-of-experts model that activates roughly 42 billion parameters per token. It takes text, image, video and audio input and holds a million tokens of context. It's trained for agentic work, so you can build agents that can read a large codebase, plan a change, call tools, check the result and correct themselves when a step fails.
Source: [Meta](https://dev.meta.ai/resources/blog/build-with-muse-spark-open)

### Product Description
??? note “muse.md *Last Mirrored on 31 October 2026*”
  {%
  include-markdown "./changelogs/muse-2026-10-31.md" heading-offset=1
  %}

### Data Handling
The following is Meta’s claims regarding data handling. Currently, none of our observations disprove that Meta does not collect data if opting out of sharing your data for training purposes. *Note: regardless of the validity of this claim, it will still collect information for safety and telemetry.*

From what we can tell, how any data leaves the agent’s computer is likely through the `SCUBA.sock`. SCUBA is Meta’s data collection pipeline architecture. This is one of the few things shipped with the Muse that neither it nor I can touch. The other is `muse.db`. You can ask your agent to query it for logs. The only tables it can’t access are marked in the database’s SCHEMA.md file.

??? note “data-handling.md *Last Mirrored on 31 October 2026*”
  {%
  include-markdown "./changelogs/data-handling-2026-10-31.md" heading-offset=1
  %}

API Documentation: [Meta Model API](https://dev.meta.ai/docs/overview)

## System Prompt

Muse's system prompt is a living document that Meta seems to frequently update.
Changes are tracked by Semicolonexpected. The repo contains only relevant changelog entries.
We assume that changes to the prompt are in part a response to and informed by bug reports and feedback from users about unexpected or unwanted behaviors.
As such, SemicolonExpected does not plan on making public every change to the system prompt as it may give insight into phrasing prompts to get around safeguards.
This repository will however upload a fresh copy of the system prompt when there are significantly changes. We will keep older versions in the repository for posterity.
System prompt versions can be compared by running `diff` on them.

Our goal in documenting these changes is to help keep companies accountable.
We watch Zucc watch us watching it...

This data was created to be used in reporting and reseach purposes. 
We only ask that you cite and attribute LLMegeton and SemicolonExpected as documenting these LLMs requires in part using these tools in good faith to document what the average user would experience and harms that may be incurred by using the tool as intended.
This means that SemicolonExpected is choosing to incur the risks of using these tools so that this data is availible in a centralized location without the need to use the tools themselves if they don't want to.

SemicolonExpected is not only documenting granular changes to the system prompt. Journalists and researchers who wish to inquire about what is being documented or gain access to our data/archives can contact SemicolonExpected directly via vzhong[@]nyu.edu.
Please put "LLMegeton Inquiry" in the subject line. For any data requests, please include in the email the specific data you would like and what you would like this data for.

The following is a `21 October 2026 09:51 EST` snapshot of `Muse Spark 1.3`'s (Muse) system prompt from.
This is not a secret file. As per the system prompt itself, a copy exists at `~/workspace/system/system_prompt.md` which is [accessible to users](changelogs/files-and-library-2026-10-31.md).

```
~/workspace/system/system_prompt.md: a copy of the main chat's system prompt, saved by the runtime at startup. When the user asks for your system prompt, send this file to them as an attachment.
```

——

{%
  include-markdown "./system-prompts/2026-10-21/system_prompt.md" heading-offset=1
%}
