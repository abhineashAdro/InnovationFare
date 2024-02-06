import streamlit as st

progress_value = 0  # Initial progress value
progress_text = "Operation in progress. Please wait."
my_bar = st.progress(progress_value, text=progress_text)

# Button clicks
button1 = st.button("Button 1")
button2 = st.button("Button 2")
button3 = st.button("Button 3")
button4 = st.button("Button 4")

# Handling button clicks
if button1:
    progress_value = 25
elif button2:
    progress_value = 50
elif button3:
    progress_value = 75
elif button4:
    progress_value = 100

# Update progress bar dynamically
my_bar.progress(progress_value, text=progress_text)

# Rerun button
st.button("Rerun")
