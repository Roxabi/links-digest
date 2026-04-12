---
title: "TheCraigHewitt/seomachine"
source: "https://github.com/TheCraigHewitt/seomachine"
date: 2025-10-29
tags: ["SEO content creation", "Claude Code workspace", "blog writing tool", "Python application"]
platform: github
author: "TheCraigHewitt"
summary: "SEO Machine is a Claude Code workspace for creating long-form, SEO-optimized blog content with research, writing, and analysis features."
---
# TheCraigHewitt/seomachine

**URL:** https://github.com/TheCraigHewitt/seomachine
**Description:** A specialized Claude Code workspace for creating long-form, SEO-optimized blog content for any business. This system helps you research, write, analyze, and optimize content that ranks well and serves your target audience.
**Language:** Python
**Stars:** 5679 | **Forks:** 803
**License:** MIT License
**Homepage:** https://seomachine.io
**Last updated:** 2026-04-10

## README (excerpt)

# SEO Machine

A specialized Claude Code workspace for creating long-form, SEO-optimized blog content for any business. This system helps you research, write, analyze, and optimize content that ranks well and serves your target audience.

## Overview

SEO Machine is built on Claude Code and provides:
- **Custom Commands**: `/research`, `/write`, `/rewrite`, `/analyze-existing`, `/optimize`, `/performance-review`, `/publish-draft`, `/article`, `/priorities`, plus specialized research and landing page commands
- **Specialized Agents**: Content analyzer, SEO optimization, meta element creation, internal linking, keyword mapping, editor, performance analysis, headline generator, CRO analyst, landing page optimizer
- **Marketing Skills**: 26 marketing skills for copywriting, CRO, A/B testing, email sequences, pricing strategy, and more
- **Advanced SEO Analysis**: Search intent detection, keyword density & clustering, content length comparison, readability scoring, SEO quality rating (0-100)
- **Data Integrations**: Google Analytics 4, Google Search Console, DataForSEO for real-time performance insights
- **Context-Driven**: Brand voice, style guide, SEO guidelines, and examples guide all content
- **Workflow Organization**: Structured directories for topics, research, drafts, and published content

## Getting Started

### Prerequisites
- [Claude Code](https://claude.com/claude-code) installed
- Anthropic API account

### Installation

1. Clone this repository:
```bash
git clone https://github.com/TheCraigHewitt/seomachine.git
cd seomachine
```

2. Install Python dependencies for analysis modules:
```bash
pip install -r data_sources/requirements.txt
```

This installs:
- Google Analytics/Search Console integrations
- DataForSEO API client
- NLP libraries (nltk, textstat)
- Machine learning (scikit-learn)
- Web scraping tools (beautifulsoup4)

3. Open in Claude Code:
```bash
claude-code .
```

4. **Customize Context Files** (Important!):

   All context files are provided as templates. Fill them out with your company's information:

   - `context/brand-voice.md` - Define your brand voice and messaging *(see examples/castos/ for reference)*
   - `context/writing-examples.md` - Add 3-5 exemplary blog posts from your site
   - `context/features.md` - List your product/service features and benefits
   - `context/internal-links-map.md` - Map your key pages for internal linking
   - `context/style-guide.md` - Fill in your style preferences
   - `context/target-keywords.md` - Add your keyword research and topic clusters
   - `context/competitor-analysis.md` - Add competitor analysis and insights
   - `context/seo-guidelines.md` - Review and adjust SEO requirements

   **Quick Start**: Check out `examples/castos/` to see a complete real-world example of all context files filled out for a podcast hosting SaaS company.

## Workflows

### Creating New Content

#### 1. Start with Research
```
/research [topic]
```

**What it does**:
- Performs keyword research
- A...