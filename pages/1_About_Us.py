import streamlit as st
from utility import check_password

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()


st.set_page_config(layout="wide")

st.header("About Us")

st.divider()

st.write("**Project Scope**")
st.write("1. Build a user-friendly interface for easy input of postal codes to search for nearby childcare centres.")
st.write("2. Implement search functionality to filter childcare centres by location and integrate with postal district information to provide location details and cohort availability.")
st.write("2. Build a chatbot for parents to find out more information on the childcare centres.")

# Add a newline for space
st.write("\n")
st.write("\n")

# Objectives
st.write("**Objectives**")
st.write(" Develop a comprehensive tool to assist parents in identifying nearby childcare centres using their postal code. This tool aims to provide detailed information about available childcare options and streamline the decision-making process for parents.")

# Add a newline for space
st.write("\n")
st.write("\n")

#Data Sources
st.write("**Data Sources**")
st.write("1. Listing of Centres from data.gov.sg")
st.write("2. Listing of Postal Districts")

# Add a newline for space
st.write("\n")
st.write("\n")

st.write("**Features**")
st.write("1. Implement a search algorithm to filter childcare centres based on the user's postal code.")
st.write("2. Display a list of nearby childcare centres with relevant details and their cohort availability.")
st.write("3. Chatbot to query for more information on the childcare centres.")

# Add a newline for space
st.write("\n")
st.write("\n")
st.write("**Creator**")
st.write("Alicia Toh | DSTA")


# Add a newline for space
st.write("\n")
st.write("\n")

st.write("**Note**")
with st.expander("Important Notice:"):
    st.write('''
            This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.
        
            Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.
             
            Always consult with qualified professionals for accurate and personalized advice.
    ''')