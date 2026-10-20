#!/usr/bin/env python3
"""Offline structural checks for the public P1 seed; not a song-classification test."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "references" / "public-style-seed-v0.1.json"
UPSTREAM_COMMIT = "a8417a2107b621fe9a1fae91edb544dc82b56b05"
UPSTREAM_SHA256 = "b5ca2f3d45e7d76c8faab18a49427875da1a18e1fbb4cf1f37a1e5249a577400"
TOP_KEYS = {
    "name", "version", "created_on", "origin", "upstream_catalog_url",
    "upstream_description", "upstream_license_claim", "scope_warning", "styles",
    "normalization_aliases", "source_notes", "upstream_commit", "upstream_source_sha256"
}
ENTRY_KEYS = {"name", "family_hint", "role", "source"}
ROLES = {
    "primary_candidate", "context", "form", "ensemble", "instrument", "format", "technique"
}
FAMILY_HINTS = {
    "Blues / folk / country", "Classical / scoring / avant-garde", "context / form",
    "Electronic / club", "Hip-hop / rap", "Jazz / funk / soul",
    "Latin / global / reggae", "Metal / hardcore / punk", "Pop / R&B", "Rock / alternative"
}
SOURCE = "Discogs public-dump derived styles"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def validate(data: object) -> tuple[int, int]:
    require(isinstance(data, dict), "seed must be a JSON object")
    require(set(data) == TOP_KEYS, "seed has missing or unexpected top-level fields")
    require(data.get("name") == "public_style_reference_p1_seed", "unexpected seed name")
    require(data.get("version") == "0.1", "unexpected seed version")
    commit = data.get("upstream_commit")
    digest = data.get("upstream_source_sha256")
    require(commit == UPSTREAM_COMMIT, "source commit does not match the reviewed P1 version")
    require(digest == UPSTREAM_SHA256, "source digest does not match the reviewed P1 version")
    expected_url = (
        "https://raw.githubusercontent.com/hastefuI/discogs-dataset-genres-styles/"
        f"{commit}/dist/styles.json"
    )
    require(data.get("upstream_catalog_url") == expected_url, "source URL must be pinned")
    require("CC0 1.0" in str(data.get("upstream_license_claim", "")),
            "source license claim must identify the upstream declaration")

    styles = data.get("styles")
    require(isinstance(styles, list) and bool(styles), "styles must be a non-empty list")
    by_name: dict[str, dict] = {}
    for index, entry in enumerate(styles):
        require(isinstance(entry, dict) and set(entry) == ENTRY_KEYS,
                f"style {index} must have only the public seed fields")
        name = entry["name"]
        require(isinstance(name, str) and name == name.strip() and bool(name),
                f"style {index} has an invalid name")
        require(not any(ord(char) < 32 for char in name), f"style {index} has control characters")
        key = name.casefold()
        require(key not in by_name, f"duplicate style name: {name}")
        require(isinstance(entry["role"], str) and entry["role"] in ROLES,
                f"invalid role for {name}")
        require(isinstance(entry["family_hint"], str) and entry["family_hint"] in FAMILY_HINTS,
                f"unexpected family hint for {name}")
        require(entry["source"] == SOURCE, f"unexpected source for {name}")
        by_name[key] = entry

    aliases = data.get("normalization_aliases")
    require(isinstance(aliases, dict), "normalization_aliases must be an object")
    alias_keys: set[str] = set()
    for alias, target in aliases.items():
        require(isinstance(alias, str) and alias == alias.strip() and bool(alias),
                "alias must be a non-empty trimmed string")
        require(isinstance(target, str) and target.casefold() in by_name,
                f"alias target missing: {alias}")
        key = alias.casefold()
        require(key not in alias_keys, f"duplicate case-insensitive alias: {alias}")
        require(key not in by_name or key == target.casefold(),
                f"alias conflicts with canonical name: {alias}")
        alias_keys.add(key)

    # A role is only a candidate hint. Even a structurally passing label still needs song evidence.
    def gate(labels: list[str], *, evidence_for_primary: bool) -> bool:
        return evidence_for_primary and any(
            by_name.get(label.casefold(), {}).get("role") == "primary_candidate"
            for label in labels
        )

    fixtures = [
        (['Instrumental'], True, False),
        (['Acoustic', 'Instrumental'], True, False),
        (['Theme', 'Soundtrack', 'Video Game Music'], True, False),
        (['Instrumental', 'Soundtrack'], True, False),
        (['Chiptune', 'Instrumental', 'Video Game Music'], False, False),
        (['Chiptune', 'Instrumental', 'Video Game Music'], True, True),
        (['Ambient', 'Instrumental'], True, True),
        (['Folk', 'Acoustic'], True, True),
        (['Unknown Style', 'Instrumental'], True, False),
    ]
    for labels, evidence, expected in fixtures:
        require(gate(labels, evidence_for_primary=evidence) == expected,
                f"structural gate fixture failed: {labels}")
    return len(styles), len(aliases)


def main() -> int:
    try:
        data = json.loads(SEED.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
        names, aliases = validate(data)
    except (OSError, ValueError) as error:
        print(f"FAIL: public style reference: {error}")
        return 1
    print(f"PASS: public style reference: {names} unique names, {aliases} aliases, 9 structural fixtures")
    print("NOT TESTED: recording evidence, heuristic accuracy, private catalog mapping, model output")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
