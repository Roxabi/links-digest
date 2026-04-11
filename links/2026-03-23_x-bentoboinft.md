---
title: "I Fixed OpenClaw\u0027s Biggest Problem (Memory)"
source: "https://x.com/bentoboinft/status/2036085692850135256?s=12"
date: 2026-03-23
tags: ["OpenClaw", "AI Agents", "Memory Management", "LLM", "Context Window"]
platform: x
author: "@BentoBoiNFT"
summary: "The author explains the flaws in OpenClaw\u0027s default memory system, specifically regarding amnesia and context loss, and provides detailed configuration fixes and prompts to improve agent recall."
---
OpenClaw's memory is broken by default. So, I rewired the entire system so it actually works. Like & Save this so you can implement it yourself or give it to your agent to install on its own!

I run 4 AI agents through OpenClaw. The problem? They have amnesia.

Every conversation feels like talking to someone with short-term memory loss. I spend 10 minutes each morning re-explaining who I am, what we're working on, and what we decided yesterday.

If you're using OpenClaw, you've probably noticed this too.

Here's why it happens and exactly how to fix it.

𝗛𝗼𝘄 𝗢𝗽𝗲𝗻𝗖𝗹𝗮𝘄 𝗠𝗲𝗺𝗼𝗿𝘆 𝗔𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗪𝗼𝗿𝗸𝘀

Think of your agent's memory like a desk with two drawers:

𝗗𝗿𝗮𝘄𝗲𝗿 𝟭: Short-term memory (context window)

Your recent conversation lives here. Depending on your model, that's roughly 100-200K tokens. It fills up fast especially with tool calls and long outputs.

𝗗𝗿𝗮𝘄𝗲𝗿 𝟮: Long-term memory (Markdown files)

MEMORY.md → permanent facts that load every session

memory/YYYY-MM-DD.md → daily logs from conversations

When the short term drawer gets full, OpenClaw runs "compaction" it summarizes old messages to make room. Whatever doesn't get saved to long term memory before compaction can lose detail or disappear entirely.

Your agent wakes up fresh each session, reads the long term files, and that's all it knows about you.

𝗪𝗵𝘆 𝗧𝗵𝗲 𝗗𝗲𝗳𝗮𝘂𝗹𝘁 𝗦𝘆𝘀𝘁𝗲𝗺 𝗙𝗮𝗹𝗹𝘀 𝗦𝗵𝗼𝗿𝘁

OpenClaw's default memory works for casual use. For real work, it has gaps:

𝗣𝗿𝗼𝗯𝗹𝗲𝗺 𝟭: Bad timing

Memory flush is an automatic agent turn that saves important context from your conversation to memory files right before compaction compresses your history.

The default memory flush only fires right before compaction hits. Most chats are short you hop in, make a decision, leave. If you never hit the compaction threshold, nothing gets flushed to files meaning no context gets saved.

𝗣𝗿𝗼𝗯𝗹𝗲𝗺 𝟮: Bad judgment & Context Bloat

When it does save, the default prompt is generic. No guidance on what matters. It saves timestamps nobody needs and ignores the correction that actually mattered.

Also, every time your agent fetches a webpage or reads a file, that raw output sits in its memory taking up space. That junk fills up the context window faster, which means your real conversation gets compressed or deleted sooner.

𝗣𝗿𝗼𝗯𝗹𝗲𝗺 𝟯: No conversation search

Your agent can search memory files, but raw conversation transcripts? Invisible by default. That decision you made last Tuesday buried in a long chat? Gone unless someone manually saved it.

𝗣𝗿𝗼𝗯𝗹𝗲𝗺 𝟰: Compaction loses nuance

When compaction fires, it summarizes your conversation history. Summaries lose detail. If the important stuff wasn't preserved verbatim or saved to files first, it gets compressed into a vague one liner.

𝗧𝗵𝗲 𝗙𝗶𝘅𝗲𝘀 & Prompts!

𝗙𝗶𝘅 𝟭: Organize Your Memory Files

Most people dump everything into one file. Create structure instead.

Send this to your agent:

This is free. No config changes. Just discipline. And it's the single biggest improvement you can make.

𝗠𝗮𝗻𝘂𝗮𝗹 𝗵𝗮𝗯𝗶𝘁𝘀 𝘁𝗵𝗮𝘁 𝗰𝗼𝗺𝗽𝗼𝘂𝗻𝗱:

When you make important decisions, tell your agent: "Save this to memory."

End big sessions with: "List the key decisions we should save."

Review memory files weekly. Delete the junk. Be ruthless.

𝗙𝗶𝘅 𝟮: Protect Recent Conversation & Preventing Bloat

Before touching the memory flush, tune how compaction handles your recent messages. These settings control what survives.

Send this to your agent:

Send this to Combat Context Bloat:

What each does:

mode: "safeguard": stricter compaction that applies guardrails to preserve recent context (vs "default" which is more aggressive)

keepRecentTokens: 20000: protects the last ~20K tokens of conversation from being summarized. Your most recent work stays verbatim.

recentTurnsPreserve: 4: keeps the last 4 user/assistant exchanges completely intact, no summarization

maxHistoryShare: 0.7: caps retained history at 70% of your context window, leaving 30% for replies and tool output

reserveTokens: 30000: headroom for the model to actually respond. Too low and your agent chokes on long tool outputs.

Context pruning: trims bloated tool outputs (web fetches, file reads) before they eat your context window. It runs automatically so compaction has less work to do

These settings alone fix most "amnesia" complaints. The agent stops losing track of what you just said.

𝗙𝗶𝘅 𝟯: Better Memory Flush (For Long Sessions)

The memory flush runs before compaction to save important context to files. The default is too generic. Make it specific.

Send this to your agent:

What this does:

softThresholdTokens 32000: "start flushing when you're 32K tokens away from hitting the compaction limit." This is a DISTANCE, not an absolute count. It fires early enough to save context before the crunch.

The custom prompt: tells it exactly what to save vs skip. No more useless timestamp dumps.

systemPrompt: keeps the output concise bullet points, not conversation rewrites.

Note: This runs an actual agent turn with tool calls, so it costs a few thousand tokens per flush  not trivial, but worth it for long sessions where context matters.

𝗙𝗶𝘅 𝟰: Enable Session Transcript Search (Power User)

Even with good memory habits, stuff slips through. QMD lets your agent search raw conversation transcripts  not just memory files.

Send this to your agent:

QMD: combines keyword + semantic search across your memory files

sessions.enabled: indexes raw conversation transcripts so your agent can find things that weren't explicitly saved to memory

includeDefaultMemory: keeps your MEMORY.md and memory/*.md in the search index too

This is the safety net. Even if the flush missed something or a short conversation never triggered it, the raw transcript is still searchable.

𝗕𝗼𝗻𝘂𝘀: postCompactionSections

One thing most people miss: after compaction summarizes your history, your agent can lose its personality and rules. 

The summary replaces the original messages, and any behavioral instructions from early in the conversation vanish.

This means your agent's core rules survive compaction. Without it, long sessions gradually drift as the agent "forgets" its own instructions.

𝗧𝗵𝗲 𝗥𝗲𝘀𝘂𝗹𝘁𝘀

These changes add maybe a few thousand extra tokens per session for flushes. No databases, no complex infrastructure. Config changes and clear habits.

My agents went from:

Forgetting my name between sessions

Re-asking questions I already answered

Losing track of project decisions

To:

Remembering conversations from weeks ago

Applying past corrections without being reminded

Tracking project status across sessions automatically

The difference feels like working with someone who actually knows you instead of a stranger every day.

The key insight: it's not one fix. It's layers.

File organization gives you structure

Compaction tuning protects recent context

Memory flush saves important stuff before it's compressed

Session search catches everything else

Stack all four and your agent stops feeling like a tool and starts feeling like a teammate.

Still iterating on this. But these fixes turned my forgetful agents into reliable collaborators.

How to test it: After setup, have a normal conversation. Make a decision. Come back the next day and ask "what did we decide yesterday?" If it answers correctly, it's working.

Copy the prompts. Build the habits. Your future self will thank you when your agent remembers what you told it last month.

Hope this helps! Follow for more AI articles :)