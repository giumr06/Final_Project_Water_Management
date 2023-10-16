import streamlit as st
import pandas as pd
from preprocessing_93 import *
import plotly.express as px
import pycountry

from sklearn import set_config
set_config(transform_output="pandas")

st.set_page_config(
        page_title="World Map with Clusters",
        page_icon="🐋",
        layout="wide"
)

st.markdown("<h1 style='text-align: center; color: ##113f67;'>World Map with Clusters</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'> Clustered Countries </h6>", unsafe_allow_html=True)

df_h_last_10 = pd.read_csv('data/heir_last_10.csv', encoding='ISO-8859-1')

df_h = df_h_last_10.drop(['Size', 'ISO Alpha-3 Code'], axis=1)
st.sidebar.dataframe(df_h)

color = ["#90f6d7", "#35bcbf", "#41506b", "#263849"]
fig = px.choropleth(
    df_h_last_10,
    locations='ISO Alpha-3 Code',
    color="Cluster",
    projection='natural earth',
    color_discrete_sequence=color,
    width=900,
    height=500
)
st.plotly_chart(fig)
left_co,cent_co,cent_2_co,right_co,right_2_co,last_co = st.columns(6)
with last_co:
        st.image("./app_images/wave_2.png",width=175)