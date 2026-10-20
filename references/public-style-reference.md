# Public Style Reference — P1 seed v0.1

This optional reference supplies candidate spellings for Style research. It is not evidence that a particular recording belongs to a style, not a hard whitelist, and not an internal-workflow catalog. The v0.8 Primary Style Validation Gate and five-field output remain authoritative.

## Provenance and reuse boundary

- The 341 names in `public-style-seed-v0.1.json` are a project-provided selection. Each name was checked for exact membership in the public `dist/styles.json` list at upstream commit `a8417a2107b621fe9a1fae91edb544dc82b56b05` (source SHA-256: `b5ca2f3d45e7d76c8faab18a49427875da1a18e1fbb4cf1f37a1e5249a577400`). This confirms public-source membership, not how the subset was originally selected.
- [The upstream project](https://github.com/hastefuI/discogs-dataset-genres-styles/tree/a8417a2107b621fe9a1fae91edb544dc82b56b05) states that its `dist/` data is [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Its software is MIT; no upstream software is copied here. The source list is derived from the Discogs data dump. This project does not copy release metadata, descriptions, images, audio, or MusicBrainz tag associations.
- `family_hint`, `role`, spelling aliases, and the accompanying listening questions were supplied for this project and authorized for inclusion. They are heuristic editorial aids, not official Discogs classifications, proof of any song's Style, or a map to a private catalog. Their accuracy has not been individually established by listening tests. The CC0 declaration for upstream `dist/` data must not be extended to these project-authored annotations or scripts; this repository currently has no separate downstream license for them.
- The uploaded ZIP, full-list builder, source workbook, internal label data, and private explanations are not part of this repository. Public availability and a CC0 claim do not certify classification accuracy or compatibility with another selector.

## Use

1. Resolve the exact recording and gather credible musical evidence first. Consult the seed only to find or normalize plausible established names; use `public-style-signatures.md` only as listening questions when a distinction is uncertain.
2. Check each candidate against the actual sound and independent sources. `primary_candidate` means a term may name a musical identity; it never means the current track qualifies. A `family_hint` is organization, not a final Genre or a reason to add a Style.
3. A form, ensemble, instrument, format, technique, or context label cannot by itself pass the Primary Style Validation Gate. Retain a genuinely relevant `Instrumental` or soundtrack label alongside a supported musical style. Do not force three labels.
4. A name missing from this **public candidate subset** may still be a valid established style. Use it when supported; do not falsely broaden it to fit the seed. Absence from this reference does **not** trigger the v0.8 out-of-catalog line in `备注`. That line applies only after an independently authorized catalog was actually checked.
5. If the seed or its raw URL cannot be read, follow the existing evidence-led open-vocabulary policy. Never treat reference lookup as a substitute for web research or listening evidence.

Run `python scripts/validate_public_style_reference.py` for offline structure and gate-fixture checks. These checks do not evaluate songs, verify individual heuristic annotations, or measure private-workflow coverage.
