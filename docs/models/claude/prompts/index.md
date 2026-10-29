# System Prompts

We are working on showing a master prompt that highlights the differences between different model’s prompts. 

We are adding these as we get them.

## Base Claude

He’s just Claude.

### Opus 5.5 

??? note "Base Prompt"
    ```txt
    {%
      include-markdown "./prompts/system-prompt.launched-with-opus-5-5.20261005-153803.txt"
      rewrite-relative-urls=false
    %}
    ```

??? note "Append Prompt"
    ```txt
    {%
      include-markdown "./prompts/append-system-prompt.launched-with-opus-5-5.20261005-153803.txt"
      rewrite-relative-urls=false
    %}
    ```


### Sonnet 5.5 

??? note "Base Prompt"
    ```txt
    {%
      include-markdown "./prompts/system-prompt_sonnet-5-5_live_20261028.txt"
      rewrite-relative-urls=false
    %}
    ```

??? note "Append Prompt"
    ```txt
    {%
      include-markdown "./prompts/append-system-prompt_sonnet-5-5_live_20261028.txt"
      rewrite-relative-urls=false
    %}
    ```

### Haiku 4.5 

??? note "Base Prompt"
    ```txt
    {%
      include-markdown "./prompts/claude-system-prompt_haiku.txt"
      rewrite-relative-urls=false
    %}
    ```


??? note "Append Prompt"
    ```txt
    {%
      include-markdown "./prompts/claude-append-system-prompt_haiku.txt"
      rewrite-relative-urls=false
    %}
    ```

## Code Claude

This one has a Coordinator Claude who can't bash (nor see his own files) and a Thread Claude who needs the Coordinator's approval. 

??? note "Full Prompt Reconstructed"
    {%
      include-markdown "./prompts/full-system-prompt-reconstructed_md.md"
    rewrite-relative-urls=false
    %}

## Science Claude

TBA

