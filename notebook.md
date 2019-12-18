## Data

Files received from Rick Lankau (email 12/18/19):
- denovotree.newick
- potatodatadictionary_forClaudia.csv
- potatometadata_forClaudia.csv
- potatorar_forsubmission.csv

We also received one script (in `scripts` folder): `phyloscript_forClaudia.R`

His explanations:

Here are some datasets to start with.
The first file (`potatodatadictionary_forClaudia.csv`) is a data dictionary explaining the meaning of all of the column headings in the following metadata file.

The metadata file (`potatometadata_forClaudia.csv`) has data on plant outcomes (tuber yields under high and low nutrients, and disease severity) for plants grown with each of the 24 different microbial communities. The values are means of three replicate pots - variances and standard errors are also included. 

The file named `potatorar_forsubmission.csv` is the bacterial community matrix. The rows are numbered according to the Field ID column in the metadata file. The column headings are the unique bacterial amplicon sequence variants (taxonomic units).

The `denovotree.newick` is the phylogenetic tree estimated from these 16S reads (hence the "denovo" in the name). At some point I will track down the actual sequence files if you want to try better means of estimating this megatree.

The `phyloscript_forClaudia.R` file is R script to import the community matrix and phylogenetic tree, and then prune the big tree down to just those tips that are represented as taxa across all of our communities. I also wrote another little bit of code to extract a sub-tree of only the microbial taxa present in any given community. I am sure there is a better way to accomplish this.




## Analyses

Next steps: We want to fit statistical/machine-learning models to accomplish two tasks:
- feature selection: identify genes associated with antibiotic-resistance
- prediction: for a given new genome, can we predict whether it will be antibiotic-resistant or not

Methods:
- regression (we need to explore penalized regression because we have more features than individuals)
- random forest
- neural networks
- ...