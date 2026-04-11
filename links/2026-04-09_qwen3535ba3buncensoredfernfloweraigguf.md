---
title: "Qwen3.5-35B-A3B-Uncensored-FernflowerAI-GGUF"
source: "https://www.reddit.com/r/LocalLLaMA/comments/1sfwauj/qwen3535ba3buncensoredfernfloweraigguf/"
date: 2026-04-09
tags: ["LLM", "Qwen", "bug-fix", "MoE", "DeltaNet"]
platform: reddit
author: "u/EvilEnginer"
summary: ""
---
# Qwen3.5-35B-A3B-Uncensored-FernflowerAI-GGUF

**Subreddit:** r/LocalLLaMA
**Author:** u/EvilEnginer
**Score:** 218 (97% upvoted)
**Comments:** 179
**Date:** 2026-04-08

**Flair:** Other

## Post Content

Hello everyone. I found and fixed training bug in Qwen3.5 35B A3B model.

Here my fixed version (Q4\_K\_L and BF16 gguf quants now available):  
Repair summary: [https://pastebin.com/aWEC8LEt](https://pastebin.com/aWEC8LEt)  
[https://huggingface.co/LuffyTheFox/Qwen3.5-35B-A3B-Uncensored-FernflowerAI-GGUF](https://huggingface.co/LuffyTheFox/Qwen3.5-35B-A3B-Uncensored-FernflowerAI-GGUF)

Upgraded system prompt that unlocks deep thinking (works great with this model):  
[https://pastebin.com/pU25DVnB](https://pastebin.com/pU25DVnB)

Chat template: [https://pastebin.com/uk9ZkxCR](https://pastebin.com/uk9ZkxCR) (supports tool calling)

**Recommended Settings (LM Studio):**

|Temperature|0.7|
|:-|:-|
|Top K Sampling|20|
|Presence Penalty|1.5|
|Repeat Penalty|Disabled  or 1.0|
|Top P Sampling|0.8|
|Min P Sampling|0|
|Seed|3407|

**History:**

I've been using Qwen 3.5 35B A3B (the uncensored version by HauhauCS) for a while. It's an incredible model - uncensored, MoE with 256 experts, hybrid DeltaNet + Attention, 40 layers, works fine on my RTX 3060 12GB GPU, and has fresh knowledge. But something was off. On short prompts it works fine. On long conversations it started "philosophizing" - losing context, repeating itself, writing broken code with strange comments.

*I spent two weeks digging through the weights.*

**What I found:**

Two tensors. In blocks 36 and 37. `ssm_conv1d.weight`.

Their scale was \~60% higher than normal (σ=0.102 vs median 0.063). Because of how AdamW works, rare experts in the last layers get a huge effective learning rate - their weights drift.

In a recurrent architecture like DeltaNet, this kills the hidden state. The model forgets context after a few tokens.

Surprisingly I didn't found any issues in Gemma 4 26B A4B - all scales were correct in model, but it has oudated 2024 knowledge.

**What I did:**

I scaled broken tensors back to normal. Nothing else. 489 other tensors were left untouched - their scale is architectural (gate\_inp, etc.).

**Results:**

* Error reduction: 88.6% - for 35B A3B.
* Error reduction: 90.7% - for 27B.
* Long conversations now stay coherent.
* Code generation works.
* No more "philosophizing", even with my complex System Prompt.

**What I learned:**

One bug. Two tensors. 64GB of model. And the entire potential of the most complex open-weight architecture was locked behind it.

If you're using MoE + recurrent hybrids (DeltaNet, Mamba, etc.), check your last blocks. AdamW might have silently broken them.

**Enjoy \^\_\^**

## Top Comments (15)

> **True_Requirement_891** (41 points)
> We need to do more investigative shit like this

  > **EvilEnginer** [OP] (18 points)
  > Yep, very true. GGUF is some kind of "blackbox" with hidden things.

    > **VoidAlchemy** (1 points)
    > fwiw, this has nothing to do with GGUF, they are patching the original weights as released.
    > 
    > But yeah GGUF can be confusing too.

> **IrisColt** (28 points)
> Just curious... who's actually responsible for the bug in this model? The GGUF creator? HauhauCS? The Qwen team? Seems like an important distinction. Asking in good faith.

  > **EvilEnginer** [OP] (30 points)
  > The bug is in the original Qwen 3.5 weights released by Alibaba. Not GGUF. Not HauhauCS. Alibaba shipped it broken. I just fixed it. The cause is training-related - AdamW + MoE + DeltaNet causes rare experts in the last layers to drift. This is a known challenge with recurrent MoE architectures, but Alibaba didn't calibrate it before release.

    > **Koalateka** (7 points)
    > Just to be sure I understood this correctly: the error was in the full precision weights originally released by Alibaba. Is that correct?

    > **IrisColt** (6 points)
    > Mother of God... Thanks for the info!!!

    > **ComplexType568** (3 points)
    > Oh wow, does this mean that the Unsloth models are also broken among the models hosted on the Alibaba API?

> **Embarrassed_Soup_279** (16 points)
> does this mean the 27B dense model have similar training bug or is it only MOE?

  > **EvilEnginer** [OP] (48 points)
  > I checked only MoE. I will take a look in 27B tomorrow and will let you know.

    > **Embarrassed_Soup_279** (2 points)
    > wowthank you !

    > **TheLastSpark** (2 points)
    > please reply if you see something like this in 27B as well!

  > **EvilEnginer** [OP] (9 points)
  > 27B is broken - confirmed. I checked this one [https://huggingface.co/unsloth/Qwen3.5-27B-GGUF/blob/main/Qwen3.5-27B-Q8\_0.gguf](https://huggingface.co/unsloth/Qwen3.5-27B-GGUF/blob/main/Qwen3.5-27B-Q8_0.gguf) . Contain 8 broken ssm\_conv1d.weight tensors.

    > **Embarrassed_Soup_279** (2 points)
    > thank you for confirm. this is really interesting. do you plan on also fixing for this variant of hauhaucs gguf?

    > **oxygen_addiction** (1 points)
    > Can you also check Stepfun 3.5?
    > It has a similar problem with overthinking.

    > **Equal_Grape2337** (1 points)
    > So that means that the 4b and 9b should have the same issues? I actively using them at [https://github.com/spokvulcan/tesseract](https://github.com/spokvulcan/tesseract)

> **apollo_mg** (6 points)
> Bravo good sir. Excellent digging, and thanks!

  > **EvilEnginer** [OP] (5 points)
  > Thank you very much :)

> **hockey-throwawayy** (3 points)
> Thanks for sharing this!
> 
> Would you be willing to do some major hand-holding and explain how to quantize this model into something that will fit 12 GB VRAM? I see the script on the HF page, but I am just totally unfamiliar with the nuts and bolts of the process. 
> 
> My local LLM setup understanding begins and ends with "if HF shows my GPU with a green icon, I can try that model." 
> 
> There are so many details to get these models running locally properly and I have yet to figure it all out. I'm looking for a good "daily driver".

  > **EvilEnginer** [OP] (3 points)
  > Just use Q4_K_L quant that I already uploaded. It's best in terms of size and quality. I am using it on my RTX 3060 12 GB. I have 10 tokens per second in LM Studio. 
  > 
  > On llama-server people get even more tokens per second, but I like LM Studio in terms of memory management.

    > **Vast_Strawberry3093** (3 points)
    > Where can i find this Q4\_K\_L quant?

    > **hockey-throwawayy** (1 points)
    > Ah I see it now, thank you!

> **hesperaux** (4 points)
> I want to understand stuff as much as you some day
> 
> Super interesting post. Thanks. 
> I am slightly skeptical of it because of who I am as a person but... You sound like you know what you're talking about. 
> 
> I am definitely gonna try this. I switched to 122B A10B because 35B A3B was.. Strange. Like you said, it got weird after 70k tokens. And it was not good at maintaining a direction. I wonder if it's related. 
> 
> Another person asked if this is only that version (abliterated) or if it's this way on the official model. Can you answer that? 
> 
> Thanks again. Cool stuff.

  > **EvilEnginer** [OP] (3 points)
  > Official model contains this bug too. I checked Unsloth BF16 quant.

> **wh33t** (3 points)
> Interesting. 
> 
> Maybe this explains why I have such poor experiences with Qwen3.5, it just becomes so fucking indecisive all of a sudden, looping itself, and no amount of parameter tuning seems to fix it. This must be the issue.

  > **EvilEnginer** [OP] (3 points)
  > That's exactly it. What you're describing - indecisive, looping, no amount of parameters fixes it - is the signature of this bug. The recurrent state in blocks 36-37 is corrupted. Model loses context, starts repeating, can't decide. Parameter tuning can't fix it because the problem is in the weights themselves. Only scaling those two tensors back to normal works. Try my fixed model with my settings and System Prompt. You'll see the difference immediately. No more loops. No more indecision. Just clean crystal clear human readable responses.

> **jikilan_** (4 points)
> Any way to notify qwen team about this?

  > **EvilEnginer** [OP] (2 points)
  > I think they are monitoring Twitter.

> **Quiet-Owl9220** (4 points)
> Hey nice job. It doesn't give up mid-sentence after extended reasoning and tool calls any more.

  > **EvilEnginer** [OP] (3 points)
  > Nice :). I'm very glad to hear that my fix works well.

> **United_Razzmatazz769** (3 points)
> Thanks for the model. Some qwen3.5 35B A3B models i have tried allways melt down past 50k  tokens. Your model definately feels better. I got past some 100k api endpoint learning planning successfully with it.

  > **EvilEnginer** [OP] (1 points)
  > Great to hear that! 100k tokens is exactly where the original model breaks. Your test confirms the fix works. Thanks for reporting back.

> **Kahvana** (3 points)
> Thank you! Can you upload the safetensor version?

  > **EvilEnginer** [OP] (2 points)
  > Thank you too \^\_\^. Of course. Already done: [https://huggingface.co/LuffyTheFox/Qwen3.5-35B-A3B-Uncensored-FernflowerAI-safetensors](https://huggingface.co/LuffyTheFox/Qwen3.5-35B-A3B-Uncensored-FernflowerAI-safetensors)

    > **Kahvana** (1 points)
    > Awesome! Thank you so much!

> **SeriousTeacher8058** (3 points)
> Why isn't there a standard tool for comparing different versions of an LLM? If I had two versions of the same LLM, and I liked a specific feature from one version that another lacks, why can't I look at the layers and scale them or swap them with the same layers from another version?

  > **Imaginary-Unit-3267** (3 points)
  > Because the mapping from parts of the neural network to traits is extremely ill-understood even by the people doing the training. To a great extent neural networks are black boxes. Figuring out how they operate takes work. The large scale architecture is well understood, but the details of how they encode the information they learn take a lot of digging, and there just isn't a standardized way to do that yet and likely won't be for a few more years yet. For more information on this, look up "mechanistic interpretability" research.

  > **EbbNorth7735** (2 points)
  > I'm sure you can. The file has a structure and it just requires splitting it up and parsing the correct parts to look at the numbers. It's what OP did.

> **WhoRoger** (3 points)
> Lol nice. Any interest in checking the small versions too? 4B, 2B, 0.8B are notoriously prone to getting stuck.
> 
> Btw that's a cute system prompt

  > **EvilEnginer** [OP] (3 points)
  > Thanks :). May be in future. Currently Qwen 3.5 35B A3B and 27B in priority.

> **EvilEnginer** [OP] (3 points)
> Currently cooking experimental Q4\_K\_XL quant of this model: [https://huggingface.co/LuffyTheFox/Qwopus3.5-27B-v3-Uncensored-FernflowerAI-GGUF](https://huggingface.co/LuffyTheFox/Qwopus3.5-27B-v3-Uncensored-FernflowerAI-GGUF) for powerful GPUs.
> 
> This would be the last test for Qwen3.5 27B model series.
> 
> If you want to run uncensored Qwopus3.5 27B on 12 GB GPU with decent speed you can use this script for compression with importance matrix support: [https://pastebin.com/p6iN1f1Z](https://pastebin.com/p6iN1f1Z)
> 
> But it will take almost forever waiting for compression ... 8 - 10 hours on Google Colab Free Tier, and during to heavy maximum compression result can be garbage.

  > **jwpbe** (1 points)
  > I've been using a 27B model variant extensively over the last few weeks, it duplicates model layers that are activated strongly on math and EQ Bench. Would you mind checking it for broken tensors? It's already very strong as it is.
  > 
  > https://huggingface.co/dnhkng/RYS-Qwen3.5-27B-FP8-XL
  > 
  > The explanation of the model: https://dnhkng.github.io/posts/rys-ii

    > **EvilEnginer** [OP] (1 points)
    > I can check this model if it will be in GGUF Q8\_0. I can't load 27B FP8 model in safetensors, because it's too much resource hungry for checking. GGUF is memory optimized for Python runtime.

  > **nemomode7** (1 points)
  > Good job! Best parameters for inference? temp, topk, etc?

    > **EvilEnginer** [OP] (1 points)
    > Simply use parameters from my post on top of this page. With default system prompt: "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."

  > **Embarrassed_Soup_279** (1 points)
  > sorry if it seems like am asking too much, but would you please check this variant of RYS qwen model as well? [https://huggingface.co/jackasda211233/Qwen3.5-27B-Uncensored-RYS-Reasoner-GGUF](https://huggingface.co/jackasda211233/Qwen3.5-27B-Uncensored-RYS-Reasoner-GGUF)  
  > it use a splice method to combine HauhauCS layers with RYS duplicated layers, and it has custom imatrix for reasoning / agentic task. iq4\_nl seems to be the best quant to use, even over bf16 with that.

    > **EvilEnginer** [OP] (2 points)
    > Okay I will check BF16 quant. This one looks really interesting. Since it's uncompressed BF16 I can check tensors precisely and fix them. Now I can fix even broken neurons in neural network. I think it's time to test my new approach on this model.

    > **EvilEnginer** [OP] (1 points)
    > Done. BF16 quant uploaded: [https://huggingface.co/LuffyTheFox/Qwen3.5-27B-Uncensored-RYS-Reasoner-FernflowerAI-GGUF](https://huggingface.co/LuffyTheFox/Qwen3.5-27B-Uncensored-RYS-Reasoner-FernflowerAI-GGUF)
    > 
    > Now i will try to process iq4\_nl as it is.
    > 
    > UPD: iq4\_nl processing doesn't work, because it's already compressed.

> **Fun_Smoke4792** (2 points)
> Remindme! In 14 hours

  > **RemindMeBot** (1 points)
  > I will be messaging you in 14 hours on [**2026-04-09 05:46:41 UTC**](http://www.wolframalpha.com/input/?i=2026-04-09%2005:46:41%20UTC%20To%20Local%20Time) to remind you of [**this link**](https://www.reddit.com/r/LocalLLaMA/comments/1sfwauj/qwen3535ba3buncensoredfernfloweraigguf/of0jzg0/?context=3)
  > 
  > [**4 OTHERS CLICKED THIS LINK**](https://www.reddit.com/message/compose/?to=RemindMeBot&amp;subject=Reminder&amp;message=%5Bhttps%3A%2F%2Fwww.reddit.com%2Fr%2FLocalLLaMA%2Fcomments%2F1sfwauj%2Fqwen3535ba3buncensoredfernfloweraigguf%2Fof0jzg0%2F%5D%0A%0ARemindMe%21%202026-04-09%2005%3A46%3A41%20UTC) to send a PM to also be reminded and to reduce spam.
  > 
  > ^(Parent commenter can ) [^(delete this message to hide from others.)](https://www.reddit.com/message/compose/?to=RemindMeBot&amp;subject=Delete%20Comment&amp;message=Delete%21%201sfwauj)
  > 
  > *****
  > 
  > |[^(Info)](https://www.reddit.com/r/RemindMeBot/comments/e1bko7/remindmebot_info_v21/)|[^(Custom)](https://www.reddit.com/message/compose/?to=RemindMeBot&amp;subject=Reminder&amp;message=%5BLink%20or%20message%20inside%20square%20brackets%5D%0A%0ARemindMe%21%20Time%20period%20here)|[^(Your Reminders)](https://www.reddit.com/message/compose/?to=RemindMeBot&amp;subject=List%20Of%20Reminders&amp;message=MyReminders%21)|[^(Feedback)](https://www.reddit.com/message/compose/?to=Watchful1&amp;subject=RemindMeBot%20Feedback)|
  > |-|-|-|-|
