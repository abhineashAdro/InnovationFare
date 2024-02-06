import streamlit as st

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
etl_image = "Images\etl.png"
data_synthesis_image = "Images\synthesis.png"
risk_analysis_image = "Images\claimPrediction.png"
power_bi_image = "Images\PowerBi.png"

col1,col2,col3,col4 = st.columns(4)

# First row
with col1:
    st.image(etl_image,width=150)
    st.subheader("Extract Transform Load")   

with col2:
    st.image(data_synthesis_image,width=150)
    
    st.subheader("DATA SYNTHESIS")
    # st.button("Start Data Synthesis")
  

with col3:
    st.image(risk_analysis_image,width=150)

    st.subheader("RISK ANALYSIS")
    # st.button("Open Risk Analysis")
  

with col4:
    st.image(power_bi_image,width=150)
    st.subheader("POWER BI")
    # st.link_button("Show Power BI Report", "https://www.microsoft.com/en-us/power-platform/products/power-bi/")
    
st.divider()
st.markdown(
    """
  **Overview**\\
  Data Pipeline Framework is a comprehensive solution designed to handle the entire data processing journey 
    efficiently. From raw data to analysis, this framework ensures a seamless and adaptable approach to modern data 
    challenges.\\
    Key Features:
    -  End-to-End Processing
    -  Modularity and Abstraction
    -  Versatile Components
    -  Use Case Flexibility
    -  Scalability and Reusability
    -  Data Governance and Compliance
"""
)
