# Term Clarification
- all y below refers to the disease, not yields
- meta data: data in potatometadata_forClaudia.csv
- taxa data: potatorar_forsubmission.csv
- RMSE/MSE: all root mean squared errors are calculated after transformed back to the un-normalized x and un-transformed y

# Data Preprocessing
1. X should be normalized (Utils.normaliation)
2. y should be transformed to normal distribution (Utils.johnson_transform)

# Findings
1. The richness of bacteria is negatively related to the plants' susceptibility. 
The more diverse the bacteria community is, the less vulnerable the potato is. 
2. In general, using meta data have a better prediction performance than taxa data. 
In addition, there are multicollinearity in meta data. Thus, using only part of meta data will have an even better prediction performance.
3. Even though the size of columns is much larger than that of rows, dimension reduction techniques do not work well, at least for PCA and Keras Auto Encoder. 
4. The most important measurements in meta data is "claderich0.25". The model is based on normalized x and transformed y and can be expressed as
y = -0.57154*x + -0.01467. There is a visualization for the model in the end of w080402. 
5. The most important bacterial communities in taxa data includes 
      ['X.8e6421538a6d7567793fc98b1ab81136',
       'X.fa9b1e9b54e8be10418ef00bd264b806',
       'X.6551fb3be9725c2f0d631e119b22c331',
       'X.1dfe3eac7261d34a2ac811ef43971b7d',
       'X.cfa439b28aaf2da993f1cfe771821bf4',
       'X.e6008920a330f2d4fdd4dfbd3ae786a6',
       'X.393f53bf9d6cc56f805cbe4227b4d222',
       'X.bd2ad541f1eb6a6e34004c1713f6b291']
  - 'X.8e6421538a6d7567793fc98b1ab81136', 'X.bd2ad541f1eb6a6e34004c1713f6b291' are negatively related to the disease score. 
  - Other features listed above are positively related to the diesease score. 
  - 'X.8e6421538a6d7567793fc98b1ab81136', 'X.fa9b1e9b54e8be10418ef00bd264b806', 'X.1dfe3eac7261d34a2ac811ef43971b7d' 
  are relatively more important compared to other bacterial communities listed above. 
  6. Random Forest and Ridge Regression tends to have a better prediction performance. However, this might has something to do with the small sample size. 
