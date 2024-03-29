import streamlit as st
from amwag.app_utilities.app_utilities import *
from amwag.app_plotting.app_plotting import *
from sklearn import set_config
set_config(transform_output="pandas")

#set up third page UI
st.set_page_config(
        page_title="The Time Forecast",
        page_icon="🐳",
        layout="centered"
)

#add page header and sub-header
st.markdown("<h1 style='text-align: center; color: ##113f67;'>The Time Forecast</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'> Here you can see a 5 years forecast from multivariate and univariate methods </h6>", unsafe_allow_html=True)

#set X and Y data for forecast
X_fc = pd.read_csv("./data/forecast_2021_2025.csv", index_col=0)
Y_fc = pd.read_csv("./data/forecast_2021_2025_targets.csv", index_col=0)
Y_past = pd.read_csv("./data/targets_over_years.csv", index_col=0)
X_past = pd.read_csv("./data/features_over_years.csv", index_col=0)
df_fc_var = pd.read_csv("./data/VAR_forecast_full.csv", index_col=0)
X_fc_var = df_fc_var.drop(columns=[tar for tar in Y_fc.columns.tolist() if not tar in ["country", "year"]])
Y_fc_var = df_fc_var[Y_fc.columns.tolist()]
df_cluster = pd.read_csv("./data/heir_last_10.csv", encoding='ISO-8859-1')

#enable options to select cluster and country within that cluster in sidebar
clust = st.sidebar.selectbox("Choose the cluster", df_cluster.sort_values("Cluster").Cluster.unique())
country = st.sidebar.selectbox("Choose a Country", df_cluster.query("Cluster == @clust")["Country Name"])

#show predicted data of selected country
Y_fc_c = Y_fc.query("country == @country")
Y_past_c = Y_past.query("country == @country")
Y_fc_var_c = Y_fc_var.query("country == @country")

#enable option to select between univariate and multivariate forecasts
uni = st.sidebar.checkbox("Show the Univariate Forecast 🦑")
multi = st.sidebar.checkbox("Show the Multivariate Forecast 🐙")
targets_fig = create_timeline(Y_fc_c, Y_fc_var_c, Y_past_c, uni, multi)

#plot the forecast according to user selections 
st.plotly_chart(targets_fig, use_container_width=True)

#enable option to select one or more features and show their forecast plots
var_name_dict = create_var_name_dict(X_past)
para_list = var_name_dict.keys()
selected_features = st.sidebar.multiselect("Choose the Variants:", para_list, placeholder="Multiple Selection")
selected_features = [var_name_dict[sf] for sf in selected_features]

X_fc_c = X_fc.query("country == @country")
X_past_c = X_past.query("country == @country")
X_fc_var_c = df_fc_var.query("country == @country")

if len(selected_features)>0:
    feature_fig = create_feature_timeline(X_fc_c, X_fc_var_c, X_past_c, uni, multi, selected_features)

    st.plotly_chart(feature_fig, use_container_width=True)

#enable option to show MAPE (mean absolute percentage error) value plots for forecast data
show_mape = st.sidebar.checkbox("show MAPE values")
if show_mape:
        st.image("./app_images/forecast_mape_values.png")
show_true_pred = st.sidebar.checkbox("show true vs. predicted values")
if show_true_pred:
        st.image("./app_images/forecast_performance_in_one.png")

left_co,cent_co,cent_2_co,right_co,right_2_co,last_co = st.columns(6)
with last_co:
        st.image("./app_images/wave_2.png",width=175)
