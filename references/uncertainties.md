# Contradictions, gaps and evidence levels

Snapshot: 2026-11-19. No ambiguity below was resolved by running Alfred or inspecting its implementation.

**Declared** means a property table or explicit prose statement. **Example-backed** means official examples demonstrate a form without fully specifying it. **Authoring choice** means a conservative convention used here. **Unspecified** means the inspected sources do not settle the detail.

| Topic | Official evidence and conflict | Package treatment |
|---|---|---|
| Script environment | [root](api/ui-json.md) says initial variables are automatically exported unless overridden; [Variables](api/variables.md) declares scriptenv=false | Explicitly set scriptenv; default unresolved |
| Root window | [Window](api/window.md) uses root-level window, absent from [ui.json](api/ui-json.md)'s list | Include window as example/prose-backed root property |
| Dark appearance | [Window](api/window.md) and [View](api/components--view.md) describe dark as forcing light | Preserve enum, flag description conflict; don't assert runtime resolution |
| View appearance default | View enum defaults inherit; prose recommends automatic | Use declared inherit |
| Shortcut precedence | [Shortcut](api/properties--shortcut.md) says deepest with root as example | Avoid collisions; exact hierarchy priority unresolved |
| Picker selected | [Picker](api/components--picker.md) header STRING, getter prose object | Separate setter string and getter object |
| Font size | [FONT](api/properties--font.md) header ENUM, table admits numeric pixels | Model names plus numeric value; numeric range unspecified |
| Pulse interval | [Pulse](api/pulse.md) range starts 0.1, default and disable value are 0 | Treat 0 as explicit exception |
| Variable default | [Variables](api/variables.md) says STRING, default null | Model string/null conservatively; structured defaults unspecified |
| Popup menu | [Popupmenu](api/actions--json--popupmenu.md) says MENU, examples show array | Use array of MENU entries; mark example-backed interpretation |
| Filetypes | [Open dialog](api/actions--json--opendialog.md) declares ARRAY, examples show string | Use array of UTI strings |
| Getter placement | [JSON Actions](api/actions--json.md) requires getter capture into variables; [Finish](api/actions--json--finish.md) permits getters directly | Capture first; direct finish behavior documented but internally inconsistent |
| Dataview selection names | [Dataview](api/components--dataview.md) prose references behaviour.allowemptyselection and modifydata; declarations use behaviour.selection.allowempty and provider modify | Follow declarations; don't invent aliases |
| Dataview selected getter | Not a formal getter declaration; [Colour Search](api/tutorials--colour-search.md) demonstrates selected.swatch.background | Mark nested selection access example-backed; complete getter return shape unspecified |
| Dataview scrollbottom | Its description repeats top | Name exists; effect unconfirmed |
| Field border | [Textfield](api/components--textfield.md) example uses bordertype but declaration is bordered | Use bordered |
| Password event | [Passwordfield](api/components--passwordfield.md) example uses trigers | Use declared events spelling triggers |
| Progress colour | [Progress](api/components--progress.md) example uses color | Use declared colour |
| Menu separator | [MENU](api/properties--menu.md) example uses Separator; enum separator | Use lowercase enum |
| Textarea boolean | [Textarea](api/components--textarea.md) quotes false in a BOOL default | Supply false boolean; raw declaration retained |
| Invalid example JSON | Textarea introductory example and some tutorial snippets have trailing commas or are fragments | Original examples here are strict JSON |
| Remove relayout | [Remove](api/actions--json--remove.md) example adds relayout, absent from its declared schema; prose says automatic | Omit undocumented flag |
| Resize null | [Window action](api/actions--json--window.md) header omits null, prose permits it | Allow null as keep-current |
| Action src | [Actions](api/actions.md) marks required but log ignores src | Preserve marker; authoring schema permits omission for log |
| Event cardinality | Shared property says ARRAY or EVENT; [Events](api/events.md) primarily describes arrays | Use arrays in examples |
| Markdown editing | [Markdownarea](api/components--markdownarea.md) intro calls it input but no editable/getter/trigger contract | Do not inherit textarea API |
| Tutorial event key | [Speak tutorial](api/tutorials--speak-the-text.md) and [Browser tutorial](api/tutorials--web-browser.md) use trigger in some snippets | Use declared triggers |
| Template tutorial parameter | [Text-to-Markdown](api/tutorials--text-to-markdown.md) uses param:outputtext without supplying it in shown instances | Local example captures textarea getter explicitly |
| Argument index | Variables page alone does not explain base; [Browser tutorial](api/tutorials--web-browser.md) explicitly identifies args[0] as first | Zero-based is tutorial-backed |
| File/template id | Shared file note lets file's id win; Templates lets instance id win | Keep mechanisms distinct |
| Form wording | [Form](api/layouts--form.md) says two vertical rows but describes left/right columns | Follow pair/column resize explanation |

## Broken official links encountered

The following URLs failed retrieval (the first provider-link failure explicitly returned HTTP 404); valid matching topics were independently reached through the technical index:

- `https://www.alfredapp.com/help/alfredui/components/providers/basic/` → [provider page](api/components--dataview--providers--basic.md)
- `https://www.alfredapp.com/help/alfredui/constraints/` → [constraints](api/layouts--constraints.md)
- `https://www.alfredapp.com/help/alfredui/shared-properties/` → [shared properties](api/components--shared-properties.md)
- `https://www.alfredapp.com/help/alfredui/view/` → [view](api/components--view.md)
- `https://www.alfredapp.com/help/alfredui/border/` → [border](api/layouts--border.md)
- `https://www.alfredapp.com/help/alfredui/json/` → [JSON actions](api/actions--json.md)

These are topic mappings, not claims that the server redirects them. Slash/no-slash variants of successful pages were deduplicated. Source coverage excludes downloadable gallery workflows, forum discussions, linked Apple references, and implementation internals.

## Unspecified contracts

Do not invent: supported minimum build for every property; all macOS-dependent defaults; unknown-key handling; regex dialect; Markdown dialect; all image/audio codecs; numeric precision/rounding; data uid collision behavior; data mutation order; cancellation behavior; callback payloads; script timeout/exit-code behavior; async completion ordering; script-environment serialization of complex values; precedence of every variable initialization source; persistence storage path; typingstopped delay; exact behavior of empty selection getters; or a WebKit JavaScript bridge.

These are documentation boundaries, not assertions that Alfred lacks such behavior. Check updated official pages or test the specific case and label the result as empirical.
