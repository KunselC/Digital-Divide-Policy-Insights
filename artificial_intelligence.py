#Name - The AI ChatBot
import streamlit as st
import openai
import os
import sys
from typing import List
# OPTIONAL: Add parent directory to import other modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Remove api_client import — no longer needed
# from utils.api_client import api_client
from config import CHATBOT_SUGGESTIONS
from components.ui_components import display_page_header, load_custom_css, display_interactive_background
def render_chatbot_page():
    """Render AI-powered policy chatbot page."""
    display_page_header(
        title="AI Policy Assistant",
        subtitle="Ask questions about digital divide policies in plain English.",
        icon_name="chatbot.svg"
    )
    _initialize_chat_session()
    _render_chat_interface()
    _render_sidebar_suggestions()
def _initialize_chat_session():
    """Initialize chat session state."""
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hi! I’m here to help you understand digital divide policies. What would you like to know?"
            }
        ]
def _render_chat_interface():
    """Render the main chat interface."""
    # Display existing chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    # Handle new user input
    if prompt := st.chat_input("What do you want to know?"):
        _handle_user_message(prompt)
def _handle_user_message(prompt: str):
    """Handle a new message from the user."""
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    # Get bot response
    with st.chat_message("assistant"):
        response_text = _get_bot_response(prompt)
        st.markdown(response_text)
    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": response_text})
def _get_bot_response(prompt: str) -> str:
    """
    Query OpenAI GPT model with the full conversation history.
    """
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    try:
        with st.spinner("Thinking..."):
            # Limit memory if needed: messages = st.session_state.messages[-10:]
            response = openai.ChatCompletion.create(
                model="gpt-4",  # or "gpt-3.5-turbo"
                messages=st.session_state.messages,
                temperature=0.7
            )
            return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Sorry, an error occurred: {str(e)}"
def _render_sidebar_suggestions():
    """Render sidebar with conversation starter buttons."""
    with st.sidebar:
        st.subheader("Don’t know where to start?")
        st.write("Try one of these conversation starters:")
        for suggestion in CHATBOT_SUGGESTIONS:
            if st.button(suggestion, key=f"sidebar_{suggestion}"):
                _handle_user_message(suggestion)
def main():
    """Main function to initialize and render the app."""
    st.set_page_config(
        page_title="AI Chatbot - NetEquity",
        layout="wide"
    )
    load_custom_css()
    display_interactive_background()
    render_chatbot_page()
if __name__ == "__main__":
    main()