from email import message
from urllib import response
import streamlit as st 
import numpy as np


# !Minimal example on how to use st.chat_message
# !using with notation
# with st.chat_message("user"):
#     st.write("Hello 👋 Human")
#     st.bar_chart(np.random.randn(30, 3))

# !Using the call methods directly in the returned objects
# message = st.chat_message("assistant")
# message.write("Hello human")
# message.bar_chart(np.random.randn(30, 3))

# !Building a bot that mirrors input using st.chat_message and st.chat_input
st.title("Echo Bot")

# Initialise chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(f"You\n\n{prompt}")
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # adding chatbot's response within the if block
    response = f"Agent\n\n{prompt}"

    with st.chat_message("assistant"):
        st.markdown(response)
    # Add asssitnat response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
