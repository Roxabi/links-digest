---
title: "siddharthvaddem/openscreen"
source: "https://github.com/siddharthvaddem/openscreen"
date: 2026-04-07
tags: ["screen recording tool", "open-source software", "demo creation app", "Screen Studio alternative"]
platform: github
author: null
summary: "OpenScreen is a free open-source screen recording tool for creating product demos with automatic zooms and customizable backgrounds."
---
# siddharthvaddem/openscreen

**URL:** https://github.com/siddharthvaddem/openscreen
**Description:** Create stunning demos for free. Open-source, no subscriptions, no watermarks, and free for commercial use. An alternative to Screen Studio. 
**Language:** TypeScript
**Stars:** 28099 | **Forks:** 1891
**License:** MIT License
**Topics:** electron, pixijs, screen-recorder, open-source, screen-capture
**Homepage:** https://openscreen.vercel.app
**Last updated:** 2026-04-11

## README (excerpt)

> [!WARNING]
> This is very much in beta and might be buggy here and there (but hope you have a good experience!).

<p align="center">
  <img src="public/openscreen.png" alt="OpenScreen Logo" width="64" />
  <br />
  <br />
  <a href="https://deepwiki.com/siddharthvaddem/openscreen">
    <img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki" />
  </a>
  &nbsp;
  <a href="https://discord.gg/yAQQhRaEeg">
    <img src="https://img.shields.io/discord/pHAUbcqNd?logo=discord&label=Discord&color=5865F2" alt="Join Discord" />
  </a>
</p>

# <p align="center">OpenScreen</p>

<p align="center"><strong>OpenScreen is your free, open-source alternative to Screen Studio (sort of).</strong></p>

If you don't want to pay $29/month for Screen Studio but want a much simpler version that does what most people seem to need, making beautiful product demos and walkthroughs, here's a free-to-use app for you. OpenScreen does not offer all Screen Studio features, but covers the basics well!

Screen Studio is an awesome product and this is definitely not a 1:1 clone. OpenScreen is a much simpler take, just the basics for folks who want control and don't want to pay. If you need all the fancy features, your best bet is to support Screen Studio (they really do a great job, haha). But if you just want something free (no gotchas) and open, this project does the job!

OpenScreen is 100% free for personal and commercial use. Use it, modify it, distribute it. (Just be cool 😁 and give a shoutout if you feel like it !)

<p align="center">
	<img src="public/preview3.png" alt="OpenScreen App Preview 3" style="height: 0.2467; margin-right: 12px;" />
	<img src="public/preview4.png" alt="OpenScreen App Preview 4" style="height: 0.1678; margin-right: 12px;" />
</p>

## Core Features
- Record specific windows or your whole screen.
- Add automatic or manual zooms (adjustable depth levels) and customize their durarion and position.
- Record microphone and system audio.
- Crop video recordings to hide parts.
- Choose between wallpapers, solid colors, gradients or a custom background.
- Motion blur for smoother pan and zoom effects.
- Add annotations (text, arrows, images).
- Trim sections of the clip.
- Customize the speed of different segments.
- Export in different aspect ratios and resolutions.

## Installation

Download the latest installer for your platform from the [GitHub Releases](https://github.com/siddharthvaddem/openscreen/releases) page.

### macOS

If you encounter issues with macOS Gatekeeper blocking the app (since it does not come with a developer certificate), you can bypass this by running the following command in your terminal after installation:

```bash
xattr -rd com.apple.quarantine /Applications/Openscreen.app
```

Note: Give your terminal Full Disk Access in **System Settings > Privacy & Security** to grant you access and then run the above command.

After running this command, proceed to **System Preferences > Security & Privacy** to grant the necessary permis...