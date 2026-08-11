#!/usr/bin/env python3
from __future__ import annotations

import json
import re
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

RAW_MATERIAL_EXTENSIONS = {
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".zip",
    ".rar",
    ".7z",
}
TEXT_EXTENSIONS = {".md", ".json", ".py", ".txt", ""}
FRONTMATTER = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.S)
YAML_KEY = re.compile(r"[A-Za-z][A-Za-z0-9_-]*\Z")
INTERNAL_URL = re.compile(
    r"https?://[^\s/]*(?:internal|intranet|private|corp)[^\s/]*(?:/[^\s]*)?",
    re.I,
)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def parse_frontmatter(source: str) -> dict[str, str]:
    """Validate the flat YAML mapping used for this skill's metadata."""
    values: dict[str, str] = {}
    for line_number, line in enumerate(source.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[:1].isspace():
            fail(f"SKILL.md frontmatter line {line_number} must be top-level")
        if ":" not in line:
            fail(f"SKILL.md frontmatter line {line_number} is not YAML key-value syntax")

        key, value = line.split(":", maxsplit=1)
        key = key.strip()
        value = value.strip()
        if not YAML_KEY.fullmatch(key):
            fail(f"SKILL.md frontmatter key {key!r} is invalid")
        if not value:
            fail(f"SKILL.md frontmatter value for {key!r} is empty")
        if key in values:
            fail(f"SKILL.md frontmatter repeats {key!r}")
        values[key] = value

    if not values:
        fail("SKILL.md frontmatter is empty")
    return values


def iter_repository_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            yield path


for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        fail(f"missing required file: {rel}")

for path in iter_repository_files():
    if path.suffix.lower() in RAW_MATERIAL_EXTENSIONS:
        fail(f"raw material file is not allowed: {path.relative_to(ROOT)}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
match = FRONTMATTER.match(skill)
if not match:
    fail("SKILL.md missing valid YAML frontmatter")

frontmatter = parse_frontmatter(match.group(1))
name = frontmatter.get("name")
description = frontmatter.get("description")
if name is None or description is None:
    fail("SKILL.md requires name and description")

if name != ROOT.name:
    fail(f"skill name {name!r} must match parent folder {ROOT.name!r}")
if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
    fail("skill name must use lowercase letters, numbers, and single hyphens")
if len(name) > 64:
    fail("skill name exceeds 64 characters")
if not (1 <= len(description) <= 1024):
    fail("description must be 1-1024 characters")

try:
    data = json.loads((ROOT / "evals/evals.json").read_text(encoding="utf-8"))
except json.JSONDecodeError as error:
    fail(f"evals/evals.json is not valid JSON: {error.msg}")

if not isinstance(data, dict):
    fail("evals/evals.json must contain a JSON object")
if data.get("skill_name") != name:
    fail("evals skill_name does not match SKILL.md name")
if not isinstance(data.get("evals"), list) or len(data["evals"]) < 3:
    fail("evals/evals.json must contain at least three evals")

for path in iter_repository_files():
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    if INTERNAL_URL.search(text):
        fail(f"obvious internal URL found in {path.relative_to(ROOT)}")

print("PASS: repository structure, frontmatter, eval JSON, and public-disclosure checks")
