import streamlit as st

st.title("Buttons and Progress")

progress_value = 0  # Initial progress value
progress_text = "Pipeline progress = " + str(progress_value) + "%"
my_bar = st.progress(progress_value, text=progress_text)

col1,col2,col3,col4=st.columns(4)
if "is_button2_disabled" not in st.session_state:
    st.session_state.is_button2_disabled = True
if "is_button3_disabled" not in st.session_state:
    st.session_state.is_button3_disabled = True
if "is_button4_disabled" not in st.session_state:
    st.session_state.is_button4_disabled = True

with col1:
    # Button 1: toggle button for Button 2
    if st.button("Button 1", key="button1"):
        st.session_state.is_button2_disabled = not st.session_state.is_button2_disabled
        progress_value = 25
        progress_text = "Pipeline progress = " + str(progress_value) + "%"
with col2:
    # Button 2: toggle button for Button 3
    if st.button("Button 2", key="button2", disabled=st.session_state.is_button2_disabled):
        st.session_state.is_button3_disabled = not st.session_state.is_button3_disabled
        progress_value = 50
        progress_text = "Pipeline progress = " + str(progress_value) + "%"
with col3:
    # Button 3: toggle button for Button 4
    if st.button("Button 3", key="button3", disabled=st.session_state.is_button3_disabled):
        st.session_state.is_button4_disabled = not st.session_state.is_button4_disabled
        progress_value = 75
        progress_text = "Pipeline progress = " + str(progress_value) + "%"
with col4:
    # Button 4: action button
    if st.button("Button 4", key="button4", disabled=st.session_state.is_button4_disabled):
        progress_value = 100
        progress_text = "Pipeline progress = " + str(progress_value) + "%"
        st.write("Action button clicked!")
        st.balloons()
# Update progress bar dynamically
my_bar.progress(progress_value, text=progress_text)