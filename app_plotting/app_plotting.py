import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_barplot(Y_true, Y_pred, Y_new):
    fig = make_subplots(rows=1, cols=3)

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

    fig.update_traces(marker_color=colors[0], selector=dict(name='Total Population with access to safe drinking water'))
    fig.update_traces(marker_color=colors[1], selector=dict(name='GDP per capita'))
    fig.update_traces(marker_color=colors[2], selector=dict(name='Water Stress'))

    return fig

def create_timeline(Y_true, Y_pred, Y_new, Y_past):
    fig = make_subplots(rows=1, cols=3)

    fig.add_trace(
        go.Scatter(x=Y_true.year ,y=Y_true["total_population_with_access_to_safe_drinking_water"]), row=1, col=1)
    fig.add_trace(
        go.Scatter(x=Y_true.year, y=Y_pred["sdw"]), row=1, col=1)
    fig.add_trace(
        go.Scatter(x=Y_true.year, y=Y_new["sdw"]), row=1, col=1)
    fig.add_trace(
        go.Scatter(x=Y_past.year ,y=Y_past["total_population_with_access_to_safe_drinking_water"]), row=1, col=1)
    
    fig.add_trace(
        go.Scatter(x=Y_true.year ,y=Y_true["gdp_per_capita"]), row=1, col=2)
    fig.add_trace(
        go.Scatter(x=Y_true.year, y=Y_pred["gdp"]), row=1, col=2)
    fig.add_trace(
        go.Scatter(x=Y_true.year, y=Y_new["gdp"]), row=1, col=2)
    fig.add_trace(
        go.Scatter(x=Y_past.year ,y=Y_past["gdp_per_capita"]), row=1, col=2)

    fig.add_trace(
        go.Scatter(x=Y_true.year ,y=Y_true["water_stress"]), row=1, col=3)
    fig.add_trace(
        go.Scatter(x=Y_true.year, y=Y_pred["ws"]), row=1, col=3)
    fig.add_trace(
        go.Scatter(x=Y_true.year, y=Y_new["ws"]), row=1, col=3)
    fig.add_trace(
        go.Scatter(x=Y_past.year ,y=Y_past["water_stress"]), row=1, col=3)

    return fig