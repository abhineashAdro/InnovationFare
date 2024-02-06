import streamlit as st
import requests

def make_api_call():
    url = "https://management.azure.com/subscriptions/901a326a-2178-4386-b836-0575520c0882/resourceGroups/ARG/providers/Microsoft.DataFactory/factories/adfstores/pipelines/CopyData_ParquetFile_to_SQLDB/createRun?api-version=2018-06-01"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjVCM25SeHRRN2ppOGVORGMzRnkwNUtmOTdaRSIsImtpZCI6IjVCM25SeHRRN2ppOGVORGMzRnkwNUtmOTdaRSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzEyYjRmYmY5LWRlYTgtNDQ5MC1iZWRlLTljYzQwMzA5YWQ2MS8iLCJpYXQiOjE3MDYyNTIyMTgsIm5iZiI6MTcwNjI1MjIxOCwiZXhwIjoxNzA2MjU2MjQzLCJhY3IiOiIxIiwiYWlvIjoiQVRRQXkvOFZBQUFBN0xpMThIUDNYV05NMDhIUHhtRnJtQ2xYR240SGhCdVpVVHV4UENFN1JDZ25NWG1md3hLandLQmVueXdFNmZwNCIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiIxOGZiY2ExNi0yMjI0LTQ1ZjYtODViMC1mN2JmMmIzOWIzZjMiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IktVTUFSIiwiZ2l2ZW5fbmFtZSI6Ik5JS0hJTCIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjEwMy4xNDIuMTA3LjE2MyIsIm5hbWUiOiJOSUtISUwgS1VNQVIgKE1DQTQwMDAxLjIxQGJpdG1lc3JhLmFjLmluKSIsIm9pZCI6IjRhZDZjYThmLWU4ZmEtNDk2My1hNjllLWQ3NmJkMDkyNjIwMSIsInB1aWQiOiIxMDAzMjAwMTY1OUQ0RjlGIiwicmgiOiIwLkFWUUEtZnUwRXFqZWtFUy0zcHpFQXdtdFlVWklmM2tBdXRkUHVrUGF3ZmoyTUJPaUFPSS4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiIyUWQ1XzZEUVlreWoxLXZucWVBZ3pxcDlqVTJoclpNSGJHZU9xMEEwMmhVIiwidGlkIjoiMTJiNGZiZjktZGVhOC00NDkwLWJlZGUtOWNjNDAzMDlhZDYxIiwidW5pcXVlX25hbWUiOiJNQ0E0MDAwMS4yMUBiaXRtZXNyYS5hYy5pbiIsInVwbiI6Ik1DQTQwMDAxLjIxQGJpdG1lc3JhLmFjLmluIiwidXRpIjoiM3liUlQ4dFRKMC1SX052eGY5YXhBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYWUiOiIxIiwieG1zX3RjZHQiOjE0MzY3NzA1ODN9.rX3D7OHLPVZjh-lru8_a2LuXzqaZIrhv9arWyTKn2WdexMjjBpcjEzn-AL68SWJhL38rDNUcKR8TVKXSju9oP0T7kzkpKsjQ3Wp3DaL1d11WYsM7weqq3jzoEa488bIOkjMRhhJw0-33l1ajL97iHy9fM2fhr4jzpSWiutZpwsEx-6ItbhPnj1fGkdvDZ2I3yp8hlrNH4JX1QCst8idFhfcVMJ5Tt5dW6AutZL7vtKc_5NV0H6UG7sLOPffPRgYs65yApyV7iW0Wgkvua_pkGW_poL1Gs__qrzQ-iVApuVhOy7xd3c2amwR9vIn3hQ6ezt-lxCdyZMwUlb4x6DjIWw'
    }

    response = requests.post(url, headers=headers)
    return response

def make_second_call(runId):
    url = f"https://management.azure.com/subscriptions/901a326a-2178-4386-b836-0575520c0882/resourceGroups/ARG/providers/Microsoft.DataFactory/factories/adfstores/pipelineruns/{runId}?api-version=2018-06-01"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjVCM25SeHRRN2ppOGVORGMzRnkwNUtmOTdaRSIsImtpZCI6IjVCM25SeHRRN2ppOGVORGMzRnkwNUtmOTdaRSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzEyYjRmYmY5LWRlYTgtNDQ5MC1iZWRlLTljYzQwMzA5YWQ2MS8iLCJpYXQiOjE3MDYyNTIyMTgsIm5iZiI6MTcwNjI1MjIxOCwiZXhwIjoxNzA2MjU2MjQzLCJhY3IiOiIxIiwiYWlvIjoiQVRRQXkvOFZBQUFBN0xpMThIUDNYV05NMDhIUHhtRnJtQ2xYR240SGhCdVpVVHV4UENFN1JDZ25NWG1md3hLandLQmVueXdFNmZwNCIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiIxOGZiY2ExNi0yMjI0LTQ1ZjYtODViMC1mN2JmMmIzOWIzZjMiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IktVTUFSIiwiZ2l2ZW5fbmFtZSI6Ik5JS0hJTCIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjEwMy4xNDIuMTA3LjE2MyIsIm5hbWUiOiJOSUtISUwgS1VNQVIgKE1DQTQwMDAxLjIxQGJpdG1lc3JhLmFjLmluKSIsIm9pZCI6IjRhZDZjYThmLWU4ZmEtNDk2My1hNjllLWQ3NmJkMDkyNjIwMSIsInB1aWQiOiIxMDAzMjAwMTY1OUQ0RjlGIiwicmgiOiIwLkFWUUEtZnUwRXFqZWtFUy0zcHpFQXdtdFlVWklmM2tBdXRkUHVrUGF3ZmoyTUJPaUFPSS4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiIyUWQ1XzZEUVlreWoxLXZucWVBZ3pxcDlqVTJoclpNSGJHZU9xMEEwMmhVIiwidGlkIjoiMTJiNGZiZjktZGVhOC00NDkwLWJlZGUtOWNjNDAzMDlhZDYxIiwidW5pcXVlX25hbWUiOiJNQ0E0MDAwMS4yMUBiaXRtZXNyYS5hYy5pbiIsInVwbiI6Ik1DQTQwMDAxLjIxQGJpdG1lc3JhLmFjLmluIiwidXRpIjoiM3liUlQ4dFRKMC1SX052eGY5YXhBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYWUiOiIxIiwieG1zX3RjZHQiOjE0MzY3NzA1ODN9.rX3D7OHLPVZjh-lru8_a2LuXzqaZIrhv9arWyTKn2WdexMjjBpcjEzn-AL68SWJhL38rDNUcKR8TVKXSju9oP0T7kzkpKsjQ3Wp3DaL1d11WYsM7weqq3jzoEa488bIOkjMRhhJw0-33l1ajL97iHy9fM2fhr4jzpSWiutZpwsEx-6ItbhPnj1fGkdvDZ2I3yp8hlrNH4JX1QCst8idFhfcVMJ5Tt5dW6AutZL7vtKc_5NV0H6UG7sLOPffPRgYs65yApyV7iW0Wgkvua_pkGW_poL1Gs__qrzQ-iVApuVhOy7xd3c2amwR9vIn3hQ6ezt-lxCdyZMwUlb4x6DjIWw'
    }

    response = requests.get(url, headers=headers)
    return response

# Declare run_Id outside the button block
run_Id = None

# Streamlit app
st.title("Azure API Call")

# Button to make API call
if st.button("Make API Call"):
    response = make_api_call()
    st.write("Response:")
    st.json(response.json())
    
    # Extract runId from the first API response
    run_Id = response.json().get("runId")

    # Display extracted runId
    st.write(f"Extracted runId: {run_Id}")

# Check if run_Id is not None before using it
if run_Id:
    if st.button("Make Second Call"):
        second_response = make_second_call(run_Id)
        st.write("Second Response:")
        #st.json(second_response.json())
    
        # Extract status from the second API response
        status = second_response.json().get("status")

        # Display extracted status
        st.write(f"Extracted status: {status}")
        if status == "Succeeded":
            st.write("PIPELINE RUN WAS SUCCESSFUL")

    

    
    







# def make_first_api_call():
#     url = "https://management.azure.com/subscriptions/901a326a-2178-4386-b836-0575520c0882/resourceGroups/ARG/providers/Microsoft.DataFactory/factories/adfstores/pipelines/CopyData_ParquetFile_to_SQLDB/createRun?api-version=2018-06-01"
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjVCM25SeHRRN2ppOGVORGMzRnkwNUtmOTdaRSIsImtpZCI6IjVCM25SeHRRN2ppOGVORGMzRnkwNUtmOTdaRSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzEyYjRmYmY5LWRlYTgtNDQ5MC1iZWRlLTljYzQwMzA5YWQ2MS8iLCJpYXQiOjE3MDYyNDUzODMsIm5iZiI6MTcwNjI0NTM4MywiZXhwIjoxNzA2MjUwNTY0LCJhY3IiOiIxIiwiYWlvIjoiQVRRQXkvOFZBQUFBTUYrZ0xpaytSbHJZdUM1YUlBRWdLMXlnb2tkT0F3UmRsMXBocFdMU0lRS3VpVzJtNlp3THVGWDF3OGM5bFY1ZyIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiIxOGZiY2ExNi0yMjI0LTQ1ZjYtODViMC1mN2JmMmIzOWIzZjMiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IktVTUFSIiwiZ2l2ZW5fbmFtZSI6Ik5JS0hJTCIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjEwMy4xNDIuMTA3LjE2MyIsIm5hbWUiOiJOSUtISUwgS1VNQVIgKE1DQTQwMDAxLjIxQGJpdG1lc3JhLmFjLmluKSIsIm9pZCI6IjRhZDZjYThmLWU4ZmEtNDk2My1hNjllLWQ3NmJkMDkyNjIwMSIsInB1aWQiOiIxMDAzMjAwMTY1OUQ0RjlGIiwicmgiOiIwLkFWUUEtZnUwRXFqZWtFUy0zcHpFQXdtdFlVWklmM2tBdXRkUHVrUGF3ZmoyTUJPaUFPSS4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiIyUWQ1XzZEUVlreWoxLXZucWVBZ3pxcDlqVTJoclpNSGJHZU9xMEEwMmhVIiwidGlkIjoiMTJiNGZiZjktZGVhOC00NDkwLWJlZGUtOWNjNDAzMDlhZDYxIiwidW5pcXVlX25hbWUiOiJNQ0E0MDAwMS4yMUBiaXRtZXNyYS5hYy5pbiIsInVwbiI6Ik1DQTQwMDAxLjIxQGJpdG1lc3JhLmFjLmluIiwidXRpIjoiTzVIaWFTMDJnRTJmeW1SSXNiM1RBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYWUiOiIxIiwieG1zX3RjZHQiOjE0MzY3NzA1ODN9.Us9PfhIpLXn2JxSysJ_rwtyc8rpl_WIgGGh62IIBWukGNzJsH6K9cV1_ck_ISdrnLMMyFmzyKqcGSeyaqwaBXuPyRlyVVfyeuTh2M6gFhRy9KZD3OKrbQiLVSzkH3uE5pxlE3zj1pwKeSWQufjUu6Gt_0GqJPxY45X9rvoj6Z1WwQtHH8e0ZC9LdMJ-_GghvTY2TJaXzzZ-vs8S0wlXPiGiIHmely-1CRGefJlWhg_C3eUYz6CgcUN2O-q8pGNJh9-6ZQ72W1LWfDaYX7Rgdx15bectONWd03H--Vsw3ULnZUJLQEZfLlpCqLt90UKAdUZHbdO2SnQ39LJr4QzMlEg'
#     }

#     response = requests.post(url, headers=headers)
#     return response

# def make_second_api_call(run_Id):
#     url = f"https://management.azure.com/subscriptions/901a326a-2178-4386-b836-0575520c0882/resourceGroups/ARG/providers/Microsoft.DataFactory/factories/adfstores/pipelineruns/{runId}?api-version=2018-06-01"

#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjVCM25SeHRRN2ppOGVORGMzRnkwNUtmOTdaRSIsImtpZCI6IjVCM25SeHRRN2ppOGVORGMzRnkwNUtmOTdaRSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzEyYjRmYmY5LWRlYTgtNDQ5MC1iZWRlLTljYzQwMzA5YWQ2MS8iLCJpYXQiOjE3MDYyNDUzODMsIm5iZiI6MTcwNjI0NTM4MywiZXhwIjoxNzA2MjUwNTY0LCJhY3IiOiIxIiwiYWlvIjoiQVRRQXkvOFZBQUFBTUYrZ0xpaytSbHJZdUM1YUlBRWdLMXlnb2tkT0F3UmRsMXBocFdMU0lRS3VpVzJtNlp3THVGWDF3OGM5bFY1ZyIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiIxOGZiY2ExNi0yMjI0LTQ1ZjYtODViMC1mN2JmMmIzOWIzZjMiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IktVTUFSIiwiZ2l2ZW5fbmFtZSI6Ik5JS0hJTCIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjEwMy4xNDIuMTA3LjE2MyIsIm5hbWUiOiJOSUtISUwgS1VNQVIgKE1DQTQwMDAxLjIxQGJpdG1lc3JhLmFjLmluKSIsIm9pZCI6IjRhZDZjYThmLWU4ZmEtNDk2My1hNjllLWQ3NmJkMDkyNjIwMSIsInB1aWQiOiIxMDAzMjAwMTY1OUQ0RjlGIiwicmgiOiIwLkFWUUEtZnUwRXFqZWtFUy0zcHpFQXdtdFlVWklmM2tBdXRkUHVrUGF3ZmoyTUJPaUFPSS4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiIyUWQ1XzZEUVlreWoxLXZucWVBZ3pxcDlqVTJoclpNSGJHZU9xMEEwMmhVIiwidGlkIjoiMTJiNGZiZjktZGVhOC00NDkwLWJlZGUtOWNjNDAzMDlhZDYxIiwidW5pcXVlX25hbWUiOiJNQ0E0MDAwMS4yMUBiaXRtZXNyYS5hYy5pbiIsInVwbiI6Ik1DQTQwMDAxLjIxQGJpdG1lc3JhLmFjLmluIiwidXRpIjoiTzVIaWFTMDJnRTJmeW1SSXNiM1RBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYWUiOiIxIiwieG1zX3RjZHQiOjE0MzY3NzA1ODN9.Us9PfhIpLXn2JxSysJ_rwtyc8rpl_WIgGGh62IIBWukGNzJsH6K9cV1_ck_ISdrnLMMyFmzyKqcGSeyaqwaBXuPyRlyVVfyeuTh2M6gFhRy9KZD3OKrbQiLVSzkH3uE5pxlE3zj1pwKeSWQufjUu6Gt_0GqJPxY45X9rvoj6Z1WwQtHH8e0ZC9LdMJ-_GghvTY2TJaXzzZ-vs8S0wlXPiGiIHmely-1CRGefJlWhg_C3eUYz6CgcUN2O-q8pGNJh9-6ZQ72W1LWfDaYX7Rgdx15bectONWd03H--Vsw3ULnZUJLQEZfLlpCqLt90UKAdUZHbdO2SnQ39LJr4QzMlEg'
#     }

#     response = requests.get(url, headers=headers)
#     return response

# # Streamlit app
# st.title("Azure API Calls")

# # Button to make first API call
# if st.button("Make First API Call"):
#     response_first_api = make_first_api_call()
    
#     if response_first_api.status_code == 200:
#         st.write("First API Response:")
#         st.json(response_first_api.json())

#         # Extract runId from the first API response
#         run_Id = response_first_api.json().get("runId")

#         # Display extracted runId
#         st.write(f"Extracted runId: {run_Id}")
#          # Print the second API URL before making the call
#         second_api_url = f"https://management.azure.com/subscriptions/901a326a-2178-4386-b836-0575520c0882/resourceGroups/ARG/providers/Microsoft.DataFactory/factories/adfstores/pipelineruns/{run_Id}?api-version=2018-06-01"
#         st.write(f"Second API URL: {second_api_url}")

        
#     else:
#         st.error(f"First API Call Failed with Status Code: {response_first_api.status_code}")
# # Button to make second API call with runId
#     if st.button("Make Second API Call"):
#             st.write("Run id: {run_Id}")
#             if run_Id:
#                 response_second_api = make_second_api_call(run_Id)
                
#                 if response_second_api.status_code == 200:
#                     st.write("Second API Response:")
#                     st.json(response_second_api.json())
#                 else:
#                     st.error(f"Second API Call Failed with Status Code: {response_second_api.status_code}")
#             else:
#                 st.warning("RunId not found in the first API response.")    