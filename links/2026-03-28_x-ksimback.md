---
title: "Two Powerful Claude Code Plugins: gstack vs CE"
source: "https://x.com/ksimback/status/2037168696259403929?s=12"
date: 2026-03-28
tags: ["Claude Code", "AI Plugins", "gstack", "Compound Engineering", "Developer Tools"]
platform: x
author: "@KSimback"
summary: "This article compares two powerful Claude Code plugins, Garry Tan\u0027s gstack for virtual team simulation and Every.to\u0027s Compound Engineering for systematic workflow methodology, guiding developers on"
---
TLDR; a new Claude Code plugin drops every day, I ignore most of them but occasionally one catches my attention, and of those, a few of them genuinely change how I do things. This article highlights two that I think should be part of everyone's setup.

The two plugins are: gstack by @garrytan and Compound Engineering by Every.to. Both turn Claude Code into a more structured environment for any project and both are free and open source.

Here's what they are, how they differ, and how to think about which one to use.

gstack: Garry Tan's Actual Setup

Garry Tan is President and CEO of Y Combinator. He was an early engineer at Palantir, cofounded Posterous (sold to Twitter), and built Bookface, YC's internal social network. In the last 60 days he shipped 600,000+ lines of production code while running YC full-time.

He published his entire Claude Code setup and called it gstack and it got 40k+ stars in 12 days - pretty impressive.

gstack gives you the same virtual team Garry uses for his own work: a CEO who stress-tests product decisions, an engineering manager who owns architecture, a designer who catches AI slop, a QA lead who opens a real browser on your staging URL, a security officer who runs audits, and a release engineer who ships the PR. It's basically an all-in-one team that covers every function from business idea to production code.

Core commands:

/office-hours - describe what you're building, get structured feedback before writing a line of code

/plan-ceo-review - business and product lens on any feature idea (will kill bad ideas fast)

/plan-eng-review - locks architecture and implementation approach before you build

/review - comprehensive code review: bugs, security, performance, style

/qa - opens a real browser via Playwright, runs diff-aware QA on your staging URL

/retro - weekly stats: lines added, commits, net LOC, a running track record of output

There's more, but this gives you a good sense for what it can do.

The philosophical core lives in ETHOS.md which Garry calls "Boil the Lake." The premise is that with AI, the marginal cost of completeness is near-zero and only takes minutes, so you always do the complete thing vs. typical startup land where you're always making tradeoffs or skipping extra steps due to time/effort.

Who it's for: I would recommend this to early-stage startup founders, especially solo builders, who want the closest thing to having a complete team wrapped around what you do. So if you're a one or two-person team trying to move like a company of twenty, this is going to be very helpful.

Compound Engineering: Every.to's Engineering Operating System

Every.to is an AI startup and media company that builds products with single-person teams. Compound Engineering is what they use to do it.

Where gstack is more of a "copy my setup" approach, Compound Engineering is an "adopt a methodology" approach. It's a full engineering operating system built on a four-step loop: Plan → Work → Review → Compound.

The GitHub has 10k+ stars, smaller than gstack's current number but its been around a bit longer and seems more battle-tested.

The CE plugin ships with 26 specialized agents, 23 workflow commands, and 13 skills - that's a lot of firepower!

The core loop:

/ce:plan - structured implementation planning before touching code

/ce:work - systematic execution against the plan, one step at a time

/ce:review - 14 specialized code reviewers running in parallel including security, performance, over-engineering, style, and more

/ce:compound - this is the differentiator

The compound step is the unique idea. After every task, it captures what was solved, what patterns emerged, and what was learned. Over time it builds a library of experiences specific to your codebase and your way of working. The idea is that each unit of work gets slightly cheaper than the last, compounding productivity the same way compounding interest compounds money.

Who it's for: If gstack is more for small founder teams and solo builders, I'd recommend CE for more established engineering teams who want systematic review and QA on every PR. It can obviously be helpful to solo builders as well, but the premise of the "compound" part is that it pays off over time so it's probably not for hobbyists who are doing experiments rather than running production apps. At least that's what I found.

How They Compare

From working with both on a few hobby projects, I'd say gstack optimizes for speed and shipping while Compound Engineering optimizes for quality and compounding over time.

gstack gets you from idea to deployed project/feature faster, but Compound Engineering makes sure every feature is better than the last.

I wouldn't say one is better than the other, they're actually solving different parts of the same problem.

The Power User Stack: Use Both

gstack and Compound Engineering are not mutually exclusive so you could use both.

You can use gstack for the fast loop of planning, building, shipping, QA. Then use Compound Engineering's review and compound steps to catch what gstack missed and capture the learnings.

Here's one way it can work in practice that I played around with:

/office-hours (gstack) - validate the idea before committing

/plan-ceo-review + /plan-eng-review (gstack) - lock product and architecture

/ce:work (Compound) - systematic execution with structured tracking

/review (gstack) or /ce:review (Compound) - pick based on depth needed; Compound's 14-agent review is more comprehensive for complex PRs

/qa (gstack) - real browser, staging URL, diff-aware

/ce:compound (Compound) - capture what was solved for future compounding

/ship (gstack) - deploy

You end up with the speed of gstack's opinionated defaults and the compounding quality curve of Compound Engineering's methodology. Together they make a pretty damn good complete system.

Both plugins are free, MIT, and open source:

gstack: github.com/garrytan/gstack

Compound Engineering: github.com/EveryInc/compound-engineering-plugin