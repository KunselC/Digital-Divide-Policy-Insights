"""
Digital Divide Policy Insights - Main Application

A Streamlit frontend for analyzing technology policies and their effectiveness 
in bridging the digital divide. Features interactive dashboards, data visualization,
and an AI-powered chatbot for policy inquiries.
"""

import streamlit as st
import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import STREAMLIT_CONFIG, PAGES, APP_TITLE, APP_SUBTITLE
from components.ui_components import load_custom_css, render_header, create_sidebar_navigation
from pages.dashboard import render_dashboard
from pages.policy_analysis import render_policy_analysis
from pages.data_trends import render_data_trends
from pages.chatbot import render_chatbot
from pages.about import render_about


def configure_app():
    """Configure Streamlit app settings."""
    st.set_page_config(**STREAMLIT_CONFIG)
    load_custom_css()


def main():
    """Main application entry point."""
    configure_app()
    
    render_header(APP_TITLE, APP_SUBTITLE)
    
    # Navigation
    selected_page = create_sidebar_navigation(PAGES)
    
    # Route to appropriate page
    page_handlers = {
        "Dashboard": render_dashboard,
        "Policy Analysis": render_policy_analysis,
        "Data Trends": render_data_trends,
        "AI Chatbot": render_chatbot,
        "About": render_about
    }
    
    handler = page_handlers.get(selected_page)
    if handler:
        handler()
    else:
        st.error(f"Page '{selected_page}' not found.")


if __name__ == "__main__":
    main()
