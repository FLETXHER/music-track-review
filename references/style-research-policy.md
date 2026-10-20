# Style Research Policy

## Principle

Style classification starts with the recording's actual sound and credible public evidence. When an explicitly authorized Style catalog is available in the current session, map supported candidates to it without sacrificing musical accuracy. Without such a catalog, use established public style terms; do not imply that a private whitelist was checked.

## Established-term rule

- Do not create descriptive compound labels on the fly merely because they sound plausible.
- Terms such as “Soul-Sampled Hip Hop”, “Industrial-Adjacent Techno”, or similar constructions must not be used unless they are demonstrably established public style names.
- When evidence supports an influence but not a recognized compound style, use an established simpler label such as Soul, East Coast Rap, Hardcore Hip-Hop, Hard Techno, etc.
- Distinguish evidence describing a sonic influence from evidence that this is an established Style name.
- Prefer fewer strongly supported dominant Styles over three speculative labels.
- For fine-grained style classification, Rate Your Music and AllMusic should be checked when accessible, then cross-checked with other appropriate sources.
- Do not treat RYM or AllMusic as absolute authorities or whitelists.

## Normalized vocabulary and dominance

- Start with web-supported candidates, then normalize them to a standard, checkable public term where that improves consistency without losing the track's identity.
- Put the dominant style first. Prefer one strongly supported style to several trace influences, and use 1–3 labels only when each one is materially part of the recording's identity.
- Keep actual musical fit first: final labels should reflect the track's dominant audible identity.
- A weak / trace influence that is not materially part of the track's identity should normally be omitted.
- If fine-grained evidence is weak or conflicting, broaden the label instead of preserving a precise but unstable candidate.

## Primary Style Validation Gate

Run this gate before every completed review. It is a classification check, not a request to fill all three Style slots.

1. **Identify the sound.** Compare rhythm and groove, drums and low end, melody and harmony, instrumentation and sound design, performance, form, production language, and defining traits of candidate styles against the exact recording and credible sources. Do not decide from the title, film/game association, artist scene, one database tag, acoustic instruments, or the absence of vocals alone.
2. **Validate the primary label.** At least one Style must describe a supported dominant *musical* identity. `Instrumental`, `Acoustic`, `Theme`, `Soundtrack`, and `Video Game Music` are useful when accurate, but a list containing only form, production attribute, or usage-context labels fails this gate. They are not banned: retain `Instrumental` for genuinely instrumental music and an appropriate soundtrack label when its role is material and supported.
3. **Test fit before specificity.** Verify the proposed style's defining audible traits. A score for a game is not automatically `Orchestral`; piano alone does not establish `Neoclassical`; acoustic instruments do not establish `Folk`; unusual timbres do not automatically establish `Experimental`. Do not flatten all electronic music into one substyle or classify from artist/label identity. Broaden when the precise style lacks evidence.
4. **Check completeness.** Confirm that the primary style is real and accurate; each additional Style is materially present; instrumental and soundtrack attributes are handled when applicable; no dominant established style is missing; and no label is redundant, weak, or inferred solely to fill a slot.

If no credible dominant style can be identified, do not invent one or present a completed review. State what remains unverified, or ask one concise question if recording identity is the obstacle.

## Optional authorized catalog mapping

The public repository does not contain a Style catalog or a fixed Style count. Use a catalog only when the user explicitly provides or authorizes access to its current version in the running environment. Treat it as read-only session input; never copy private rows, explanations, priority data, source files, or private links into this repository or public tests.

1. Check that Style names are present and unique; inspect provided categories and aliases for blanks, duplicates, and ambiguous near matches. Do not silently choose between conflicting entries.
2. Identify the true musical style *before* mapping. Match to an exact catalog name or a documented synonym when the recording fits; use a broader catalog term only if it remains musically accurate. Category and alias metadata help disambiguate; they cannot override actual sound.
3. Put the supported dominant style first. Add only material secondary styles. If a real important style is absent, use an accurate broader catalog label when available and put the uncovered specific public term in the first line of `备注`, without duplicating a Style label already used.
4. If no accurate catalog term describes the dominant style, use its established public name in `Style` rather than a false in-catalog substitute. Do not repeat that name in `备注`; list only other important uncovered styles there. The primary-style gate takes precedence over forcing a catalog match.

When no authorized catalog is available, use established public terms directly in `Style`. Do not claim in-catalog or out-of-catalog status, and do not add an out-of-catalog note line.

### Out-of-catalog note format

Only after an authorized catalog has actually been checked, if important supported styles remain uncovered, list their public names separated by ` / ` on the first line of the existing `备注` field. Continue with one short line each for Mainstream Appeal and Musicality. Do not add a sixth field, repeat names already represented in `Style`, or add boilerplate about catalog coverage.

## Workflow

1. Resolve the exact recording and form style candidates from its musical characteristics and public evidence.
2. Check whether each candidate is an established name used by reputable databases, publications, artists/labels, or specialist communities.
3. If an authorized catalog is present, map only accurate matches; otherwise normalize to defensible public terms.
4. Rank by dominant audible identity, keep material secondary styles, omit trace influences, and broaden weakly supported precision.
5. Run the Primary Style Validation Gate before returning a completed review.

## Good behavior

- A rap track can be `East Coast Rap` even if another database only says `Hip Hop`, when the regional style is well supported.
- A track with clear jazz-derived sampling/arrangement can use `Jazzy Hip-Hop` or another established jazz-rap term when evidence supports it.
- A modern work that borrows 1970s soul production can still be categorized by its contemporary primary style while also carrying a meaningful soul-related style label.

## Avoid

- copying every style tag found online;
- treating database co-occurrence as proof that a style applies;
- forcing every influence into the final answer;
- rejecting a useful established term only because one reference list omits it;
- inventing labels such as `Proto-X-Adjacent` unless that phrase is itself an established public term.

## Broad families versus final Style

Broad genre families can orient internal research, including hybrid recordings, but v0.8 does not output a `Genre` field. The completed review normally contains 1–3 Styles, with a supported dominant musical style first.
