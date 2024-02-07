import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(
    page_title="Data Pipeline (Accelerator)",
    page_icon="👋",
    layout="wide"
)
# Add this line to set the page layout
# st.set_page_config(layout="wide")

st.write("# Welcome to Innovation Fair! 👋")

# st.sidebar.success("Select a demo above.")

# Define image paths
etl_image = "Images/etl.png"
data_synthesis_image = "Images/synthesis.png"
risk_analysis_image = "Images/claimPrediction.png"
power_bi_image = "Images/PowerBi.png"
dq_system_image = 'Images/Data Quality.jpg'
col1,col2,col3,col4,col5 = st.columns(5)

# First row
with col1:
    st.image(dq_system_image,width=120)
    st.subheader("Data Quality System")
     

with col2:
    st.image(etl_image,width=120)
    st.subheader("Extract Transform Load") 
    
    # st.button("Start Data Synthesis")
  

with col3:
    st.image(data_synthesis_image,width=120)
    st.subheader("DATA SYNTHESIS")
    
    # st.button("Open Risk Analysis")
  

with col4:
    st.image(risk_analysis_image,width=120)
    st.subheader("RISK ANALYSIS")
    
with col5:
    st.image(power_bi_image,width=120)
    st.subheader("POWER BI")
    # st.link_button("Show Power BI Report", "https://www.microsoft.com/en-us/power-platform/products/power-bi/")

    

st.divider()
st.markdown(
    """
  
### Background & Pivotal Challenges:

- Flexibilty Issues

- Modularity Challenges

- Data Quality Impact

- Security and Compliance Complexity

- Reusability Concerns

## **PRODUCT NAME**\

Data Pipeline Framework is a comprehensive solution designed to handle the entire data processing journey

efficiently. From raw data to analysis, this framework ensures a seamless and adaptable approach to modern data

challenges.\

### Features

- A modular data pipeline with independent components

- Foster complementary components to maximize overall impact.

- Enable efficient customization of individual components.

- Simultaneously address data quality and security challenges.

- An adaptive framework serving as an accelerator.

- Incorporate robust data governance measures within the framework.
    
"""
)

# components.iframe('https://adrosonic-my.sharepoint.com/:p:/p/abhineash_kishan/EbjZj7e7wV9OqTaqx_cszZAByU0xNPX54f3py2iFUH2IbQ?e=t1DrqW&nav=eyJzSWQiOjM2OCwiY0lkIjozOTE0Njc0MzcwfQ',height=476)

# -  End-to-End Processing
#     -  Modularity and Abstraction
#     -  Versatile Components
#     -  Use Case Flexibility
#     -  Scalability and Reusability
#     -  Data Governance and Compliance