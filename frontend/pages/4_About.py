"""
About Page
"""

import streamlit as st
import sys
import os

# Add the parent directory to the Python path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.ui_components import (
    display_page_header, 
    render_info_box, 
    render_section_header, 
    load_custom_css,
    display_interactive_background,
    render_feature_card
)


def render_about_page():
    """Render professional about page with project information."""
    display_page_header(
        title="About NetEquity", 
        subtitle="What this platform is all about.",
        icon_name="about.svg"
    )
    
    _render_project_overview()
    _render_key_features()
    _render_policies_analyzed()
    _render_data_sources()
    _render_technology_stack()
    _render_contact_info()


def _render_project_overview():
    """Render professional project overview section."""
    
    st.markdown("""
    ## Our Mission
    
    We built **NetEquity** to make data about the digital divide easier for everyone to understand. 
    Our goal is to show how different policies are working (or not working) so that we can find 
    better ways to ensure everyone has access to technology.
    
    ### Why it Matters
    
    Being disconnected today means missing out on school, jobs, and even healthcare. 
    By looking at the data, we can help policymakers make smarter decisions and build a more equitable future.
    """)
    
    render_info_box(
        "<strong>Our Goal:</strong> To connect policy decisions to real-world results.",
        "info"
    )


def _render_key_features():
    """Render professional key features section."""
    render_section_header("What You Can Do Here", "A quick tour of the platform's features")
    
    # Create feature cards in columns
    col1, col2 = st.columns(2)
    
    with col1:
        render_feature_card(
            "View the Dashboard",
            "Get a quick overview of all policies and their effectiveness scores.",
            "dashboard.svg"
        )
        render_feature_card(
            "Explore Trends",
            "See how digital access has changed over time for different groups.",
            "data-trends.svg"
        )
        render_feature_card(
            "Chat with the AI",
            "Ask questions in plain English to get simple answers about complex policies.",
            "chatbot.svg"
        )
    
    with col2:
        render_feature_card(
            "Analyze Policies",
            "Dig into the details of specific policies to see what makes them work.",
            "policy-analysis.svg"
        )
        render_feature_card(
            "Check Demographics",
            "See how the digital divide affects people based on income, location, and age.",
            "trends.svg"
        )
        render_feature_card(
            "Visualize Data",
            "Interact with charts and graphs that bring the data to life.",
            "policy.svg"
        )


def _render_policies_analyzed():
    """Render policies analyzed section."""
    st.markdown("""
    ### Policies Analyzed:
    
    1. **Digital Equity Act (2021)** - Federal legislation ensuring equitable digital access
    2. **Affordable Connectivity Program (2021)** - Discounted internet for eligible households  
    3. **Rural Digital Opportunity Fund (2020)** - FCC program for rural broadband infrastructure
    
    Each policy is evaluated based on multiple effectiveness metrics including:
    - Broadband access improvements
    - Digital literacy enhancement
    - Cost-effectiveness
    - Geographic coverage
    """)


def _render_data_sources():
    """Render data sources section."""
    st.markdown("""
    ### Data Sources:
    
    - **Federal Communications Commission (FCC)** - Broadband deployment and adoption data
    - **National Telecommunications and Information Administration (NTIA)** - Digital equity metrics
    - **U.S. Census Bureau** - Demographic and socioeconomic data
    - **Pew Research Center** - Digital divide research and surveys
    - **Bureau of Economic Analysis** - Economic impact assessments
    """)


def _render_technology_stack():
    """Render technology stack section."""
    st.markdown("""
    ### Technology Stack:
    
    **Backend:**
    - Python Flask API
    - RESTful architecture
    - Modular service layer design
    - Data validation and error handling
    
    **Frontend:**
    - Streamlit framework
    - Plotly for interactive visualizations
    - Responsive design
    - Component-based architecture
    
    **Data Processing:**
    - Pandas for data manipulation
    - NumPy for numerical computations
    - Statistical analysis libraries
    """)


def _render_contact_info():
    """Render contact information section."""
    st.markdown("""
    ### Project Information:
    
    This is an educational template project designed to demonstrate best practices 
    in policy analysis platform development. The codebase follows modern software 
    engineering principles including:
    
    - **Modular Architecture**: Clean separation of concerns
    - **API Design**: RESTful endpoints with proper error handling
    - **Code Quality**: Comprehensive documentation and type hints
    - **Scalability**: Designed for easy extension and deployment
    
    ### Getting Started:
    
    To explore the codebase or contribute to the project:
    1. Review the API documentation in the backend code
    2. Examine the modular frontend components
    3. Check the data models and service layers
    4. Review the configuration and deployment scripts
    """)
    
    # Add expandable sections for technical details
    with st.expander("View Technical Architecture"):
        st.markdown("""
        **Frontend Structure:**
        ```
        frontend/
        ├── app.py              # Main application entry point
        ├── config.py           # Configuration settings
        ├── components/         # Reusable UI components
        ├── pages/              # Individual page modules
        └── utils/              # Utility functions
        ```
        
        **Backend Structure:**
        ```
        api/
        ├── app.py              # Flask application factory
        ├── routes/             # API endpoint definitions
        ├── services/           # Business logic layer
        ├── models/             # Data models
        └── utils/              # Helper utilities
        ```
        """)
    
    with st.expander("View Development Guidelines"):
        st.markdown("""
        **Code Standards:**
        - Type hints for all function parameters and returns
        - Comprehensive docstrings following Google style
        - Modular design with single responsibility principle
        - Error handling with user-friendly messages
        - Consistent naming conventions
        
        **Best Practices:**
        - Configuration through environment variables
        - API versioning and backward compatibility
        - Responsive UI design
        - Performance optimization
        - Security considerations
        """)

def main():
    """Main function to set up and render the page."""
    from components.ui_components import load_custom_css, display_interactive_background
    
    st.set_page_config(
        page_title="About - NetEquity",
        layout="wide"
    )
    load_custom_css()
    display_interactive_background()
    render_about_page()

if __name__ == "__main__":
    main()
