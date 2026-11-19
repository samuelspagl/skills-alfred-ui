# opendialog Action

[Official source](https://www.alfredapp.com/help/alfredui/actions/json/opendialog/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Configure file/folder selection, accepted UTI types, starting folder, prompt/message and multiple selection. Setvariable names the destination variable: a string for single selection, an array when multiselect=true. Action runs when the prompt is accepted and can consume that variable. Filetypes is declared ARRAY but shown as a string in examples; use an array. Cancel callbacks and the value left after cancellation are not documented.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `canchoosefiles` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/opendialog/#property-canchoosefiles) |
| `canchoosefolders` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/opendialog/#property-canchoosefolders) |
| `filetypes` | Properties | ARRAY | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/opendialog/#property-filetypes) |
| `folder` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/opendialog/#property-folder) |
| `prompt` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/opendialog/#property-prompt) |
| `message` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/opendialog/#property-message) |
| `multiselect` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/opendialog/#property-multiselect) |
| `setvariable` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/opendialog/#property-setvariable) |
| `action` | Properties | ACTION \| ARRAY | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/opendialog/#property-action) |

## Related local references

- [Package index](../../INDEX.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
