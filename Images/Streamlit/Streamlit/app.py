import streamlit as st
import requests 
import time 
# Add this line to set the page layout
st.set_page_config(layout="wide")

# Define image paths
etl_image = "images/etl.png"
data_synthesis_image = "images/synthesis.png"
risk_analysis_image = "images/riskanalysis.png"
power_bi_image = "images/powerbi.png"

st.markdown("""
    <style>
        # .stButton button {
        #     background-color: white;
        #     color: black;
        #     font-weight: bold;
        # }
        # .stLinkButton a {
        #     background-color: white;
        #     color: black !important;
        #     font-weight: bold;
        #     text-decoration: none;
        # }
        # .stLinkButton a:hover {
        #     background-color: blue;
        #     color: pink !important;
        #     font-weight: bold;
        #     text-decoration: none;
        # }
        #data-pipeline-app{
            text-align:center;
        }
       
       
    </style>
""", unsafe_allow_html=True)
st.title("Data Pipeline App")
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjVCM25SeHRRN2ppOGVORGMzRnkwNUtmOTdaRSIsImtpZCI6IjVCM25SeHRRN2ppOGVORGMzRnkwNUtmOTdaRSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzEyYjRmYmY5LWRlYTgtNDQ5MC1iZWRlLTljYzQwMzA5YWQ2MS8iLCJpYXQiOjE3MDY0OTc4MzMsIm5iZiI6MTcwNjQ5NzgzMywiZXhwIjoxNzA2NTAyMjQ5LCJhY3IiOiIxIiwiYWlvIjoiQVRRQXkvOFZBQUFBZG5jOC9RSmhtclhucVMwcUhPbllDaTAzNk9wUHIvQ2t5d016NkZLSHdBMEEzWWdMTEtaN3J6SnlySWRpd1cxdiIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiIxOGZiY2ExNi0yMjI0LTQ1ZjYtODViMC1mN2JmMmIzOWIzZjMiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IktVTUFSIiwiZ2l2ZW5fbmFtZSI6Ik5JS0hJTCIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjEwMy4xNDIuMTA3LjE2MyIsIm5hbWUiOiJOSUtISUwgS1VNQVIgKE1DQTQwMDAxLjIxQGJpdG1lc3JhLmFjLmluKSIsIm9pZCI6IjRhZDZjYThmLWU4ZmEtNDk2My1hNjllLWQ3NmJkMDkyNjIwMSIsInB1aWQiOiIxMDAzMjAwMTY1OUQ0RjlGIiwicmgiOiIwLkFWUUEtZnUwRXFqZWtFUy0zcHpFQXdtdFlVWklmM2tBdXRkUHVrUGF3ZmoyTUJPaUFPSS4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiIyUWQ1XzZEUVlreWoxLXZucWVBZ3pxcDlqVTJoclpNSGJHZU9xMEEwMmhVIiwidGlkIjoiMTJiNGZiZjktZGVhOC00NDkwLWJlZGUtOWNjNDAzMDlhZDYxIiwidW5pcXVlX25hbWUiOiJNQ0E0MDAwMS4yMUBiaXRtZXNyYS5hYy5pbiIsInVwbiI6Ik1DQTQwMDAxLjIxQGJpdG1lc3JhLmFjLmluIiwidXRpIjoiNk55NnR6S2xKa2V0Z0ZJYUxzTWdBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYWUiOiIxIiwieG1zX3RjZHQiOjE0MzY3NzA1ODN9.S3NfXp1IkuJFpIqDCTa5JMEvSnzFm8yiMrPDOMbLPtB_ACvxt9xIgGxMZZ700wVERtTauPoHcUyef6iLyqolGuD5AiVA-yZJtnKWN3RyVevX_OVfX5SdqiGUHoDGDERBWM3ssMjiKeS8c-WpStCoOYn55NASnXGXIw6nvrgkzEPWKXnd7A8p4JZUHwjEv3I57njKIyyAGfLLRpljtA4ZhnSjIFNH4_Ryesq04xraeueRLbO-_3bI2q20_Oo6HkRpS-f_2hIKo7t4iSgmg3yFq2FD4FONjhp1BVql54ZwY6TYoXO9lKl2-M7yFy-9AiJyOIjC7FvWsI1pNHJUqMN4bA'
}

def call_adf_api(headers):
    api_url = "https://management.azure.com/subscriptions/901a326a-2178-4386-b836-0575520c0882/resourceGroups/ARG/providers/Microsoft.DataFactory/factories/adfstores/pipelines/CSVtoParquet/createRun?api-version=2018-06-01"
    response = requests.post(api_url, headers=headers)
    return response

def check_pipeline_status(runId, headers):
    api_url = f"https://management.azure.com/subscriptions/901a326a-2178-4386-b836-0575520c0882/resourceGroups/ARG/providers/Microsoft.DataFactory/factories/adfstores/pipelineruns/{runId}?api-version=2018-06-01"
    response = requests.get(api_url, headers=headers)
    return response

col1,col2,col3,col4 = st.columns(4)

# First row
with col1:
    st.image(etl_image,width=200)
    st.subheader("ETL")
    if st.button("Start ETL"):
        # Replace these placeholders with your actual values

        pipeline_run_response = call_adf_api(headers)
        #st.write("Response:")
        #st.json(pipeline_run_response.json())
        # Debugging: Print the response to check its structure
        print("Debug - Pipeline Run Response:", pipeline_run_response)

        # Extract runId from the first API response
        runId = pipeline_run_response.json().get("runId")

        # Display extracted runId
        #st.write(f"Extracted runId: {runId}")
        if runId is not None:
            with st.spinner('Running the pipeline...'):
                while True:
                    # Check status after a delay
                    time.sleep(5)  # Adjust delay as needed
                    response = check_pipeline_status(runId, headers)
                    status = response.json().get("status")  # Use get method to avoid KeyError if "status" is missing
                    #st.write(f"Current Pipeline status: {status}")
                    if status == "Succeeded":
                        st.success('Pipeline Success!')
                        st.balloons()
                        initial_status = "Succeeded"
                        is_second_button_disabled=False
                        break
                    elif status == "Failed":
                        st.error('Pipeline Failed!')
                        break                             
        else:
            st.write("Error: 'runId' not found in the Pipeline Run Response.")

    

with col2:
    st.image(data_synthesis_image,width=200)
    
    st.subheader("DATA SYNTHESIS")
    st.button("Start Data Synthesis")
  

with col3:
    st.image(risk_analysis_image,width=200)

    st.subheader("RISK ANALYSIS")
    st.button("Open Risk Analysis")
  

with col4:
    st.image(power_bi_image,width=200)
    st.subheader("POWER BI")
    st.link_button("Show Power BI Report", "https://www.microsoft.com/en-us/power-platform/products/power-bi/")
    