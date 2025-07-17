"""
UI styling and component utilities for the Digital Divide Policy frontend.
"""

import streamlit as st


def load_custom_css():
    """Load custom CSS styles for the application."""
    st.markdown("""
    <style>
        .main-header {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .metric-card {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 10px;
            border-left: 4px solid #667eea;
            margin: 0.5rem 0;
        }
        .policy-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 1rem 0;
            border-left: 4px solid #28a745;
        }
        .chat-container {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
        }
    </style>
    """, unsafe_allow_html=True)


def render_header(title: str, subtitle: str):
    """
    Render the main application header.
    
    Args:
        title: Main title text
        subtitle: Subtitle text
    """
    st.markdown(f"""
    <div class="main-header">
        <h1>📊 {title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def render_policy_card(policy: dict):
    """
    Render a policy information card.
    
    Args:
        policy: Policy data dictionary
    """
    st.markdown(f"""
    <div class="policy-card">
        <h3>{policy['name']}</h3>
        <p><strong>Description:</strong> {policy['description']}</p>
        <p><strong>Status:</strong> {policy['status'].title()}</p>
        <p><strong>Implementation Date:</strong> {policy['implementation_date']}</p>
    </div>
    """, unsafe_allow_html=True)


def format_metric_value(value, format_type: str = "auto") -> str:
    """
    Format metric values for display.
    
    Args:
        value: The value to format
        format_type: Type of formatting to apply
        
    Returns:
        Formatted string value
    """
    if format_type == "percentage":
        return f"{value:.1f}%" if isinstance(value, (int, float)) else str(value)
    elif format_type == "currency":
        return f"${value:,.0f}" if isinstance(value, (int, float)) else str(value)
    elif format_type == "number":
        return f"{value:,.1f}" if isinstance(value, (int, float)) else str(value)
    else:
        return f"{value:,.1f}" if isinstance(value, (int, float)) else str(value)


def create_sidebar_navigation(pages: list, current_page: str = None) -> str:
    """
    Create sidebar navigation.
    
    Args:
        pages: List of page names
        current_page: Currently selected page
        
    Returns:
        Selected page name
    """
    st.sidebar.title("Navigation")
    return st.sidebar.selectbox(
        "Choose a page:",
        pages,
        index=pages.index(current_page) if current_page in pages else 0
    )
