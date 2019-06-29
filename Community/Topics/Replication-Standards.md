# Standards for Reproduction of Results in Computational Economics 

<!-- At the 2019 meetings of the Society for Computational Economics, a group developers of computational economics toolkits gathered to discuss problems confronting the field. -->

There is widespread agreement that an obstacle to progress in computational economics is the difficulty of replicating or reproducing computational results.

A key application of toolkits for computational economics is to provide a robust way to address this problem. A number of toolkits have collections of examples of how to reproduce or replicate the results of specific models or papers. 

The aim of this page is to define a set of standards and guidelines that should make it easier for newcomers to use toolkits in this way.

The idea is that if an example from a particular toolkit satisfies a set of criteria (certified by the developer of the example), then it should be included in a comprehensive list of reproductions that can be tracked centrally, ideally providing a "one stop shop" for people looking for a way to get started understanding either a particular paper or a particular toolkit.

Specifically, subject to further discussion and amendment by the community (feel free to propose edits!), we propose that examples of a reproduction be categorized in the following tiers:

1. Bronze:
   - Produces some useful set of computational results
1. Gold:
   - Produces all of the main computational results
1. Platinum
   - Reproduces an entire paper from source documents (LaTeX, code, etc) with all its computational results 

Our aim is to produce an automated list of examples across toolkits categorized in this way.

For an example to be included in our index, the provider should certify that a checklist of requirements has been satisfied. (Many of the requirements should be satisfiable by reference -- usually links -- to resources at the toolkit's home location).

Minimal checklist required for all tiers:
  - [ ] There is a README file that contains:
     - [ ] The necessary information to find a statement of the model being replicated (e.g., a link to a paper)
	 - [ ] The necessary information to install the toolkit tools needed by the replication
	 - [ ] A step-by-step guide to how to install the toolkit and run the replication
  - [ ] There is a logfile or other record of what a successful run of the tool produces


Checklist for gold tier:
   - [ ] Definition of what the provider considers the 'main results'
   
Checklist for platinum tier:
   - [ ] Definition of the "canonical" version being reproduced (e.g., the citation to the full publication)
   
