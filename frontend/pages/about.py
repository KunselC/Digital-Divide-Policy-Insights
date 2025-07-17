"""
About page for Digital Divide Policy Insights.
"""

import streamlit as st


def render_about():
    """Render professional about page with project information."""
    from components.ui_components import render_section_header, render_info_box
    
    render_section_header(
        "About This Project", 
        "Learn more about the Digital Divide Policy Insights platform and its mission"
    )
    
    _render_project_overview()
    _render_key_features()
    _render_policies_analyzed()
    _render_data_sources()
    _render_technology_stack()
    _render_contact_info()


def _render_project_overview():
    """Render professional project overview section."""
    from components.ui_components import render_info_box
    
    st.markdown("""
    ## 🎯 Mission & Vision
    
    The **Digital Divide Policy Insights Platform** provides comprehensive analysis of technology policies 
    aimed at bridging the digital divide in the United States. Our mission is to make policy 
    effectiveness data accessible, understandable, and actionable for researchers, policymakers, 
    and the general public.
    
    ### Why This Matters
    
    The digital divide affects millions of Americans, limiting access to education, healthcare, 
    employment opportunities, and essential services. By analyzing policy effectiveness through 
    data-driven insights, we can help identify what works and guide future policy decisions.
    """)
    
    render_info_box(
        "🎯 <strong>Our Goal:</strong> To bridge the gap between policy implementation and measurable outcomes in digital equity initiatives.",
        "info"
    )


def _render_key_features():
    """Render professional key features section."""
    from components.ui_components import render_section_header
    
    render_section_header("Platform Features", "Comprehensive tools for policy analysis and insights")
    
    # Create feature cards in columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>📊 Policy Dashboard</h4>
            <p>Comprehensive overview of all digital divide policies with real-time effectiveness scores and implementation status.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <h4>📈 Trend Analysis</h4>
            <p>Historical data visualization showing the measurable impact of policies on digital access metrics over time.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <h4>🤖 AI Assistant</h4>
            <p>Interactive chatbot powered by advanced AI to answer policy questions and provide detailed explanations.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>📋 Policy Analysis</h4>
            <p>Deep-dive analysis of individual policies including effectiveness metrics, implementation challenges, and outcomes.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <h4>🎯 Demographics Breakdown</h4>
            <p>Detailed analysis of digital access disparities by income level, geographic location, and age demographics.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <h4>📊 Data Visualization</h4>
            <p>Interactive charts and graphs with professional styling that make complex policy data easy to understand.</p>
        </div>
        """, unsafe_allow_html=True)


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
