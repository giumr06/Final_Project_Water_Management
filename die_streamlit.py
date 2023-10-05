from preprocessing import *
import streamlit as st
import pandas as pd
import pickle
from xgboost import XGBRegressor

from sklearn import set_config
set_config(transform_output="pandas")

st.write("Welcome to project Amwag:")

def load_pickle(pk):
    with open(pk+'.pkl', 'rb') as file:
        loaded_file = pickle.load(file)
    return loaded_file

X = load_pickle("data_2020")

country = st.selectbox('choose_country', X.country) 
model_dict = load_pickle('model')

X_country = X.query("country == @country")

df_prediction = pd.DataFrame({k: model_dict[k].predict(X_country) for k in model_dict})
       
st.write(X_country)
st.write(df_prediction)



