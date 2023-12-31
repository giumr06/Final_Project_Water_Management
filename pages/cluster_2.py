import streamlit as st
import pandas as pd
import pycountry
import plotly.express as px


from sklearn import set_config
set_config(transform_output="pandas")

st.set_page_config(
        page_title="The Cluster Map",
        page_icon="🐋",
        layout="wide"
)

st.markdown("<h1 style='text-align: center; color: ##113f67;'> The Cluster Map</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'> The four groups of countries based in the data </h6>", unsafe_allow_html=True)

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
    "I. Indo-African": 45,
    "II. The Scattered Clusters": 32,
    "III. BRICS like": 48,
    "IV. EU / US": 36,
    "Total": 161 
}
sidebar_data = filtered_df.drop(["Size", "ISO Alpha-3 Code","Cluster"],axis=1)
st.sidebar.dataframe(sidebar_data)
st.sidebar.title("Cluster Information")

for cluster, size in cluster_info.items():
    st.sidebar.text(f"{cluster}: {size}")
left_co_2,cent_co_2,cent_2_co_2,right_co_2,right_2_co_2,last_co_2 = st.columns(6)
with last_co_2:
    st.image("./app_images/wave_2.png",width=170)