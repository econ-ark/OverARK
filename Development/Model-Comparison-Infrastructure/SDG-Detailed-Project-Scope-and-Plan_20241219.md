# SDG Detailed Project Scope and Plan

The purpose of this project is to develop infrastructure that will let us systematically compare alternative computational solutions to "the same" model
- The marquee comparison will be for the Krusell-Smith model:
    - Specifically, the comparison will be between 
        - the Maliar, Maliar, and Winant deep learning solution
            - which is already implemented as a REMARK (see below)
        - the two other solutions that are (also) already available in the econ-ark ecosystem
- The comparison infrastructure should be developed with an eye to generality
    - That generality will be demonstrated by applying the infrastructure to another problem
        - Because of its simplicity, the other solution will be to the Aiyagari model

The steps to accomplish these goals need to be taken in the order in which they are outlined below
- With a check-in stage between the headers before proceeding to the next
    - If we are not agreed on the prior steps, later work will likely be wasted effort

## Step: Inventory Existing Solutions
- These are the solutions I know of 
  - **Aiyagari Model**:
    - Adam Edwards (last year)
        - [EdwardsA](https://github.com/Adam-Edwards-JHU/Aiyagari1994QJE)
    - Compare it with the solution produced by Zixuan Huang and Mingzuo Sun:
        - [HuangZ-SunM](https://econ-ark.org/materials/aiyagari)
  - **Krusell-Smith Model**:
    - Marc Maliar's: "Deep-Learning Code for Solving Krusell-Smith Heterogeneous-Agent Model."
        - [Kruesll-Smiath/MaliarM](https://econ-ark.org/materials/deep-learning-euler-method-krusell-smith/)
    - Matt White's replication using the HARK toolkit
        - [Krusell-Smith/mnwhite](https://github.com/econ-ark/KrusellSmith/)
    - The SSJ implementation by Will Du
        - [Krusell-Smith/SSJ](https://github.com/econ-ark/HARK/blob/master/examples/ConsNewKeynesianModel/KS-HARK-presentation.ipynb)
    - The DARKOLO solution:
        - [KrusellSmith/Darkolo](https://github.com/econ-ark/DARKolo/tree/master/chimeras/KrusellSmith)
- Do a thorough search of the Econ-ARK resources to see if there are other solutions to either of these
    - Use AI's with questions like:
        - "Are there examples of the Krusell-Smith model solved using the Econ-ARK/HARK toolkit"

## Step: Update Models

Ensure the above models
- run correctly as they stand
    - if so, update them as needed to integrate with the current HARK toolkit and DOLO frameworks
- are broken somehow
    - if so, then investigate whether it is easy or hard to fix them

## Step: Take Stock of Solutions
- For each inventoried item, recommend whether to keep it in the comparison set
- If you can't get it to work, the answer will be no
- If you can get it to work, the answer might still be no
    - If it does not contribute much
- There should be at least three solutions in each comparison set
    - If a third version of Aiyagari is needed, use 
        - [Aiyagari/QuantEcon](https://python.quantecon.org/aiyagari.html)

## Step: Take Stock of Error Metrics
- Familiarize yourself with and reproduce error metrics:
  - For **Krusell-Smith**:
    - Use the metrics defined by Maliar, Maliar, and Winberry (MMW, 2021) in Section 5 of their paper.
    - Compare the following methods using appropriate metrics
        - [SSJ (using HARK toolkit)]((https://github.com/econ-ark/HARK/blob/master/examples/ConsNewKeynesianModel/KS-HARK-presentation.ipynb)
)
        - [Original Krusell-Smith method (existing EconArk replication)](https://github.com/econ-ark/KrusellSmith/)
        - [MMW (using Marc Maliar's REMARK)]((https://econ-ark.org/materials/deep-learning-euler-method-krusell-smith/))
  - For **Aiyagari**:
      - Examine the literature citing Aiyagari's paper
      - Determine the metrics most commonly used to compare a new solution to the original

## Step: Development and Implementation
- Implementation and testing of `ModelComparison` Class
- Instance of a `ModelComparison` class will take in 
    - economic parameters and 
    - parameters and specifications (grid size etc.) for the solutution method of a model and:
    -  Generate outputs for the solution methods identified (and implemented) as above. 
- If required, revise the `ModelComparison` class specification below. 
This ends the set of sequential steps that need to be taken.

The remainder of this document fleshes out some details of the implementation

# `ModelComparison` Class Specification 

## Objective

Develop a class to compare different solution methods for heterogeneous agent models. 

Note: The objective is NOT to develop a different or improved or symbolic representation of the problem. That is another workflow

The class will:
1. Accept an input that is a Markdown document
   - That document should be a brief description of the models being compared
3. Accept model parameters, including preferences, shocks, and production functions:
   - **Preferences**: Discount rate, risk aversion, capital share, etc.
   - **Shocks**: Aggregate and idiosyncratic shock processes.
       - e.g. Transition matrix for labor productivity states
       - e.g. Transition matrix for aggregate states
   - **Production**: Capital share, depreciation, and TFP processes.
   - Anything else that defines the mathematical structure of the problem
       - For example, the serial correlation coefficient for the income growth process
       - The initial distribution of agents
   - These should be specified as a "single source of truth"
   - The existing solutions need to be rewritten
       - to guarantee that they obtain these configurations from the ModelComparison class
4. Solution-method-specific paramters
   - **Solution Method Parameters**: 
       - Krusell-Smith: e.g., Number of moments, number of agents
       - HARK: assumptions about grid structure
       - MMW: Neural network configurations
           - layers
           - number of neurons per layer
           - basis functions: ReLu, etc?
5. Provide solutions using multiple methods:
   - **Krusell-Smith Method**: 
       - As implemented in HARK
   - **MMW Methods** (see Section 4 for Maliar Maliar and Winant (2021))
     - Euler-equation-based deep learning.
     - Bellman-equation-based deep learning.
     - Lifetime-reward maximization using deep learning.
   - **Sequence Space Jacobian (SSJ)**
       - Distance to steady state
6. Return relevant outputs:
   - Policy functions for individual savings and consumption.
   - Aggregate dynamics (e.g., equilibrium prices, wealth distribution).
   - Metrics to compare solutions

## Key Features

### 2. Solution Methods
- **`solve(method: str)`**:
  - Solve the model using the specified method:
    - `krusell_smith/HARK`: Implements fixed-point iteration based on the original log-linear law of motion.
    - `maliar_winant_euler`: Uses deep learning to minimize Euler residuals.
    - `maliar_winant_bellman`: Optimizes the Bellman equation using a neural network.
    - `maliar_winant_reward`: Maximizes the lifetime reward with a deep-learning framework.
    - `ssj`
### 3. Simulation
- **`simulate_policy()`**:
  - Simulate the model forward using the solved policy function.
  - Generate time-series data for individual agents and aggregate variables (e.g., wealth, prices).
### 4. Outputs
- Policy functions. 
- Aggregate time-series and moments:
  - Wealth and income distributions.
  - Equilibrium factor prices ($r_t$, $w_t$).
  - Aggregate capital evolution over time.
### 5. Error Metrics

Use the metrics used by Maliar et al. (2021), including those for Euler residuals, Bellman errors, and convergence diagnostics, as appropriate for the solution method.
