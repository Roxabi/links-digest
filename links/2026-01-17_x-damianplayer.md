---
title: "how to automate your life with claude code (for non-technical people).."
source: "https://x.com/damianplayer/status/2012611857392009242"
date: 2026-01-17
tags: ["claude code", "task automation", "ai workflow", "non-technical users"]
platform: x
author: "@damianplayer"
summary: "A step-by-step guide teaches non-technical users how to automate repetitive tasks using Claude Code through a four-step workflow."
---
the people learning this now will have a massive head start. six months from now, everyone will know how to do this. here's how to start before it's obvious.

most people open claude code and stare at a blank terminal for 20 minutes.

they see everyone on twitter shipping apps, automations, full products. then they close it because they have no idea what to build.

the problem isn't claude code. the problem is they skipped the most important step.

why most people fail

claude code looks intimidating. terminal. blinking cursor. feels like you need to be a developer.

you don't.

claude code is just a chat window with an AI that can actually do things. read files. write code. search the web. build entire systems.

the people failing aren't failing because they lack technical skills. they're failing because they don't know what to ask for.

they open claude code thinking "i should build an app" instead of thinking "what's annoying me right now that i could fix?"

that's the shift.

the 4-step workflow

i've watched dozens of people go from "i don't know what to build" to shipping automations that save them hours every week.

they all follow the same process.

step 1: inventory your week

before you touch claude code, grab a piece of paper.

write down everything you did last week that felt repetitive. tedious. annoying.

researching competitors

formatting reports

pulling data from one place to another

writing the same emails over and over

organizing files

these aren't sexy app ideas. they won't get likes on twitter.

but they're real problems you actually have. that's the point.

your first automation shouldn't be a side project. it should be the boring stuff that eats 2-3 hours of your week.

that's where you start.

step 2: explore solutions with claude

now open claude code.

don't tell it to build anything yet. tell it what you're trying to solve.

"i spend 2 hours every week researching competitor youtube channels. i look at their top videos, what's working, what topics are trending. is there a way to automate this?"

then ask for options.

"give me 3 different ways to do this with pros and cons for each."

claude will give you paths you didn't know existed. official APIs. free tools. scraping methods. third party services.

here's the key: push for simpler.

if claude suggests something that requires API keys and billing setup, ask "is there a free version that doesn't require all that?"

there usually is.

don't accept the first answer. explore. ask follow-ups. treat it like a conversation with someone who knows more than you.

because that's exactly what it is.

step 3: plan before you build

this is where most people mess up.

they get excited. claude gives them an option that sounds good. they say "ok build it" and let claude run.

bad idea.

AI makes assumptions. lots of them. when you skip the planning step, those assumptions become bugs you fix later.

here's what to do instead:

press shift+tab until you see "plan mode" at the bottom

tell claude: "write me a spec for this. what it should do, what the inputs are, what the output looks like. don't write any code yet."

review the spec

cut everything you don't need for version one

AI always tries to do too much. you'll see features you didn't ask for. complexity you don't need.

the spec is your contract with claude. once you approve it, then you let it build.

this step takes 10 minutes. saves hours of debugging later.

step 4: build and iterate

now you're ready.

tell claude to implement the spec. watch it work.

it will create files. write code. set up systems. you don't need to understand any of it.

when errors pop up (they will), copy the error and paste it back. say "fix this."

this is the loop: build, error, fix, repeat.

don't expect perfection on the first run. expect a working draft you can improve.

the whole process might take an hour for your first automation. the second one takes 30 minutes. by the fifth, you're moving fast.

real example: the youtube researcher

let me show you what this looks like in practice.

i wanted to automate competitor research for youtube. manually, this took 2 hours per week. checking channels, noting top videos, spotting trends.

step 1: i told claude the problem.

"i want to build a command where i type /youtube and a channel name, and it outputs a research file with top videos, view counts, and insights about what's working."

step 2: claude gave me 3 options. official youtube API (complicated setup), web scraping (fragile), or a free tool called yt-dlp.

i asked: "what about yt-dlp? i heard that's simpler."

claude confirmed. no API keys. no billing. just works.

step 3: i switched to plan mode and asked for a spec.

claude produced a document:

input: channel name

output: markdown file with top 10 videos by views

includes: title, view count, duration, key insights

i cut the "thumbnail analysis" feature it added. didn't need it.

step 4: i told claude to build it.

10 minutes later, i had a working command. type /youtube [channel name], get a full research report.

what used to take 2 hours now takes 30 seconds.

stacking commands (where it gets powerful)

once you've built one automation, you can chain them together.

the youtube researcher gives me data. now i build another command that takes that research and suggests video ideas based on my niche.

research → ideation → outline → script draft.

each piece is simple. together they're powerful.

i've seen people chain commands so well they let claude code run for 10+ hours autonomously. building entire projects while they sleep.

that's the endgame. but it starts with one simple automation.

the 70/80 rule

here's what nobody tells you about vibe coding:

70-80% of it is writing documents. not code.

plans. specs. requirements. descriptions of what you want in plain english.

the AI writes the code. your job is explaining what you want clearly enough that it doesn't make bad assumptions.

this is why non-technical people can be great at this.

you're not competing on coding skills. you're competing on communication skills. clarity. specificity.

if you can write a clear email, you can vibe code.

the real skill

let me be direct about what's happening here.

you're not learning to code. you're learning to manage an AI that codes for you.

that's a different skill. and right now, almost nobody has it.

the people winning with claude code aren't developers. they're people who know what problems need solving and can communicate those problems clearly.

technical skills are getting commoditized by the day. AI writes better code than most junior developers already.

but knowing which problems to solve? knowing how to break a big goal into small steps? knowing how to review output and catch what's wrong?

that's human work. and it's not going anywhere.

the window

six months from now, everyone will know how to do this.

claude code will have a nicer interface. there will be courses and certifications. it will feel normal.

right now it still feels hard. intimidating. like you need permission to try.

you don't.

the people building this skill today will have a massive head start. not because the skill is hard, but because they started before it was obvious.

start here

if you've never used claude code:

go to anthropic's website and install it (one terminal command)

open it by typing "claude" in your terminal

describe one repetitive task from your week

ask for 3 ways to automate it

pick the simplest one

switch to plan mode, ask for a spec

review and simplify

let it build

iterate until it works

no courses. no prerequisites. no coding bootcamp.

just you, a problem worth solving, and an AI that can build the solution.

the tools are free. the opportunity is now.

stop staring at the blank terminal. start talking to it.

want 200+ ready-to-use prompts?

found a site nobody talks about with copy-paste claude code prompts for:

react components

python scripts

typescript projects

automation workflows

data processing

API integrations

no thinking required. just paste and let claude build.

RT + comment "PROMPTS" and i'll send the link (must be following so i can DM)