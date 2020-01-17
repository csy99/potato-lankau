- Project started on November 2019
- Members
    - Katherine Fu (Junior, CS, Stat)
    - Songyang Cheng (Junior, Information systems, CS)
    - Haoming Chen (Junior, Stat, Math)

# Details data
- Data matrix $X \in R^{n \times p}$ where n is the number of plant plots, and p are characteristics of soil in plot (chemical, microbiome)
- Response $Y$: disease of plants or yield
- Type of analysis:
    - penalized regression tools ($n < p$)
    - random forest
    - neural networks

# Steps to clone the repo locally

1. In the terminal, go to the folder where you want to put the local repository using `cd`
2. Type:
```shell
git clone https://github.com/solislemuslab/potato-lankau.git
```
3. Inside this folder, create a subfolder called `data` where you will put the data. This folder is ignored in the `.gitignore` file, so nothing inside this folder will be pushed to github