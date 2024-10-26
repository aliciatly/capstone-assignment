import streamlit as st
from utility import check_password
from logics.customer_query_handler import process_user_message 
#process_user_message



# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()


st.set_page_config(layout="wide")

st.header("Childcare Centre Chatbot")

st.divider()

st.write("We can provide you more information on the childcare centres near your area:)")
st.write("Please state the area which you want to search.")
#fetcheed_api_key = os.getenv("API_KEY")
#genai.configure(api_key = fetcheed_api_key)


#simple LLM chatbot
#chat = model.start_chat()
#def LLM_Response(question):
 #   response = chat.send_message(question,stream=True)
  #  return response


user_quest = st.text_input("Ask a question:")
btn = st.button("Submit")

if btn and user_quest:
    st.toast(f"User Input Submitted - {user_quest}")
    st.divider()
    response = process_user_message(user_quest)
    st.write(response)


