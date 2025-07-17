"""
UI styling and component utilities for the Digital Divide Policy frontend.
"""

import streamlit as st


"""
UI styling and component utilities for the Digital Divide Policy frontend.
"""

import streamlit as st


def load_custom_css():
    """Load professional custom CSS styles for the application."""
    st.markdown("""
    <style>
        /* Import Professional Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Global Variables */
        :root {
            --primary-color: #2563eb;
            --primary-dark: #1d4ed8;
            --secondary-color: #64748b;
            --accent-color: #0ea5e9;
            --success-color: #059669;
            --warning-color: #d97706;
            --error-color: #dc2626;
            --background-primary: #ffffff;
            --background-secondary: #f8fafc;
            --background-tertiary: #f1f5f9;
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --text-muted: #64748b;
            --border-color: #e2e8f0;
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            --radius-sm: 6px;
            --radius-md: 8px;
            --radius-lg: 12px;
        }
        
        /* Base Styles */
        .stApp {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        /* Hide Streamlit Branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Main Content Area */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }
        
        /* Professional Header */
        .main-header {
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
            color: white;
            padding: 3rem 2rem;
            border-radius: var(--radius-lg);
            margin-bottom: 2.5rem;
            text-align: center;
            position: relative;
            overflow: hidden;
            box-shadow: var(--shadow-lg);
        }
        
        .main-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 100" fill="white" opacity="0.1"><polygon points="0,0 0,100 1000,80 1000,0"/></svg>');
            background-size: cover;
        }
        
        .main-header h1 {
            font-size: 2.5rem;
            font-weight: 700;
            margin: 0 0 0.5rem 0;
            position: relative;
            z-index: 1;
        }
        
        .main-header p {
            font-size: 1.1rem;
            font-weight: 400;
            margin: 0;
            opacity: 0.9;
            position: relative;
            z-index: 1;
        }
        
        /* Professional Cards */
        .metric-card {
            background: var(--background-primary);
            padding: 1.5rem;
            border-radius: var(--radius-lg);
            border: 1px solid var(--border-color);
            margin: 1rem 0;
            box-shadow: var(--shadow-sm);
            transition: all 0.2s ease;
            position: relative;
        }
        
        .metric-card:hover {
            box-shadow: var(--shadow-md);
            transform: translateY(-2px);
        }
        
        .metric-card::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 4px;
            background: var(--primary-color);
            border-radius: var(--radius-sm) 0 0 var(--radius-sm);
        }
        
        .policy-card {
            background: var(--background-primary);
            padding: 2rem;
            border-radius: var(--radius-lg);
            border: 1px solid var(--border-color);
            margin: 1.5rem 0;
            box-shadow: var(--shadow-sm);
            transition: all 0.2s ease;
            position: relative;
        }
        
        .policy-card:hover {
            box-shadow: var(--shadow-md);
            transform: translateY(-2px);
        }
        
        .policy-card::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 4px;
            background: var(--success-color);
            border-radius: var(--radius-sm) 0 0 var(--radius-sm);
        }
        
        .policy-card h3 {
            color: var(--text-primary);
            font-weight: 600;
            margin: 0 0 1rem 0;
            font-size: 1.25rem;
        }
        
        .policy-card p {
            color: var(--text-secondary);
            margin: 0.5rem 0;
            line-height: 1.6;
        }
        
        /* Status Badges */
        .status-badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.025em;
        }
        
        .status-active {
            background: #dcfce7;
            color: #166534;
        }
        
        .status-pending {
            background: #fef3c7;
            color: #92400e;
        }
        
        .status-inactive {
            background: #fee2e2;
            color: #991b1b;
        }
        
        /* Chat Container */
        .chat-container {
            background: var(--background-secondary);
            padding: 1.5rem;
            border-radius: var(--radius-lg);
            border: 1px solid var(--border-color);
            margin: 1.5rem 0;
        }
        
        /* Professional Navigation */
        .nav-container {
            background: var(--background-primary);
            border-radius: var(--radius-lg);
            padding: 1rem;
            margin-bottom: 2rem;
            border: 1px solid var(--border-color);
            box-shadow: var(--shadow-sm);
        }
        
        /* Sidebar Styling */
        .css-1d391kg {
            background: var(--background-secondary);
        }
        
        .css-1d391kg .css-10trblm {
            color: var(--text-primary);
            font-weight: 600;
        }
        
        /* Metrics Styling */
        [data-testid="metric-container"] {
            background: var(--background-primary);
            border: 1px solid var(--border-color);
            padding: 1rem;
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-sm);
            transition: all 0.2s ease;
        }
        
        [data-testid="metric-container"]:hover {
            box-shadow: var(--shadow-md);
            transform: translateY(-1px);
        }
        
        /* Plotly Chart Styling */
        .js-plotly-plot .plotly .modebar {
            background: transparent !important;
        }
        
        .js-plotly-plot .plotly .modebar-btn {
            color: var(--text-muted) !important;
        }
        
        /* Professional Tables */
        .dataframe {
            border: none !important;
            border-radius: var(--radius-md);
            overflow: hidden;
            box-shadow: var(--shadow-sm);
        }
        
        .dataframe th {
            background: var(--background-tertiary) !important;
            color: var(--text-primary) !important;
            font-weight: 600 !important;
            border: none !important;
            padding: 1rem !important;
        }
        
        .dataframe td {
            border: none !important;
            padding: 0.75rem 1rem !important;
            border-bottom: 1px solid var(--border-color) !important;
        }
        
        /* Buttons */
        .stButton > button {
            background: var(--primary-color);
            color: white;
            border: none;
            border-radius: var(--radius-md);
            padding: 0.75rem 1.5rem;
            font-weight: 500;
            transition: all 0.2s ease;
            box-shadow: var(--shadow-sm);
        }
        
        .stButton > button:hover {
            background: var(--primary-dark);
            box-shadow: var(--shadow-md);
            transform: translateY(-1px);
        }
        
        /* Select Boxes */
        .stSelectbox > div > div > div {
            background: var(--background-primary);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
        }
        
        /* Text Inputs */
        .stTextInput > div > div > input {
            background: var(--background-primary);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            color: var(--text-primary);
        }
        
        /* Success/Error Messages */
        .stAlert > div {
            border-radius: var(--radius-md);
            border: none;
            box-shadow: var(--shadow-sm);
        }
        
        /* Mobile Responsiveness */
        @media (max-width: 768px) {
            .main-header h1 {
                font-size: 2rem;
            }
            
            .main-header p {
                font-size: 1rem;
            }
            
            .policy-card, .metric-card {
                padding: 1.25rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)


def render_header(title: str, subtitle: str):
    """
    Render the professional application header.
    
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
    Render a professional policy information card.
    
    Args:
        policy: Policy data dictionary
    """
    status = policy.get('status', 'unknown').lower()
    status_class = f"status-{status}" if status in ['active', 'pending', 'inactive'] else "status-pending"
    
    st.markdown(f"""
    <div class="policy-card">
        <h3>{policy.get('name', 'Unnamed Policy')}</h3>
        <span class="status-badge {status_class}">{policy.get('status', 'Unknown').title()}</span>
        <p><strong>Description:</strong> {policy.get('description', 'No description available.')}</p>
        <p><strong>Implementation Date:</strong> {policy.get('implementation_date', 'Not specified')}</p>
        <p><strong>Effectiveness Score:</strong> {policy.get('effectiveness_score', 'N/A')}/10</p>
    </div>
    """, unsafe_allow_html=True)


def render_metric_card(title: str, value: str, delta: str = None, delta_color: str = "normal"):
    """
    Render a professional metric card.
    
    Args:
        title: Metric title
        value: Metric value
        delta: Change indicator
        delta_color: Color of delta (normal, positive, negative)
    """
    delta_class = ""
    if delta:
        if delta_color == "positive":
            delta_class = "color: var(--success-color);"
        elif delta_color == "negative":
            delta_class = "color: var(--error-color);"
        else:
            delta_class = "color: var(--text-muted);"
    
    delta_html = f'<p style="margin: 0.5rem 0 0 0; font-size: 0.875rem; {delta_class}">{delta}</p>' if delta else ""
    
    st.markdown(f"""
    <div class="metric-card">
        <h4 style="margin: 0 0 0.5rem 0; color: var(--text-secondary); font-size: 0.875rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.05em;">{title}</h4>
        <p style="margin: 0; font-size: 2rem; font-weight: 700; color: var(--text-primary);">{value}</p>
        {delta_html}
    </div>
    """, unsafe_allow_html=True)


def render_section_header(title: str, description: str = None):
    """
    Render a professional section header.
    
    Args:
        title: Section title
        description: Optional section description
    """
    description_html = f'<p style="color: var(--text-secondary); margin: 0.5rem 0 0 0; font-size: 1rem;">{description}</p>' if description else ""
    
    st.markdown(f"""
    <div style="margin: 2rem 0 1.5rem 0; padding-bottom: 1rem; border-bottom: 1px solid var(--border-color);">
        <h2 style="margin: 0; color: var(--text-primary); font-size: 1.5rem; font-weight: 600;">{title}</h2>
        {description_html}
    </div>
    """, unsafe_allow_html=True)


def render_info_box(content: str, box_type: str = "info"):
    """
    Render a professional information box.
    
    Args:
        content: Box content
        box_type: Type of box (info, success, warning, error)
    """
    colors = {
        "info": {"bg": "#eff6ff", "border": "#3b82f6", "text": "#1e40af"},
        "success": {"bg": "#f0fdf4", "border": "#22c55e", "text": "#15803d"},
        "warning": {"bg": "#fffbeb", "border": "#f59e0b", "text": "#d97706"},
        "error": {"bg": "#fef2f2", "border": "#ef4444", "text": "#dc2626"}
    }
    
    color_scheme = colors.get(box_type, colors["info"])
    
    st.markdown(f"""
    <div style="
        background: {color_scheme['bg']};
        border: 1px solid {color_scheme['border']};
        border-left: 4px solid {color_scheme['border']};
        color: {color_scheme['text']};
        padding: 1rem;
        border-radius: var(--radius-md);
        margin: 1rem 0;
    ">
        {content}
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


def create_navigation_tabs(pages: list, current_page: str = None) -> str:
    """
    Create modern tab-based navigation instead of sidebar.
    
    Args:
        pages: List of page names
        current_page: Currently selected page
        
    Returns:
        Selected page name
    """
    # Create navigation tabs
    tabs = st.tabs([f"📊 {page}" if page == "Dashboard" 
                   else f"📋 {page}" if page == "Policy Analysis"
                   else f"📈 {page}" if page == "Data Trends" 
                   else f"🤖 {page}" if page == "AI Chatbot"
                   else f"ℹ️ {page}" for page in pages])
    
    # Return the active tab index
    for i, tab in enumerate(tabs):
        if tab:
            return pages[i]
    
    return pages[0]


def create_sidebar_navigation(pages: list, current_page: str = None) -> str:
    """
    Create professional sidebar navigation with icons.
    
    Args:
        pages: List of page names
        current_page: Currently selected page
        
    Returns:
        Selected page name
    """
    # Add professional sidebar styling
    st.sidebar.markdown("""
    <style>
        .nav-header {
            padding: 1rem 0;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 1rem;
        }
        .nav-header h2 {
            color: var(--text-primary);
            font-size: 1.25rem;
            font-weight: 600;
            margin: 0;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown('<div class="nav-header"><h2>🧭 Navigation</h2></div>', unsafe_allow_html=True)
    
    # Create page options with icons
    page_icons = {
        "Dashboard": "📊",
        "Policy Analysis": "📋", 
        "Data Trends": "📈",
        "AI Chatbot": "🤖",
        "About": "ℹ️"
    }
    
    page_options = [f"{page_icons.get(page, '📄')} {page}" for page in pages]
    
    selected_option = st.sidebar.selectbox(
        "Choose a page:",
        page_options,
        index=pages.index(current_page) if current_page in pages else 0,
        label_visibility="collapsed"
    )
    
    # Extract the page name without icon
    selected_page = selected_option.split(" ", 1)[1] if " " in selected_option else selected_option
    
    return selected_page
