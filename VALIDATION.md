# Validation report

Checked 2026-11-19 against the linked official documentation snapshot.

## Passed

- Crawled the official AlfredUI documentation tree and the linked workflow-object setup page. Deduplicated slash/no-slash variants into **70 distinct source pages**; recorded six failed links separately.
- Matched **368 property/function declaration blocks** to the original HTML. Every inventory entry's source anchor exists in its source page. This total includes repeated shared/layout declarations and functions, not just unique writable fields.
- Covered all **16 JSON commands**, **six layouts**, **13 native component types**, the **file/template pseudo-components**, and the **five named custom property types**.
- Reviewed source prose and examples for semantics not expressed by property blocks, including maps, array item structures, null behavior, getter return shapes and conditional requirements. Recorded conflicts rather than asserting inferred runtime fixes.
- Validated skill frontmatter and naming using the skill-creator validator.
- Validated the unofficial schema against JSON Schema Draft 2020-12. Its **58 definitions** accepted all eight complete UI examples, all 16 command examples, and all six layout examples.
- Confirmed that deliberately invalid component and action discriminators are rejected by the authoring schema.
- Parsed all **38 JSON files** in the package as strict JSON, including data fragments and manifests.
- Checked all local Markdown links, example window roots, literal component-id uniqueness, and bundled script paths using `scripts/check_package.py`.
- Checked shell syntax for both bundled response scripts and ran each independently. Both returned parseable JSON containing an update.ids map. No UI actions or command fragments were executed.

## Limits

No Alfred runtime session was launched. UI rendering, focus, keyboard shortcuts, selection, async ordering, permissions, notifications, file dialogs, persistence, browser navigation and version-dependent styling were not exercised in Alfred. No empirical behavior is claimed for the source contradictions.

The schema intentionally permits unknown properties and many placeholder forms. It is not a substitute for contextual review, and does not enforce all constraints listed in the references. Partial update payloads, including pulse reconfiguration, need contextual handling rather than validation as full construction objects. See [schema guide](references/schema-guide.md).

The [source manifest](references/sources.json) provides retrieval dates and hashes of the retrieved HTML for traceability. Raw source HTML remains outside this deliverable; the package is an original structured technical reference with source links, not an archive of the publisher's manuals.

## Recheck after editing

From the skill directory, run:

```sh
python3 scripts/check_package.py
```

That integrity check uses only Python's standard library. JSON Schema validation requires a Draft 2020-12 validator, which is not bundled. Run the examples in the intended Alfred version and launch mode before relying on runtime behavior. Record build, macOS version, steps, and observed outcomes separately from documented claims.
