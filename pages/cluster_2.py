import streamlit as st
import pandas as pd
import pycountry
import plotly.express as px


from sklearn import set_config
set_config(transform_output="pandas")

st.set_page_config(
        page_title="World Map with Clusters",
        page_icon="🐋",
        layout="wide"
)

st.markdown("<h1 style='text-align: center; color: ##113f67;'> World Map with Clusters </h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'> Cluster Countries </h6>", unsafe_allow_html=True)

df_h_last_10 = pd.read_csv('data/heir_last_10.csv', encoding='ISO-8859-1')
df_h_last_10.drop([104,108,106],axis=0, inplace=True)

cluster_options = [0] + list(df_h_last_10.sort_values("Cluster")['Cluster'].unique()) 
selected_cluster = st.sidebar.selectbox("Select Cluster Number:", cluster_options)

if selected_cluster == 0:
    filtered_df = df_h_last_10 
else:
    filtered_df = df_h_last_10[df_h_last_10['Cluster'] == selected_cluster]

color = ["#90f6d7", "#35bcbf", "#41506b", "#263849"]
fig = px.choropleth(
    filtered_df,
    locations='ISO Alpha-3 Code',
    color="Cluster",
    projection='natural earth',
    color_discrete_sequence=color,
    width=900,
    height=500
)
st.plotly_chart(fig)

cluster_info = { 
    "Wave": 32,
    "Indo-African": 45,
    "EU - US": 36,
    "BRICS like": 48,
    "Total": 161 
}
sidebar_data = filtered_df.drop(["Size", "ISO Alpha-3 Code"],axis=1)
st.sidebar.dataframe(sidebar_data)
st.sidebar.title("Cluster Information")
for cluster, size in cluster_info.items():
    st.sidebar.text(f"{cluster}: {size}")