- Project started on November 2019
- Members
    - Katherine Fu (Junior, CS, Stat)
    - Songyang Cheng (Junior, Information systems, CS)

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

# Songyang's Files 
- Python Scripts will be .py files
- All visualization will be .ipynb files with naming rules: week number + date
- A serious bug in work for week 3 and week 4 work has been identified in week 6. 
Thus, week 3 and week 4 work should not be cited. All analysis has been redone in week 6. 
For the sake of integrity, the buggy files are not deleted. 
## summary for each file
- w010119  
Conducted exploratory data analysis.  
Visualized the pattern for both potato yield and disease severity.  
- w020202  
Checked y distribution. Converted to normal distribution.  
Plotted correlation Heat Map for meta data and yt.  
Plotted standard deviation for each field (biological difference).  
Tried out basic random forest model.  
- w030209 (buggy)  
Plotted euclidean distance between different fields. (no bugs here)  
Tuning Random Forest models. (bugs exist in train-test split)  
- w040216 (buggy)  
Explored XGBoost models. (bugs exist in train-test split)   
- w050223
Plotted correlation Heat Map for part of (selected) meta+taxa data and yt.     
Plotted linear relationship between each selected feature and y/yt.  
- w060303
Corrected bugs in week 3 and week 4 by redoing train-test split.  
Explored PCA and Keras Auto Encoder.  
- w070319  
Explored Pair Wise Selection. 
Explored Ridge Regression.  
- w080402
Further explored Ridge Regression.  
Explored Lasso Regression.  
Visualized two best models.  
- w090408 
Visualized full model selection tree.  
- w100416
Verified the difference between Linear Regression and Ridge Regression.  
- w110506  
Created for the purpose of writing my report. Nothing new.      










