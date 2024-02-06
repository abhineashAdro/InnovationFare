
import streamlit as st
import time
# import pandas as pd
# import numpy as np
import requests
st.set_page_config(layout="wide")
col1,col2,col3,col4 = st.columns(4)

# First row
with col1:
    st.image("Images\etl.png",width=150)
    st.subheader("Extract Transform Load")
    st.caption("Currently in Extract Transform and Load")   
st.progress(10)
 

def call_adf_api(headers):
    api_url = "https://management.azure.com/subscriptions/755be828-9363-4e92-89a5-ab3085c02979/resourceGroups/resource101/providers/Microsoft.DataFactory/factories/databricks-adro/pipelines/adbAdro/createRun?api-version=2018-06-01"
    response = requests.post(api_url, headers=headers)
    return response

def check_pipeline_status(runId, headers):
    api_url = f"https://management.azure.com/subscriptions/755be828-9363-4e92-89a5-ab3085c02979/resourceGroups/resource101/providers/Microsoft.DataFactory/factories/databricks-adro/pipelineruns/{runId}?api-version=2018-06-01"
    response = requests.get(api_url, headers=headers)
    return response

access_token = st.text_input("Insert the access token")
#payload = {}
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {access_token}'
}
if st.button("Start ETL"):
        # Replace these placeholders with your actual values

        pipeline_run_response = call_adf_api(headers)
        #st.write("Response:")
        #st.json(pipeline_run_response.json())
        # Debugging: Print the response to check its structure
        st.info(f"Pipeline Run Response: {pipeline_run_response}")

        # Extract runId from the first API response
        runId = pipeline_run_response.json().get("runId")

        # Display extracted runId
        #st.write(f"Extracted runId: {runId}")
        if runId is not None:
            st.success('Pipeline Triggered Successfully!')
            st.balloons()
            # with st.spinner('Running the pipeline...'):
            #     while True:
            #         # Check status after a delay
            #         time.sleep(5)  # Adjust delay as needed
            #         response = check_pipeline_status(runId, headers)
            #         # st.info(response.json())
            #         status = response.json().get("status")  # Use get method to avoid KeyError if "status" is missing
            #         st.info(status)
            #         #st.write(f"Current Pipeline status: {status}")
            #         if status == "Succeeded":
            #             st.success('Pipeline Success!')
            #             st.balloons()
            #             initial_status = "Succeeded"
            #             is_second_button_disabled=False
            #             break
            #         elif status == "Failed":
            #             st.error('Pipeline Failed!')
            #             break                             
        else:
            st.error("Error: 'runId' not found in the Pipeline Run Response.")
