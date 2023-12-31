import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from amwag.app_utilities.app_utilities import *

def create_barplot(Y_true, Y_pred, Y_new):
    fig = make_subplots(rows=1, cols=3, horizontal_spacing = 0.15)

    fig.add_trace(
        go.Bar(x=["Original Value", "First prediciton", "New prediction"], y=[Y_true["total_population_with_access_to_safe_drinking_water"].iloc[0], Y_pred["sdw"].iloc[0], Y_new["sdw"].iloc[0]],
        name="Total Population with access to safe drinking water"),
        row=1, col=1)
    
    fig.add_trace(
        go.Bar(x=["Original Value", "First prediciton", "New prediction"], y=[Y_true["gdp_per_capita"].iloc[0], Y_pred["gdp"].iloc[0], Y_new["gdp"].iloc[0]],
        name="GDP per capita"),
        row=1, col=2)

    fig.add_trace(
        go.Bar(x=["Original Value", "First prediciton", "New prediction"], y=[Y_true["water_stress"].iloc[0], Y_pred["ws"].iloc[0], Y_new["ws"].iloc[0]],
        name="Water Stress"),
        row=1, col=3)

    colors = ['#d1e4d1', '#79a8a9', '#1f4e5f']
    fig.update_layout(legend=dict(font=dict(color='#3c4245')), width=900, height=500)
    fig.update_traces(marker_color=colors[0], selector=dict(name='Total Population with access to safe drinking water'))
    fig.update_traces(marker_color=colors[1], selector=dict(name='GDP per capita'))
    fig.update_traces(marker_color=colors[2], selector=dict(name='Water Stress'))

    fig.update_yaxes(title_text="% of population", row=1, col=1)
    fig.update_yaxes(title_text="US$ per inhabitant", row=1, col=2)
    fig.update_yaxes(title_text="%", row=1, col=3)

    fig.update_layout(legend=dict(
    yanchor="top",
    y=1.3,
    xanchor="left",
    x=0.01
    ))

    return fig

def create_timeline(Y_fc, Y_mfc, Y_past, uni, multi):
    fig = make_subplots(rows=3, cols=1)
    fig.update_layout({"height":650})

    # past
    fig.add_trace(
        go.Scatter(x=Y_past.year ,y=Y_past["total_population_with_access_to_safe_drinking_water"],
        name='Total Population with access to safe drinking water'),
        row=1, col=1)
    fig.add_trace(
        go.Scatter(x=Y_past.year ,y=Y_past["gdp_per_capita"],
        name="GDP per capita"),
        row=2, col=1)
    fig.add_trace(
        go.Scatter(x=Y_past.year ,y=Y_past["water_stress"],
        name="Water Stress"),
        row=3, col=1)
    
    # forecast
    fc_colors = ["#c06c84", "#ff6f3c"]
    # univariate
    if uni:
        fig.add_trace(
            go.Scatter(x=Y_fc.year ,y=Y_fc["total_population_with_access_to_safe_drinking_water"],
            marker=dict(color=fc_colors[0]),
            name="Holt-Winters' forecast"),
            row=1, col=1)
        fig.add_trace(
            go.Scatter(x=Y_fc.year ,y=Y_fc["gdp_per_capita"],
            marker=dict(color=fc_colors[0]),
            showlegend=False),
            row=2, col=1)
        fig.add_trace(
            go.Scatter(x=Y_fc.year ,y=Y_fc["water_stress"],
            marker=dict(color=fc_colors[0]),
            showlegend=False),
            row=3, col=1)

    # multivariate
    if multi:
        fig.add_trace(
            go.Scatter(x=Y_mfc.year ,y=Y_mfc["total_population_with_access_to_safe_drinking_water"],
            marker=dict(color=fc_colors[1]),
            name="VAR forecast"),
            row=1, col=1)
        fig.add_trace(
            go.Scatter(x=Y_mfc.year ,y=Y_mfc["gdp_per_capita"],
            marker=dict(color=fc_colors[1]),
            showlegend=False),
            row=2, col=1)
        fig.add_trace(
            go.Scatter(x=Y_mfc.year ,y=Y_mfc["water_stress"],
            marker=dict(color=fc_colors[1]),
            showlegend=False),
            row=3, col=1)

    colors = ['#d1e4d1', '#79a8a9', '#1f4e5f']

    fig.update_layout(legend=dict(font=dict(size=14,color='#5f6769')))
    fig.update_traces(marker_color=colors[0], selector=dict(name='Total Population with access to safe drinking water'))
    fig.update_traces(marker_color=colors[1], selector=dict(name='GDP per capita'))
    fig.update_traces(marker_color=colors[2], selector=dict(name='Water Stress'))

    fig.update_layout(legend=dict(
    yanchor="top",
    y=1.3,
    xanchor="left",
    x=0.01
    ))

    fig.update_xaxes(title_text="year", col=1, row=3)
    fig.update_yaxes(title_text="% of population", row=1, col=1)
    fig.update_yaxes(title_text="US$ per inhabitant", row=2, col=1)
    fig.update_yaxes(title_text="%", row=3, col=1)

    return fig


def create_feature_timeline(X_fc, X_mfc, X_past, uni, multi, sfs):
    df_units = pd.read_csv("./data/feature_units.csv")

    fig = make_subplots(rows=len(sfs), cols=1)
    fig.update_layout({"height":180+120*len(sfs)})

    reverse_var_name_dict = create_reverse_var_name_dict(X_past)

    for i, feature in enumerate(sfs):
    # past
        fig.add_trace(
            go.Scatter(x=X_past.year ,y=X_past[feature],
            name=reverse_var_name_dict[feature]),
            row=i+1, col=1)
        fig.update_yaxes(title_text=df_units[feature].iloc[0], row=i+1, col=1)
    
    # forecast
        fc_colors = ["#c06c84", "#ff6f3c"]
    # univariate
        if uni:
            fig.add_trace(
                go.Scatter(x=X_fc.year ,y=X_fc[feature],
                marker=dict(color=fc_colors[0]),
                showlegend=False),
                row=i+1, col=1)

    # multivariate
        if multi:
            fig.add_trace(
                go.Scatter(x=X_mfc.year ,y=X_mfc[feature],
                marker=dict(color=fc_colors[1]),
                showlegend=False),
                row=i+1, col=1)

    fig.update_layout(legend=dict(
    yanchor="top",
    y=1.2,
    xanchor="left",
    x=0.01
    ))

    fig.update_xaxes(title_text="year", col=1, row=len(sfs))

    return fig