# Data

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

## Description of data (meeting 1/29)

- 13 fields on the exploratory data (2015)
- 13 different fields on the confirmatory data (2017)
- From each field, a sample of soil was extracted and from this sample, bacterial counts were measured (and also different diversity indeces)
- Then, soil sample was divided in two experiments: low and high nutrients. In each experiment, three plants were grown
- After X time, yield was measured

Separately:
- For each of the fields (13 in 2015, 13 different ones in 2017), soil sample was extracted, and measures of bacterial composition were obtained
- Three plants were planted per field, and after X time, disease severity was measured

### Notes
- For each field and type of experiment, we only have mean and sd for yield (not the values for the three plants)
- We believe that there is no measure of bacterial composition after the experiment

### Questions to ask Lankau group
- How was "yield" measured?
- How was "disease severity" measured?
- Would it be possible to have the measures for the three plants (instead of only mean/sd)?
- Was bacterial composition measured after experiment?
- Are we concerned that there seem to be huge differences in yield between 2015 and 2017? Other causes like rain/weather? Maybe we do not care if we study datasets separatedly

- How do clade richness and diversity relate to the bacteria information? In another word, how do we know which types of bacteria are in which clades (based on units distance from the tree root)?
- How to define between the broad and fine phylogenetic scales?
- Would the nutrients also increase the bacteria diversity so the plant outcomes might result from higher diversity? 


# Analyses

Next steps: We want to fit statistical/machine-learning models to accomplish two tasks:
- feature selection: identify soil characteristics associated with plant growth/disease
- prediction: for a given new soil, can we predict whether the plant will grow/be sick?

Methods:
- regression (we need to explore penalized regression because we have more features than individuals)
- random forest
- neural networks
- ...
