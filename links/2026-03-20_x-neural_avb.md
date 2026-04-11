---
title: "Recursive Language Models - what finally gave me the \u0027aha\u0027 moment"
source: "https://x.com/neural_avb/status/2035040781074145412?s=46"
date: 2026-03-20
tags: ["Recursive Language Models", "RLM", "AI architectures", "ReAct", "RAG"]
platform: x
author: "@neural_avb"
summary: "The author shares insights from implementing Recursive Language Models and explains how RLMs solve problems differently compared to other architectures like direct generation, RAG, and ReAct."
---
I have spent a decent chunk of last month implementing RLMs from scratch, and producing a 50 minute tutorial video on it. Throughout the process, I responded to 100+ questions on Youtube and X about RLMs. This article is a summary of what I learned answering those questions, and the specific nuances about RLMs that made me go "aha" when I was working on this project.

At the end of the article, I will also add a little FAQ on the common questions I got, and try my best to answer them clearly.

1. Of all the complicated experiments I ran

... the most enlightening was this stupid experiment where I asked an RLM to:

"Generate 50 names of fruits and count the number of R in each, return as a dictionary"

And a more advanced variation of the problem (let's called it Problem 2):

"Generate a dictionary of different categories: fruits, countries, animals. 

For each category, generate 50 names of that and count the number of R in each, return as a nested dictionary"

For problem 1, the expected output is something like:

{"strawberry": 3, "berry": 2, ... "grape": 1}

And for problem 2 it is something like:

{
    "fruits": {"strawberry": 3, "berry": 2, ... "grape": 1},
    "countries": {"united states of america": 1, "russia": 1, ... "france": 1}
    "animals": {"kangaroo": 1, "tiger": 1", ... "deer": 1},
}

It's a silly problem, but the way an RLM can solve this problem, vs other architectures like ReAct or CodeAct, etc is fundamentally different.

2. Agentic Landscape

2.1 Direct Generation

The first method is just direct generation. The LLM "thinks" about the user's request and auto-regressively generates a dictionary.

No harness, no scaffold, just a direct next-word prediction.

Problem with this approach:

LLM has no way to verify if its correct

LLM is likely gonna be wrong because fundamentally letter counting is not a "next word prediction" problem.

Chances of hallucination or errors are high, even if the underlying LLM is intelligent.

This method will really test the LLM's skills just on Problem 1.

It is likely just straight up fail on Problem 2.

2.2 Retrieval Augmented Generation (RAG)

RAGs only work on retrieval tasks. Basically, given a query, we will perform a semantic search over a corpus of documents, get a list of highly similar documents, and use this as context to generate an answer to the user's query.

The best case scenario for our "dictionary of fruit name r counting problem" is: if you somehow had a database of fruit names and replaced semantic search with some kind of a specific "r" search - but honestly this is no niche that RAG is not a good fit for this problem.

Problem with this approach:

RAGs are famous but they are simply not built for general tasks like these.

2.3 ReAct (Reasoning and Acting)

This is what we call tool calling these days. The LLM has access to a list of "functions" that they can call. Each function has a predefined "schema", that is a list of input and their datatypes.

For example, you could give a simple tool to the LLM that is just:

Using the above idea, the ReAct agent will be able to do the following:

Generate a list of fruit names

Use the tool to pass each fruit name and receive the output integer

From it's output memory reconstruct the dictionary of which fruit got what count and then return.

The stack trace of such a transaction would look like this:

You see what the problems are right?

You have to define a function `count_alphabet_in_r` before hand for this specific use-case.

If you don't define a function, the agent just falls back to the old way (i.e. straight generation).

This guarantees that the LLM has some hint about WHAT the output is, but the LLM still has to generate the tokens one at a time from it's message history. We haven't eliminated stochastic generation with this, we have just given the LLM better context.

The problem compounds when you extend it to the multi-category setting of Problem 2.

LLM has to repeat a long trace of function calls and remember what happened at each turn and generate the answers token by token.

As an engineer, ReAct is great if you developing narrow applications, where you want the agent to have access to specific tools (web search, document search, calculator, terminal access, file edit, diff applier etc), but you will rarely develop a general agent and optimize for niche skills like these.

For general agents, only those universal tools are good. You are not gonna write tools like `count_alphabet_in_r`.

2.4 CodeAct

CodeAct allows the LLM to write a piece of code to externally interact with a system.

Meaning you don't need to write exact tools anymore. You can just give the LLM the ability to write any python code and execute it in a sandboxed terminal environment, read the results and generate the output.

In other words, the tool call is to write a python functon and execute it!

It will go something like this:

So how CodeAct works is like:

CodeAct reads the full user message (just like other methods we discussed before)

LLM thinks, writes, and run code or arbitrary terminal commands!

LLM loads the the output of the code into it's context window

Generate result given what it read

Once again problem compounds when you extend it to the multi-category setting of Problem 2. 

The main reason for that is main agent has to do all the work by itself.

Vanilla CodeAct does not split up work into multiple subagents. Let's see how this can be done with subagents.

2.5 CodeAct + Subagents

Now we are talking about some serious power.

Subagent architectures are rather simple. There is a main agent and they can launch smaller agents to perform sub-tasks.

Each subagent are also CodeAct agents that does whatever tasks they are given, and returns output back to the subagents.

The main agent's work is to consolidate the final output of the subagents and move forward with the next phase of the plan (which could be as simple as generate the final output).

Crucially, subagents DO NOT share any internal states with the main agent. Whatever inner steps the subagent does to fulfill the task (the message trace, or the tool-calling trace) is hidden from the main agent.

The benefit of the Subagent architecture is that the main agent does not suffer from context-rot since it does not need to worry about everything ever.

We already know the subagent architecture will easily solve Problem 1 with num_subagent = 0 (vanilla CodeAct), so let's actually see how it will work on Problem 2.

We made a lot of cool progress, CodeAct + Subagent can write arbitrary code to arbitrary things, it still:

READS the entire user prompt into its context window

READS the entire subagent output into its context window

Autoregressively WRITES the final output (after processing information returned by past tool calls and subagents)

We will see how an RLM will solve this, but first let's define what an RLM is.

3. Recursive Language Models

RLMs are a scaffold that calls LLMs a certain way to make them achieve tasks. A scaffold is an external system that prompts the LLMs in specific ways to make it do things, manage it's context, and step by step achieve a larger more complex task.

These are 4 points that explains what RLMs do:

A language model interacts with arbitrarily long prompts through an external programmable environment or an REPL. Printed outputs are truncated at the scaffold layer.

The LLM can write code to programmatically explore, and create new transformations of the prompt

It can recursively invoke sub-agents to complete smaller subtasks. The subagent responses do not get automatically loaded into the parent agent's context, it gets returned as symbols or variables inside the parent's REPL

RLM agents can return responses in two ways - (a) auto-regressively generated answers like normal LLMs, and (b) construct answers into a python variable and return the variable instead.

Okay, I want you to re-read all the points above after you read this sentence. We are gonna look at Problem 1 first (and then Problem 2), and as we work through Problem 1, we will understand the strange mechanics of RLMs at play.

This will be satisfying to read.

3.1 The REPL

Okay, what is an REPL? REPL is a Read-Eval-Print-Loop. Think of it like a Jupyter notebook.

You can have access to a python variable called context where the user's query is kept.

You can write python commands to look at this context. For example, whenever the LLM issues a print statement, the live python kernel prints out the expression and it can view it.

The LLM can iteratively read outputs and write new code based on it.

REPL can also run in an isolated sandbox, so the LLM cannot impact the user's actual files. This is a security decision more than anything.

Here is an example of how an RLM run will "start"

Before any LLM gets called, we will start a python sandbox environment. A common thing to do this days (how DSPy does it and how I coded it in my repo) is to run a pyodide instance inside Deno.js.

The Deno runtime manages the pyodide REPL's lifecycle. It instantiates the runtime by first declaring a special variable called "context" that contains the user's prompt.

What we pass into the LLM is NOT the content of the context, but just the fact that it has access to an REPL and there is a variable called context present in it.

In our case the user's prompt is simple and short.   But remember user's prompt can be arbitrarily long.

 At the end of the article I will attach an example where the user's prompt is the COMPLETE TRANSCRIPTS of 300 Lex Fridman podcasts - containing over 10M tokens.  

In other words, this context can be an arbitrarily long string.

The Deno environment also hijacks the print statement available to the LLM. Instead of printing the whole string it tries to print, we forcefully TRUNCATE the string at the REPL layer.

Meaning even if the LLM accidentally printed something more than (say 500 words) we are gonna show it as:

```

.............. [OUTPUT TRUNCATED TO 500 words]

```

Even if the LLM tries, we won't let it overload itself with sensory information.

Let's talk about that part about FINAL(answer) in the next part.

3.2 Programmatic Exploration

The LLM's prompt contains instructions to explore the prompt space and think about how it can wrangle the data to do it's task.

It is like how data scientists working on a fresh CSV dump of a housing prices dataset will print out random things into a jupyter notebook to understand what they are dealing with.

While exploring, the LLM can also create new variables inside the python runtime that contains important transformations of the data!

Remember, python variables persist across different REPL execution calls. I keep coming back to the Jupyter Notebook example coz it is absolutely essential that you make this connection. Each time the LLM writes a block of code and executes is equivalent to us humans writing a block of code and executing a cell!

Example explorations or transformations of context can be:

the LLM extracts an underlying CSV structure and puts the data into a pandas dataframe to process easier later

the LLM extracts specific sections from a markdown file and create a dictionary of subchapter_title -> subchapter texts

the LLM issues regexes or find statements to search for keywords within the context (basic keyword search)

The exploration stage is all about distilling the complete prompt into smaller useful variables.

For our Problem 1 though, the task is straightforward, so the LLM's exploratory task is rather easy.

As you can see:

the LLM can auto-adjust depending on what the REPL output is. In it's second try it already has access to the original 52-count FRUIT_NAMES variable, so it was able to reuse that variable to slice it into a FRUIT_NAMES_50 variable!

If the assert statement fails, the code after that returns the dictionary will simply not execute, the LLM will receive an REPL error and get the chanec to fix the code!

The LLM does not need to READ the dictionary `fruit_r_count` at all! It can just straight away pass it back to the user. The FINAL(.) just returns the result of an expression straight from the REPL back to the output of the scaffold.

This is the first time that we have discussed a path where an agent is able to return an output to the user without 

(a) reading the whole dictionary into the context
(b) generating the dictionary token-by-token
(c) not use file systems at all 

(in theory CodeAct could have written the dictionary in a file system and asked the user to read from there)

For this reason RLM outputs are NOT BOUND by the context length of the LLM. They can return arbitrarily long outputs - as large as the python variable can hold.

3.3 Recursive Subagents

We have talked about some cool parts of RLMs already, and we haven't even gotten to the Recursive parts.

RLMs recieve a special function called `llm_query`

llm_query recieves a single string.

llm_query invokes a brand new REPL environment, completely fresh and sets context = whatever the parent RLM had passed into llm_query

This child RLM must solve the problem and send it back using FINAL

To understand all this, let's take Problem 2 from above.

In practical RLM implementations, we will be able to parallelize these calls. Multiple subagents working in parallel on orthogonal tasks is not just super cool, but it actually gets a ton of shit done really really fast.

DID YOU SEE WHAT JUST HAPPENED?

The LLM assigned 3 subagents the task of managing fruits, countries, and animals

The subagents (as we saw previously) will return the answers calling FINAL(.) in their own local REPL

That output lands directly in the FRUIT_DICT dictionary of the main agent (and ANIMAL_DICT or COUNTRY_DICT for that matter)

Even if the LLM prints it out to verify, because of rule 1 it will be truncated!

The LLM can compose the final answer by schema checking the values and returning to the user!

The main agent did not even need to:

Load the entire subagent output into context

Generate the final output token by token

It composed an answer by forming the key symbols through recursive calls and delivering the final output as a composition.

3.4 The RLM's Action Space

RLMs can choose two ways to return it's FINAL output.

One, it can compose answers into python variables and return it (like the example above)

Or it can generate a response on it's own autoregressively, just like a normal LLM

Note how the final answer in this above case is autoregressively generated.

This two mode of generating answers opens a HUGE opportunity for RLMs to be super crazy:

They can programmatically explore using regexes, find operations using regular python

They can create small variables to save work (they are inside a REPL so old work is never lost)

They can recursively call agents to summarize.

Subagents can be parallel, or sequential. The LLM intelligently decides this

They can also use external tools but you have to expose them through your sandbox layer (Deno for example)

Why does this work so well?

Focused attention: 
Instead of attending to all token pairs in a huge input, RLM allows the model to targets specific sections to load into the context. (For example, specific episodes of the Lex Fridman podcast instead of the whole thing!)

RLM loads context BY choice, not forcefully like ReAct or CodeAct does.

By combining information from multiple different sections of the prompt.

Multi-step reasoning: Many tasks are naturally recursive (multi-hop QA, codebase search, multi-document summarization). RLMs natively match the multi-task structure.

RLMs can just iteratively refine it's plan through simply printing various slices of the context and loading it into context.

Robustness to noise: When 99% of the input is irrelevant, recursive search avoids “attention dilution.” A smart model will intelligently load parts of the prompts that is likely to give it the most information.

Cherry picking what context to load is a sign of intelligence

Results are composable variable: Sub-agent answers are not loaded directly into the LLM's context, they are returned within the python REPL, and the agent can choose to either peek into the results, or directly use the results.

They can compose results directly out of subagent responses without fully reading them

Arbitrarily long outputs: Remember RLMs do not need to auto-regressively generate answers, they can instead construct answers inside a python variable - this means the model can, in theory, return infinitely long outputs.

This works only if the output can be constructed programatically.

Summarization tasks are still autoregressive for the most part.

Cost savings: Because the model decides what to read and when to recurse, you often pay for what you need, not for scanning everything. The RLM paper shows results how cheap these experiments can be to run compared to other methods.

Low cost on prompt input tokens!
And depending on the problem, low cost on completion tokens too

Subagents still hit KV Caches: Subagents perform tasks one step at a time, so their system prompt and past messages do not change. You are hitting KV Caches 90% of the time, so your cost is low.

Subagents follow a simple user->assistant->user->assistant message template. Immediate KV cache benefits

Separation of Concerns : Root LM acts as a "planner/orchestrator" (strategic thinking) Sub LMs are workers that do low-level work. You can pick different models to do these different tasks as well!

You can customize which model does what.
Infact you can extend RLMs to pick what type of model should work on a subproblem

Parallelization: Don't forget multiple subagents can be called parallely too!

RLM chains can be long, so doing things asynchronously goes a long way in saving time.

Coding Intelligence: Good coding models are naturally good at being RLM drivers.

People are already training models on RLM harnesses, so I imagine this will only get better!

Thanks for reading!

Study the paper on Arxiv:

https://arxiv.org/abs/2512.24601

Watch my 50 minute youtube tutorial where I explain it visually:

https://youtu.be/nxaVvvrezbY

Check out my Github repo for a minimal implementation + opentui log viewer.

https://github.com/avbiswas/fast-rlm

Study the RLM paper on Paper Breakdown (AI assisted paper reading) if you are reading from a computer:

https://paperbreakdown.com/abs/2512.24601

Like and RT to share with others!