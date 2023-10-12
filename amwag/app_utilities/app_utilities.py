import pandas as pd
import pickle
from xgboost import XGBRegressor

from sklearn import set_config
set_config(transform_output="pandas")

def load_pickle(pk):
    with open(pk+'.pkl', 'rb') as file:
        loaded_file = pickle.load(file)
    return loaded_file

def prepare_single_set(X, Y_true, country, para, para_val, year=None):
    X_country = X.query("country == @country")
    Y_true_c = Y_true.query("country == @country")
    if year:
        X_country = X_country.query("year == @year")
        Y_true_c = Y_true_c.query("year == @year")
    X_new = X_country.copy(deep=True)
    X_new[para].iloc[0] += para_val*X_new[para].iloc[0]

    return X_country, X_new, Y_true_c

def prepare_timeseries_set(X, Y_true, Y_past, country, para, para_val):
    X_country = X.query("country == @country")
    X_new = X_country.copy(deep=True)
    X_new[para] =  X_new[para].apply(lambda x: x + para_val*x)
    Y_true_c = Y_true.query("country == @country")
    Y_ts_past = Y_past.query("country == @country")

    return X_country, X_new, Y_true_c, Y_ts_past

def get_single_predictions(model_dict, X):
    return pd.DataFrame({k: model_dict[k].predict(X) for k in model_dict})

def get_timeseries_predictions(model_dict, X):
    pred_over_years_dict = {k: [] for k in model_dict}
    for y in X.year.unique():
        for k, m in model_dict.items():
            X_y = X.query("year == @y")
            pred_over_years_dict[k].append(m.predict(X_y)[0])

    return pd.DataFrame(pred_over_years_dict)

def create_var_name_dict(df):
    initial_names = df.drop(["country", "year"], axis=1).columns.tolist()
    var_name_dict = {n.replace("_"," ").replace("%", "percentage"): n for n in initial_names}
    return var_name_dict