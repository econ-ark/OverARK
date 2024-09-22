# Working Group on Modeling Language Development

## [Econ-ARK](https://econ-ark.org/) is developing a
[*modeling language*](https://ampl.com/wp-content/uploads/amlopt.pdf)
for representing dynamic structural models. 

An essential requirement for this plan to be successful is that we draw on the wisdom of experts in the profession who can provide us with feedback and constructive criticism as our plans evolve.

-   Will *organize a workshop to present preliminary version* of the
    language to a working group and solicit feedback. Funding for this
    event is requested in the grant.

-   HARK doesn't formally represent models internally. Will develop
    model specification for HARK to inform language design. *This will
    not restrict the modeling language*.

-   Language will have explicit separation of representation of the
    "pure mathematical" or "Platonic ideal" model vs computational
    implementation.

-   Economics is not immune to "failure to replicate," and the reasons
    can be subtle. There are well-known examples papers in top journals
    whose results were reversed by due to issues with numeric methods.

-   Frontier models have features that make solution not "well behaved"
    (e.g. discrete-continuous choice). "Most interesting" papers might
    be most susceptible to hard-to-detect numeric complications.

-   Even without any new software, a common format for representing
    choices about numeric integrals, discretized state spaces, etc is a
    big step in the right direction.

-   Greatly reduces burden on reader / evaluator to understand what was
    *actually done*-- the *first prerequisite* to independently
    reproducing the work.

-   Some top journals use a ["data
    editor"](https://www.econometricsociety.org/publications/es-data-editor-website)
    who tries to reproduce results in accepted papers, using the
    authors' own files. Reproduces paper results; does *not* address
    robustness.

-   "Robustness checks" in refereeing focus on model specification, not
    numeric details.

-   Systematic representation / documentation of computational methods
    (etc) could make it feasible to *actually* investigate whether and
    how "hidden choices" affect conclusions.

-   There is no "standard software" in structural modeling, nor standard
    *anything*. Other than well known numeric packages (`numpy`,
    `lapack`), researchers hand code everything.

-   Some economists publish toolkits for solving particular types of
    models or handling a specific method, but there's no commonality
    among them or way to link them.

-   Some software tools are "inherited" from adviser or coauthors; need
    to be an "insider".

-   Some overlap among toolkit capabilities. How does their output
    compare when given *exact same* problem? Currently no easy way to
    specify "exact same".

-   Includes AI / deep learning platforms not specifically designed for
    economics.

-   Common platform for interacting with multiple toolkits would
    accelerate research.

-   Economists are independent and opinionated. The kinds of economists
    who will be invited to the workshop have strong opinions about the
    topic and want to be included.

-   Dynamic models are diverse, many with some "unusual" feature. It
    would not be reasonable for a small team to "get everything"
    *without significant outside feedback*.
