import streamlit as st
from amwag.app_utilities.preprocessing import *
from amwag.app_utilities.app_utilities import *
from amwag.app_plotting.app_plotting import *
from sklearn import set_config
set_config(transform_output="pandas")


st.markdown("## Welcome to project Amwag:")
st.write("Here you can see forecasts from multivariate and univariate methods")

# X = pd.read_csv("./data/forecast_2021_2025.csv", index_col=0)
Y_fc = pd.read_csv("./data/forecast_2021_2025_targets.csv", index_col=0)
Y_past = pd.read_csv("./data/targets_over_years.csv", index_col=0)

country = st.sidebar.selectbox("choose country", Y_fc.country.unique())

Y_fc_c = Y_fc.query("country == @country")
Y_past_c = Y_past.query("country == @country")

targets_fig = create_timeline(Y_fc_c, Y_past_c)

st.plotly_chart(targets_fig, use_container_width=True)