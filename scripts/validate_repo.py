#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "SKILL.md",
    "references/scoring-guide.md",
    "references/web-research.md",
    "references/style-research-policy.md",
    "references/genre-family-guide.md",
    "references/examples.md",
    "evals/evals.json",
]

# Keep source/project-specific material out of a publishable repository.
FORBIDDEN = [
    "音乐" + "S" + "FT",
    "R" + "ef" + "筛选",
    "for" + r"\s*" + "外部",
    "内" + "外部",
    "byte" + "dance",
    "lark" + "office",
    "飞" + "书",
]

def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)

for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        fail(f"missing required file: {rel}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
match = re.match(r"\A---\n(.*?)\n---\n", skill, flags=re.S)
if not match:
    fail("SKILL.md missing YAML frontmatter")

frontmatter = match.group(1)
name_match = re.search(r"^name:\s*(.+)$", frontmatter, flags=re.M)
desc_match = re.search(r"^description:\s*(.+)$", frontmatter, flags=re.M)
if not name_match or not desc_match:
    fail("SKILL.md requires name and description")

name = name_match.group(1).strip()
if name != ROOT.name:
    fail(f"skill name {name!r} must match parent folder {ROOT.name!r}")
if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
    fail("skill name must use lowercase letters, numbers, and single hyphens")
if len(name) > 64:
    fail("skill name exceeds 64 characters")

description = desc_match.group(1).strip()
if not (1 <= len(description) <= 1024):
    fail("description must be 1-1024 characters")

data = json.loads((ROOT / "evals/evals.json").read_text(encoding="utf-8"))
if data.get("skill_name") != name:
    fail("evals skill_name does not match SKILL.md name")
if not isinstance(data.get("evals"), list) or len(data["evals"]) < 3:
    fail("evals/evals.json must contain at least three evals")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.suffix.lower() not in {".md", ".json", ".py", ".txt", ""}:
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    for pattern in FORBIDDEN:
        if re.search(pattern, text, flags=re.I):
            fail(f"forbidden source/project marker {pattern!r} found in {path.relative_to(ROOT)}")

print("PASS: repository structure, frontmatter, eval JSON, and disclosure scan")
