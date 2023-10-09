import streamlit as st
from st_pages import Page, show_pages

# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page("./pages/die_streamlit.py", "Home", "🏠"),
        Page("./pages/Model_Prediction.py", "Model Prediction", "🐳"),
    ]
)