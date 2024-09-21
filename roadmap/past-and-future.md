# Econ-ARK's Plans for a Modeling Language, September 21, 2024

## **Overview** 
[Econ-ARK](https://econ-ark.org/) is developing a 
[*modeling language*](https://ampl.com/wp-content/uploads/amlopt.pdf)
for representing dynamic structural models.[^1] This document summarizes what
we've done so far and what we aim to do next.

[^1]: "Language" may not be quite the right word; the idea is closer to a specification for a standard to represent models. 

## **What We've Done So Far** 
Our primary software output is
[HARK](https://github.com/econ-ark/HARK), a Python package for solving
and simulating heterogeneous agent (HA) models, either for HA-Macro or for structural micro modeling.

-   Installable from the command line (`pip install econ-ark`)

-   Extensive [documentation](https://docs.econ-ark.org)

-   [A Gentle Introduction](https://econ-ark.org/materials/gentle-intro-to-hark/).

-   Includes [variations](https://docs.econ-ark.org/Documentation/reference/index.html)
    on the canonical consumption-saving problem, including: 
        - shocks to marginal utility of consumption, aggregate shocks, an exogenous discrete state, endogenous labor supply, portfolio allocation, and much more

-   [framework](https://docs.econ-ark.org/Documentation/reference/tools/core.html#HARK.core.Market) for representing (and solving for) aggregative equilibrium (either for the  macroeconomy or, say, for an industry), using a generalized Krusell-Smith-style algorithm.

-   Can be used for structural micro as well, e.g. [endogenous pricing
    of health insurance](http://www.mnwhite.org/DynInsSelPaper.pdf).

-   Has
    [tools](https://github.com/econ-ark/HARK/blob/master/HARK/dcegm.py)
    for discrete-continuous choice models, with an [example
    implementation](https://econ-ark.org/materials/endogenousretirement/).

-   [integration](https://docs.econ-ark.org/examples/ConsNewKeynesianModel/SSJ_example.html) with the [SSJ toolkit](https://github.com/shade-econ/sequence-jacobian) to enable analysis of (e.g.) HANK models in HARK.

-   Models are [*documented* to
    explain](https://docs.econ-ark.org/Documentation/reference/ConsumptionSaving/ConsRiskyAssetModel.html#HARK.ConsumptionSaving.ConsRiskyAssetModel.IndShockRiskyAssetConsumerType) usage and features.

Econ-ARK has also designed the
[REMARK](https://github.com/econ-ark/REMARK) structure for archiving
research projects and reproductions of other papers that use HARK. Examples include
reproductions of Jeppe Druedahl's
[guide](https://econ-ark.org/materials/durableconsumertype/) to
non-convex consumption-saving models, the [deep learning
method](https://econ-ark.org/materials/deep-learning-euler-method-krusell-smith/)
from Maliar, Maliar, & Winant (2018), and Alan Lujan's $\text{EGM}^n$
[method notebook](https://econ-ark.org/materials/sequentialegm/).

## **Problems We're Trying to Address:** 

Current practice in computational economics research impedes reproducibility, robustness, and transparency.

-   Exact model specifications, and especially computational and numeric
    details of the solution and/or estimation method, are not well
    communicated in published research.

-   Economic conclusions may hinge on obscure arbitrary choices
    (e.g., approximation gridpoints)

-   Key implementation details might be in online appendix, or only in the
    code itself.

-   Impact of these details on conclusions are usually impossible to probe in the
    refereeing and editorial processes.

-   Because it is often difficult to run someone else's handcrafted code, reproducing or replicating someone else's project often "starts from zero" (and is therefore very budensome and slow)

-   There is no easy way to directly compare two implementations of the
    same project or idea, and even deciding whether two papers are
    using "the same" model can be difficult.


## **What We're Going to Do:** 

Econ-ARK's solution is to develop a new schema for unambiguously describing the mathematical and computational structure of a model along with all details required for solution.

-   The high-level (mathematical) model description will be a lot like a [DYNARE](https://www.dynare.org/) `mod file` but capable of representing a much broader class of models (Markov decision processes, including but not limited to Bellman problems).

-   Difference in philosopy with DYNARE is that we will separate model description 
from solution methods, so that problems can be specified exactly and rigorously, independently of the solution method (or before any solution method has been devised).

-   A counterpart to the abstract model description will be a "numerics" description that surfaces all of the configurations and choices for the numerical approach used

## How We're Going to Do It

We already have a primitive sketch of what the mathematical part of such a schema might look like, building on DYNARE and [Dolo](https://pypi.org/project/dolo) 

-   Capabilities of the schema will be informed by *iterative feedback from a working-group of experts* in the field. 
    -    If the schema can't describe a feature they want, it needs to be improved.

-   We will engage with proprietors of existing toolkits
    - Make sure that the schema can represent all the things their kits can do
    - Get their feedback about additional capabilities needed

-   Comprehensively survey the existing tools available outside of economics
    - A thorough search has convinced us that none of them does what we need
    - But several have components and ideas that we will incorporate

## Why Will the World Be Better When We're Done?

-   Greatly reduces burden on reader / evaluator to understand what was
    *actually done*-- the *first prerequisite* to independently
    reproducing the work.

-   It will be possible to solve the *exact same* problem using different tools
    - For debugging
    - For accuracy and speed
    - For transparency 

-   We aim to design the schema so that it provides the information necessary to use AI / deep learning platforms not specifically designed for economics
    - Allowing comparison of these new solution methods to existing

-   Common platform for interacting with multiple toolkits would
    accelerate research.
