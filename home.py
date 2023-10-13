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
        Page("./pages/model.py", "The Amwag Module", "🐳"),
        Page("./pages/forecast.py", "The Amwag Forecast", "🐬")
    ]
)
##
home_page = st.sidebar.radio(
    "Select",
    ["The Project", "About us"],
    captions = ["Water Management", "The Amwag Group"])

if home_page == 'About us':
    st.markdown("<h1 style='text-align: center; color: #385170;'>The Amwag Group  مجموعه امواج</h1>", unsafe_allow_html=True)
    st.markdown("  ")
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
    left_co_2,cent_co_2,cent_2_co_2,right_co_2,right_2_co_2,last_co_2 = st.columns(6)
    with last_co_2:
        st.image("./app_images/wave_2.png",width=170)
        st.markdown("  ")
        
if home_page == 'The Project':
        st.markdown("<h1 style='text-align: center; color: #385170;'>The Amwag  أمواج</h1>", unsafe_allow_html=True)
        st.markdown(
           
           """
            The Amwag (أمواج), from the Egyptian-arabic word for "waves”, it’s a project that seeks to transform our understanding of sustainable development. This initiative combines data from the [AQUASTAT portal](https://data.apps.fao.org/aquastat/?lang=en)( a fundamental source of information on water resources and management) to unravel the complexity surrounding water stress, GDP per capita, and the availability of safe drinking water in a certain country from 1964. 

            Water is the lifeblood of human civilization, influencing economic prosperity, social well-being, and environmental sustainability. Comprehending how to harmonize the crucial factors of water stress, economic growth, and public health is paramount in a world where 25 countries contend with extreme water stress annually, imperilling the lives and livelihoods of billions.
            
            """
        )
        left_co,cent_co,cent_2_co,right_co,right_2_co,last_co = st.columns(6)
        with cent_2_co:
            st.image("./app_images/wave_1.png",width=180) 
            st.markdown("    ")
        st.markdown(
           
            """
           ##### Understanding Global Water Stress
           Global water stress has emerged as a pivotal challenge that threatens livelihoods and economies. This critical issue is characterized by the demand for water surpassing its availability, a trend that has seen a doubling of water demand since 1960. Various factors contribute to this surge in demand, including population growth, the needs of agriculture, energy production, and industry. Furthermore, inadequate investments in water infrastructure, unsustainable water policies, and the effects of climate change on water supply further exacerbate the problem. \n
           As a result, water-stressed areas face two primary categories of vulnerabilities: those with extreme water stress, using over 80% of their available supply, and those with high water stress, consuming 40% of their supply. This situation often leads to water shortages, with profound implications for communities and industries dependent on this finite resource.\n
           On the other hand, water demand in wealthier regions like North America and Europe has plateaued, thanks to investments in water-use efficiency. However, international trade introduces complexities, with water embedded in global trade contributing to rising water stress in lower-middle-income countries.\n
           While these challenges are formidable, the Amwag project highlights an essential insight: water stress doesn't necessarily equate to a water crisis. Examining examples like Singapore and Las Vegas, we discover that societies can thrive under water-scarce conditions through innovative strategies. These include measures such as replacing water-intensive grass, implementing desalination processes, and harnessing the potential of wastewater treatment.\n
           In conclusion, The Amwag project's mission is to bridge the gap between data and action by translating this valuable information into actionable insights and strategies. It's purpose is to address water stress, promote economic growth, and ensure access to safe drinking water. In this way, the Amwag project aspires to be a catalyst for positive change in the face of the growing global water stress challenge.\n

           - References:\n 
            [AQUASTAT](https://www.fao.org/aquastat/en/)\n
            [United Nations - Unwater](https://www.unwater.org/)\n
            [Aqueduct](https://www.wri.org/aqueduct)\n
            [25 Countries, Housing One-quarter of the Population, Face Extremely High Water Stress](https://www.wri.org/insights/highest-water-stressed-countries)\n
            [World Resources Institute - Fresh Water Topic ](https://www.wri.org/water)\n
            [UNESCO - Water for people, water for life: the United Nations world water development report](https://unesdoc.unesco.org/ark:/48223/pf0000129726)
            """
        )
        left_co_2,cent_co_2,cent_2_co_2,right_co_2,right_2_co_2,last_co_2 = st.columns(6)
        with last_co_2:
            st.image("./app_images/wave_2.png",width=170)