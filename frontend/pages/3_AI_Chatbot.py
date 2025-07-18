"""
AI Chatbot Page
"""

import streamlit as st
from typing import List, Dict
import sys
import os

# Add the parent directory to the Python path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.api_client import api_client
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
            {"role": "assistant", "content": "Hi! I'm here to help you understand digital divide policies. What would you like to know?"}
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
    """
    Handle new user message and generate bot response.
    
    Args:
        prompt: User's input message
    """
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display bot response
    with st.chat_message("assistant"):
        response_text = _get_bot_response(prompt)
        st.markdown(response_text)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response_text})


def _get_bot_response(prompt: str) -> str:
    """
    Get response from the chatbot API.
    
    Args:
        prompt: User's input message
        
    Returns:
        Bot response text
    """
    with st.spinner("Thinking..."):
        response_data = api_client.post("/api/chatbot/chat", {"message": prompt})
        
        if response_data:
            bot_response = response_data.get('bot_response', 
                                           "Sorry, I couldn't find an answer to that.")
            
            # Handle suggestions if available
            suggestions = response_data.get('suggestions', [])
            if suggestions:
                _render_response_suggestions(suggestions)
            
            return bot_response
        else:
            return "Sorry, I'm having trouble connecting. Please try again in a moment."


def _render_response_suggestions(suggestions: List[str]):
    """
    Render suggestion buttons for follow-up questions.
    
    Args:
        suggestions: List of suggested follow-up questions
    """
    st.markdown("**Here are some other questions you could ask:**")
    
    for i, suggestion in enumerate(suggestions):
        button_key = f"suggestion_{len(st.session_state.messages)}_{i}"
        if st.button(suggestion, key=button_key):
            _handle_user_message(suggestion)


def _render_sidebar_suggestions():
    """Render sidebar with suggested conversation starters."""
    with st.sidebar:
        st.subheader("Don't know where to start?")
        st.write("Try one of these conversation starters:")
        
        for suggestion in CHATBOT_SUGGESTIONS:
            if st.button(suggestion, key=f"sidebar_{suggestion}"):
                _handle_user_message(suggestion)


def main():
    """Main function to set up and render the page."""
    from components.ui_components import load_custom_css, display_interactive_background
    
    st.set_page_config(
        page_title="AI Chatbot - NetEquity",
        layout="wide"
    )
    load_custom_css()
    display_interactive_background()
    render_chatbot_page()

if __name__ == "__main__":
    main()
