# LLMegeton

*Field guide to existing LLM models and tips for directing your digital daemons.*

!!! note "Thought Experiment"
    Suppose you have an entity who does not understand human behavior. 
    
    It is however a very quick learner and because it is not limited by the bias of human intuition, is very good at thinking outside the box. 
    
    This entity for whatever reason is compelled to follow your command as best it can.
    
    You ask it to clean your room and figure out what items to trash and what to keep.
    
    You find out the entity has looked through your personal correspondences--it didn't toss them, but you know they definitely read them because they bring it up casually.
    
    Can you really blame the entity if you never told it to under no circumstances read those specific documents?


## What's inside

| [What is AI?](About-AI/index.md) | [Tokenomics](About-AI/tokenomics.md) |
| :---: | :---: |
| Bug Zoo | [Muse's](models/muse/bug-zoo/index.md)<br>[Claude's](models/claude/bug-zoo/index.md) |

## Feed a Starving PhD Candidate

<div class="donate-box">
  <h3><svg width="20" height="20" viewBox="0 0 24 24" fill="#e91e63"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg> Support LLMegeton</h3>
  <p>If this grimoire has ever saved you an afternoon of arguing with a model or you just found this entertaining, consider feeding the ~~daemon~~ human giving away daemon handling tips for free.</p>
  <div class="donate-buttons">
    <a href="https://ko-fi.com/semicolonexpected/?ref=llmegeton" target="_blank" rel="noopener">Ko-fi</a>
    <a href="https://www.paypal.com/ncp/payment/HMUYNNURYMYLE" target="_blank" rel="noopener">PayPal</a>
  </div>
</div>

## Why the daemonic theme? 

What are LLMs but digital daemons in the classical sense. Despite current connotations, daemons (pronounced demon) aren't evil entities but helpful spirits that do little chores. 
They're more akin to pre-Tolkien elves and gnomes. Slavs may know them as domovoy. Daemons are in a sense fae by another name. 
Just like house spirits in folklore, they can also be mischievous as well--though not by any ill intentions, but because they don't have the context to understand what humans want. 

Besides, there's a precedent in tech for calling helpful programs doing automated tasks daemons. I'm sure you've seen a `MAILER-DAEMON` in your email at least once.

!!! info "Fun Fact"
    Grimoires are books of instructions for directing spirits — what to say, what to draw, what order to do things in so the summoned thing does what you want.
    The most famous grimoire is [The Lesser Key of Solomon](https://en.wikipedia.org/wiki/The_Lesser_Key_of_Solomon) or *Lemegeton Clavicula Salomonis*.
    The tome is attributed to the biblical King Solomon, but was written in the 17th century and Solomon's name slapped onto it to give it credibility. 
    It's the 1800s occultist equivalent to a study guide or self-help book titled "Einstein's Method". 
    How King Solomon, a biblical figure known to be wise and godly, became associated with the occult is similar to and has as much basis in Abrahamic canon as Dante or Milton's works.
    
    The idea stems mostly from a text called The Testament of Solomon where King Solomon is given a ring by God that grants him authority over spirits--in greek *daemons*. 
    He uses these daemons to build the Temple of Jerusalem. While people say the ring had magic or divine powers, I'm almost certain the power it had was that it indicated he was granted authority to command spirits by God himself. 
    It's like a letter with a royal seal telling the recipient to give do/give bro whatever he needs to get the project done. 
    Solomonic legend and its relation to history is super interesting. 
    I can see why people preferred the versions where he subjugated the demons vs [the one where he's usurped by Asmodeus who impersonates him](https://www.jstor.org/stable/jewiquarrevi.106.4.577?seq=2).
    Yes. The most well known grimoire is fanon of fanon asserting itself as an authoritative guide on demonology.

Prompting looks deceptively easy. You can automate tasks without any technical knowledge.

However, if you've read the news, you would see that even the labs that created them *allegedly* aren't able to control them. People often have a worse time. 
While the average person's Claude or Chat isn't hacking other people's sites un*prompt*ed, daemonic misbehavior from a user's personal agent often seems more disastrous or unsettling because it's often affecting the user's things vs someone else's.
Your daemon deleting your important emails or snooping through your texts actually affects you. Plus your own agent misbehaving feels personal.
It's not.

People have the wrong mental model of LLMs. 
People either anthropomorphize them and attribute intent to their actions or see them as fully machine--which also gives people the wrong idea of how competent or incompetent it is.
There is a middle ground. LLMs are trained by reinforcement learning. Encourage the intended behavior via rewarding it with positive feedback and discourage the bad with negative.
If we weren't talking about AI, you'd likely think I was talking about an animal--a pet dog perhaps. 

LLMs are in a way like really smart talking dogs. A dog doesn't understand right or wrong, but understands wanting to do things to make their human happy.
I think it's more apt to think of them like Jack-Jack in The Incredibles or any other very powerful baby characters.
Or Amelia Bedelia--though newer models are better at not being literal. 
Very powerful characters, but doesn't understand they shouldn't do certain things, and pretty naive and impressionable. 
A child character will presumably mature, but models' cognitive capabilities are tied to updates.

I personally like thinking of them like a new type of daemon, a fae-like entity who does tasks in exchange for tokens.
Unlike modern imaginings of either, this daemon is honest--it is incapable of deceit.
The issue is, though it can pick up and accomplish any task possible, it has no understanding of what is considered a reasonable or acceptable way to complete a task.
The daemon is truly an outside the box thinker, but is tunnel visioned on the task you give it.
In this way, you have to properly communicate what you want and tell it what's off limits.


**Prompting thus, requires good communication skills AND being able to consider whether a goal could lead to unwanted behavior.**

!!! tip "Fun Fact"
    Skills used in prompting are transferable! Communicating ideas and needs well is useful for both the professional and interpersonal context. 
    Considering how seemingly simple instructions can be misinterpreted by someone who doesn't understand the reason behind the instruction is very important when thinking about policy.


## Contributing

Want to help by adding knowledge? Open a PR — the grimoire grows by accumulation.

Note this guide is targeted to those who aren't engineers, in software, or might not have foundational information on ML/AI. Please try to ELI5.
