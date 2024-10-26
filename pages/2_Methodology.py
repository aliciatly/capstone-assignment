import streamlit as st
from utility import check_password

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()


st.set_page_config(layout="wide")

st.header("Methodology")

st.divider()

file_path = 'data/capstone.drawio.png'
st.image(file_path)