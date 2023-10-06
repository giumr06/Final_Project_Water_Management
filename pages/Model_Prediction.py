from preprocessing import *
import streamlit as st
import pandas as pd
import pickle
from xgboost import XGBRegressor
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from sklearn import set_config
set_config( transform_output="pandas")

st.set_page_config(
        page_title="model prediction",
        page_icon="🐳",
        layout="centered"
)

st.header("Welcome to Amwag Project")
st.write("Model Predictor:")

def load_pickle(pk):
    with open(pk+'.pkl', 'rb') as file:
        loaded_file = pickle.load(file)
    return loaded_file

def create_barplot(Y_true, Y_pred, Y_new):
    fig = make_subplots(rows=1, cols=3)

    fig.add_trace(
        go.Bar(x=["Original value", "Initial Prediction", "New Prediction"], y=[Y_true["total_population_with_access_to_safe_drinking_water"].iloc[0], Y_pred["sdw"].iloc[0], Y_new["sdw"].iloc[0]],
        name="Total Population with access to safe drinking water"),
        row=1, col=1)
    
    fig.add_trace(
        go.Bar(x=["Original value", "Initial Prediction", "New Prediction"], y=[Y_true["gdp_per_capita"].iloc[0], Y_pred["gdp"].iloc[0], Y_new["gdp"].iloc[0]],
        name="GDP per capita"),
        row=1, col=2)

    fig.add_trace(
        go.Bar(x=["Original value", "Initial Prediction", "New Prediction"], y=[Y_true["water_stress"].iloc[0], Y_pred["ws"].iloc[0], Y_new["ws"].iloc[0]],
        name="Water Stress"),
        row=1, col=3)

    return fig

X = load_pickle("data_2020")
Y_true = load_pickle("targets_2020")

n_paras = st.selectbox

country = st.selectbox("Choose a Country", X.country)
para_list = X.drop(["country", "year"], axis=1).columns.tolist()

# list_02 = []
# for i in para_list:
#             i = i.replace("_"," ")
#             i = i.capitalize()
#             list_02.append(i)

para_0 = st.selectbox("Choose parameter", para_list)
para_0_val = st.slider("Fraction of initial value", min_value=-1., max_value=1., value=0., step=0.01, format=None)

model_dict = load_pickle('model')

X_country = X.query("country == @country")
X_new = X_country.copy(deep=True)
X_new[para_0].iloc[0] += para_0_val*X_new[para_0].iloc[0]
# print(X_new[para_0].iloc[0])
Y_true_c = Y_true.query("country == @country")

Y_pred = pd.DataFrame({k: model_dict[k].predict(X_country) for k in model_dict})
Y_new = pd.DataFrame({k: model_dict[k].predict(X_new) for k in model_dict})

my_fig = create_barplot(Y_true_c, Y_pred, Y_new)

colors = ['#d1e4d1', '#1f4e5f', '#79a8a9']

my_fig.update_traces(marker_color=colors[0], selector=dict(name='Total Population with access to safe drinking water'))
my_fig.update_traces(marker_color=colors[1], selector=dict(name='GDP per capita'))
my_fig.update_traces(marker_color=colors[2], selector=dict(name='Water Stress'))

st.plotly_chart(my_fig, use_container_width=True)
       
# st.write(X_country)
# st.write(df_prediction)



