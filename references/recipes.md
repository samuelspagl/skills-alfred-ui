# Practical recipes and example index

The examples are original compositions of documented API features. All `.alfredui` directories contain a complete `ui.json`; other JSON files are explicitly fragments. Static checks do not establish runtime compatibility.

## Load a complete example

In an Alfred workflow, add an Alfred UI object and point its file setting to the chosen `.alfredui` package. Connect a Keyword or Hotkey input and choose internal or external launch. The [official workflow page](api/workflows--user-interface--alfredui.md) explains this setup. For isolated component snippets, the official [Try Alfred UI workflow](https://alfred.app/workflows/alfredapp/try-alfred-ui/) is another option. Do not treat a component snippet as a complete ui.json.

| Example | What to try | Sources |
|---|---|---|
| [hello](../examples/hello.alfredui/ui.json) | Launch; click Say ready to speak a sentence | [Window](api/window.md), [Button](api/components--button.md), [Speak](api/actions--json--speak.md) |
| [form](../examples/form.alfredui/ui.json) | Change fields; return args and variables to the downstream workflow object | [Form](api/layouts--form.md), [Picker](api/components--picker.md), [Finish](api/actions--json--finish.md) |
| [searchable-list](../examples/searchable-list.alfredui/ui.json) | Type indoor/outdoor to filter two rows; observe selection styling | [Dataview](api/components--dataview.md), [Provider](api/components--dataview--providers--basic.md), [Filter](api/components--dataview--filters--basic.md) |
| [markdown](../examples/markdown.alfredui/ui.json) | Edit the left area and click Render | [Textarea](api/components--textarea.md), [Markdownarea](api/components--markdownarea.md), [Update](api/actions--json--update.md) |
| [browser](../examples/browser.alfredui/ui.json) | Launch externally; enter a full URL and press Return; try navigation buttons | [WebKit](api/components--webkitview.md), [Browser tutorial](api/tutorials--web-browser.md) |
| [templates](../examples/templates.alfredui/ui.json) | Reuse a caption template twice with distinct instance ids | [Templates](api/templates.md) |
| [pulse](../examples/pulse.alfredui/ui.json) | Observe periodic clock updates; Stop disables the pulse | [Pulse](api/pulse.md), [Update](api/actions--json--update.md) |
| [script-action](../examples/script-action.alfredui/ui.json) | Run a background script returning a UI update | [Actions](api/actions.md), [JSON Actions](api/actions--json.md) |

Keep executable permissions on `scripts/tick.sh` and `scripts/respond.sh` when copying examples. They use `/bin/sh` and emit JSON on stdout. Each has been run separately during validation, but not by Alfred. The clock's time string format is deliberately limited; arbitrary text should be JSON-encoded using a proper serializer in your chosen language.

## Capture a getter before changing the UI

Use `action.variables` to capture `{value:input.text}`, then reference `{var:body}` inside `action.src.update`. This avoids assuming that getters can be evaluated after a command has already replaced the source component. The markdown and form examples show this pattern. A variable change alone is not a promise that previously rendered text will update; send an update command.

## Build a searchable dataview

1. Create a textfield with id query and a dataview with id places.
2. Set data.src to an array of row objects. Reserve uid for identity; use literal keys such as name.text for cell bindings.
3. Define cell.root components with corresponding ids.
4. Put reset values in cell.init for every property affected by selection styling; cell objects are reused.
5. Configure data.filter with fields in args and `{value:query.text}` in match.
6. On query's changed event, call the places filterdata function. For costly backend requests, consider typingstopped and async rather than running a blocking script on every keystroke.

See [row shape](../examples/data/row.json). Strings for uid are a local convention supported by the documented uid-targeting properties; duplicate behavior remains unspecified.

## Modify rows without rebuilding the component

The three payloads target the searchable-list example and are suitable as `type: json` action.src or a script's JSON response:

- [Insert](../examples/data/modify.json): add park after coast using `data.modify.insert`.
- [Replace](../examples/data/replace.json): replace coast using `data.modify.replace.srcmap`.
- [Delete](../examples/data/delete.json): remove library using `data.modify.delete.uids`.

These are separate recipes, not an asserted transaction order. `autoselect` defaults true per modification branch; component select can override reselection. The provider modification names differ from UI component insert/replace/remove commands. Source: [basic provider](api/components--dataview--providers--basic.md).

## Choose and compose layouts

[Stack](../examples/layouts/stack.json) overlays components; it does not create a vertical list. [Inline](../examples/layouts/inline.json) handles an axis. [Border](../examples/layouts/border.json) divides regions. [Grid](../examples/layouts/grid.json) creates equal cells. [Form](../examples/layouts/form.json) pairs labels/controls. [Flex](../examples/layouts/flex.json) uses explicit coordinates and weights.

These files are component fragments. Place one under window.root or in a view's components array. For border children, supply region; for flex children, supply grid constraints. Source: [Layouts](api/layouts.md).

## Reuse external content

Use a template when parameters differ between instances; use a file pseudo-component when loading a component definition with wrapper constraints; use `{file:components/card.json}` for preprocessing inclusion. For large plain data arrays, `{fileraw:resources/rows.json}` avoids recursive preprocessing. All paths start at the package root. Templates and file pseudo-components have different documented id precedence. Sources: [Templates](api/templates.md), [File](api/components--file.md), [Placeholders](api/placeholders.md).

## Import and persist variables

[variable-config.json](../examples/variable-config.json) is a root-configuration fragment. It imports the first launch argument, explicitly imports a workflow variable, and configures a persistent preference. Merge it with a root window to make a complete UI. Set scriptenv explicitly. A bundleid is required for persistence. General variable values may be structured, but configured default is documented as string/null. Sources: [Variables](api/variables.md), [Browser tutorial](api/tutorials--web-browser.md).

## Use JSON commands

Each file below is a **command payload**, not an outer ACTION and not a whole UI. For a button, wrap it as `{"type":"json","src": PAYLOAD}` in an event action. Replace target ids with existing compatible components. Payloads for copy, open, share, sound, speak and notifications have real effects when you run them.

| Command | Example | Preconditions / consequence |
|---|---|---|
| remove | [JSON](../examples/commands/remove.json) | temporary exists; removes it and triggers layout |
| insert | [JSON](../examples/commands/insert.json) | container is a view; appends child |
| update | [JSON](../examples/commands/update.json) | heading exists; changes properties with layout |
| replace | [JSON](../examples/commands/replace.json) | heading exists; replaces its component type |
| sheet | [JSON](../examples/commands/sheet.json) | opens details; Escape dismisses; close with `{"sheet":{"close":"details"}}` |
| share | [JSON](../examples/commands/share.json) | shows sharing options for a URL |
| sound | [JSON](../examples/commands/sound.json) | plays system sound |
| speak | [JSON](../examples/commands/speak.json) | speaks the text |
| copy | [JSON](../examples/commands/copy.json) | replaces clipboard text |
| open | [JSON](../examples/commands/open.json) | opens example URL through macOS |
| opendialog | [JSON](../examples/commands/opendialog.json) | selects images then opens the chosen files |
| window | [JSON](../examples/commands/window.json) | changes content width, derives height |
| notification | [JSON](../examples/commands/notification.json) | posts/replaces a fixed-uid notification |
| functions | [JSON](../examples/commands/functions.json) | editor must be a textarea |
| popupmenu | [JSON](../examples/commands/popupmenu.json) | menuAnchor exists; one item speaks |
| finish | [JSON](../examples/commands/finish.json) | closes UI, returns workflow output |

[JSON Actions](api/actions--json.md) lists the processing order; each command page in the [index](../INDEX.md) defines its schema. Do not rely on JSON key order as a sequencing mechanism.

## Diagnose a problem

Check JSON syntax, target ids, path roots, event spelling and getters first. For layout debugging enable debug.colourful; external UIs can use a reloadshortcut. For workflow execution configure log.internal; for external execution choose a file or console. Avoid recording password getter contents. If an update changes desired dimensions, consider relayout=true. Internal and external window sizing differ. See [Debug](api/debug.md), [Log](api/log.md), [Window](api/window.md), and the [ambiguity register](uncertainties.md).
