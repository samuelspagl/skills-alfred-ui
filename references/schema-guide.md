# Schema guide

## Three different kinds of schema

1. **Documented declarations** in `schemas/documented-api.json` and the API reference tables: a factual inventory of source property blocks, nesting, declared types, getter markers, defaults, ranges and values. Repeated shared/layout declarations remain repeated where the official pages repeat them. The 368 entries include functions; they are not 368 unique setter properties.
2. **Object structure explained in prose/examples**: for example the root window, file pseudo-component, arbitrary maps, array element types, and picker getter shape. These are explained in the relevant pages and supplementary notes below.
3. **Unofficial authoring JSON Schema** in `schemas/alfredui.schema.json`: Draft 2020-12, with a root reference to ui-json and reusable `$defs`. It is an aid, not an Alfred-provided schema or a complete runtime validator.

All relative links below are relative to this reference folder. Consult the [source manifest](sources.json) and per-field source anchors for provenance.

## Reading the tables

- Dot paths express nesting, not necessarily literal JSON keys. `items.text` describes each picker item; `post.uid` describes each posted notification. In contrast, dataview row keys such as `name.text` are literal dotted keys.
- Missing Required, default, range or getter markers mean **unspecified**, not optional in every context, false, zero, unlimited, or getter-capable.
- Recommended differs from Required. Contextual requirements include border region, flex grid, and sheet id when Escape closing is disabled.
- STRING and BOOL map to JSON string and boolean; INTEGER to whole numbers; DOUBLE to numbers. ENUM values are listed per property. Custom types point to their dedicated pages.
- Numeric ranges describe Alfred's clamping behavior. The authoring schema preserves them in `x-declaration`; it deliberately does not turn every clamping range into a validation rejection.
- Function rows are executable names, not settable JSON fields.
- Getter type can differ from setter type. Picker `selected` is set with a string but read as an object with text/value.
- Some null support is documented in prose rather than the header, such as window action resize dimensions. Null is not universally permitted.

## Structured objects not fully represented by property blocks

| Object / location | Shape and evidence |
|---|---|
| root `window` | Window object; evidenced by [Window](api/window.md) examples, missing from the root property list |
| root `variablesconfig` | name → per-variable configuration object; [Variables](api/variables.md) |
| `variables` | name → JSON value; structured values supported by [Placeholders](api/placeholders.md) |
| root `templates` | name → reusable component object; [Templates](api/templates.md) |
| root `colours` | name → COLOUR string; [root configuration](api/ui-json.md) |
| view `components` | array of component objects; whole-value file placeholders can expand into component objects |
| picker `items` | array of objects with type/text/value; selected getter returns text/value object |
| basic provider `src` | array of arbitrary objects; uid reserved; dotted keys address cell properties |
| cell `init` / `selected` | maps from dotted component/property keys to values |
| provider replace `srcmap` | uid → replacement row object |
| update `ids` | component id → partial property object |
| replace `ids` | component id → replacement component object |
| insert `ids` | parent view id → array of component objects |
| functions `ids` | component id → function name or array of names |
| notification `post` | one notification object or array of objects |
| shared `menu` / submenu | array of MENU item objects; popupmenu examples also use this array |
| `action` fields | ACTION object or action array where declared |
| template `params` | parameter-name → supplied value; exact permitted value-type constraints unspecified |

## Authoring schema boundaries

The schema models nested objects, enums, component selection, shared properties, action/event types, key reference relationships, and explicit required fields. Some facts evidenced only in prose are annotated. It allows unknown properties, so it **will not catch every misspelling**. That is intentional: the documentation does not define an unknown-key rejection policy and is incomplete in places.

Whole-placeholder strings are broadly accepted in property positions to support preprocessed authoring JSON. This is more permissive than the actual context-specific placeholder rules: acceptance does not authorize `{value:...}` in arbitrary fields or Pulse arguments. Composed placeholders inside enum/numeric fields may not be meaningfully validated before expansion. The schema does not execute preprocessing, resolve files, expand templates, query UI getters or simulate layout.

It does not enforce all contextual requirements, globally unique ids, dynamic target existence, layout capacity, array-string element types wherever unspecified, data uid semantics, platform availability, all command modes, supported getters/functions, or asynchronous ordering. Update payloads remain partial objects and are not validated as complete replacement components. A pulse reconfiguration response can omit src; the generic full pulse definition is not suitable for validating that partial update without adjustment.

Use the property inventory and [uncertainties](uncertainties.md) for the faithful declaration record. Use Alfred itself for runtime behavior.
