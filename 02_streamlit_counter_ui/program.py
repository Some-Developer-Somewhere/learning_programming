# Install python module streamlit:
# > python -m pip install streamlit
#
# Run this python streamlit application (dont use the "python" command):
# > streamlit run program.py
#
# Use this program/web server:
# It should start your browser automatically with the correct url

import streamlit as st

# Initialize the count in session state if not already present
if 'count' not in st.session_state:
    st.session_state.count = 0

st.title("Counter")

# Increment count when the button is pressed
if st.button('Count'):
    st.session_state.count += 1

st.write(f"Current Count: {st.session_state.count}")
