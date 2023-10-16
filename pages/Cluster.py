import streamlit as st
import pandas as pd
import pycountry
import plotly.express as px


from sklearn import set_config
set_config(transform_output="pandas")

st.set_page_config(
        page_title="The Amwag Forecast",
        page_icon="🐬",
        layout="wide"
)

st.markdown("<h1 style='text-align: center; color: ##113f67;'>World Map with Clusters </h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'> Cluster Countries </h6>", unsafe_allow_html=True)


# df_h_last_10 = pd.read_csv('data/heir_last_10.csv', encoding='ISO-8859-1')

# # Create a select box for choosing a cluster number
# selected_cluster = st.sidebar.selectbox("Select Cluster Number:", df_h_last_10['Cluster'].unique())

# # Filter the DataFrame based on the selected cluster
# filtered_df = df_h_last_10[df_h_last_10['Cluster'] == selected_cluster]

# # Display the filtered DataFrame in the sidebar
# st.sidebar.dataframe(filtered_df)


# # Create a choropleth map using Plotly Express
# fig = px.choropleth(
#     filtered_df,
#     locations='ISO Alpha-3 Code',
#     color='Cluster',
#     color_continuous_scale='Viridis',
#     projection='natural earth',
#     width=1300,
#     height=900
# )

# st.plotly_chart(fig)


df_h_last_10 = pd.read_csv('data/heir_last_10.csv', encoding='ISO-8859-1')

# Create a select box for choosing a cluster number
cluster_options = [0] + list(df_h_last_10['Cluster'].unique())  # Include 0 to show all clusters
selected_cluster = st.sidebar.selectbox("Select Cluster Number:", cluster_options)

# Filter the DataFrame based on the selected cluster
if selected_cluster == 0:
    filtered_df = df_h_last_10  # Show all clusters
else:
    filtered_df = df_h_last_10[df_h_last_10['Cluster'] == selected_cluster]

# Display the filtered DataFrame in the sidebar
st.sidebar.dataframe(filtered_df)

# Create a choropleth map using Plotly Express
fig = px.choropleth(
    filtered_df,
    locations='ISO Alpha-3 Code',
    color='Cluster',
    color_continuous_scale='Viridis',
    projection='natural earth',
    width=1400,
    height=900
)
st.plotly_chart(fig)



cluster_info = {
    "Cluster": "Num of Countries", 
    "Cluster 1": 32,
    "Cluster 2": 45,
    "Cluster 3": 36,
    "Cluster 4": 48,
    "Total": 161 
}

# Display the cluster information in the Streamlit sidebar
st.sidebar.title("Cluster Information")
for cluster, size in cluster_info.items():
    st.sidebar.text(f"{cluster}: {size}")

# df_h_last_10 = pd.read_csv('data/heir_last_10.csv', encoding='ISO-8859-1')
# df_h = df_h_last_10.drop(['Size', 'ISO Alpha-3 Code'], axis=1)

# selected_cluster = st.sidebar.selectbox("Select Cluster Number:", df_h['Cluster'].unique())
# st.sidebar.dataframe(df_h)


# selected_cluster = st.sidebar.selectbox("Select Cluster Number:", df_h['Cluster'].unique())

# # Filter the DataFrame based on the selected cluster
# filtered_df = df_h[df_h['Cluster'] == selected_cluster]

# # Display the filtered DataFrame in the sidebar
# st.sidebar.dataframe(filtered_df)



# fig = px.choropleth(
#     df_h_last_10,
#     locations='ISO Alpha-3 Code',
#     color='Cluster',
#     color_continuous_scale='Plasma',
#     projection='natural earth',
#     width=1400,
#     height=900
# )
# st.plotly_chart(fig)




