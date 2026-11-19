# AlfredUI Agent Skill

A structured agent skill and API reference for **Alfred 6 AlfredUI**, covering native interfaces built with `.alfredui` packages and JSON.

Based on the [official AlfredUI technical documentation](https://www.alfredapp.com/help/alfredui/#technical-documentation), checked on **19 November 2026**. This is an independent reference, not an official Alfred publication.

## Start here

- **[SKILL.md](SKILL.md)** — agent instructions and reference routing.
- **[INDEX.md](INDEX.md)** — complete documentation index.
- **[Practical recipes](references/recipes.md)** — examples and integration patterns.
- **[Documentation conflicts](references/uncertainties.md)** — contradictory examples, gaps, and evidence levels.

## What's included

| Resource | Coverage |
| --- | --- |
| API references | 70 source-linked pages and 368 property/function declaration entries, including nested fields and repeated shared declarations |
| Components | 13 native component types plus file and template pseudo-components |
| Layouts | Stack, border, grid, inline, form, and flex |
| Actions | Events, action dispatch, and all 16 documented JSON commands |
| Shared data | Colours, fonts, images, shortcuts, menus, variables, placeholders, and templates |
| Runtime support | Pulse, logging, debugging, windows, and workflow integration |
| Schemas | Machine-readable declaration inventory and an unofficial JSON Schema with 58 definitions |
| Examples | Eight complete UI packages, 16 command payloads, six layout fragments, and data-modification examples |

## Installation

### With the Skills CLI (recommended)

```sh
npx skills add samuelspagl/skills-alfred-ui --skill alfred-ui
```

Or use Bun's package runner:

```sh
bunx skills add samuelspagl/skills-alfred-ui --skill alfred-ui
```

The CLI installs to the current project by default. Add `-g` for a global installation or `-a <agent>` to select a supported agent. Preview discovery without installing:

```sh
npx skills add samuelspagl/skills-alfred-ui --list
```

The repository's root `SKILL.md` is discovered automatically; no separate npm publication is needed. The current Skills CLI documents Node.js 22.20 or later. Bun normally honors Node shebangs; to use Bun's runtime explicitly, run:

```sh
bunx --bun skills add samuelspagl/skills-alfred-ui --skill alfred-ui
```

Discovery was verified against this public repository using `bunx --bun skills@latest add samuelspagl/skills-alfred-ui --list`, which found the `alfred-ui` skill. This was a discovery check, not an installation into a user's agent configuration.

Sources: [Skills installation options](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add), [skill discovery](https://github.com/vercel-labs/skills/blob/main/docs/creating-skills.md#skill-discovery), [runtime requirements](https://github.com/vercel-labs/skills#install-a-skill), and [Bun's bunx documentation](https://bun.sh/docs/pm/bunx).

### Manual installation

Clone this repository into a directory named `alfred-ui` in your agent's configured skills directory:

```sh
git clone https://github.com/samuelspagl/skills-alfred-ui.git /path/to/your/skills/alfred-ui
```

Replace `/path/to/your/skills` with the directory your agent uses. The repository root is the skill folder: keep `SKILL.md`, `references/`, `schemas/`, `scripts/`, and `examples/` together.

Alternatively, use GitHub's **Code → Download ZIP**, extract it, and copy the folder into your skills directory as `alfred-ui`. The references can also be read directly without installing a skill.

## Using the skill

Ask your agent to use the AlfredUI skill for requests such as:

- “Build an AlfredUI form that returns its values to the workflow.”
- “Create a searchable dataview with selection styling.”
- “Review this ui.json against the documented properties and flag uncertain behavior.”
- “Explain how placeholders resolve in an action versus a pulse.”

The skill directs the agent to relevant reference pages rather than loading the entire manual at once. API entries link back to their official sources.

## Trying the examples

Configure an Alfred UI workflow object to load one of these packages, and choose internal or external launch as appropriate:

| Package | Demonstrates |
| --- | --- |
| [hello.alfredui](examples/hello.alfredui/ui.json) | Basic layout and speech action |
| [form.alfredui](examples/form.alfredui/ui.json) | Inputs, picker, checkbox, and workflow output |
| [searchable-list.alfredui](examples/searchable-list.alfredui/ui.json) | Data cells, filtering, and selection styling |
| [markdown.alfredui](examples/markdown.alfredui/ui.json) | Text input and Markdown rendering |
| [browser.alfredui](examples/browser.alfredui/ui.json) | WebKit navigation and address updates |
| [templates.alfredui](examples/templates.alfredui/ui.json) | Reusable parameterized components |
| [pulse.alfredui](examples/pulse.alfredui/ui.json) | Periodic script responses |
| [script-action.alfredui](examples/script-action.alfredui/ui.json) | Asynchronous script response |

The files in `examples/commands/`, `examples/layouts/`, and `examples/data/` are fragments, not complete UI packages. See the [recipes](references/recipes.md) for placement and target-id requirements. Preserve executable permissions on the bundled shell scripts.

## Repository structure

```text
.
├── SKILL.md                 Agent entry point
├── INDEX.md                 Complete reference index
├── VALIDATION.md            Checks performed and limitations
├── CHECKSUMS.sha256         Tracked deliverable checksums
├── references/
│   ├── api/                 Per-topic API references
│   ├── recipes.md           Practical examples
│   ├── schema-guide.md      Schema interpretation and limits
│   ├── uncertainties.md     Conflicts and undocumented details
│   └── sources.json         Source URLs, retrieval dates, and hashes
├── schemas/
│   ├── documented-api.json  Factual declaration inventory
│   └── alfredui.schema.json Unofficial authoring schema
├── examples/                Complete packages and fragments
└── scripts/
    └── check_package.py     Local integrity checks
```

## Validation

Run the standard-library integrity checker from the repository root:

```sh
python3 scripts/check_package.py
```

It checks JSON syntax, local Markdown links, example window roots, literal component ids, and bundled script paths. It does not launch Alfred or execute UI actions.

The original package also passed Draft 2020-12 schema validation, example schema checks, and isolated shell-response checks. **The example UIs have not been tested inside Alfred.** See [VALIDATION.md](VALIDATION.md) for the precise scope.

The JSON Schema is deliberately permissive and is **not an official runtime contract**. It accepts unknown fields and does not enforce every contextual rule. Read the [schema guide](references/schema-guide.md) before using it as a validator.

## Sources and maintenance

The [source manifest](references/sources.json) records the official pages and hashes of the retrieved HTML. The package preserves API identifiers and technical declarations with independently written explanations and examples; it does not redistribute raw documentation pages.

When updating the reference:

1. Verify changes against official documentation and retain source links.
2. Distinguish explicit declarations, example-backed behavior, authoring choices, and unknowns.
3. Update affected references, schemas, examples, and the snapshot date.
4. Run the integrity checks and record any actual Alfred runtime testing separately.
5. Regenerate `CHECKSUMS.sha256` after changing tracked deliverables.

Alfred is a trademark of Running with Crayons Ltd. This repository is not affiliated with or endorsed by its publisher.
