import streamlit as st
from amwag.app_utilities.app_utilities import *
from amwag.app_plotting.app_plotting import *

from sklearn import set_config
set_config(transform_output="pandas")

st.set_page_config(
        page_title="The Ripple Effect",
        page_icon="🐬",
        layout="centered"
)

st.markdown("<h1 style='text-align: center; color: ##113f67;'>The Ripple Effect </h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'> Here you can see our module prediction</h6>", unsafe_allow_html=True)
st.write("     ")
X = pd.read_csv("./data/data_2020.csv", index_col=0)
Y_true = pd.read_csv("./data/targets_2020.csv", index_col=0)
df_cluster = pd.read_csv("./data/heir_last_10.csv", encoding='ISO-8859-1')

var_name_dict = create_var_name_dict(X)

clust = st.sidebar.selectbox("Choose the cluster", df_cluster.sort_values("Cluster").Cluster.unique())
country = st.sidebar.selectbox("Choose a Country", df_cluster.query("Cluster == @clust")["Country Name"])
extra_paras = st.sidebar.selectbox("Number of additional metrics", [0,1,2])
para_list = var_name_dict.keys()
para_0 = st.sidebar.selectbox("Choose a metric", para_list)
para_0 = var_name_dict[para_0]
para_0_val = st.sidebar.slider("Fraction of initial value", min_value=-1., max_value=1., value=0., step=0.01, format=None)

para_dict ={para_0: para_0_val}
for am in range(extra_paras):
        para_x = st.sidebar.selectbox(f"Choose additional metric {am+1}", [p for p in para_list if not var_name_dict[p] in para_dict])
        para_x = var_name_dict[para_x]
        para_x_val = st.sidebar.slider(f"Fraction of initial value (additional metric {am+1})", min_value=-1., max_value=1., value=0., step=0.01, format=None)
        para_dict[para_x] = para_x_val

model_dict = load_pickle('model')

X_country, X_new, Y_true_c = prepare_single_set(X, Y_true, country, para_dict)

Y_pred = get_single_predictions(model_dict, X_country)
Y_new = get_single_predictions(model_dict, X_new)

my_fig = create_barplot(Y_true_c, Y_pred, Y_new)
st.plotly_chart(my_fig)

show_performance = st.sidebar.checkbox("show performance")
if show_performance:
        st.image("./app_images/prediction_performance_drinking_water.png")
        st.image("./app_images/prediction_performance_gdp.png")
        st.image("./app_images/prediction_performance_water_stress.png")

left_co,cent_co,cent_2_co,right_co,right_2_co,last_co = st.columns(6)
with last_co:
        st.image("./app_images/wave_2.png",width=175)