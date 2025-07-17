"""
AI chatbot page for Digital Divide Policy Insights.
"""

import streamlit as st
from typing import List, Dict

from utils.api_client import api_client
from config import CHATBOT_SUGGESTIONS


def render_chatbot():
    """Render AI-powered policy chatbot page."""
    st.header("🤖 AI Policy Assistant")
    st.markdown("Ask me anything about digital divide policies and their effectiveness!")
    
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
            st.session_state.messages.append({"role": "user", "content": suggestion})
            st.experimental_rerun()


def _render_sidebar_suggestions():
    """Render quick start suggestions in sidebar."""
    st.sidebar.subheader("Quick Questions")
    
    for i, suggestion in enumerate(CHATBOT_SUGGESTIONS):
        button_key = f"sidebar_{suggestion}_{i}"
        if st.sidebar.button(suggestion, key=button_key):
            st.session_state.messages.append({"role": "user", "content": suggestion})
            st.experimental_rerun()


def _clear_chat_history():
    """Clear chat history (utility function)."""
    if st.sidebar.button("Clear Chat History"):
        st.session_state.messages = []
        st.experimental_rerun()
