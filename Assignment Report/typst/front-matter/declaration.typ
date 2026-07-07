#import "../metadata.typ": *
#import "../template.typ": *

#align(center)[
  #text(size: 16pt, weight: "bold")[Declaration]
]

#v(0.8cm)

I declare that this report is my own work except where the work of others is
clearly acknowledged and cited. The submitted analysis is based on the stated
dataset and the accompanying source code and notebooks. I have not presented
this report, in whole or in part, for another academic award.

Generative-AI assistance was used for research-workflow support, code and
report review, language editing, and Typst document assembly. All literature
claims, references, notebook outputs, numerical results, interpretations, and
final wording were checked against the cited sources and the saved assignment
evidence. Responsibility for the submitted work remains with the student.

#v(1.2cm)

#table(
  columns: (1fr, 2fr),
  align: (left, left),
  inset: (x: 6pt, y: 10pt),
  stroke: (x, y) => if y > 0 { (top: 0.5pt + rule-grey) },
  [*Student name*], [#student-name],
  [*Student ID*], [#student-id],
  [*Signature*], [#line(length: 70%, stroke: 0.5pt + black)],
  [*Date*], [#declaration-date],
)
