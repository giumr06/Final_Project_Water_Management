import streamlit as st
from app_utilities.preprocessing import *
from app_utilities.app_utilities import *
from app_plotting.app_plotting import *

from sklearn import set_config
set_config(transform_output="pandas")

st.markdown("## Welcome to project Amwag:")
st.write("Here you can see forecasts...")

X = pd.read_csv("./data/forecast_2021_2025.csv", index_col=0)
Y_true = pd.read_csv("./data/forecast_2021_2025_targets.csv", index_col=0)
Y_past = pd.read_csv("./data/targets_over_years.csv", index_col=0)

country = st.selectbox("choose country", X.country.unique())

year = st.selectbox("choose year", X.year.unique())

para_list = X.drop(["country", "year"], axis=1).columns.tolist()
para_0 = st.selectbox("choose parameter", para_list)

plot_options = ["bar","line"]
plot = st.selectbox(label="choose your board", options=plot_options)

para_0_val = st.slider("fraction of initial value", min_value=-1., max_value=1., value=0., step=0.01, format=None)

model_dict = load_pickle('model')

X_country, X_new, Y_true_c = prepare_single_set(X, Y_true, country, para_0, para_0_val, year=year)
X_ts, X_ts_new, Y_ts_true, Y_ts_past = prepare_timeseries_set(X, Y_true, Y_past, country, para_0, para_0_val)

Y_pred = get_single_predictions(model_dict, X_country)
Y_new = get_single_predictions(model_dict, X_new)

Y_ts_pred = get_timeseries_predictions(model_dict, X_ts)
Y_ts_new = get_timeseries_predictions(model_dict, X_ts_new)


if plot == 'bar':
    my_fig = create_barplot(Y_true_c, Y_pred, Y_new)

    colors = ['#d1e4d1', '#79a8a9', '#1f4e5f']

    my_fig.update_traces(marker_color=colors[0], selector=dict(name='Total Population with access to safe drinking water'))
    my_fig.update_traces(marker_color=colors[1], selector=dict(name='GDP per capita'))
    my_fig.update_traces(marker_color=colors[2], selector=dict(name='Water Stress'))

    st.plotly_chart(my_fig, use_container_width=True)
    
if plot == 'line':
    my_fig = create_timeline(Y_ts_true, Y_ts_pred, Y_ts_new, Y_ts_past)
    st.plotly_chart(my_fig, use_container_width=True)