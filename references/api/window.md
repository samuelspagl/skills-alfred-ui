# Window

[Official source](https://www.alfredapp.com/help/alfredui/window/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Put this object under `window`; `root` contains the component hierarchy, preferably a view. External size defaults to 800×600; inside Alfred, width follows the theme and height can follow content. `minsize` and `maxsize` bound dimensions; no defaults are stated for them. `movablebybackground` defaults differently: false externally, true inside Alfred. `borderless` removes the title and disables toolbar options while enabling window corner rounding. A toolbar is created by configuring `toolbar`; full-size content can extend behind it. `frameautosave` is external-only and keyed by package location. Window resizing and button availability are separate flags. `level` is an AppKit NSWindowLevel integer; no supported-range guarantee is given. Functions: `close` closes this window, `zoom` maximizes, `minimise` minimizes. Use `finish` to return workflow output. The prose describing `dark` mistakenly says light; the enum itself is documented, its prose conflicts.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `root` | Properties | OBJECT | Required | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-root) |
| `id` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-id) |
| `title` | Properties | STRING | Recommended | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-title) |
| `blur` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-blur) |
| `movablebybackground` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-movablebybackground) |
| `level` | Properties | INTEGER | Default: 0 | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-level) |
| `appearance` | Properties | ENUM | Default: "automatic" | "automatic", "light", "dark" | [§](https://www.alfredapp.com/help/alfredui/window/#property-appearance) |
| `size` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-size) |
| `size.width` | Properties | INTEGER | Default: 800 , Range: 50-10000 , Optional when running UI inside of Alfred | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-size-width) |
| `size.height` | Properties | INTEGER | Default: 600 , Range: 50-10000 , Optional when running UI inside of Alfred | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-size-height) |
| `minsize` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-minsize) |
| `minsize.width` | Properties | INTEGER | — | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-minsize-width) |
| `minsize.height` | Properties | INTEGER | — | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-minsize-height) |
| `maxsize` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-maxsize) |
| `maxsize.width` | Properties | INTEGER | — | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-maxsize-width) |
| `maxsize.height` | Properties | INTEGER | — | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-maxsize-height) |
| `borderless` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-borderless) |
| `closeable` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-closeable) |
| `minimisable` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-minimisable) |
| `resizeable` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-resizeable) |
| `fullscreenable` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-fullscreenable) |
| `fullsizecontentview` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-fullsizecontentview) |
| `frameautosave` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-frameautosave) |
| `titlevisibility` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-titlevisibility) |
| `titlebarappearstransparent` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-titlebarappearstransparent) |
| `toolbar` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-toolbar) |
| `toolbar.type` | Properties | ENUM | Default: "unified" | "unified", "unifiedcompact" | [§](https://www.alfredapp.com/help/alfredui/window/#property-toolbar-type) |
| `padding` | Properties | INTEGER | Default: 0, Range: 0-32 | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-padding) |
| `cornerradius` | Properties | INTEGER | Default: 0, Range: 0-128 | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-cornerradius) |
| `close` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-close) |
| `zoom` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-zoom) |
| `minimise` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/window/#property-minimise) |

## Related local references

- [view Component](components--view.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
