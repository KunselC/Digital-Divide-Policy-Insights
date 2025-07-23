"""
NetEquity - Digital Divide Policy Insights

Main entry point for the Streamlit application.
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
    display_3d_globe_component,
    display_simple_3d_globe
)

def render_dashboard_tab():
    """Renders the main dashboard content."""
    display_page_header(
        title="NetEquity Dashboard",
        subtitle="Digital divide insights through data visualization and AI-powered analysis.",
        icon_name="dashboard.svg"
    )
    
    # Platform overview
    st.markdown("""
    <div class="content-box">
        <h2>Platform Overview</h2>
        <p>Welcome to NetEquity! This platform provides tools and insights for understanding 
        and addressing the digital divide through data visualization and AI-powered insights.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Page summaries
    st.subheader("Available Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="content-box">
            <h4>Data Trends</h4>
            <p>Explore temporal patterns in digital access and connectivity data across countries and regions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="content-box">
            <h4>AI Assistant</h4>
            <p>Chat with AI about digital policies or generate policy petitions based on data insights.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="content-box">
            <h4>ML Predictions</h4>
            <p>Use machine learning models to predict digital presence factors and analyze feature importance.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Second row
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="content-box">
            <h4>3D Globe Visualization</h4>
            <p>Interactive 3D model of global submarine cable networks (see next tab).</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="content-box">
            <h4>About Platform</h4>
            <p>Learn about the platform's features, technology stack, and mission.</p>
        </div>
        """, unsafe_allow_html=True)

def render_globe_tab():
    """Renders the 3D globe visualization tab."""
    display_page_header(
        title="Global Submarine Cable Network",
        subtitle="Interactive 3D visualization of the world's digital infrastructure.",
        icon_name="dashboard.svg"
    )
    
    st.markdown("""
    <div class="content-box">
        <p>This interactive 3D visualization shows the global network of submarine fiber optic cables 
        that form the backbone of the internet. Choose between the detailed cable model or a lightweight globe view.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create sub-tabs for different 3D views
    detailed_tab, simple_tab = st.tabs(["🌊 Submarine Cables (Detailed)", "🌍 Globe (Lightweight)"])
    
    with detailed_tab:
        st.markdown("""
        <div class="content-box">
            <h4>Detailed Submarine Cable Network</h4>
            <p>This high-detail 3D model shows the actual underwater fiber optic cables. 
            <strong>Note:</strong> This model is 9.7MB and may take 10-30 seconds to load.</p>
        </div>
        """, unsafe_allow_html=True)
        
        display_3d_globe_component()
    
    with simple_tab:
        st.markdown("""
        <div class="content-box">
            <h4>Interactive Globe View</h4>
            <p>A lightweight 3D globe that loads instantly with smooth mouse interaction. 
            Perfect for users who want quick visualization without waiting for large model files.</p>
        </div>
        """, unsafe_allow_html=True)
        
        display_simple_3d_globe()

def main():
    """Main function to set up and render the application."""
    st.set_page_config(**STREAMLIT_CONFIG)
    load_custom_css()
    display_interactive_background()

    # Create tabs for dashboard and 3D globe
    tab1, tab2 = st.tabs(["Dashboard", "3D Globe"])

    with tab1:
        render_dashboard_tab()
    
    with tab2:
        render_globe_tab()

if __name__ == "__main__":
    main()
