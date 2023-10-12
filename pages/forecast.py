import streamlit as st
from amwag.app_utilities.preprocessing import *
from amwag.app_utilities.app_utilities import *
from amwag.app_plotting.app_plotting import *
from sklearn import set_config
set_config(transform_output="pandas")


st.markdown("## Welcome to project Amwag:")
st.write("Here you can see forecasts from multivariate and univariate methods")

X_fc = pd.read_csv("./data/forecast_2021_2025.csv", index_col=0)
Y_fc = pd.read_csv("./data/forecast_2021_2025_targets.csv", index_col=0)
Y_past = pd.read_csv("./data/targets_over_years.csv", index_col=0)
X_past = pd.read_csv("./data/features_over_years.csv", index_col=0)
df_fc_var = pd.read_csv("./data/VAR_forecast_full.csv", index_col=0)
X_fc_var = df_fc_var.drop(columns=[tar for tar in Y_fc.columns.tolist() if not tar in ["country", "year"]])
Y_fc_var = df_fc_var[Y_fc.columns.tolist()]

country = st.sidebar.selectbox("choose country", Y_fc.country.unique())

# targets
Y_fc_c = Y_fc.query("country == @country")
Y_past_c = Y_past.query("country == @country")
Y_fc_var_c = Y_fc_var.query("country == @country")

uni = st.sidebar.checkbox("show Holt-Winters' forecast (univariate)")
multi = st.sidebar.checkbox("show VAR forecast (multivariate)")
targets_fig = create_timeline(Y_fc_c, Y_fc_var_c, Y_past_c, uni, multi)

st.plotly_chart(targets_fig, use_container_width=True)

# features
var_name_dict = create_var_name_dict(X_past)
para_list = var_name_dict.keys()
selected_features = st.sidebar.multiselect("choose parameters to show:", para_list)
selected_features = [var_name_dict[sf] for sf in selected_features]

X_fc_c = X_fc.query("country == @country")
X_past_c = X_past.query("country == @country")
X_fc_var_c = df_fc_var.query("country == @country")

if len(selected_features)>0:
    feature_fig = create_feature_timeline(X_fc_c, X_fc_var_c, X_past_c, uni, multi, selected_features)

    st.plotly_chart(feature_fig, use_container_width=True)