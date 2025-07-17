"""
About page for Digital Divide Policy Insights.
"""

import streamlit as st


def render_about():
    """Render about page with project information."""
    st.header("ℹ️ About This Project")
    
    _render_project_overview()
    _render_key_features()
    _render_policies_analyzed()
    _render_data_sources()
    _render_technology_stack()
    _render_contact_info()


def _render_project_overview():
    """Render project overview section."""
    st.markdown("""
    ## Digital Divide Policy Insights Platform
    
    This platform provides comprehensive analysis of technology policies aimed at 
    bridging the digital divide in the United States. Our goal is to make policy 
    effectiveness data accessible and understandable for researchers, policymakers, 
    and the general public.
    """)


def _render_key_features():
    """Render key features section."""
    st.markdown("""
    ### Key Features:
    
    - **Policy Dashboard**: Overview of all digital divide policies and their effectiveness scores
    - **Trend Analysis**: Historical data showing the impact of policies on digital access metrics
    - **AI Chatbot**: Interactive assistant for policy questions and explanations
    - **Data Visualization**: Interactive charts and graphs showing policy effectiveness
    - **Demographics Analysis**: Breakdown of digital access by income, geography, and age
    """)


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
