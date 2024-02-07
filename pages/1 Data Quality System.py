import streamlit as st


dq_system_image = 'Images/Data Quality.jpg'
col1,col2,col3,col4,col5 = st.columns(5)

# First row
with col1:
    st.image(dq_system_image,width=120)
    st.subheader("Data Quality System")
    st.caption("Let's see what Data Quality system is?")
st.progress(10)
st.write("# Data Quality System")
st.divider()
coll1,coll2,coll3,coll4 = st.columns(4)

with coll1:
    st.image('Images/data rules.PNG',width=50)
    st.text('Data Rules')#,divider=True)
with coll2:
    st.image('Images/rules execution.PNG',width=45)
    st.text('Rules Execution')
with coll3:
    st.image('Images/Exception Handling.PNG',width=50)
    st.text('Exception Handling')
with coll4:
    st.image('Images/Reporting.PNG',width=44)
    st.text('Reporting')
st.divider()
st.markdown(
    """
            - Agnostic data quality system integrated into the pipeline.
            - Connects to both source and exception databases.
            - User-friendly portal for rule creation based on specific needs.
            - Rules can be executed on-demand by users.
            - Captures exceptions in a structured format in the exception database.
            - Facilitates comprehensive analysis and reporting for improved data quality and reliability.

            """)