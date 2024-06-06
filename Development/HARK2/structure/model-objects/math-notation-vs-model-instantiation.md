# What Should Be The Strucutre of an Interval...

## 20240606-update

Lets call our object for an interval "mything"

Desiderata:
- structure _independent_ of the code that creates it ...
  - ... and can therefore be modified by any "external" code
  - even, say, Julia or (god forbid) FORTRAN
  - ideally, all of the structure should be easily transportable
	- into Julia, say
	- so as to make structures easily representable by standards
	- e.g., sympy compatible math
- It has multiple components which can be constructed individually
  - Pure math: mything.math?
	- contains ranges, domains, other abstract things
	- example: trans shock \theta is a mean-one truncated lognormal
		- define the names of the parameters thetaMin, thetaMax, thetaVar, etc
  - Abstract description of approximations
    - mything.approximators
	  - example: we're approximating the \theta distn with n equiprobable gridpoints
	  - want to allow multiple choices here, so people can compare
  - Concrete numerical specs of approximators
    - e.g., in the equiprobable, n=7
  - Stuff we build - like approx solutions, value funcs, etc
    - mything.bilt (all my names are negotiable)


Below is the earlier text:

Here's a proposal, which we might think of as an augmented version of Alan's Blocks.

Here, I'm using `Interval` to distinguish my object from Alan's `Block`

To address up front an objection that I anticipate: 'If we are solving an infinite-horizon problem it is silly to build machinery for keeping track of multiple distinct intervals, because every period will be the same.'

My response is that
- even an infinite horizon problem must be solved from some starting point that is not (yet) the solution
- in debugging those solutions, it is likely to be useful to have the sequence of improving guesses
- once the problem has reached convergence, you can throw out the history

Furthermore, solving infinite horizon problems using the SSJ toolbox actually requires you be able to anticipate the consequences of an MIT shock many periods into the future.

I continue to think that, as part of our theme that we are NOT doing MDP's but rather Bellman problems, we explicitly attach everything we construct to objects we call value functions. So, in particular, the decision rules would be obtained by `vFunc.dr`.  Partly this is to guarantee that decision rules and other things that are consistent with or derived from the value function do not accidentally get detached and moved to some place where some other value function is relevant.

At a minimum, each interval must have a `vFuncBegPrd` and a `vFuncEndPrd`.  It might also have some content in between:

```
>>> interval_generic
[vFuncBegPrd,{vFuncMid,}vFuncEndPrd] 
```
where the {} indicate that `vFuncMid` is optional.

```
>>> interval_generic['vFuncMid']
[{list of objects}]
```

```
>>> interval_generic.solve()
>>> dir(interval_generic.vFuncMid)
{ results include the fact that there is a decision rule `vFuncMid.dr` }
```

Between `vFuncBegPrd` and `vFuncEndPrd` the first possibility for `{objects}` is the possibility that it might be a sequence of 'stages' (possibly a sequence of length 1, because the agent might have only one problem to solve). To the stage solutions, I propose that we do _not_ attach a continuation value function or use Matt's linkage machinery; instead, we always assume that `vFuncEndStg` is always the `vFuncBegStg` of the succeeding object (and that the succeeding object for the last stage is in the `vFuncEndPrd` of the interval that contains the stages). Also, `vFuncBegPrd` should automatically `get` the `vFuncBeg` of the first item in the `{objects}.`  This will be the last step of the solution of the `interval`.

Each of the stages must have a `vFuncBegStg` and may (or may not) have a `vFuncMidStg` in which a decision problem is solved.

One key difference between intervals and stages is that no calendar time elapses during the steps of a stage or as a result of a transition from one stage to the next in a problem.  Whereas between one interval and the next we take care of everything that has to do with time.

We will want to prohibit embedding intervals in stages, because an interval requires the passage of time and stages prohibit the passage of time.

But we can allow embedding of intervals in intervals, to any arbitrary degree of nesting. So we might have a structure like:

```
interval_year = [vFuncBegYr,[interval_qrtr1,interval_qtr2,interval_qtr3,interval_qtr4],vFuncEndYr]
interval_qrtr = [vFuncBegQtr,[interval_mnth1,interval_mnth2,interval_mnth3],vFuncEndQtr]
```
and on down as far as we like.

This has the convenient structure that when solving an interval, the solver can crawl backwards by beginning with the last item in `[{objects}]` and then the last item in any embedded objects and so on; then when it has solved backwards all the `[{objects}]` in the bottom turtle, it moves back up one turtle and ... so on.  It is similarly convenient when moving forward for the purposes of simulation.

This should all work with the notation in my SMDSOPs lecture notes. 

There remains the question of how someone might retrieve the items that are embedded in this `interval` object.

Let's start with the complicated case in which in the interval the agent solves the portfolio choice problem followed by the consumption problem. How about something like:

```
>>> interval.subproblem['shrFunc'].dr
{python's description of the object}
```

```
>>> interval.subproblem['cFunc'].dr
{python's description of the object}
```

And how about the case with subintervals instead of stages?  If, say, they wanted the sequence of monthly problems in of the third quarter,

```
>>> qrtr3=interval.subproblem['qrtr'=3]
{python's description of the object}
```

```
>>> qtr3mnth2=qtr3['mnth'=2]
{python's description of the object}
```

```
>>> qtr3mnth2=qtr3['mnth'=2]
{python's description of the object}
>>> type(qrtr3mnth2)
{its an interval object}
>>> qtr3mnth2.subproblem['shrFunc']
{python's description of the shrFunc}
>>> qtr3mnth2.subproblem['cFunc']
{python's description of the cFunc}
```

This seems rather painful, but remember that at present we are only really talking about establishing a solid foundational structure for our problems.  If they have a good structure, it should be relatively easy to write more user-friendly tools that just know how to do the more intricate things.  So, it would be easy enough to write some code that would know that 'Aug' is the 2nd month of third quarter, and then to allow the person to interact with a suitably structured `interval` using something like 

```
>>> interval.get(what='cFunc',month='Aug')
```


# Mathematical Representation

One of our goals is to have a complete mapping between the mathematical representation and the computational instantiation of our models, I want to work hard (and jointly) on the math notation and the computational objects.  In my experience, writing up the math often brings to mind important points that otherwise might be missed.

For that purpose, here are direct links to relevant sections of my https://llorracc.github.io/SolvingMicroDSOPs notes:

[notation](https://llorracc.github.io/SolvingMicroDSOPs-Public/#moves)

[multiple-control-variables](https://llorracc.github.io/SolvingMicroDSOPs-Public/#multiple-control-variables)

[the-usual-theory](https://llorracc.github.io/SolvingMicroDSOPs-Public/#the-usual-theory)

