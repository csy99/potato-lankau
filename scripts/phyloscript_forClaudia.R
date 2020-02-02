library(ape)
library(phytools)
library(picante)
library(reshape2)

#first we import our phylogenetic tree 
denovotree = read.tree("denovotree.newick")

#for convenience, we convert tip labels to a character string
newtiplabel = paste("X.",denovotree$tip.label,sep="")
denovotree$tip.label <- newtiplabel

#remove any ASVs from the tree that do not correspond to ASVs found in our rarefied community matrix
potatorar = read.csv("potatorar_forsubmission.csv")
potato2 = potatorar[,-1]
rownames(potato2) <- potatorar[,1]
potato2 = potato2[,order(colnames(potato2))]


pruneddenovotree = prune.sample(potato2, denovotree)

#to extract trees representing the bacterial taxa present in a given community
# for instance, for community 1 (field CF1)
#first, get rid of any taxa columns that have 0 sequences in this particular community
# comm1 = potato[1,]
comm1 = potato2[1 , ]
comm1 = comm1[colSums(comm1)>0]
prunedtreecomm1 = prune.sample(comm1, denovotree)


#there is probably a much more elegant way to do this, and then repeat for all of the different communities
#but I am not very good at coding in R (or anywhere for that matter)

#traditional phylogenetic diversity metrics

pdall = pd(potato2,pruneddenovotree, include.root=TRUE)
phydist = cophenetic(pruneddenovotree)

a= match.phylo.comm(prunedtree, potatorar)

match.comm.dist(potato2,phydist)
mpd.result = mpd(potato2,phydist, abundance.weighted=TRUE)
mntd.result = mntd(potato2, phydist, abundance.weighted=TRUE)


