# Working Group on Model Development

To implement the goals in the [roadmap](https://)


**Overview:** [Econ-ARK](https://econ-ark.org/) is developing a
[*modeling language*](https://ampl.com/wp-content/uploads/amlopt.pdf)
for representing dynamic structural models. This memo summarizes what
we've done so far and what we aim to do next.

**What Econ-ARK Has Done:** Our progress since founding in 2016 is
summarized here. Our primary software output is
[HARK](https://github.com/econ-ark/HARK), a Python package for solving
and simulating heterogeneous agents (HA) macroeconomic models.

-   HARK is a framework for HA models that makes it easy to add or
    change *ex ante* heterogeneity among agents, in both infinite
    horizon and lifecycle frameworks.

-   You can install it from the command line (`pip install econ-ark`) or
    see a gentle introduction
    [here](https://econ-ark.org/materials/gentle-intro-to-hark/).

-   Includes [representations of
    variations](https://docs.econ-ark.org/Documentation/reference/index.html)
    on the canonical consumption-saving problem, including: shocks to
    marginal utility of consumption, a second consumption good with
    random marginal utility, aggregate productivity shocks, an exogenous
    discrete state, endogenous labor supply, portfolio allocation,
    non-normalizable income processes, etc.

-   Also has a
    [framework](https://docs.econ-ark.org/Documentation/reference/tools/core.html#HARK.core.Market)
    for representing (and solving for) aggregative equilibrium, using a
    generalized Krusell-Smith-style algorithm.

-   Can be used for structural micro as well, e.g. [endogenous pricing
    of health insurance](http://www.mnwhite.org/DynInsSelPaper.pdf).

-   Has
    [tools](https://github.com/econ-ark/HARK/blob/master/HARK/dcegm.py)
    for discrete-continuous choice models, with an [example
    implementation](https://econ-ark.org/materials/endogenousretirement/).

-   Recently begun
    [integrating](https://docs.econ-ark.org/examples/ConsNewKeynesianModel/SSJ_example.html)
    with the [SSJ
    toolkit](https://github.com/shade-econ/sequence-jacobian) to enable
    analysis of (e.g.) HANK models in HARK.

-   Models are [*documented* to
    explain](https://docs.econ-ark.org/Documentation/reference/ConsumptionSaving/ConsRiskyAssetModel.html#HARK.ConsumptionSaving.ConsRiskyAssetModel.IndShockRiskyAssetConsumerType)
    what they mean/do, but these equations (etc) are not *encoded* in
    HARK itself. *That's what we're going to change with this grant.*

Econ-ARK has also designed the
[REMARK](https://github.com/econ-ark/REMARK) structure for archiving
research projects and reproductions of other papers that use HARK. *This
grant application is not about REMARKs.* You might be interested in the
reproductions of Jeppe Druedahl's
[guide](https://econ-ark.org/materials/durableconsumertype/) to
non-convex consumption-saving models, the [deep learning
method](https://econ-ark.org/materials/deep-learning-euler-method-krusell-smith/)
from Maliar, Maliar, & Winant (2018), and Alan Lujan's $\text{EGM}^n$
[method notebook](https://econ-ark.org/materials/sequentialegm/).

**What We're Trying to Address:** In broad terms, our organizational
focus is on reproducibility and robustness in economic research. We
don't think there's a "replicability crisis" *per se* (at least, not
yet), but we want to address the following significant issues related to
replicability:

-   Exact model specifications, and especially computational and numeric
    details of the solution and/or estimation method, are not well
    communicated in published research.

-   Dependency of economic conclusions on obscure arbitrary choices
    (e.g., approximation gridpoints)

-   Implementation details might be in online appendix, or only in the
    code itself.

-   Impact of these details on conclusions is not really probed in the
    refereeing process.

-   Reproducing or replicating someone else's project often "starts from
    zero".

-   There is no easy way to directly compare two implementations of the
    same project or idea, and even verifying that two things are
    tackling "the same" problem is difficult.

**What We're Going to Do:** Econ-ARK's proposed solution is a new scheme
for unambiguously specifying both the precise mathematical structure of
a model *and* the methods and approximations used to numerically solve
the model and generate output from it.

-   A lot like [DYNARE](https://www.dynare.org/) for a (much) wider
    class of models: feature set broad enough to be used for HA macro,
    dynamic structural microeconomics, industrial organization, etc.

-   DYNARE model file contents are strictly informed by DYNARE solution
    capabilities: can only specify model features that the package is
    capable of handling.

-   New modeling language *not* tied to any particular software. Meant
    to be common/shared way to precisely represent models *across*
    solution methods or software packages.

-   Large feature set informed by *iterative feedback from working group
    of experts* in the field. If language can't describe a feature they
    want, then it needs to expand.

-   Will *organize a workshop to present preliminary version* of the
    language to a working group and solicit feedback. Funding for this
    event is requested in the grant.

-   HARK doesn't formally represent models internally. Will develop
    model specification for HARK to inform language design. *This will
    not restrict the modeling language*.

-   Language will have explicit separation of representation of the
    "pure mathematical" or "Platonic ideal" model vs computational
    implementation.

-   This grant application is to make HARK "language compatible" as
    groundwork, establish working group, begin developing modeling
    language, and hold workshop.

-   *Completing* development of the language exceeds scope of this
    grant. We have ambitious future plans for what can be done with the
    modeling language.

**What We Want to Accomplish:** There are several potential upsides that
we hope to achieve with this project, some of which we have explicitly
discussed with you. Your letter need not advocate for the proposal, but
feel free to use any of these points if you want.

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
