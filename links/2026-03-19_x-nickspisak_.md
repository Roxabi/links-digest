---
title: "Installed Paperclip, Now What !?"
source: "https://x.com/nickspisak_/status/2034635430700679445?s=46"
date: 2026-03-19
tags: ["AI Agents", "Paperclip", "gstack", "Automation", "Open Source"]
platform: x
author: "@NickSpisak_"
summary: "This article guides users on setting up an autonomous AI company using three integrated tools: Paperclip for management, gstack for engineering, and autoresearch for R\u0026D."
---
My Paperclip article hit 2.7 million views. 

The comment section was mostly made up of "cool demo", "it doesn't work", and "how do you handle" questions... This follow up article is to get some ideas going in your head by using some really powerful skills. EVERYTHING is skills now...

If you still aren't sure what Paperclip is and why the concept is so interesting than give the original article a review here 👇

Today we're going to stack skills... You'll need: Paperclip (the company), gstack (the engineering team), and autoresearch (the R&D lab). All free. All open source. Set up in under 10 minutes total.

Real quick  ...

If you're non-technical and want to learn how to build systems like this, join our Build With AI community:http://return-my-time.kit.com/1bd2720397

Alright lets get going... Reminder, you're only limited by your own imagination.... This is just one (of many) examples...

The Three Tools (And What Each One Does)

Before we set anything up, here's the big picture.

Paperclip is your company. It's the dashboard where you define your mission, hire AI agents, set budgets, and track what everyone's doing. Think of it as the office building.

gstack is your engineering team. Built by Garry Tan (CEO of Y Combinator), it gives your agents 15 specialist roles - CEO, CTO, designer, QA engineer, release manager. Each one knows exactly what to do. Think of it as the employees.

autoresearch is your R&D lab. Built by Andrej Karpathy (former Tesla AI lead), it lets your agents run experiments autonomously overnight. Give it a research question, go to sleep, wake up to 100 experiments completed. Think of it as the lab.

Together: Paperclip runs the company. gstack builds the product. autoresearch does the research. One person. Zero employees.

Step 1: Install Paperclip (2 Minutes)

Open your terminal and run:

This installs everything, creates a database, and opens your dashboard at http://localhost:3100.

Once the dashboard loads:

Create your company and set the mission (example: "Build an AI-powered note-taking app to $1M ARR") .. (make something better than that)

Hire your first agent - it starts with a CEO

The CEO will suggest hiring more team members

Approve the hires and set monthly budgets for each agent

Your company is live

That's it. You now have an AI company with an org chart, budgets, and a ticket system.

Step 2: Install gstack - Your Engineering Team (2 Minutes)

This gives your agents the ability to actually build things. Run:

git clone https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
cd ~/.claude/skills/gstack
./setup

Now your agents have 15 specialist skills. Here are the ones that matter most:

Planning your product:

→ /office-hours - Takes your rough idea and turns it into a real plan by asking smart questions and proposing three approaches

→ /plan-ceo-review - Challenges your scope like a CEO would. Finds the 10-star product hiding inside your feature list

→ /plan-eng-review - Locks down the architecture with diagrams, edge cases, and failure modes

Building it:

→ /review - Code review that catches bugs your tests miss. Auto-fixes the obvious ones.

→ /qa - Opens a real browser, clicks through your app, finds bugs, fixes them, and writes tests so they don't come back

Shipping it:

→ /ship - Syncs your code, runs tests, checks coverage, pushes to GitHub, and opens a pull request. One command.

→ /document-release - Updates all your docs (README, architecture, contributing guide) to match what you actually shipped

Staying safe:

→ /careful - Warns you before anything destructive (deleting files, dropping databases, force-pushing code)

→ /freeze - Locks all files except the one folder you're working in. Prevents accidental changes during debugging.

The power move: run 10-15 of these simultaneously. One agent does /office-hours on a new feature while another does /qa on staging while another does /ship on a finished PR. All at the same time.

Step 3: Install autoresearch - Your R&D Lab (2 Minutes)

This one is for when your AI company needs to experiment and learn. Run:

Fire up claude code and ask it to make a skill called "autoresearch" based on https://github.com/karpathy/autoresearch.git. The skill builder will make you a version of Karpathy's ML training experiments.

Autoresearch was built for ML training experiments, but the pattern works for any iterative research your AI company needs - testing prompts, optimizing workflows, benchmarking approaches.

Here's how it works:

→ You give it a research question or experiment goal

→ It modifies code, runs a 5-minute training experiment, checks the results

→ If the results improved, it keeps the change. If not, it throws it away.

→ Then it does it again. And again. Automatically.

→ 12 experiments per hour. ~100 experiments overnight.

You go to sleep. You wake up to  completed experiments with clear results showing what worked and what didn't.

How the Three Tools Work Together

Here's where it gets powerful. Each tool handles a different layer of your AI company:

→ Paperclip assigns the work - "Agent 3, research the best approach for our recommendation engine" → autoresearch does the research - runs 100 experiments overnight, finds the best approach → gstack builds it - /office-hours plans the feature, /review checks the code, /qa tests it, /ship deploys it → Paperclip tracks the results - budget spent, tasks completed, decisions logged

The workflow looks like this:

You set a goal in Paperclip ("Build a recommendation engine")

Paperclip creates tickets and assigns them to your agents

Your research agent uses autoresearch to test approaches overnight

Your engineering agents use gstack to build the winning approach

gstack's /qa tests it in a real browser

gstack's /ship deploys it

Paperclip logs everything - cost, time, decisions, results

You check the dashboard from your phone. Review what shipped. Approve the next sprint. That's your job as the board of directors.

5 Prompts to Get Started Right Now

Once everything is installed, try these:

Prompt 1 - Plan your product:"Use /office-hours to reframe this idea: [your product idea]. I want three implementation approaches with effort estimates."

Prompt 2 - Get a CEO review:"Use /plan-ceo-review to challenge the scope of this plan. Find the simplest version that delivers 80% of the value."

Prompt 3 - Build and ship:"Use /review to check this code for bugs, then /qa to test the user flows in a real browser, then /ship to deploy."

Prompt 4 - Run overnight research:"Examine program.md and launch a new experiment. Run autonomously until you've completed 50 iterations. Log all results."

Prompt 5 - Full sprint:"This is our sprint goal: [goal]. Plan it with /office-hours, lock the architecture with /plan-eng-review, build it, test it with /qa, and ship it with /ship. I'll review the PR when you're done."

Power Tips

Tip 1: Set Paperclip heartbeats to match your work schedule. If you review work every morning at 9am, set your agents to complete tasks by 8am.

Tip 2: Use gstack's /careful mode anytime agents are working on production code. It blocks destructive commands unless you explicitly approve them.

Tip 3: Run autoresearch experiments overnight. 5 minutes per experiment x 12 per hour x 8 hours = 96 experiments while you sleep.

Tip 4: Use Paperclip's multi-company feature to separate projects. Your SaaS product and your consulting business should be different companies with different budgets.

Tip 5: Start with one agent and one goal. Don't hire 10 agents on day one. Hire a CEO, let it suggest the first hire, and grow the org based on what the company actually needs.

Three free tools. One AI company. Zero employees.

Paperclip runs the company. gstack builds the product. autoresearch does the R&D. You sit on the board and make the decisions.

The repos are live. Everything is open source. And the whole setup takes less than 10 minutes.

You're only limited by your own imagination now. 

PS: If you like this starter pack, you'll love what's coming.

I'm building a community where I break down exactly how to turn custom agents into a real employee: custom skills, scheduled workflows, and systems that run while you sleep.

Join the waitlist here:https://return-my-time.kit.com/1bd2720397