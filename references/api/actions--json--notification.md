# notification Action

[Official source](https://www.alfredapp.com/help/alfredui/actions/json/notification/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Post accepts a notification object or an array. Each entry can provide uid, title and text. Omitted uid gets a random UUID; reusing uid replaces the previous notification. Remove accepts a uid or uid array. For external UIs, banners appear only while the window is not frontmost, but notifications are still added to Notification Centre. Permission handling and ordering between post/remove are not specified.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `post` | Properties | OBJECT \| ARRAY | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/notification/#property-post) |
| `post.uid` | Properties | STRING | Default: A random UUID | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/notification/#property-post-uid) |
| `post.title` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/notification/#property-post-title) |
| `post.text` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/notification/#property-post-text) |
| `remove` | Properties | STRING \| ARRAY | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/notification/#property-remove) |

## Related local references

- [Package index](../../INDEX.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
