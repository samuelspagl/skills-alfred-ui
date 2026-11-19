---
name: alfred-ui
description: Build, explain, review, and debug Alfred 6 AlfredUI JSON packages, components, layouts, data providers, events, actions, and workflow integration using a source-linked API reference.
---

# AlfredUI

Use this skill for `.alfredui` packages and the AlfredUI API. Ordinary Alfred Script Filter JSON is a different format.

## Working approach

1. Identify whether the UI runs inside Alfred or externally, and whether the task concerns a complete `ui.json`, a component, or a JSON-action response.
2. Read the relevant entries from [INDEX.md](INDEX.md). For new UIs, start with [structure](references/api/structure.md), [root configuration](references/api/ui-json.md), [window](references/api/window.md), [shared properties](references/api/components--shared-properties.md), and the chosen layout/component pages. Read only the additional references needed.
3. Keep component ids globally unique. Layout properties belong on views; placement constraints belong on children. Relative resource paths start at the package root, except the documented logging exception.
4. For interactivity, consult [events](references/api/events.md), [actions](references/api/actions.md), and [placeholder timing](references/api/placeholders.md). Capture UI getters in action variables before using them in JSON commands. Keep scripts responsive or use async deliberately; don't assume late results still match current UI state.
5. For data-driven interfaces, read the [dataview](references/api/components--dataview.md), [provider](references/api/components--dataview--providers--basic.md), and [filter](references/api/components--dataview--filters--basic.md) references together. Initialize reused cell state explicitly.
6. Check [uncertainties](references/uncertainties.md) when a tutorial/example conflicts with a property declaration. Prefer declared spellings, label evidence from examples, and do not invent unsupported flags, getters, defaults, or callback contracts. Recheck the official source when newer behavior matters; this snapshot is dated 2026-11-19.
7. Use [recipes](references/recipes.md) and the original [examples](examples/) as starting points. Validate strict JSON, resource paths, ids, event names, and contextual constraints. Test the UI in Alfred when available; static validation alone is not runtime verification.

## References and helpers

- [Complete index](INDEX.md): 70 source-linked pages, including all documented commands and custom types.
- [Schema guide](references/schema-guide.md): how to interpret declarations and the unofficial permissive JSON Schema.
- [Machine-readable API inventory](schemas/documented-api.json): exact field paths, declared types, ranges, markers, getters, enums, and source anchors.
- [Recipes](references/recipes.md): original runnable package examples and contextual command fragments.
- [Validation report](VALIDATION.md): checks performed and remaining limits.
- `python3 scripts/check_package.py`: checks this reference package's links, JSON, and bundled example resource references; it does not execute UI side effects.

Preserve the user's task scope: producing a skill or UI file does not itself authorize installation, launching commands, or changing a live workflow. Follow existing task authorization for those actions.
