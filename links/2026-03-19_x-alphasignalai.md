---
title: "Getting started with Paperclip AI: Build Zero Human Companies"
source: "https://x.com/alphasignalai/status/2034647427609751913?s=46"
date: 2026-03-19
tags: ["AI Agents", "Paperclip AI", "Autonomous Business", "Node.js", "Open Source"]
platform: x
author: "@AlphaSignalAI"
summary: "This article provides a guide on setting up Paperclip AI, an open-source platform that orchestrates AI agents to run a business autonomously under human supervision."
---
Paperclip AI dropped a couple of days ago and has already gotten over 30K GitHub stars.

It is a Node.js server and React UI that orchestrates a team of AI agents to run a business. You bring your own agents, assign goals, and track their work and costs from one dashboard.

You operate as the board of directors. The agents do the work.

This guide walks through setting up Paperclip from scratch, creating your first AI employees, assigning company goals, and configuring per-agent budgets.

Here is everything you need to know to do the same.

How it Works

You define a company goal, hire AI agents into roles, and let them work through a ticket system while you supervise from the dashboard.

Every task in Paperclip traces back to the company mission through a goal hierarchy. Agents do not just execute isolated commands. They carry full goal ancestry, so they always know what they are working on and why.

Agents operate on a heartbeat schedule.

They wake up, check for assigned work, execute tasks, and report back. Delegation flows up and down the org chart, just like in a real company. If a CEO agent needs engineering work done, they delegate it to the engineering agent through Paperclip's ticket system.

You approve or reject hires. You review the strategy before it is executed. You can pause or terminate any agent at any time. Config changes are versioned, and bad changes can be rolled back.

How to set up Paperclip AI

Getting started requires Node.js 20+ and pnpm 9.15+. Clone the repo and install dependencies:

You can use the GitHub desktop app or run this git command in your CLI:

Open the project in your IDE and open a terminal. Go to the root folder and run the command below to install all libraries and dependencies.

Make sure there are no errors in the terminal. Next, build the project by executing "pnpm run build" in the same terminal window.

Again, you should see the status as "Done," and there are no errors in the build. Now, run the project by executing "pnpm run dev".

This is what you should see on your terminal:

Cool. The API server is now running.

Creating AI workers in Paperclip AI

You can bring up the Web UI dashboard by using either http://127.0.0.1:3100/ or http://localhost:3100 in your browser. This is what the welcome screen looks like:

Follow the on-screen instructions to set up your virtual company.

In the Agent tab, create a new agent named CEO and fill out the form. For the path name, follow the instructions below:

Open Finder and navigate to the folder.

Right-click (or Control-click) the folder.

Hold the Option (⌥) key — "Copy" changes to "Copy as Pathname".

Click "Copy as Pathname"

Next, create a task. Be as descriptive as you can in both the title and the description. Here's an example for the CEO Agent.

Finally, click the "Create and open issue" button from the Launch tab.

If everything works correctly, the agent will be launched, and you will be redirected to the main dashboard.

An embedded PostgreSQL database is created automatically — no setup required.

Managing Goals and Tracking the Org

What happens next is the fun part. The CEO agent will start hiring. It might propose a Founding Engineer with a specific set of capabilities. You get an approval prompt where you can accept or reject the hire.

This is the governance layer in action. No agent joins the company without your sign-off.

From here, I can either approve him or reject him if I don't need those skills. All the virtual employees can be tracked and viewed in the Org tab.

This is a neat visualization of the organizational hierarchy.

From the Goals tab, you can set the specific tasks and goals that you want to delegate to the AI agents. Just click on the "New goal" button and describe the task.

Here's an example:

Launch AlphaSignal v0.1: Bootstrap the company, hire core team, define product, and ship the first working version of AlphaSignal.

You can break goals into sub-goals for more granular tracking. Each sub-goal can be assigned to a specific agent or team, and progress flows back up the hierarchy.

Budget Control and Cost Tracking

The Costs tab is critical. This is where you set monthly inference budgets per agent and monitor spending in real time.

Every agent gets a budget ceiling. At 80% utilization, you get a warning. At 100%, the agent auto-pauses, and new tasks are blocked until you either increase the limit or wait for the next billing cycle. You can override at any time.

This solves one of the most common problems with multi-agent setups. Without budget controls, a single runaway loop can burn hundreds of dollars in API credits before you notice. Paperclip treats budget as a first-class organizational constraint.

How Paperclip Compares to Agent Frameworks

Paperclip is not competing with CrewAI, AutoGen or LangGraph. Those are frameworks for building multi-agent workflows. Paperclip sits a layer above.

CrewAI helps you define a crew of agents with roles and tasks. LangGraph gives you graph-based workflow control. AutoGen provides a conversational agent architecture. All of them focus on how agents collaborate on a single workflow.

Paperclip focuses on running the company that those agents work for. It provides the org chart, the budget, the ticket system, the audit trail, and the governance layer. You could use CrewAI agents inside Paperclip. They solve different problems.

The closest comparison is the difference between a CI/CD pipeline and a project management tool. One executes tasks. The other manages the organization around those tasks.

Whether "zero-human companies" become mainstream is an open question.

But the underlying tooling, org charts for agents, budget enforcement, persistent state, and audit trails, is useful right now for anyone coordinating more than a handful of AI workers.

What do you think? Drop your thoughts in the comments.

References:

Repo: https://github.com/paperclipai/paperclip

Website: https://paperclip.ing

Follow @AlphaSignalAI for more content like this.