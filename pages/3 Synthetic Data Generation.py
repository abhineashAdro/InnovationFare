import streamlit as st
import pandas as pd
import bz2file as bz2
import pickle
# import numpy as np
# import requests
# import json
# from datetime import date, timedelta
import pyodbc

st.spinner("Loading Important Libraries and Models")
from ydata_synthetic.synthesizers.regular import RegularSynthesizer

st.set_page_config(layout="wide")
col1,col2,col3,col4,col5 = st.columns(5)
with col1:
    st.image('Images/Data Quality.jpg',width=120)
    st.subheader("Data Quality System")
    st.caption("Data Quality System Review Done.")

with col2:
    st.image("Images/etl.png",width=120)
    st.subheader("Extract Transform Load") 
    st.caption("ETL is completed.....Moving to Data Synthesis")
  
with col3:
    st.image("Images/synthesis.png",width=120)
    st.subheader("Data Synthesis and Generation")
    st.caption("Currently in Data Synthesis") 

st.progress(50)

def make_syhtetic_data(numberOfPolicywithClaim,numberOfPolicyWithoutClaim):
#   data = bz2.BZ2File('Compressed_Models/comp_onlyPolicy.pbz2','rb')
#   data = pickle.load(data)
  synth = RegularSynthesizer.load("Models/onlyPolicy.pkl")
  policy_claim = RegularSynthesizer.load("Models/policyClaim.pkl")
  policy_data = synth.sample(int(numberOfPolicyWithoutClaim))
  policy_claim_data = policy_claim.sample(int(numberOfPolicywithClaim))
  policy_2 = policy_claim_data[['CUST_ID', 'EXECUTIVE', 'BODY', 'MAKE', 'MODEL', 'USE_OF_VEHICLE',
       'MODEL_YEAR', 'CHASSIS_NO', 'REGN', 'POLICY_NO', 'POL_EFF_DATE',
       'POL_EXPIRY_DATE', 'SUM INSURED', 'POL_ISSUE_DATE', 'PREMIUM2',
       'DRV_DOB', 'DRV_DLI', 'VEH_SEATS', 'PRODUCT', 'POLICYTYPE',
       'Nationality']]
  claims_data = policy_claim_data[['Claims_Account Code', 'Claims_DATE OF _INTIMATION',
       'Claims_DATE OF _ACCIDENT', 'Claims_PLACE OF _LOSS', 'Claims_CLAIM NO',
       'Claims_AGE', 'Claims_TYPE', 'Claims_DRIVING _LICENSE ISSUE',
       'Claims_BODY TYPE', 'Claims_MAKE', 'Claims_MODEL', 'Claims_YEAR',
       'Claims_CHASIS NO', 'Claims_REG', 'Claims_SUM INSURED', 'POLICY_NO',
       'Claims_POLICY START', 'Claims_POLICY END', 'Claims_INTIMATED_AMOUNT',
       'Claims_INTIMATED_SF', 'Claims_EXECUTIVE', 'Claims_PRODUCT',
       'Claims_POLICYTYPE', 'Claims_NATIONALITY']]
  policy_d = pd.concat([policy_data,policy_2],axis=0)
  return policy_d,claims_data


numberOfPolicywithClaim = st.number_input("Enter the No. of Policy to generate with Claim")
numberOfPolicywithoutClaim = st.number_input('Enter the No. of Policy to Genrate without Claim')
# sql_table_policy = st.text_input("Enter the Name of Policy Table in SQL DB")
# sql_table_claim = st.text_input("Enter the Name of Claim Table in SQL DB")

# policy_schema = f"CREATE TABLE [{sql_table_policy}] ("
# claim_schema = f"CREATE TABLE [{sql_table_claim}] ("


if st.button('Synthetic Data Generation and Insert into SQL'):
    if numberOfPolicywithClaim<=0 or numberOfPolicywithoutClaim<=0:
        st.error('Please put the number above or euqal to 1')
    else:
        policy_s, claim_s = make_syhtetic_data(numberOfPolicywithClaim, numberOfPolicywithoutClaim)
        policy_s.columns = [c.replace(' ','_') for c in policy_s.columns]
        claim_s.columns = [c.replace(' ','_') for c in claim_s.columns]
        policy_s['CUST_ID'] = policy_s['CUST_ID'].astype(int)
        policy_s['CUST_ID'] = policy_s['CUST_ID'].abs()
        claim_s['Claims_Account_Code'] = claim_s['Claims_Account_Code'].astype(int)
        claim_s['Claims_Account_Code'] = claim_s['Claims_Account_Code'].abs()
        st.markdown("Policy Data: -")
        st.dataframe(policy_s)
        st.markdown("Claim Data")
        st.dataframe(claim_s)
        # policy_s.to_excel("PolicyData.xlsx", index=False)
        # claim_s.to_excel('Claim.xlsx', index=False)
        
        server = "adroserver.database.windows.net"
        databasee = "finalDatabase"
        username = "amikars"
        password = "killshot@6911"
        # st.write(claim_s.info())
        with st.spinner():
           cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + databasee + ';UID=' + username + ';PWD=' + password)
           cursor = cnxn.cursor()
           cursor.fast_executemany = True  #Set fast_executemany  = True
           cursor.execute("SELECT count(*) as counti from [dbo].[policy]")
           num = cursor.fetchall()
           st.info(f"Total Records in policies before Data Synthesis {num[0][0]}")
           for index, row in policy_s.iterrows():
               cursor.execute("INSERT INTO [dbo].[policy] (CUST_ID, EXECUTIVE, BODY, MAKE, MODEL, USE_OF_VEHICLE, MODEL_YEAR, CHASSIS_NO, REGN, POLICY_NO, POL_EFF_DATE, POL_EXPIRY_DATE, [SUM INSURED], POL_ISSUE_DATE, PREMIUM2, DRV_DOB, DRV_DLI, VEH_SEATS, PRODUCT, POLICYTYPE, Nationality) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)",
                              row.CUST_ID, row.EXECUTIVE, row.BODY, row.MAKE, row.MODEL, row.USE_OF_VEHICLE, row.MODEL_YEAR, row.CHASSIS_NO, row.REGN, row.POLICY_NO, row.POL_EFF_DATE, row.POL_EXPIRY_DATE, row.SUM_INSURED, row.POL_ISSUE_DATE, row.PREMIUM2, row.DRV_DOB, row.DRV_DLI, row.VEH_SEATS, row.PRODUCT, row.POLICYTYPE, row.Nationality)

           cnxn.commit()
           st.write("Policy Data inserted successfully.")
           cursor.execute("SELECT count(*) as counti from [dbo].[policy]")
           num = cursor.fetchall()
           st.info(f"Total Records in policies after Data Synthesis {num[0][0]}")

           cursor.execute("SELECT count(*) as counti from [dbo].[claims]")
           num = cursor.fetchall()
           st.info(f"Total Records in claim before Data Synthesis {num[0][0]}")

           for index, row in claim_s.iterrows():
               cursor.execute("INSERT INTO [dbo].[claims] ([Claims_Account Code], [Claims_DATE OF _INTIMATION], [Claims_DATE OF _ACCIDENT], [Claims_PLACE OF _LOSS], [Claims_CLAIM NO], Claims_AGE, Claims_TYPE, [Claims_DRIVING _LICENSE ISSUE], [Claims_BODY TYPE], Claims_MAKE, Claims_MODEL, Claims_YEAR, [Claims_CHASIS NO], Claims_REG, [Claims_SUM INSURED], POLICY_NO, [Claims_POLICY START], [Claims_POLICY END], Claims_INTIMATED_AMOUNT, Claims_INTIMATED_SF, Claims_EXECUTIVE, Claims_PRODUCT, Claims_POLICYTYPE, Claims_NATIONALITY)  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",  
                              row.Claims_Account_Code, row.Claims_DATE_OF__INTIMATION, row.Claims_DATE_OF__ACCIDENT, row.Claims_PLACE_OF__LOSS, row.Claims_CLAIM_NO, row.Claims_AGE, row.Claims_TYPE, row.Claims_DRIVING__LICENSE_ISSUE, row.Claims_BODY_TYPE, row.Claims_MAKE, row.Claims_MODEL, row.Claims_YEAR, row.Claims_CHASIS_NO, row.Claims_REG, row.Claims_SUM_INSURED, row.POLICY_NO, row.Claims_POLICY_START, row.Claims_POLICY_END, row.Claims_INTIMATED_AMOUNT, row.Claims_INTIMATED_SF, row.Claims_EXECUTIVE, row.Claims_PRODUCT, row.Claims_POLICYTYPE, row.Claims_NATIONALITY)

           cnxn.commit()
           st.write("Claim Data inserted successfully.")
           cursor.execute("SELECT count(*) as counti from [dbo].[claims]")
           num = cursor.fetchall()
           st.info(f"Total Records in claim After Data Synthesis {num[0][0]}")
           cursor.close()
           st.snow()

# if st.button('Synthetic Data Generation and Insert into SQL'):
#   policy_s,claim_s = make_syhtetic_data(numberOfPolicywithClaim,numberOfPolicywithoutClaim)
#   st.markdown("Policy Data: -")
#   st.dataframe(policy_s)
#   st.markdown("Claim Data")
#   st.dataframe(claim_s)
#   policy_s.to_excel("PolicyData.xlsx",index=False)
#   claim_s.to_excel('Claim.xlsx',index=False)
#   # st.write(policy_s.info())
#   # policy_s.columns = [c.replace(' ','_') for c in policy_s.columns]
#   server = "adfdbserverstore.database.windows.net"#st.text_input("Your Server Name")
#   databasee = "adroinnovate" # st.text_input("Your Database Name")
#   username = "adfadmserve" #st.text_input("User Name")
#   password = "Adfadm@123" #st.text_input("Password",type="password")
  
#   # if st.button('Insert Into SQL'): 
#   st.write('Inserting into SQL')
#   with st.spinner():
#      cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+databasee+';UID='+username+';PWD='+   password)
#      cursor = cnxn.cursor()
#      for index, row in policy_s.iterrows():
#       st.write(row)
#       cursor.execute("INSERT INTO [dbo].[policies] (CUST_ID, EXECUTIVE, BODY, MAKE, MODEL, USE_OF_VEHICLE, MODEL_YEAR, CHASSIS_NO, REGN, POLICY_NO, POL_EFF_DATE, POL_EXPIRY_DATE, [SUM INSURED], POL_ISSUE_DATE, PREMIUM2, DRV_DOB, DRV_DLI, VEH_SEATS, PRODUCT, POLICYTYPE, Nationality) values(?,?)",row.CUST_ID, row.EXECUTIVE, row.BODY, row.MAKE, row.MODEL, row.USE_OF_VEHICLE, row.MODEL_YEAR, row.CHASSIS_NO, row.REGN, row.POLICY_NO, row.POL_EFF_DATE, row.POL_EXPIRY_DATE, row["SUM INSURED"], row.POL_ISSUE_DATE, {row.PREMIUM2}, {row.  DRV_DOB}, {row.DRV_DLI}, {row.VEH_SEATS}, {row.PRODUCT}, {row.POLICYTYPE}, {row.Nationality})")
#     #  cnxn.commit()
#     #  cursor.close()











#   lenthP = len(policy_s.columns)
#   st.dataframe(policy_s.info())
#   for col in policy_s.columns:
#     if policy_s[col].dtype == 'object':
#       if col == policy_s.columns[lenthP-1]:
#         policy_schema = policy_schema + f"[{col}] [varchar] NOT NULL"
#       else:
#         policy_schema = policy_schema + f"[{col}] [varchar] NOT NULL,"  
#     else:
#       if col == policy_s.columns[lenthP-1]:
#         policy_schema = policy_schema + f"[{col}] [int] NOT NULL"
#       else:
#         policy_schema = policy_schema + f"[{col}] [int] NOT NULL,"
#   policy_schema = policy_schema + ") GO"
#   st.markdown(policy_schema)
#   lenthC = len(claim_s.columns)
#   st.dataframe(claim_s.info())
#   for col in claim_s.columns:
#     if claim_s[col].dtype == 'object':
#       if col == claim_s.columns[lenthC-1]:
#         claim_schema = claim_schema + f"[{col}] [varchar] NOT NULL"
#       else:
#         claim_schema = claim_schema + f"[{col}] [varchar] NOT NULL,"  
#     else:
#       if col == claim_s.columns[lenthC-1]:
#         claim_schema = claim_schema + f"[{col}] [int] NOT NULL"
#       else:
#         claim_schema = claim_schema + f"[{col}] [int] NOT NULL,"
#   claim_schema = claim_schema + ") GO"
#   st.markdown(claim_schema)

# st.write('Insert Into the SQL Database')
