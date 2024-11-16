import streamlit as st

# Configure the page layout and appearance
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Display header
st.header("🤖 Chatbot main page")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm a basic chatbot. How can I help you today?"},
        {"role": "user", "content": "this is a test for a user input"}
    ]
# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

