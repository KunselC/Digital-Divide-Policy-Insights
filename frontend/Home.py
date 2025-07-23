"""
NetEquity: Digital Divide Policy Insights

This is the main entry point for the Streamlit application.
"""

import streamlit as st
import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import STREAMLIT_CONFIG, APP_TITLE
from components.ui_components import (
    load_custom_css, 
    display_interactive_background
)

def main():
    """Main function to run the Streamlit application."""
    st.set_page_config(**STREAMLIT_CONFIG)
    load_custom_css()
    display_interactive_background()
    
    st.title(f"Welcome to {APP_TITLE}")
    st.markdown("Select a page from the sidebar to explore digital divide policies and data.")
    st.sidebar.success("Select a page above.")

if __name__ == "__main__":
    main()
