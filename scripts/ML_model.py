import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor, plot_importance
import xgboost as xgb
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV

import Utils


# build XGBoost model.
# input:
# X, y: training data
# xVal, yVal: validation set
# ytrain_d_orig, yval_d_orig: true observations (not prediction) before data transformation.
# output:
# train_pred_orig: prediction for training set
# test_pred_orig: prediction for validation set
# feat_imp: a list of important features identified by the model
def xgb_fit(alg, X, y, xVal=None, yVal=None, train_cv=True, cv_folds=5, early_stopping_rounds=50,
            show_progress=False, trans_param=None, fs=(9, 3)):
    if train_cv:
        xgb_param = alg.get_xgb_params()
        xgtrain = xgb.DMatrix(X.values, label=y.values)
        cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=alg.get_params()['n_estimators'], nfold=cv_folds,
                          metrics='rmse', early_stopping_rounds=early_stopping_rounds, show_stdv=show_progress)
        alg.set_params(n_estimators=cvresult.shape[0])

    # Fit the algorithm on the data
    alg.fit(X, y, eval_metric='rmse')

    # data transformation
    gamma, eta, epsilon, lbda = trans_param
    ytrain_d_orig = Utils.johnson_inverse(y, gamma, eta, epsilon, lbda)
    yval_d_orig = Utils.johnson_inverse(yVal, gamma, eta, epsilon, lbda)

    # Predict data set:
    train_pred = alg.predict(X)
    train_pred_orig = Utils.johnson_inverse(train_pred, gamma, eta, epsilon, lbda)

    val_pred = alg.predict(xVal)
    val_pred_orig = Utils.johnson_inverse(val_pred, gamma, eta, epsilon, lbda)

    # Print model report:
    mse_train = mean_squared_error(train_pred_orig, ytrain_d_orig)
    mse_val = mean_squared_error(val_pred_orig, yval_d_orig)
    print("\nXGBoost Model Report")
    print("RMSE for training set: {}".format(np.sqrt(mse_train)))
    print("RMSE for validation set: {}".format(np.sqrt(mse_val)))

    plt.figure(figsize=fs)
    feat_imp = pd.Series(alg.get_booster().get_fscore()).sort_values(ascending=False)
    tmp = feat_imp[:21][::-1]  # only plot the 20 most important features
    tmp.plot(kind='barh', color="blue")
    plt.title('Feature Importance (limited to first 20)', fontsize=20)
    plt.ylabel('Feature Relative Importance', fontsize=15)

    return train_pred_orig, val_pred_orig, feat_imp


# build XGBoost model.
# input:
# X, y: training data
# xVal, yVal: validation set
# ytrain_orig, yval_orig: true observations (not prediction) before data transformation.
# output:
# train_pred_orig: prediction for training set
# test_pred_orig: prediction for validation set
# importances: a list of important features identified by the model
def rf_fit(rf, X, y, xVal=None, yVal=None, trans_param=None, fs=(9, 3)):
    rf.fit(X, y)
    # data transformation
    gamma, eta, epsilon, lbda = trans_param
    ytrain_orig = Utils.johnson_inverse(y, gamma, eta, epsilon, lbda)
    yval_orig = Utils.johnson_inverse(yVal, gamma, eta, epsilon, lbda)

    # prediction
    train_pred = pd.Series(rf.predict(X))
    train_pred_orig = Utils.johnson_inverse(train_pred, gamma, eta, epsilon, lbda)
    val_pred = pd.Series(rf.predict(xVal))
    val_pred_orig = Utils.johnson_inverse(val_pred, gamma, eta, epsilon, lbda)

    # Print model report:
    mse_train = mean_squared_error(train_pred_orig, ytrain_orig)
    mse_val = mean_squared_error(val_pred_orig, yval_orig)
    print("\nRandom Forest Model Report")
    print("RMSE for training set: {}".format(np.sqrt(mse_train)))
    print("RMSE for validation set: {}".format(np.sqrt(mse_val)))

    features = X.columns
    importances = rf.feature_importances_
    top = np.argsort(importances)[-19:]  # top 20 features
    plt.figure(figsize=fs)
    plt.title('Feature Importance (limited to first 20)', fontsize=20)
    plt.barh(range(len(top)), importances[top], color='b', align='center')
    plt.yticks(range(len(top)), [features[i] for i in top])
    plt.xlabel('Feature Relative Importance', fontsize=15)
    plt.show()
    return train_pred_orig, val_pred_orig, features[top], rf


def ridge_fit(ridge, X, y, xVal=None, yVal=None, trans_param=None, fs=(9, 3)):
    ridge.fit(X, y)
    # data transformation
    gamma, eta, epsilon, lbda = trans_param
    ytrain_orig = Utils.johnson_inverse(y, gamma, eta, epsilon, lbda)
    yval_orig = Utils.johnson_inverse(yVal, gamma, eta, epsilon, lbda)

    # prediction
    train_pred = pd.Series(ridge.predict(X))
    train_pred_orig = Utils.johnson_inverse(train_pred, gamma, eta, epsilon, lbda)
    val_pred = pd.Series(ridge.predict(xVal))
    val_pred_orig = Utils.johnson_inverse(val_pred, gamma, eta, epsilon, lbda)

    # Print model report:
    mse_train = mean_squared_error(train_pred_orig, ytrain_orig)
    mse_val = mean_squared_error(val_pred_orig, yval_orig)
    print("\nRidge Regression Model Report")
    print("RMSE for training set: {}".format(np.sqrt(mse_train)))
    print("RMSE for validation set: {}".format(np.sqrt(mse_val)))

    return ridge.coef_, ridge.intercept_


def linear_fit(lin_model, X, y, xVal=None, yVal=None, trans_param=None, fs=(9, 3)):
    lin_model.fit(X, y)
    # data transformation
    gamma, eta, epsilon, lbda = trans_param
    ytrain_orig = Utils.johnson_inverse(y, gamma, eta, epsilon, lbda)
    yval_orig = Utils.johnson_inverse(yVal, gamma, eta, epsilon, lbda)

    # prediction
    train_pred = pd.Series(lin_model.predict(X))
    train_pred_orig = Utils.johnson_inverse(train_pred, gamma, eta, epsilon, lbda)
    val_pred = pd.Series(lin_model.predict(xVal))
    val_pred_orig = Utils.johnson_inverse(val_pred, gamma, eta, epsilon, lbda)

    # Print model report:
    mse_train = mean_squared_error(train_pred_orig, ytrain_orig)
    mse_val = mean_squared_error(val_pred_orig, yval_orig)
    print("\nLinear Regression Model Report")
    print("RMSE for training set: {}".format(np.sqrt(mse_train)))
    print("RMSE for validation set: {}".format(np.sqrt(mse_val)))

    return lin_model.coef_, lin_model.intercept_


def random_search(alg, tuning, X, y, xVal=None, yVal=None, trans_param=None, n_iter=100, cv=5, seed=2):
    random = RandomizedSearchCV(estimator=alg, param_distributions=tuning, n_iter=n_iter, cv=cv, random_state=seed)
    random.fit(X, y)

    # data transformation
    gamma, eta, epsilon, lbda = trans_param
    ytrain_orig = Utils.johnson_inverse(y, gamma, eta, epsilon, lbda)
    yval_orig = Utils.johnson_inverse(yVal, gamma, eta, epsilon, lbda)

    # prediction
    train_pred = pd.Series(random.predict(X))
    train_pred_orig = Utils.johnson_inverse(train_pred, gamma, eta, epsilon, lbda)
    val_pred = pd.Series(random.predict(xVal))
    val_pred_orig = Utils.johnson_inverse(val_pred, gamma, eta, epsilon, lbda)

    # evaluation:
    mse_train = mean_squared_error(train_pred_orig, ytrain_orig)
    mse_val = mean_squared_error(val_pred_orig, yval_orig)
    print("\nRandomized Search Tuning Report")
    print("RMSE for traning set: {}".format(np.sqrt(mse_train)))
    print("RMSE for validation set: {}".format(np.sqrt(mse_val)))

    return train_pred_orig, val_pred_orig, random.best_estimator_, random.best_params_


def grid_search(alg, tuning, X, y, xVal=None, yVal=None, trans_param=None, cv=5):
    grid_search = GridSearchCV(estimator=alg, param_grid=tuning, scoring='neg_mean_squared_error', cv=cv)
    grid_search.fit(X, y)

    # data transformation
    gamma, eta, epsilon, lbda = trans_param
    ytrain_orig = Utils.johnson_inverse(y, gamma, eta, epsilon, lbda)
    yval_orig = Utils.johnson_inverse(yVal, gamma, eta, epsilon, lbda)

    # prediction
    train_pred = pd.Series(grid_search.predict(X))
    train_pred_orig = Utils.johnson_inverse(train_pred, gamma, eta, epsilon, lbda)
    val_pred = pd.Series(grid_search.predict(xVal))
    val_pred_orig = Utils.johnson_inverse(val_pred, gamma, eta, epsilon, lbda)

    # evaluation:
    mse_train = mean_squared_error(train_pred_orig, ytrain_orig)
    mse_val = mean_squared_error(val_pred_orig, yval_orig)
    print("\nGrid Search Tuning Report")
    print("RMSE for traning set: {}".format(np.sqrt(mse_train)))
    print("RMSE for validation set: {}".format(np.sqrt(mse_val)))

    return train_pred_orig, val_pred_orig, grid_search.best_estimator_, grid_search.best_params_
