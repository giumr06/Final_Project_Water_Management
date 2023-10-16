import streamlit as st
from amwag.app_utilities.preprocessing import *
from amwag.app_utilities.app_utilities import *
from amwag.app_plotting.app_plotting import *

from sklearn import set_config
set_config(transform_output="pandas")

st.set_page_config(
        page_title="The Ripple Effect",
        page_icon="🐳",
        layout="centered"
)

st.markdown("<h1 style='text-align: center; color: ##113f67;'>The Ripple Effect </h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'> Here you can see our module prediction for each variant </h6>", unsafe_allow_html=True)
st.write("     ")
X = pd.read_csv("./data/data_2020.csv", index_col=0)
Y_true = pd.read_csv("./data/targets_2020.csv", index_col=0)

var_name_dict = create_var_name_dict(X)

country = st.sidebar.selectbox("Choose a Country", X.country)
para_list = var_name_dict.keys()
para_0 = st.sidebar.selectbox("Choose a Variant", para_list)
para_0 = var_name_dict[para_0]
para_0_val = st.sidebar.slider("Percentage of change in the original value", min_value=-1., max_value=1., value=0., step=0.01, format=None)

model_dict = load_pickle('model')

X_country, X_new, Y_true_c = prepare_single_set(X, Y_true, country, para_0, para_0_val)

Y_pred = get_single_predictions(model_dict, X_country)
Y_new = get_single_predictions(model_dict, X_new)

my_fig = create_barplot(Y_true_c, Y_pred, Y_new)
st.plotly_chart(my_fig)


left_co,cent_co,cent_2_co,right_co,right_2_co,last_co = st.columns(6)
with last_co:
        st.image("./app_images/wave_2.png",width=175)