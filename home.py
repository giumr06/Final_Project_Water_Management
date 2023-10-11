import streamlit as st
from st_pages import Page, show_pages

st.set_page_config(
        page_title="home",
        page_icon="🌊",
        layout="centered",
        initial_sidebar_state="expanded"
)
#
show_pages(
    [
        Page("home.py", "Home", "🌊"),
        Page("./pages/model.py", "Model Prediction", "🐳"),
        Page("./pages/forecast.py", "Time Series Prediction", "🐬")
    ]
)
##
home_page = st.sidebar.radio(
    "Select",
    ["The Project", "About us"],
    captions = ["Water Management", "The Amwag Group"])

if home_page == 'About us':
    st.markdown("<h1 style='text-align: center; color: #385170;'>The Amwag Group  مجموعه امواج</h1>", unsafe_allow_html=True)
    st.markdown("""
             This project was proposed as the final project of the Data Science boot camp from Spiced Academy (10.2023).
             
             #### Our main goals: 
            
             I- To create an interactive website that can predict possible effects on targets by tweaking parameters.
             
             II- Make a presentation on correlations and clustering of countries based on water use habits.
             
             #### Our main challenges:\n
             The project relies on AQUASTAT as its data source, and while AQUASTAT provides a wealth of data on water resources and agricultural water management, it encounters several challenges:\n
                
                - Lack of Complete Time-Series Data: \n
                     I - AQUASTAT's data often lacks complete time series, making it intricate to analyze trends and gain a comprehensive understanding of water's socioeconomic context. This limitation can curtail the scope of interpretation. \n
                     II - In the same category of problem, due to initiatives that are not computed in the data as social-political changes that could have happened locally, the data has a Non-stationarity behaviour meaning that the changes do not follow a stable pattern but mostly seem to admit a rather random progression in the given time frame. \n

                - Data Gaps: \n
                     Data gaps in AQUASTAT are mainly attributed to a lack of information and capacity at the national level. This increased the challenges in collecting comprehensive and accurate data for the training process. \n

                - Methodology Changes and Data Updates: \n
                     Frequent updates and changes in data methodology can render prior series invalid, leading to confusion and incorrect attribution of data to more recent years.

                - Inconsistent Terminology: \n
                     Discrepancies in terminology between countries and international organizations contribute to confusion and complicate data interpretation. For this reason, and also for a better understanding of the features used in this project,  please access the [ AQUASTAT glossary](https://www.fao.org/aquastat/en/databases/glossary/)\n
                     
                - We acknowledge these limitations and strives to ensure that data interpretation remain transparent and accounts for these constraints.\n

             #### The Amwag project was create by:  \n                                                                                                                                                      
             [Stephan O. Adler](https://www.linkedin.com/in/stephan-o-adler/) 
            
             [Giulia Miranda Reis](https://www.linkedin.com/in/giuliamirandareis/) 
           
             [Uta Bösch](https://www.linkedin.com/)
           
             [Mike Moner](https://www.linkedin.com/in/mike-moner/)
           
             [David Aleksov](https://www.linkedin.com/in/davidaleksov/)
              
             """
             
             )
if home_page == 'The Project':
        st.markdown("<h1 style='text-align: center; color: #385170;'>The Amwag  أمواج</h1>", unsafe_allow_html=True)
        st.markdown(
           
           """
           The Amwag (أمواج), from the Egyptian-arabic word for "waves”, it’s a project that seeks to transform our understanding of sustainable development. This initiative combines data from the [AQUASTAT portal](https://data.apps.fao.org/aquastat/?lang=en)( a fundamental source of information on water resources and management) to unravel the complexity surrounding water stress, GDP per capita, and the availability of safe drinking water in a certain country from 1964. 

            Water is the lifeblood of human civilization, influencing economic prosperity, social well-being, and environmental sustainability. Comprehending how to harmonize the crucial factors of water stress, economic growth, and public health is paramount in a world where 25 countries contend with extreme water stress annually, imperilling the lives and livelihoods of billions.

        
            Please also check:\n 
            [AQUASTAT](https://www.fao.org/aquastat/en/)\n
            [United Nations - Unwater](https://www.unwater.org/)\n
            [Aqueduct](https://www.wri.org/aqueduct)\n
            [25 Countries, Housing One-quarter of the Population, Face Extremely High Water Stress](https://www.wri.org/insights/highest-water-stressed-countries)\n
            [World Resources Institute - Fresh Water Topic ](https://www.wri.org/water)\n
            
            """
        )
        