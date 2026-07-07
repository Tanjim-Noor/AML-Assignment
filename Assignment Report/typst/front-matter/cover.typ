#import "../metadata.typ": *
#import "../template.typ": *

#align(center)[
  #image("../../assets/apu-logo.jpg", width: 4.6cm)
  #v(0.2cm)
  #text(size: 14pt, weight: "bold")[ASIA PACIFIC UNIVERSITY OF TECHNOLOGY & INNOVATION]
  #v(0.65cm)
  #text(size: 18pt, weight: "bold", fill: apu-red)[#assessment-type]
]

#v(0.45cm)

#table(
  columns: (1.15fr, 2fr),
  align: (left, left),
  inset: (x: 8pt, y: 7pt),
  stroke: 0.5pt + rule-grey,
  fill: (x, _) => if x == 0 { pale-grey },
  ..field-row([Module code], module-code),
  ..field-row([Module name], module-name),
  ..field-row([Intake code], intake-code),
  ..field-row([Hand-out date], handout-date),
  ..field-row([Hand-in date], handin-date),
  ..field-row([Weightage], weightage),
  ..field-row([Student name], student-name),
  ..field-row([Student ID], student-id),
)

#v(0.55cm)

#align(center)[
  #text(size: 14pt, weight: "bold")[#report-title]
]

#v(1fr)

#block(
  width: 100%,
  inset: 10pt,
  stroke: 0.5pt + rule-grey,
)[
  #set text(size: 9.5pt)
  #set par(justify: false, leading: 0.25em, first-line-indent: 0pt, spacing: 3pt)
  *Instructions to candidates*

  - Submit the assignment through Moodle.
  - Support answers with references cited in APA 7th edition style.
  - Late submission receives zero unless Extenuating Circumstances are upheld.
  - Plagiarism cases will be penalised.
  - A minimum overall mark of 50% is required to pass the module.
]
