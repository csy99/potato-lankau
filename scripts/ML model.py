from xgboost import XGBRegressor
from xgboost import plot_importance
import xgboost as xgb
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
def xgbfit(alg, X, y, xVal=None, yVal=None, train_cv=True, cv_folds=5, early_stopping_rounds=50,
           show_progress=False, ytrain_d_orig=None, yval_d_orig=None, fs=(9, 3)):
    if train_cv:
        xgb_param = alg.get_xgb_params()
        xgtrain = xgb.DMatrix(X.values, label=y.values)
        cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=alg.get_params()['n_estimators'], nfold=cv_folds,
                          metrics='rmse', early_stopping_rounds=early_stopping_rounds, show_stdv=show_progress)
        alg.set_params(n_estimators=cvresult.shape[0])

    # Fit the algorithm on the data
    alg.fit(X, y, eval_metric='rmse')

    # Predict data set:
    train_pred = alg.predict(X)
    train_pred_orig = Utils.johnson_inverse(train_pred, gamma, eta, epsilon, lbda)

    val_pred = alg.predict(xVal)
    test_pred_orig = Utils.johnson_inverse(val_pred, gamma, eta, epsilon, lbda)

    # Print model report:
    mse_train = mean_squared_error(train_pred_orig, ytrain_d_orig)
    mse_val = mean_squared_error(test_pred_orig, yval_d_orig)
    print("\nModel Report")
    print("RMSE for traning set: {}".format(np.sqrt(mse_train)))
    print("RMSE for validation set: {}".format(np.sqrt(mse_val)))

    plt.figure(figsize=fs)
    feat_imp = pd.Series(alg.get_booster().get_fscore()).sort_values(ascending=False)
    tmp = feat_imp[:21]  # only plot the 20 most important features
    tmp.plot(kind='bar', color="blue")
    plt.title('Feature Importances (limited to first 20)', fontsize=20)
    plt.ylabel('Feature Importance Score', fontsize=15)

    return train_pred_orig, test_pred_orig, feat_imp


