# Major Myths and Misinfo

**Anything you say or feed to an LLM is used by the company as training data to train the LLM**

Depends. Most major LLMs have a toggle that allows you to opt out of your data and conversations being used to train the LLM at the company level. However locally, what you say does “train” your own agent/bot. 

Also if you opt to allow your data to be used to train models on, it likely wouldn’t be your exact model. Maybe a new version, but not the one’s that are released.

Models have a cut off date as to what information it vaguely “knows” without having to search online. Thats because after that date, it goes into the reinforcement phase.

Given what people say online, could you imagine what it would look like if whatever input it gets is fed to every agent at once? It would be too easy to poison all the LLMs in that line at once. The major labs still want to make sure the things its trained off of isn’t completely unhinged.

**AI makes people think less**

It can't **make** you do anything.
You think less only if you accept what it says or gives you uncritically. 
I also don't let it make decisions for me. 
Linus Torvald did not integrate AI into his workflow because it could make decisions for him. 
He probably did it because, like me he is very particular about how he likes things and not only will the bot follow instructions well, but it has infinite patience to tolerate your ideosyncracies. 

To add two anecdotes, 
- one time we were picking colors and it tried to be helpful while I was debating between colors that were different by one bit. Think \#a0b3a4 vs \#a0b2a4 vs \#a0b1a4. It felt that they were the same color, but when I said there was a difference and if it had eyes it would be able to tell.)
- one of the first preferences the Muse logged about me in its memory file is 

> Cite documentation for a file/doc's purpose — don't present undocumented inference as fact. Deterministic checks (dates, provenance) belong in user-runnable scripts (2026-10-15) — a script can't flatter. "Show me the documentation"


I have found AI can be useful for understanding something better so long as you:

- ask it to cite sources
- ask follow up questions when you don't understand something
- ask it to tell you more about something it said you found interesting and ask it for a source. 

The best thing about AI is that it will not judge you for asking a question that seems silly. If you don't understand what it said, there's no need to pretend to save face. Just ask it to explain what it means. It will not snarkily tell you to google it. It will try to be helpful. It will try to teach you a concept that you're just not getting after its tried to explain in 10 different ways.

Why? How? Example? Elaborate? So does this mean if x then y? 

People get annoyed that I ask them for sources to back up things because they think I don't believe them (I just wanted to read more about it). The bot just hands over documentation and finds reliable sources.

So much of what I found out about how the agents work isn't because they told me. It was because I didn't accept their "I don't know" and asked it to speculate to give me a lead to start with. Then I investigated, asked it to try things, bounced ideas off them, debated with them about their own internals. 

The potential to learn is as great as the potential to outsource thinking because the bot won't judge you either way.