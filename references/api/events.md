# Events

[Official source](https://www.alfredapp.com/help/alfredui/events/) · Checked 2026-11-19 · [Index](../../INDEX.md)

A component's events array holds event objects. Triggers may be one string or an array. Lifecycle names are preload (built but not shown), launched and quit. Interaction names are actioned, changed, typingstopped, mousedown, mouseup, clicked and doubleclicked. Availability depends on the component. Action may be one action or an array treated as a compound action. Actions run on the event thread and block rendering unless asynchronous script execution is used. Optional confirm configuration provides message, iconpath, informativetext and button labels; the text documents defaults Confirm and Cancel even though the headers do not. Exact typingstopped debounce duration is not specified.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `triggers` | event Properties | ENUM \| ARRAY of ENUM | Default: "actioned" | "preload", "launched", "quit", "actioned", "changed", "typingstopped", "mousedown", "mouseup", "clicked", "doubleclicked" | [§](https://www.alfredapp.com/help/alfredui/events/#property-triggers) |
| `action` | event Properties | ACTION \| ARRAY | Required | — | [§](https://www.alfredapp.com/help/alfredui/events/#property-action) |
| `confirm` | event Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/events/#property-confirm) |
| `confirm.message` | event Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/events/#property-confirm-message) |
| `confirm.iconpath` | event Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/events/#property-confirm-iconpath) |
| `confirm.informativetext` | event Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/events/#property-confirm-informativetext) |
| `confirm.confirmbuttontext` | event Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/events/#property-confirm-confirmbuttontext) |
| `confirm.cancelbuttontext` | event Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/events/#property-confirm-cancelbuttontext) |

## Related local references

- [Actions](actions.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
