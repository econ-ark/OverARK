::: singlespace
Prof Christopher D. Carroll\
Wyman Park Building 590\
Johns Hopkins University\
Baltimore, MD 21211

February X, 2024
:::

\[Human\]:

In 2017, the newly founded [Econ-ARK](http://www.econ-ark.org) project
received a generous grant from the [Alfred P. Sloan
Foundation](https://sloan.org) to develop the [HARK
toolkit](https://github.com/econ-ark/HARK), a software package for
solving, simulating, and estimating heterogeneous agents models in
economics (either heterogeneous agent macro or structural micro). With
[NumFocus](https://numfocus.org/) as our fiscal sponsor, we have since
received additional funding from other sources (including the [Think
Forward
Initiative](https://inomics.com/institution/think-forward-initiative-1258337)
and [T. Rowe Price](https://www.troweprice.com/en) as a "no strings
attached" corporate sponsor) to continue the work and expand the range
of models offered in the HARK package, allowing us to largely achieve
our original set of goals. With this experience underneath our belt, we
now see that our next steps involve developing a *language* for
expressing dynamic structural models that can specify computational
methods, describe simulation procedures, and generate model output. I am
writing to you to ask whether \[organization\] might be interested in
funding this endeavor.

To fix ideas, a structural model would be formalized as a model file: a
set of statements characterizing its components, like how a budget
constraint might be captured with a simple equation saying that assets
are whatever is left of the consumer's money after consumption: `a=m-c`
(of course much more sophisticated mathematical propositions would also
be accommodated). The language (or perhaps a better term would be
schema) will provide a common format for describing dynamic structural
models convey model content in a human- and machine-readable way, but is
independent of the code to actually solve and implement the model. As we
develop the schema, we would simultaneously develop a software platform
to parse the model file into the implied code.

The [Dynare](https://www.dynare.org/) package provides a prototype
example of the *kind* of thing we have in mind, but limitations in its
syntax and specification mean that it cannot be used or extended for the
kinds of models that are now *de rigeur* in both micro and macro
modeling. When explaining our work on HARK, we have found that other
economists often interpret it through the lens of Dynare, with the hope
that we have already built "Dynare for heterogeneous agents." This has
left us no doubt that there is a large demand for exactly such a tool.
With our prior experience implementing HARK, and given recent advances
in other software tools, we are now prepared to design and create it.

Prior to beginning work on the new platform, we conducted a thorough
search of *other* academic fields, investigating whether a general
dynamic modeling schema has already been developed. Having explored all
the nooks and crannies of the internet, we are confident that there is
no comparable or related project that could be adapted or expanded for
our purposes. We found that the universe of modeling- and
optimization-adjacent software is both diverse and diffuse: We found
many of the building blocks necessary to accomplish our goal, but no
schemes for putting the building blocks together into anything like what
we need. The lack of a common platform for representing dynamic models
is akin to the lack of cohesion among the various artificial
intelligence (AI) and deep learning toolkits that have recently been
developed. Translated into that context, the AI equivalent would be a
language that described the AI problem to be solved in a
platform-independent way, allowing a user then to solve exactly the same
model with each of the competing AI tools. (The problem is even more
ambitious in that context than in ours, but what we accomplish might be
a good stepping stone toward a platform-independent AI tool.)

This work will also significantly improve the transparency and
replicability of structural economics research. Behind closed doors,
everyone who works on these kinds of models admits (and laments) what
they know to be true: Everyone's results depend on a host of ancillary
assumptions -- how many gridpoints to use, how many agents to simulate,
etc. While it is now expected that researchers will publicly archive
their code, for many projects the code might as well be written in
Klingon (so far as accessibility and transparency and replicability are
concerned). Even worse, there is no direct relationship between the
model as expressed *on paper* and the problem as solved *in code*-- the
academic refereeing system focuses deeply on the economics of the
abstract math, and relies on trust with respect to the numerics. Indeed,
there are famous examples of papers that have been published based on
their strong economic content, but whose quantitative (and sometimes
qualitative) results were later discovered to be based on errant code.

Our proposed modeling language aims to rectify these systemic issues
with the workflow of economic research. If a model specification file is
used to generate a numeric solution and model output, a reader or
evaluator can be confident that the model presented on paper matches its
execution in code. Furthermore, our language will include a format for
specifying the methods used to solve the model numerically,
transparently conveying this information alongside the "pure"
mathematical content of the model. The software platform can thus act as
a vehicle for evaluating the performance of a numeric solution to a
theoretical model.

Our proposed platform will accelerate the development of models on the
frontier of economic research, allow for the verifiability of numeric
output from such models, and improve communication and collaboration
among researchers. In addition to academic work, the platform would be
of significant use both to governments (including central banks and
financial regulators) in conducting prospective analyses of potential
policy actions, and to private financial institutions who wish to make
decisions or provide advice that is informed by a structural model
(e.g. a model of optimal retirement savings). In developing the language
and the software platform, we will seek out input from a variety
stakeholders to ensure that their modeling needs are met.

Thank you very much for your time and consideration in this matter, and
I look forward to further discussion with you.

Sincerely,

![image](CDCsignature.jpg)

Christopher D. Carroll, Professor of Economics, Johns Hopkins University
