"""
AI chatbot page for Digital Divide Policy Insights.
"""

import streamlit as st
from typing import List, Dict

from utils.api_client import api_client
from config import CHATBOT_SUGGESTIONS
from components.ui_components import render_section_header


def render_chatbot_page():
    """Render AI-powered policy chatbot page."""
    render_section_header("AI Policy Assistant", "Ask me anything about digital divide policies and their effectiveness!")
    
    _initialize_chat_session()
    _render_chat_interface()
    _render_sidebar_suggestions()


def _initialize_chat_session():
    """Initialize chat session state."""
    if "messages" not in st.session_state:
        st.session_state.messages = []


def _render_chat_interface():
    """Render the main chat interface."""
    # Display existing chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Handle new user input
    if prompt := st.chat_input("Ask about digital divide policies..."):
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
                                           'Sorry, I could not process your request.')
            
            # Handle suggestions if available
            suggestions = response_data.get('suggestions', [])
            if suggestions:
                _render_response_suggestions(suggestions)
            
            return bot_response
        else:
            return "Sorry, I'm having trouble connecting to the server. Please try again later."


def _render_response_suggestions(suggestions: List[str]):
    """
    Render suggestion buttons for follow-up questions.
    
    Args:
        suggestions: List of suggested follow-up questions
    """
    st.markdown("**You might also ask:**")
    
    for i, suggestion in enumerate(suggestions):
        button_key = f"suggestion_{len(st.session_state.messages)}_{i}"
        if st.button(suggestion, key=button_key):
            _handle_user_message(suggestion)


def _render_sidebar_suggestions():
    """Render suggested questions in the sidebar."""
    with st.sidebar:
        st.subheader("Try asking:")
        for suggestion in CHATBOT_SUGGESTIONS:
            if st.button(suggestion, key=f"sidebar_{suggestion}"):
                _handle_user_message(suggestion)

if __name__ == "__main__":
    from components.ui_components import load_custom_css
    st.set_page_config(layout="wide", page_title="AI Chatbot - Digital Divide Policy Insights", page_icon="frontend/assets/icons/chatbot.svg")
    load_custom_css()
    render_chatbot_page()
