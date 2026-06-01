# Citations and Bibliography in Typst

## Bibliography Setup

```typst
// At the end of the document
#bibliography("references.bib", title: "References")

// With explicit style
#bibliography("references.bib", style: "apa")

// Multiple bib files
#bibliography(("refs1.bib", "refs2.bib"))
```

## Citation Forms

`@key` is shorthand for `#cite(<key>)`. Both produce the `"normal"` form (rendering depends on the active citation style; for APA, this is parenthetical).

```typst
// Normal (default): renders as "(Atz, 2022)" in APA style
@atz2022
#cite(<atz2022>)

// Narrative/prose: renders as "Atz (2022)"
#cite(<atz2022>, form: "prose")

// Author only: renders as "Atz"
#cite(<atz2022>, form: "author")

// Year only: renders as "2022"
#cite(<atz2022>, form: "year")

// Full entry (mimics bibliography format)
#cite(<atz2022>, form: "full")

// Suppress inline display but include in bibliography
#cite(<atz2022>, form: none)
```

## Supplements (Page Numbers, Chapters)

```typst
// With @key syntax
@atz2022[p.~7]

// With #cite
#cite(<atz2022>, supplement: [p.~7])
```

## Common Patterns

```typst
// Narrative citation in a sentence
#cite(<atz2022>, form: "prose") argues that...

// Parenthetical at end of clause
...as shown in prior work @atz2022.

// Multiple sources
...documented across fields @atz2022 @jones2023.
```

## Available Styles

Typst supports CSL (Citation Style Language) files. Common built-in styles:

- `"apa"` - APA 7th edition
- `"chicago-author-date"` - Chicago author-date
- `"chicago-notes"` - Chicago notes and bibliography
- `"ieee"` - IEEE
- `"mla"` - MLA

```typst
// Use a custom CSL file
#bibliography("refs.bib", style: "custom-style.csl")
```

## Anti-Patterns

| Avoid | Prefer | Reason |
|-------|--------|--------|
| Manual reference lists | `#bibliography()` | Automatic formatting |
| `@key` for narrative cites | `#cite(<key>, form: "prose")` | Correct rendering |
| Hard-coded citation text | `#cite()` with appropriate form | Style-independent |
