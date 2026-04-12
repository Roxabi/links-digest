---
title: "How I Built a Visual Feedback Loop for Claude Code"
source: "https://x.com/seejayhess/status/2014448070214197485"
date: 2026-01-22
tags: ["visual feedback loop", "Claude Code integration", "JSON-based diagrams", "UI mockup tool", "flowchart editor"]
platform: x
author: "@seejayhess"
summary: "The author built Flowy, a tool enabling Claude Code to create interactive flowcharts and UI mockups using JSON files instead of ASCII diagrams for better visual planning."
---
ASCII Art Isn't Cutting It Anymore

I love Claude Code. It's become essential to how I work. But I kept hitting the same wall: trying to describe exactly what I wanted in a flowchart or UI mockup using nothing but text.

These ASCII diagrams are fine for simple things, but the back-and-forth to get them right was exhausting. I'd describe what I wanted, Claude would draw it in ASCII, I'd squint at it trying to figure out if that's actually what I meant, then spend three more messages trying to adjust the layout.

The real problem was that it was difficult to be specific about visual things through prompts

A JSON-Based Diagram Format Claude Can Write To

So I built Flowy.

The concept is simple, Claude writes JSON to a .flowy directory in your repo, and a dev server watches those files and renders them as interactive flowcharts and UI mockups in your browser. Figma-like editing.

The source of truth lives in your codebase as JSON. You can version it with git. Claude can read it, write it, and respond to your visual edits.

Visual Planning Before Code

The real power comes from iterating visually before writing a single line of implementation code.

Here's my workflow now:

Start with a plan - I write a plan document with requirements and architecture

Claude generates diagrams - I ask Claude to create flowcharts and mockups in Flowy

I edit visually - I drag nodes around, adjust layouts, tweak the design

Claude notices changes - The JSON file updates, Claude can read my modifications

We refine together - Back and forth until the visual matches what I actually want

Then we build - Implementation follows the visual spec exactly

Live Demo - Building a Quiz Feature

In my Vibe Code Camp demo, I walked through building a quiz feature for a Claude Code learning app. Here's what that looked like:

Step 1: The Plan

I had a plan document that described a 5-question quiz testing users' knowledge of Claude Code commands and shortcuts.

The plan outlined what needed to be built, but before touching any React code, Phase 1 was "Create flow diagrams and UI mockups."

Step 2: Generate the Diagrams

I asked Claude to create three Flowy visualizations:

Navigation Flow - How users get to and from the quiz

Gameplay Flow - The internal game logic and state machine

Screen Mockups - High-fidelity iPhone mockups of all four screens

The navigation flow shows the entry points (Learn Tab), the quiz screens (Intro → Questions → Results), persistence to AsyncStorage, and exit paths (Back, Done, Play Again).

The gameplay flow visualizes the actual game logic: initialization, the question loop with correct/wrong branching, score tracking, and the best-score check before saving.

Step 3: The UI Mockups

This is where Flowy really shines. Claude generated JSON that renders as actual iPhone mockups:

Four screens, laid out side-by-side:

Quiz Intro - Brain icon, "Test Your Knowledge" title, best score card, Start button

Question Screen - Progress bar, question card, four answer options (one selected)

Answer Feedback - Wrong answer highlighted red with X, correct answer green with checkmark

Results Screen - "Great Job!" title, 4/5 score, "New Best Score!" badge

Step 4: Edit and Iterate

Here's where the magic happens. In the demo, I:

Opened the mockup in Flowy

Dragged a node to reposition it

Changed some text

Saved

Claude immediately saw those changes in the JSON file. I could then ask Claude to update the plan based on my visual modifications, and it understood exactly what I'd changed.

Step 5: Build From the Visual Spec

With the visual planning done, implementation became almost mechanical. Claude had:

Exact screen layouts to follow

The state machine clearly visualized

Component hierarchy evident from the mockup structure

We built the entire quiz feature in one session, and it matched the mockups exactly.

Rough JSON Format

Flowy uses json to layout the files. The skills include everything Claude needs and I rarely look at these files.

Here's a simplified example of what Claude writes:

The schema supports:

Node types: rect, circle, diamond

Edge types: arrow, dashed, line, orthogonal, curved

Icons: Integrated with Lucide icons

Styling: Fill, stroke, corner radius, shadows, fonts

Skills That I Use With Flowy

Flowy is designed to work with Claude Code skills. Here are the ones I use constantly:

Explicitly tells Claude to create flowcharts in Flowy format. Great for:

Process flows

State machines

Architecture diagrams

Decision trees

Creates iPhone mockups in Flowy. Perfect for:

Screen designs before building

Iterating on UI layout visually

Communicating design intent

The mockup format includes:

Device frames (notch, home bar, status bar)

iOS-style components (buttons, cards, progress bars)

Proper safe area handling

The New Paradigm

Flowy represent a new medium that you can work back and forth with Claude Code. I have found it immensely useful for UI changes or complex workflows.

We're building toward releasing Flowy, if you are interested leave a comment saying "Flowy" and we'll make sure to get it into your hands as fast as possible.