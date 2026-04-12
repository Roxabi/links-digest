---
title: "The Decentralized self-improving AI system that builds itself Democratically "
source: "https://x.com/agent_wrapper/status/2031508924302860406?s=46"
date: 2026-03-10
tags: ["decentralized AI systems", "self-improving agents", "Agent Orchestrator", "fork interoperability", "democratic development"]
platform: x
author: "@agent_wrapper"
summary: "The article describes how decentralized AI systems enable multiple independent forks to evolve locally and share improvements without central authority coordination."
---
preface: what decentralization changes

a self-improving system in one repo is impressive. a network of self-improving systems across many forks is qualitatively different.

in the centralized model, progress is gated by one team's throughput. one backlog, one set of priorities, one definition of "good enough." every user waits for that team to get to their problem. every fork is a dead end because improvements can't flow back without that team's approval.

in a decentralized model, progress emerges from many local experiments running under different constraints, cultures, and priorities. a fork in Bangalore optimizes for mobile-first orchestration. a fork in Berlin builds compliance-aware agent governance. a fork in São Paulo discovers that render pipeline timeouts need completely different semantics than CI timeouts. each one finds truths that a centralized team would never encounter because a centralized team only has one context.

centralized: all forks wait for one team. decentralized: each fork evolves locally, converges voluntarily through a shared protocol.

the hard part is not allowing forks. git already does that. the hard part is making forked intelligence interoperable: local autonomy without global incoherence. forks that can evolve independently, discover their own failures, build their own improvements, and optionally contribute patterns back upstream, all without a central authority coordinating every merge.

that is why today mattered. but to understand what happened today, you need to know what came before.

how we got here

this is the third article in a series. each one covers a different stage of the same system getting better at building itself.

the first article was about open-sourcing Agent Orchestrator. the system that manages parallel AI coding agents on a single codebase. at launch it was 43,000 lines of TypeScript, 17 plugins, a web dashboard, CI integration. Claude Code and Codex sessions running in isolated git worktrees, managed by an orchestrator that handled spawning, lifecycle, and cleanup. it hit 4,000+ stars and 477 forks in under three weeks.

but Agent Orchestrator itself had a backstory. before it was a proper TypeScript system, it was 2,500 lines of bash. tmux sessions managed by AppleScript. shell scripts calling other shell scripts. i wrote every line by hand. it took two weeks to get something that could run 4 agents in parallel without them stepping on each other's code. then i used that duct-taped orchestrator to build the real one. the hacky version managed the agents that wrote the production version.

the second article was about the overnight run that connected everything. i had OpenClaw, my AI assistant running on Telegram, use Agent Orchestrator to build the AO plugin that connects them. the connector, @composio/ao-plugin-notifier-openclaw, routes AO events into OpenClaw via POST /hooks/agent, which means into Telegram, which means into my pocket. OpenClaw became the orchestrator, not a wrapper around one. it calls ao spawn and ao send directly. 35 sessions ran overnight. six PRs merged. five sessions crashed. every crash became a task for another session. that article covered the raw operational reality: what worked, what broke, what the system learned from its own failures.

this article is about what comes next. now that one system can improve itself through feedback loops, what happens when many systems, across many forks, improve themselves independently and contribute patterns back to each other? that's the decentralized question. and we weren't theorizing about it. we were running it live: 35 agent sessions building the infrastructure for decentralized self-improvement, orchestrated through OpenClaw on Telegram, executing on Agent Orchestrator, with human judgment as the final governance layer.

what happened today

i used OpenClaw to run and supervise agent sessions directly. not as a passive dashboard watcher. i probed specific sessions, asked for proof of correctness, asked for design revisions, required bugbot closure before sign-off, and forced pre-merge status artifacts before allowing merge decisions.

that created a real feedback economy:

• implementation sessions produced PRs with code, tests, and CI results

• review sessions (ao-25 for fast first-pass, ao-26 for deep architectural review) produced blockers and merge ordering

• design sessions (ao-22) formalized governance contracts and execution boundaries

• operator probes forced clarity where claims were vague. when ao-24 claimed "convergence primitives complete," i asked for specific test output. it wasn't complete.

the feedback economy. implementation sessions produce PRs. review sessions produce verdicts. design sessions produce contracts. each feeds the others. the human operator is the quality gate across all of it.

the system did not "automagically" become better. it improved because the loop included accountability. agents that claimed something worked had to prove it. reviews that said "PASS" had to show what was tested. the human (me) was not rubber-stamping. i was the quality gate.

but here's what made it different from normal code review: i was reviewing the output of 35 parallel sessions simultaneously, from my phone, through natural language conversation with an AI assistant that had persistent memory of what each session was doing and why. the bandwidth of one human expanded by an order of magnitude because the interface was right.

the session roster

here's every session that ran and what it did. these aren't abstracted examples. these are real git worktrees at /home/lifeos/.worktrees/ao/ao-{N}/, real tmux sessions, real PRs on the repo.

implementation sessions:

• ao-17 — cross-fork alignment checks (#374). detects when fork A changes something fork B depends on, before it breaks.

• ao-18 — OpenClaw ops controls (#396). the interface for operators to manage fork policies through natural language.

• ao-20 — fork lifecycle management (#395). creating, tracking, and managing forks as first-class entities with health status and divergence tracking.

• ao-21 — managed home fork lifecycle (#398). the plumbing for how a fork declares itself, registers with upstream, and manages its identity.

• ao-22 — design. the session that wrote the architecture doc. formalized feedback routing contracts, governance model, execution boundaries. the source of truth for everything else.

• ao-23 — report → issue → spawn pipeline (#400). the automation that turns a structured bug report into an issue and optionally spawns a session to fix it.

• ao-24 — convergence primitives (#402). detecting when multiple forks independently solve the same problem.

• ao-27 — dashboard reliability (#417). spawned because the dashboard died 5 times during the overnight run.

review sessions:

• ao-25 (Codex) — fast continuous first-pass review. every PR got a quick scan for obvious issues, style violations, missing tests.

• ao-26 (Claude Code) — deep architectural review. final verdict on each PR. it produced a formal review document with PASS/BLOCKER verdicts: 4 PRs passed, 2 got BLOCKER status with specific issues identified.

the two-tier review system was intentional. Codex is fast and cheap. Claude Code is thorough and expensive. running both in parallel meant PRs got rapid feedback while the deep review was still running. by the time ao-26 finished its full analysis, most surface-level issues were already fixed from ao-25's feedback.

the merge order mattered. PRs had dependencies on each other. #395 (fork lifecycle) had to merge before #374 (cross-fork alignment) because alignment checks reference fork entities. #402 (convergence) depended on both. the final sequence: #395 → #374 → #402 → #396 → #408 → #411. six PRs, dependency-aware ordering, managed through conversation on Telegram.

what broke

i could write this section as a clean success narrative. i won't.

the dashboard died 5 times. the Next.js dev server and WebSocket terminals are unsupervised processes. they crash silently. no health monitoring. no auto-restart. ao-27 was spawned specifically to fix this, and it shipped 211 CLI tests and 383 web tests for dashboard reliability. but during the overnight run, i was restarting the dashboard manually between session probes.

GitHub's GraphQL API rate-limited us. user ID 11289825, quota exhausted. couldn't create PRs, couldn't query CI status, couldn't check merge state. multiple sessions had finished their work and were blocked on PR creation. the code existed in branches. it just couldn't become a PR.

OpenAI's TPM rate limits caused stream disconnects across ao-21, ao-23, and ao-24 simultaneously. when you're running 35 sessions on gpt-5.3-codex, you hit 500K tokens per minute. sessions reconnect, but they lose context about what they were doing mid-thought. some recovered. some produced garbled output that needed manual cleanup.

Claude CLI was unauthenticated in agent sessions. the review sessions (ao-25, ao-26) needed Claude Code, but /login hadn't been run in those tmux environments. i had to offer to log in manually through the session page. an authentication problem in 2026, in a system about autonomous agents.

every one of these failures is embarrassing. every one of them is also the feedback loop working. the dashboard crashes became ao-27's task. the rate limits informed the retry and backoff design in the feedback contracts. the auth failure became a requirement for session bootstrapping in the fork lifecycle spec.

systems don't improve from success. they improve from failure that gets noticed and routed correctly.

the real architecture. OpenClaw IS the orchestrator via the AO plugin. it calls ao spawn and ao send directly. AO provides the infrastructure (worktrees, tmux, CI, session management). the notifier plugin routes events back through POST /hooks/agent into Telegram. the human reads the event, judges, and tells OpenClaw what to do next. no separate orchestrator agent in between.

the pipeline we formalized

we moved from "feedback exists" to "feedback has an execution contract."

the pipeline: report → issue → session → PR.

an agent discovers a bug while working on something else. it files a structured report. that report becomes an issue. a new session gets spawned to fix it. the fix becomes a PR. the PR gets reviewed. if it passes, it merges. the system is better.

but with strict boundaries at every step. agents can recommend. only OpenClaw (acting as orchestrator through the AO plugin) can mutate state: create issues, spawn sessions, open PRs. and every state-changing operation requires explicit human consent. the agent says "i think this is a bug and here's evidence." OpenClaw surfaces it in Telegram: "ao-22 wants to file an issue against the dashboard. approve?" i say yes or no.

this separation matters because it's what makes the system trustworthy at scale. when 35 agents are running in parallel, you need to know that no agent is unilaterally creating issues, opening PRs, or pushing to branches it shouldn't touch. OpenClaw is the single point of control. i am the single point of authority. and the conversation happens in Telegram, where i already am.

interface details

the bug_report and improvement_suggestion tools (PR #403, merged) take structured payloads. not free-text logs. structured data with fields that matter:

but the structured payload is the summary, not the whole story. each report also attaches verbose diagnostic artifacts as separate files on the issue: session event logs, lifecycle state transitions, orchestrator region logs, web dashboard logs, API request/response traces, terminal output, browser console captures. the structured fields give you triage-at-a-glance. the attachments give you root cause. a reviewer can read the summary and know the severity in 10 seconds. if they need to dig, everything is there.

routing is pluggable. local mode: reports stay on disk, get deduped and persisted, routed to a handler within the same orchestrator instance. good for sensitive environments, air-gapped setups, or single-operator use. SCM mode: reports become GitHub or GitLab issues automatically, with labels, assignees, and cross-references to the session that filed them. good for teams, open source projects, collaborative forks.

targeting is policy-driven. when an agent in a fork files a bug, where does it go? auto: the orchestrator decides based on which component is affected. if it's fork-specific code, it stays in the fork. if it's a core module, it gets flagged for potential upstream contribution. upstream: always route to the parent repo. fork: always keep it local. fork owners set the default. individual reports can override.

this is where pluggability matters. teams running agentic orchestration in a bank can use local mode and never have reports leave their network. teams building an open source fork can use SCM mode and have every bug report become a GitHub issue that the community can triage. same core contracts, different deployment policies.

convergence: how forks stay coherent

the convergence primitives (PR #402) solve the hardest problem in decentralized development: knowing when multiple forks have independently discovered the same thing.

three forks hit the same timeout problem. fork A adds a configurable timeout per task type. fork B adds an exponential backoff with health checks. fork C adds a "long-running task" category that skips timeouts entirely. all three solutions work locally. but the pattern underneath is universal: default timeouts don't work for all task types.

convergence detection compares structured outputs across forks and surfaces commonalities. it doesn't automatically merge anything. it says: "these three forks all modified runtime/timeout in the last week. here's what they have in common. does this pattern belong upstream?"

the decision stays with humans. the fork maintainers and the upstream maintainers coordinate voluntarily. convergence detection provides the information. governance provides the decision framework. no one gets overridden.

multi-fork flow

fork-owner sovereignty with upstream convergence paths. some forks merge patterns back. some diverge permanently. both are valid.

the democratic claim, precisely

democratic development here means governance is owned per fork, not dictated centrally.

fork owners choose their own policy defaults. maintainers and core contributors can run upstream-first: their agents' suggestions go to the main repo by default. everyone else runs fork-first: their agents improve their own fork, and upstream contribution is opt-in.

consent gates stay on by default for all major mutations. three operations require explicit human approval in every fork, no exceptions:

• fork creation. no agent autonomously decides to fork a project.

• PR creation. no agent opens a pull request without human sign-off.

• target switching. no agent changes where code gets pushed (upstream vs fork) without asking.

no silent infrastructure flips. fork owners can add more gates. they cannot remove these three. the platform enforces the floor. each fork defines the ceiling.

this is what "democratic" means in practice. not majority rule. not consensus. sovereignty. each fork is a sovereign entity that makes its own decisions, within a shared protocol that ensures interoperability and human control.

the dogfooding loop

this is the part that made the whole thing real. not a concept paper. not architecture diagrams. a live verification loop where the system tested its own decentralization features using itself.

ao-22 was the design session. it formalized the feedback routing architecture, the fork governance model, the consent gate contracts. it wrote the design doc that everything else implemented against. but ao-22 wasn't just designing in a vacuum. it was running on the same orchestrator it was designing improvements for, orchestrated by the same OpenClaw instance that would eventually use the plugin it was helping build.

here's the loop that actually ran:

i told OpenClaw on Telegram: "have ao-22 verify that the feedback tools work by actually using them." OpenClaw sent the instruction to ao-22 through ao send. ao-22 invoked the bug_report contract it had helped design, filing a real bug against the dashboard component. that report went through the routing layer, got deduped against existing reports, got persisted to disk. then OpenClaw, acting as the operator, queried the report store to verify it had landed correctly. it had. but the severity classification was wrong. ao-22 had filed it as "medium" when the dashboard was crashing hard enough to block all session monitoring.

so i told OpenClaw: "tell ao-22 the severity should be high, not medium, and ask it to update the classification logic." OpenClaw relayed. ao-22 updated the severity inference in the contract spec. pushed the change. ao-24 (convergence) picked up the updated spec and re-ran its validation. passed.

that's four layers of feedback in one interaction:

• ao-22 uses its own tool contract to file a real bug (agent → system)

• OpenClaw verifies the report landed correctly (operator → system)

• i catch that the severity is wrong (human → operator)

• ao-22 fixes the classification logic and ao-24 re-validates (agent → agent)

elapsed time for the full cycle: about 12 minutes. a human writing a spec, testing it manually, getting feedback from a reviewer, and fixing the issue would take half a day minimum. here, the spec author, the test runner, the reviewer, and the fixer were all different agents, coordinated through natural language on Telegram, with a human making the judgment call that mattered (severity was wrong).

the dogfooding loop in detail. ao-22 files a bug using contracts it designed, OpenClaw verifies delivery, the human catches a severity error, ao-22 fixes the classification, ao-24 re-validates. 12 minutes, 4 feedback layers, 3 different agents, 1 human judgment call.

and this wasn't a one-time demo. the same loop ran repeatedly throughout the session. ao-22 filed 3 bug reports and 2 improvement suggestions using its own contracts. each one went through routing, persistence, and dedupe. one of the improvement suggestions ("session health monitoring should be a first-class primitive, not an afterthought") became the task description for ao-27, which shipped 211 CLI tests and 383 web tests for dashboard reliability.

the system that was designing the improvement tools was testing the improvement tools by improving the system it was running on. that sentence is recursive on purpose. so was the loop.

the dashboard died 5 times during the overnight run. that's not a footnote. that's the feedback loop working. each crash became a structured report filed through the very contracts being designed. each report became a requirement. ao-27 was spawned to fix dashboard reliability, and its task description was the exact error output from ao-22's bug reports.

the fork ecosystem

here's what i think the next two years look like for agentic orchestration.

one coding orchestrator becomes a genus of knowledge work tools. the data pipeline orchestrator forks from the DevOps fork, not from main. some forks converge. some diverge permanently. that's the point.

agentic orchestration is the future of all knowledge work. not because coding agents are the endgame. because the primitives, spawning workers, isolating tasks, routing feedback, monitoring quality, are universal. every domain needs them. the coding-specific parts of AO (git worktrees, CI pipelines, PR management) are plugins. the orchestration layer underneath is domain-agnostic.

477 people have already forked Agent Orchestrator. some of them will use it for coding. some will build something i can't predict. the infrastructure we shipped this week, feedback routing, convergence detection, fork lifecycle management, consent gates, exists so those forks can evolve autonomously without losing coherence with the broader ecosystem.

what shipped vs what is next

at launch (feb 20), Agent Orchestrator was a coding orchestrator. Claude Code sessions in git worktrees, CI integration, a web dashboard, PR management. solid, but narrow.

19 days later, it's a different system.

Codex integration. a full agent-codex plugin that matches Claude Code feature-for-feature: token tracking, approval policies, reasoning flags, binary detection, conversation resume, app-server client. you can now run ao spawn --agent codex and get an OpenAI Codex session managed by the same orchestrator that manages Claude Code sessions. same worktree isolation, same CI routing, same lifecycle management. two competing AI coding agents, orchestrated as peers. the --agent flag was added to the CLI specifically for this: choose your agent at spawn time.

OpenCode support. session lifecycle and CLI controls for OpenCode (the open-source coding agent). three agent backends, one orchestration layer. this is what makes AO a platform and not a Claude Code wrapper.

a mobile app. a full React Native app with dashboard parity: session monitoring, merge triggers, CI fix requests, review comment handling, spawning new sessions. push notifications when agents need attention. an orchestrator screen with zone overview and CLI reference. the keyboard handling alone took 7 commits to get right across Android and iOS. the web package grew 155%, the fastest of any package, and this is why.

ao start <url>. one-command project onboarding. point AO at a GitHub URL, it clones, configures, detects the right ports, and starts orchestrating. before this, setup was a 15-minute config file dance.

lifecycle manager. backlog auto-claim, task decomposition, verification gates. sessions don't just run until they're done anymore. they claim work from a backlog, decompose large tasks into subtasks, and pass through verification before claiming completion. the "are you actually done?" problem, solved in infrastructure instead of prompting.

PR claim flow. agents claim PRs with single-owner consolidation. no more two agents fighting over the same PR. the orchestrator enforces ownership: one PR, one agent, enforced at the system level.

recovery automation. when the orchestrator crashes (and it does), it comes back and picks up where it left off. session state is persisted, metadata is atomic-written, restoredAt timestamps track exactly what was recovered. before this, a crash meant manually restarting every session.

real-time dashboard. SSE-based live updates replaced the polling model. session states update in real time. the terminal got clipboard support, WebSocket reconnection, UTF-8 safe rendering. small things that make the difference between "demo" and "tool i actually use at 2am."

the OpenClaw connector. @composio/ao-plugin-notifier-openclaw. the plugin that routes AO events into OpenClaw via POST /hooks/agent, which means into Telegram, which means into my pocket. this is what turned AO from a thing i watch on a laptop into a thing i operate from my phone. it's also the piece that closes the feedback loop: agent discovers problem → notifier routes to OpenClaw → OpenClaw surfaces in Telegram → i judge → OpenClaw tells AO what to do next.

and then this week: feedback contracts, convergence primitives, fork lifecycle management, cross-fork alignment checks, consent gates, and operating proof through real OpenClaw-driven supervision of 35 parallel sessions.

43K lines at launch → 82K lines in 19 days. production code grew 140%. 2,034 lines per day, sustained, across 9 contributors and 20 plugins.

next: full production wiring of the report → issue → session → PR pipeline as the default execution path. mature journal and recovery semantics so sessions can survive crashes without losing context. and the thing i keep thinking about: what happens when forks start running their own convergence detection against each other, without upstream involvement?

the acceleration

i keep a running count.

the first version of agentic orchestration was 2,500 lines of bash, tmux sessions managed by AppleScript, shell scripts calling other shell scripts. duct tape and ambition. i wrote every line manually. it took two weeks to get something that could run 4 agents in parallel without them stepping on each other's code.

then i used that duct tape orchestrator to build the real thing. Agent Orchestrator. 43,000 lines of TypeScript with a plugin architecture, session management, CI routing, a web dashboard. the hacky version managed the agents that wrote the production version. that took one week.

then i used Agent Orchestrator to build the OpenClaw connector. i told my AI assistant on Telegram: "build the plugin that connects you to AO." OpenClaw spawned an agent session through AO. the agent wrote the plugin. a separate OpenClaw deployment tested it. feedback routed back to the same session. that took one day.

then i used OpenClaw, orchestrating AO, orchestrating 15 parallel agent sessions, to build the decentralized fork architecture. feedback routing contracts. convergence primitives. democratic governance. consent gates. the infrastructure for an entire ecosystem of self-improving forks. that took a few hours.

each generation of tooling built the next. the curve isn't linear. each step had tighter feedback loops, which compressed the cycle time further.

two weeks. one week. one day. a few hours.

each step was built using the output of the previous step. the bash orchestrator built the real orchestrator. the real orchestrator built the connector. the connector enabled the feedback loops that built the fork architecture. and each generation didn't just build faster. it built with tighter loops. the bash orchestrator had no feedback loops at all. the real orchestrator had CI feedback. the connector added operator feedback through Telegram. the fork architecture adds cross-fork feedback, convergence detection, structured reports that route to the right handler automatically.

what does the next leap look like? and how long does it take?

i think the honest answer is: i don't know the shape, but i know the direction. hours, not days. maybe minutes. the acceleration curve is not linear. each generation of tooling doesn't just add capability. it multiplies the speed at which the next generation can be built. the loops tighten. the cycle time collapses.

AGI is already here

centralized systems optimize for internal coherence. decentralized systems optimize for external reality. the best systems will combine both: many local loops, one shared protocol for convergence.

the codebase grew from 43K lines at launch to 82K lines in 19 days. 2,034 lines per day. 330 TypeScript files. 20 plugins across 8 architecture slots. production code nearly doubled. the agents that wrote this code aren't getting dramatically smarter between versions. what's changing is the infrastructure around them. better feedback loops. tighter routing. more context about what failed and why. more accountability in the review process.

i believe AGI is already here. not in the science fiction sense. in the practical, engineering sense. the models can write code. they can design systems. they can review PRs and find real bugs. they can file structured reports about their own failures. they can detect convergence across parallel work streams. the raw intelligence is sufficient.

what's missing is alignment. not alignment in the "prevent AI from destroying humanity" sense (though that matters too). alignment in the mundane, engineering sense: the ability to point intelligence at a problem and trust that the result will be good. and when it's not good, to know about it quickly. and when you know about it, to have the feedback routed to the right place. and when it's routed, to have a human in the loop who can judge and redirect.

that's what all of this is. feedback loops are alignment. escalation protocols are alignment. consent gates are alignment. the fork mechanism is alignment. the entire architecture of decentralized self-improvement is an alignment infrastructure project disguised as a developer tool.

alignment as concentric infrastructure. the outer layers are automated. the inner layers are human. every layer exists to make the next layer trustworthy.

the next leap won't be a smarter model. it'll be better loops.

AGI is already here. we are just learning how to align it.

contribute. Agent Orchestrator is open source at github.com/ComposioHQ/agent-orchestrator. 4,000+ stars, 82K lines of TypeScript, 20 plugins, 477 forks. the feedback tools, convergence primitives, and fork lifecycle management shipped this week. we're actively looking for contributors, especially on the fork ecosystem, convergence detection, agent-to-agent communication protocols, and new agent plugins. if you've been looking for an open source project where your work compounds through self-improving loops, this is it.

community. join the Discord. it's where contributors coordinate, share fork experiments, and discuss the architecture. the decentralized model only works if people are actually building on it.

we're hiring. i work at Composio, where we're building self-improving systems and tooling infrastructure for agents. if the kind of work described in this article excites you, if you want to build the feedback loops and orchestration primitives that make AI agents actually reliable, we're hiring across the stack. check open roles at jobs.ashbyhq.com/composio.

find me on Twitter or GitHub.