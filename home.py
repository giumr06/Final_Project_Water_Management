import streamlit as st
from st_pages import Page, show_pages

st.set_page_config(
        page_title="home",
        page_icon="🌊",
        layout="centered",
        initial_sidebar_state="expanded"
)

show_pages(
    [
        Page("./pages/die_streamlit.py", "Original Page", "🌑"),
        Page("home.py", "Home", "🌊"),
        Page("./pages/model_prediction.py", "Model Prediction", "🐳"),
        #Page("./pages/time_series_prediction.py", "Time Series Prediction", "🐬")
    ]
)
##
home_page = st.sidebar.radio(
    "Select",
    ["The Project", "About us"],
    captions = ["Water Management", "The Amwag Group"])

if home_page == 'About us':
    st.title("The Amwag Group")
    st.markdown("""
             This project was proposed as the final project of the Data Science boot camp from Spiced Academy (10.2023).
             
             Our main goals were: 
              
             1- To create an interactive website that can predict possible effects on targets by tweaking parameters.
             
             2- Make a presentation on correlations and clustering of countries based on water use habits.
             
             
             The Amwag project was create by:                                                                                                                                                        
             [Stephan O. Adler](https://www.linkedin.com/in/stephan-o-adler/) 
             
             [Giulia Miranda Reis](https://www.linkedin.com/in/giuliamirandareis/) 
           
             Uta Bösch
           
             [Mike Moner](https://www.linkedin.com/in/mike-moner/)
           
             [David Aleksov](https://www.linkedin.com/in/davidaleksov/)
              
             """
             
             )
if home_page == 'The Project':
        st.write("Water Management.")