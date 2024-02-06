import streamlit as st

if 'but_a' not in st.session_state:
    st.session_state.disabled = True

button_a = st.button('a', key='but_a')
button_b = st.button('b', key='but_b')

if button_a:
    st.session_state.disabled = False
if button_b:
    st.session_state.disabled = True

button_c = st.button('c', key='but_c', disabled=st.session_state.disabled)

st.write(button_a, button_b, button_c)
