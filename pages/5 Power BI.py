
import streamlit as st
import pandas as pd
import numpy as np
# import requests

html='<iframe title="claimnpolicy 1" width="900" height="450" src="https://app.powerbi.com/reportEmbed?reportId=98c64d75-9c58-4efc-9322-95effe596eb5&autoAuth=true&ctid=cb66d0ff-e482-4ae1-bd42-a199c2f96350" frameborder="0" allowFullScreen="true"></iframe>'

st.set_page_config(layout="wide")
col1,col2,col3,col4 = st.columns(4)


with col1:
    st.image("Images\etl.png",width=150)
    st.subheader("Extract Transform Load") 
    st.caption("ETL is completed")
  
with col2:
    st.image("Images\synthesis.png",width=150)
    st.subheader("Data Synthesis and Generation")
    st.caption("Data Synthesis is done.") 
  
with col3:
   st.image("Images/claimPrediction.png",width=150)
   st.subheader("Risk Score Prediction")
   st.caption("Claim Prediction is Done") 

with col4:
   st.image("Images\PowerBi.png",width=150)
   st.subheader("Power BI Dashboard")
   st.caption("Analyze your data") 

st.progress(100)

with st.container():
    st.markdown(html,unsafe_allow_html=True)