"""
NetEquity Dashboard - Main Entry Point

This is the main entry point for the Streamlit application.
"""

import streamlit as st
import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import STREAMLIT_CONFIG
from components.ui_components import (
    display_page_header,
    load_custom_css,
    display_interactive_background,
    display_3d_globe_component
)

def render_dashboard_tab():
    """Renders the content for the dashboard tab."""
    display_page_header(
        title="Dashboard",
        subtitle="Platform overview and quick navigation to key features.",
        icon_name="dashboard.svg"
    )
    
    # Platform overview in content box
    st.markdown("""
    <div class="content-box">
        <h2>Platform Overview</h2>
        <p>Welcome to NetEquity! This platform provides tools and insights for understanding 
        and addressing the digital divide through data visualization and AI-powered insights.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Page summaries
    st.subheader("Page Summaries")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="content-box">
            <h4>Data Trends</h4>
            <p>Explore temporal patterns in digital access and connectivity data.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="content-box">
            <h4>AI Assistant</h4>
            <p>Chat with AI about digital policies or generate policy petitions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="content-box">
            <h4>ML Predictions</h4>
            <p>Use machine learning to predict digital presence factors.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="content-box">
            <h4>3D Globe</h4>
            <p>Interactive visualization of global submarine cable networks (see next tab).</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="content-box">
            <h4>About</h4>
            <p>Learn about the platform's features and technology.</p>
        </div>
        """, unsafe_allow_html=True)

def render_globe_tab():
    """Renders the 3D globe visualization tab."""
    st.subheader("Interactive 3D Globe")
    st.markdown("""
        <div class="content-box">
            <p>This interactive 3D model visualizes the global network of submarine fiber optic cables. Rotate the globe to explore the intricate web that connects our world.</p>
        </div>
    """, unsafe_allow_html=True)
    
    display_3d_globe_component()

def main():
    """Main function to set up and render the page."""
    st.set_page_config(**STREAMLIT_CONFIG)
    load_custom_css()
    display_interactive_background()

    tab1, tab2 = st.tabs(["Dashboard", "3D Globe"])

    with tab1:
        render_dashboard_tab()
    
    with tab2:
        render_globe_tab()


if __name__ == "__main__":
    main()
