#import "metadata.typ": *
#import "template.typ": *

#show: report-template.with(title: report-title)

// APU assignment cover: intentionally unnumbered.
#include "front-matter/cover.typ"
#pagebreak()

// Front matter: lower-case Roman page numbers.
#counter(page).update(1)
#set page(
  header: front-header,
  numbering: "i",
)
#include "front-matter/declaration.typ"
#pagebreak()
#include "front-matter/title.typ"
#pagebreak()
#include "front-matter/abstract.typ"
#pagebreak()

#outline(title: [Table of Contents], indent: auto)
#pagebreak()
#outline(
  title: [List of Figures],
  target: figure.where(kind: image),
  indent: auto,
)
#pagebreak()
#outline(
  title: [List of Tables],
  target: figure.where(kind: table),
  indent: auto,
)
#pagebreak()

// Main matter: Arabic page numbers restart at 1.
#counter(page).update(1)
#set page(
  header: main-header,
  numbering: "1",
)
#include "sections/01_introduction_aim_objectives.typ"
#include "sections/02_related_works.typ"
#include "sections/03_methods.typ"
#include "sections/04_dataset_preparation.typ"
#include "sections/05_model_implementation.typ"
#include "sections/06_model_validation.typ"
#include "sections/07_analysis_and_recommendations.typ"
#include "sections/08_conclusion.typ"
#include "back-matter/references.typ"
#include "back-matter/acknowledgements.typ"
