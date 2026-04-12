---
title: "Million Dollar Product : 12 Rules to Building Something Users Love"
source: "https://x.com/hartdrawss/status/2027270166422372763?s=46"
date: 2026-02-27
tags: ["product development", "user experience", "MVP building", "startup strategy", "product design"]
platform: x
author: "@Hartdrawss"
summary: "The article outlines 12 rules for building successful products, emphasizing user personas, UX principles, brand foundation, and information architecture over technical infrastructure choices."
---
I've built 50+ MVPs for founders in the last year and the pattern I keep seeing is always the same.

Founders obsess over the stack. They debate Next.js vs Remix, Supabase vs Firebase, Claude vs GPT. They spend weeks on infrastructure decisions and then ship a product that users open once and never return to.

The world is flooded with vibe coded look-alikes. Buggy tools, poor user experience, zero retention.

The problem is never the stack. The problem is that nobody stopped to think about the product.

Here is everything that actually goes into building something users love.

1. Nail Your User Persona Before You Write a Single Line of Code

Most founders define their audience as "founders" or "SMBs" or "enterprises" and move on. That is not a persona. That is a category.

A real user persona goes much deeper. It maps the exact daily workflow of the person using your product. It identifies their specific frustration and the workaround they are currently using to solve it. It accounts for their technical literacy, which directly determines how complex or simple your interactions need to be.

The test is simple. If you cannot describe your target user in two sentences, you are not ready to build yet. Every design decision, every UX pattern, every onboarding step flows from who that person actually is. Get this wrong and everything downstream is built on a broken foundation.

2. Articulate What the Product Should Feel Like Before You Open Figma

There is a difference between what a product does and what it feels like to use it.

Before any screens get designed, you need to define your UX principles. Is this product fast and minimal, designed for power users who know what they want? Or is it guided and hand-holdy, designed for someone who needs to be walked through every step? These are fundamentally different products even if they solve the same problem.

From there, map the critical user journey from the moment someone lands to the moment they experience their first value. That moment is what product people call the "aha moment" and it is the most important moment in your entire product. Everything in your UX should be engineered to get the user to that moment as fast as possible.

UX is not a design decision. It is a product decision. Treat it like one.

3. Build Your Brand Foundation Before Your First Component

Brand is not a logo. It is not a colour palette. It is not something you figure out after the product is built.

Brand is the sum of every decision your product makes in front of a user. It is your product name and why it was chosen. It is your tagline and whether it communicates the real value or just sounds clever. It is your brand pillars, the two or three things your product fundamentally stands for. It is your positioning statement, the clear articulation of who this is for and why it is different.

Most critically, brand is your voice and tone. Every label, every button text, every empty state message, every error notification is a brand decision. "Scaling your focus" communicates something completely different than "Choose a plan." "Work, Draft" communicates something completely different than "Untitled document 3." These micro decisions compound over an entire product experience into either trust or confusion.

Define this foundation before you build. It will inform every component you create.

4. Map Your Information Architecture Before Any Screens

Information architecture is the skeleton of your product and almost nobody thinks about it before they start building.

IA means mapping every page, every section and every user flow on paper before a single screen gets designed. It means defining your navigation model clearly. Will this product use a sidebar, a top nav or bottom tabs? Each choice communicates something different and works better for different use cases.

The most important principle in IA is to group features by user intent, not by how you built them. Developers naturally want to organise things by how they are structured in the codebase. Users organise things by what they are trying to accomplish. These are almost always different. Build the navigation for the user, not for yourself.

IA done wrong means users cannot find features you spent weeks building. They exist in the product but they are invisible. That is a product failure regardless of how well the features work.

5. Layout Consistency Across Roles is Non Negotiable

If your product has role based access, which most modern SaaS products do, every role needs to experience the same logic even when they are seeing different data.

This means the same component behaviour across all views. The same visual hierarchy regardless of which role is logged in. The same interaction patterns whether you are an admin, a manager or an end user. Define a master layout grid and commit to never breaking it across pages.

Users should never feel like they switched products when they switch roles or navigate between sections. That feeling of inconsistency is invisible when you get it right and immediately obvious when you get it wrong. It is one of the clearest signals of whether a product was thoughtfully built or assembled in a hurry.

6. Build Your Design System Before Your First Screen

Most vibe coders open Figma and start drawing components immediately. We build the token system first.

A token system means your spacing scale is defined before anything is placed on a page. Your type scale is locked in before any text is styled. Your colour tokens, the named variables that carry meaning across the entire product, exist before a single component is created.

From there you build the component library: buttons, inputs, cards, modals, navigation elements. Each component gets all of its states documented and designed. Default, hover, active, disabled, error. Not just the states that look good but all of them.

This is the single biggest differentiator between a product that feels like it costs $500 and one that feels like it costs $50,000. Users cannot name what they are feeling. But they feel it immediately.

7. Colour Palette is a Retention Decision

Most founders pick colours they like. That is the wrong filter entirely.

The right question is: what colours does your user trust? A fintech product and a children's learning app should never share the same palette because the emotional and psychological associations are completely different. Colour communicates trust, urgency, safety and delight before a single word is read.

Define your full token set. Primary and secondary brand colours. Semantic colours, which are the most important and most ignored, covering success, warning, error and informational states. And your neutral scale, which carries more of your UI than most founders realise.

Colour communicates before words do. It is doing work in your product whether you designed it intentionally or not.

8. Every Product State Needs to Be Designed

This is where most products fall apart completely.

The happy path is what gets designed. The user lands, the data loads, everything works. Shipped.

But real users encounter every other state constantly. The loading state when data is being fetched. The empty state when a user is new and there is nothing to display yet. The error state when something goes wrong. The edit state when content is being modified. The success state when an action is completed.

The zero data state deserves special attention because it is the state every single new user encounters first and it is almost universally ignored. What does your product look like on day one when a user has not done anything yet? That experience determines whether they come back on day two.

Error messages are another critical failure point. An error message should tell a user exactly what to do next, not just what went wrong. "Something went wrong" is not an error message. It is an abandonment trigger.

95% of vibe coded products only design the happy path. The edge cases are where users quit or where they fall in love.

9. Onboarding Should Collect Just Enough

The biggest onboarding mistake founders make is trying to learn everything about the user on day one.

Good onboarding is built around one question: what is the minimum information needed to deliver a valuable first session? Anything beyond that is friction. Every extra field, every additional step, every optional question that feels mandatory is a user you lost before they ever experienced your product.

The principle to apply here is progressive disclosure. Ask for what you need at the start. As the user gets comfortable and derives more value from the product, ask for more. Trust is earned before data is collected, not the other way around.

Never gate your product behind a ten step setup flow. The goal of onboarding is to get the user to their first value moment as fast as possible. That is it.

10. Performance is a Product Feature

Load time targets should be defined before you build, not measured after you ship.

The standard to aim for is under two seconds for any core user action. Lazy load everything that is not immediately visible. Use skeleton screens instead of spinners wherever possible because perceived performance matters as much as actual performance. When a user sees a skeleton screen, their brain registers that the content is coming. When they see a spinner, their brain registers that they are waiting.

Users do not blame their internet connection when an app is slow. They blame the product. Performance is invisible when you get it right and the first thing users mention in negative reviews when you get it wrong.

11. Micro Interactions Are the Difference

This is the layer almost every vibe coder skips entirely and it is the layer that makes users say "this just feels good" without being able to explain why.

Every button click needs feedback. Every form submission needs a response. Every page transition needs a signal. The animation duration sweet spot is between 150 milliseconds and 300 milliseconds. Fast enough to feel snappy and responsive. Slow enough for the brain to register that something happened.

Micro interactions are not decorative. They are functional. They tell the user their action was received. They make the product feel alive rather than static. They are the difference between a product that users describe as "smooth" versus one they describe as "clunky" even if the underlying functionality is identical.

12. Build for the Second Session, Not the First

Anyone can make a good first impression. The real metric is whether your user comes back on day three.

Every product has an activation event, a specific action that, once completed, strongly predicts long term retention. Your job is to identify that activation event and then engineer your entire first session experience around getting users to it as fast as possible.

This changes how you think about every decision. It is not "how do we make the product look impressive on first launch?" It is "how do we get users to the moment where they cannot imagine not having this product?"

Day one retention is easy. Day three retention is the real test. If users are not coming back, the product failed. Not the marketing. Not the distribution. The product.

The Full Picture

Clear user persona. Defined UX feel. Solid brand foundation. Tight information architecture. Consistent layout system across roles. Proper design tokens. A colour palette your user trusts. Every state designed. Minimal friction onboarding. Fast performance. Intentional micro interactions. Built for the second session.

This is how you build a product people come back to, not just open once and forget.

Most founders think great products come from great ideas. They don't. They come from great decisions made at every layer of the product, from the first user persona exercise all the way down to the 150 millisecond button animation.

The vibe coded look-alikes flooding the market right now cut corners at every one of these layers. That is exactly why they fail.

Do the work the others won't. That is the only real differentiator that matters.