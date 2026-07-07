#let apu-red = rgb("#d71920")
#let rule-grey = rgb("#777777")
#let pale-grey = rgb("#f2f2f2")

#let report-template(title: none, body) = {
  set document(title: title)
  set text(
    font: "Times New Roman",
    size: 12pt,
    lang: "en",
    region: "GB",
  )
  set page(
    paper: "a4",
    margin: (
      left: 1.5in,
      right: 1in,
      top: 1in,
      bottom: 1in,
    ),
    numbering: none,
  )
  set par(
    justify: true,
    leading: 0.5em,
    spacing: 0.55em,
    first-line-indent: 0.5in,
  )
  set heading(numbering: "1.1")
  set figure(gap: 0.7em)

  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    block(above: 0pt, below: 12pt)[
      #set text(size: 14pt, weight: "bold")
      #it
    ]
  }
  show heading.where(level: 2): it => {
    block(above: 12pt, below: 6pt)[
      #set text(size: 12pt, weight: "bold")
      #it
    ]
  }
  show figure.caption: set text(size: 10pt)
  show figure.caption: set par(justify: false, leading: 0.25em, first-line-indent: 0pt)
  show outline.entry: set text(size: 11pt)

  body
}

#let field-row(label, value) = (
  [#strong(label)],
  [#value],
)

#let report-quote(body) = block(
  width: 100%,
  inset: (left: 12pt, right: 12pt, top: 8pt, bottom: 8pt),
  stroke: (left: 2pt + apu-red),
  fill: pale-grey,
)[
  #set par(first-line-indent: 0pt, spacing: 0pt)
  #emph(body)
]

#let reference-entry(body) = block(
  below: 0pt,
  inset: (left: 0.5in),
)[
  #set par(
    justify: false,
    leading: 0.5em,
    spacing: 0pt,
    first-line-indent: 0pt,
  )
  #h(-0.5in)#body
]

#let compact-table(body, size: 9pt) = {
  set text(size: size)
  set par(
    justify: false,
    leading: 0.2em,
    spacing: 0pt,
    first-line-indent: 0pt,
  )
  body
}

#let front-header = context [
  #set text(size: 9pt, fill: rule-grey)
  CT046-3-M-AML
  #h(1fr)
  Applied Machine Learning
]

#let main-header = context [
  #set text(size: 9pt, fill: rule-grey)
  CT046-3-M-AML
  #h(1fr)
  GPA Change Prediction
]
