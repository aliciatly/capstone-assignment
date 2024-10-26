import streamlit as st
from utility import check_password

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()


st.set_page_config(layout="wide")

st.header("Main")

st.divider()

st.write("This is a Streamlit App that can assist parents in identifying nearby childcare centres in their area.")
file_path = 'data/family.png'
st.image(file_path)
