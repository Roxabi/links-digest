---
title: "Overhype and marketing | MIROFISH decoded"
source: "https://x.com/aleiahlock/status/2034933878968705503?s=46"
date: 2026-03-20
tags: ["MiroFish", "Artificial Intelligence", "Swarm Intelligence", "Code Analysis", "Marketing Hype"]
platform: x
author: "@AleiahLock"
summary: "A code-based investigation reveals that MiroFish is not a revolutionary predictive swarm intelligence engine but rather a wrapper for existing third-party tools and commercial LLMs with no native AI"
---
The 30 Million Artificial Intelligence Prediction Engine is Just a Chatbot in a Fancy Suit

MiroFish (yes another agent swarm) claims to be the world's first open-source swarm intelligence engine capable of modelling reality with millions of intelligent agents.

However, looking directly at their own python codebase & technical documentation reveals a very different reality. It is a highly effective piece of engineering that sticks together existing third-party tools, but it is not a smart engine & it cannot predict anything.

Here is the exact breakdown of how the so called Predict Anything illusion works, proven by their own source code,

The World's first claim is false,  the website claims MiroFish is the first universal swarm intelligence engine. In reality, their own documentation admits they are simply integrating the OASIS framework from camel-ai. They did not invent the simulation core; they just used an existing open-source tool built by someone else.

The brain is rented (llm_client. py),  the software has no custom artificial intelligence. Looking at llm_client. py, it simply uses standard code to send text prompts to commercial providers like OpenAI. It is a middleman, not a visionary.

The memory is outsourced (zep_tools. py),  the creators boast about agents having long-term memory to create emergent behaviour. The code in zep_tools. py shows they are entirely relying on a commercial cloud service called Zep to store & search text.

The digital citizens (oasis_profile_generator. py),  The complex digital society is just a script asking the language model to generate character profiles. The file oasis_profile_generator. py tells the model to invent an age, a gender, and a standard personality type. These are not living agents; they are basic text files.

The social dynamics (run_twitter_simulation. py & run_reddit_simulation.   py),  the software claims to simulate messy social evolution. In reality, the files run_twitter_simulation. py and run_reddit_simulation. py strictly force the language models to pick their next move from a tiny menu, such as choosing to like a post or do nothing. It is a multiple choice quiz, not free will.

The astronomical API bill,  because the engine relies entirely on external third parties, it is financially unscalable. Every single simulated thought, memory search, and social media post requires a paid API call via llm_client. py and zep_tools. py. Running a large-scale simulation would generate an enormous bill for the user.

Is it even a swarm?,  while the marketing uses Swarm Intelligence to sound futuristic, the technical implementation is a standard multi-agent loop where each agent is a separate call to a central commercial LLM. It is essentially a sequential script masquerading as a collective consciousness.

If it truly predicts,  the creators would never release the code to the public; they would keep it a guarded secret and use it to become billionaires by predicting the stock market.