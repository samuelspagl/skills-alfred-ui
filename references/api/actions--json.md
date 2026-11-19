# JSON Actions

[Official source](https://www.alfredapp.com/help/alfredui/actions/json/) · Checked 2026-11-19 · [Index](../../INDEX.md)

A JSON-action payload may set variables and pulse and contain the commands listed below. Capture UI getters into action variables before commands execute, then substitute var placeholders in commands. Documented command order is remove, insert, update, replace, sheet, share, sound, speak, copy, open, opendialog, window, notification, functions, popupmenu, finish. Object key insertion order does not change that documented order. The page does not state exact ordering between variables/pulse updates and every command. Commands may be supplied directly as action.src or returned by a script. This payload is distinct from the outer action object containing type/src/args.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `variables` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-variables) |
| `pulse` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-pulse) |
| `remove` | JSON Action Commands | JSON ACTION | View properties | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-remove) |
| `insert` | JSON Action Commands | JSON ACTION | View properties | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-insert) |
| `update` | JSON Action Commands | JSON ACTION | View properties | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-update) |
| `replace` | JSON Action Commands | JSON ACTION | View properties | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-replace) |
| `sheet` | JSON Action Commands | JSON ACTION | View properties | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-sheet) |
| `share` | JSON Action Commands | JSON ACTION | View properties | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-share) |
| `sound` | JSON Action Commands | JSON ACTION | View properties | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-sound) |
| `speak` | JSON Action Commands | JSON ACTION | View properties | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-speak) |
| `copy` | JSON Action Commands | JSON ACTION | View properties | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-copy) |
| `open` | JSON Action Commands | JSON ACTION | View properties | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-open) |
| `opendialog` | JSON Action Commands | JSON ACTION | View properties | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-opendialog) |
| `window` | JSON Action Commands | JSON ACTION | View properties | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-window) |
| `notification` | JSON Action Commands | JSON ACTION | View properties | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-notification) |
| `functions` | JSON Action Commands | JSON ACTION | View properties | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-functions) |
| `popupmenu` | JSON Action Commands | JSON ACTION | View properties | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-popupmenu) |
| `finish` | JSON Action Commands | JSON ACTION | View properties | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/#property-finish) |

## Related local references

- [Events](events.md)
- [Shared Properties](components--shared-properties.md)
- [Properties](properties.md)
- [Getters](properties--getters.md)
- [Pulse](pulse.md)
- [remove Action](actions--json--remove.md)
- [insert Action](actions--json--insert.md)
- [update Action](actions--json--update.md)
- [replace Action](actions--json--replace.md)
- [sheet Action](actions--json--sheet.md)
- [share Action](actions--json--share.md)
- [sound Action](actions--json--sound.md)
- [speak Action](actions--json--speak.md)
- [copy Action](actions--json--copy.md)
- [open Action](actions--json--open.md)
- [opendialog Action](actions--json--opendialog.md)
- [window Action](actions--json--window.md)
- [notification Action](actions--json--notification.md)
- [functions Action](actions--json--functions.md)
- [popupmenu Action](actions--json--popupmenu.md)
- [finish Action](actions--json--finish.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
