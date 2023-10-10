import streamlit as st
from app_utilities.preprocessing import *
from app_utilities.app_utilities import *
from app_plotting.app_plotting import *

from sklearn import set_config
set_config(transform_output="pandas")

st.write("Welcome to project Amwag:")

X = pd.read_csv("data_2020.csv", index_col=0)
Y_true = pd.read_csv("targets_2020.csv", index_col=0)

country = st.selectbox("choose country", X.country)
para_list = X.drop(["country", "year"], axis=1).columns.tolist()
para_0 = st.selectbox("choose parameter", para_list)
para_0_val = st.slider("fraction of initial value", min_value=-1., max_value=1., value=0., step=0.01, format=None)

model_dict = load_pickle('model')

X_country, X_new, Y_true_c = prepare_single_set(X, Y_true, country, para_0, para_0_val)

Y_pred = get_single_predictions(model_dict, X_country)
Y_new = get_single_predictions(model_dict, X_new)

my_fig = create_barplot(Y_true_c, Y_pred, Y_new)
st.plotly_chart(my_fig, use_container_width=True)