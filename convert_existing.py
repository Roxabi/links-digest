#!/usr/bin/env python3
"""Convert existing MD files to frontmatter format."""

import re
from pathlib import Path

SOURCE_DIR = Path(__file__).parent / "links"
DEST_DIR = Path(__file__).parent / "links"


# Platform detection
def detect_platform(url: str) -> str:
    url_lower = url.lower()
    if "github.com" in url_lower:
        return "github"
    elif "x.com" in url_lower or "twitter.com" in url_lower:
        return "x"
    elif "youtube.com" in url_lower or "youtu.be" in url_lower:
        return "youtube"
    elif "reddit.com" in url_lower:
        return "reddit"
    elif "gist.github.com" in url_lower:
        return "gist"
    elif "skills.sh" in url_lower:
        return "skills"
    else:
        return "web"


def parse_existing_md(filepath: Path) -> dict:
    """Parse existing MD format into frontmatter data."""
    with open(filepath) as f:
        content = f.read()

    lines = content.split("\n")

    # Extract title (first # header)
    title = ""
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break

    # Extract source
    source = ""
    source_match = re.search(r"\*\*Source:\*\*\s*(https?://[^\s]+)", content)
    if source_match:
        source = source_match.group(1)

    # Extract date from filename or content
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", filepath.stem)
    date = date_match.group(1) if date_match else "2026-01-01"

    # Extract tags
    tags = []
    tags_match = re.search(r"\*\*Tags:\*\*\s*(.+)", content)
    if tags_match:
        tags = [t.strip() for t in tags_match.group(1).split(",")]

    # Extract author (for X posts)
    author = None
    author_match = re.search(r"\*\*Author:\*\*\s*(@?\w+)", content)
    if author_match:
        author = author_match.group(1)

    # Extract summary (first paragraph after ---, skip tables/lists)
    summary = ""
    parts = content.split("\n---\n")
    if len(parts) >= 2:
        body = parts[-1].strip()
        # Get first non-header, non-table, non-list paragraph
        for para in body.split("\n\n"):
            para = para.strip()
            if (
                para
                and not para.startswith("#")
                and not para.startswith("|")
                and not para.startswith("- ")
                and not para.startswith("* ")
            ):
                # Truncate to 150 chars for card display
                summary = para[:150] + "..." if len(para) > 150 else para
                break

    # Platform
    platform = detect_platform(source)

    return {
        "title": title,
        "source": source,
        "date": date,
        "tags": tags,
        "platform": platform,
        "author": author,
        "summary": summary,
        "content": content,
    }


def to_frontmatter(data: dict) -> str:
    """Convert data to frontmatter format."""
    lines = ["---"]
    lines.append(f'title: "{data["title"]}"')
    lines.append(f'source: "{data["source"]}"')
    lines.append(f"date: {data['date']}")
    lines.append(f"tags: {data['tags']}")
    lines.append(f"platform: {data['platform']}")
    lines.append(f"author: {data['author'] or 'null'}")
    lines.append(f'summary: "{data["summary"] or ""}"')
    lines.append("---")
    lines.append("")
    lines.append(f"# {data['title']}")
    lines.append("")
    lines.append(f"**Source:** {data['source']}")
    lines.append(f"**Date:** {data['date']}")
    if data["author"]:
        lines.append(f"**Author:** {data['author']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(data["content"].split("---")[-1].strip())

    return "\n".join(lines)


def main():
    DEST_DIR.mkdir(parents=True, exist_ok=True)

    md_files = list(SOURCE_DIR.glob("*.md"))
    print(f"Found {len(md_files)} MD files to convert")

    for filepath in md_files:
        if filepath.name == "INDEX.md":
            continue

        print(f"Converting {filepath.name}...")
        data = parse_existing_md(filepath)
        frontmatter = to_frontmatter(data)

        dest_path = DEST_DIR / filepath.name
        with open(dest_path, "w") as f:
            f.write(frontmatter)

        print(f"  → {dest_path}")

    print(f"\nDone! Converted {len(md_files) - 1} files to {DEST_DIR}")


if __name__ == "__main__":
    main()
