"""
UI styling and component utilities for the Digital Divide Policy frontend.
"""

import streamlit as st
import base64
import os


def get_icon(icon_name: str) -> str:
    """
    Finds an icon in the assets folder, encodes it in base64, and returns a data URI.
    
    Args:
        icon_name: The filename of the icon (e.g., "home.svg").
    
    Returns:
        A base64-encoded data URI for the SVG image.
    """
    # Get the current file's directory (components/)
    current_dir = os.path.dirname(__file__)
    # Go up one level to frontend/, then to assets/icons/
    icon_path = os.path.join(current_dir, "..", "assets", "icons", icon_name)
    icon_path = os.path.abspath(icon_path)  # Resolve the absolute path
    
    if not os.path.exists(icon_path):
        # Try alternative path for different deployment scenarios
        alt_path = os.path.join(os.getcwd(), "frontend", "assets", "icons", icon_name)
        if os.path.exists(alt_path):
            icon_path = alt_path
        else:
            # Return empty string if icon not found
            return ""
    
    try:
        with open(icon_path, "rb") as f:
            icon_bytes = f.read()
        icon_base64 = base64.b64encode(icon_bytes).decode("utf-8")
        return f"data:image/svg+xml;base64,{icon_base64}"
    except Exception:
        return ""


def load_custom_css():
    """Load professional custom CSS styles for the application."""
    st.markdown("""
    <style>
        /* Import Professional Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Global Variables - Modern Clean Theme */
        :root {
            --primary-color: #2563eb; /* Modern blue */
            --primary-dark: #1d4ed8;
            --secondary-color: #64748b; /* Slate gray */
            --accent-color: #f8fafc; 
            --success-color: #10b981;
            --warning-color: #f59e0b;
            --error-color: #ef4444;
            --background-primary: #f8fafc; /* Light gray-white */
            --background-secondary: #f1f5f9; /* Slightly darker light gray */
            --background-tertiary: #e2e8f0; /* Medium light gray */
            --text-primary: #0f172a; /* Dark slate */
            --text-secondary: #475569; /* Medium slate */
            --text-muted: #94a3b8; /* Light slate */
            --border-color: #e2e8f0;
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            --radius-sm: 0.375rem;
            --radius-md: 0.5rem;
            --radius-lg: 0.75rem;
            --card-bg: rgba(255, 255, 255, 0.9);
        }

        /* Interactive Parallax Background */
        .parallax-container {
            position: fixed;
            width: 100vw;
            height: 100vh;
            top: 0;
            left: 0;
            background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 50%, #cbd5e1 100%);
            overflow: hidden;
            z-index: -2;
        }

        .parallax-layer {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            transition: transform 0.1s ease-out;
        }

        .parallax-container .icon {
            position: absolute;
            opacity: 0.08;
            will-change: transform;
            transition: opacity 0.3s ease;
        }

        .parallax-container .icon img {
            width: 100%;
            height: 100%;
            filter: invert(0.3) sepia(1) saturate(0.5) hue-rotate(200deg) brightness(0.8);
        }
        
        /* Positioning and sizing of icons */
        .icon:nth-child(1) { top: 10%; left: 15%; width: 50px; height: 50px; }
        .icon:nth-child(2) { top: 25%; left: 80%; width: 30px; height: 30px; }
        .icon:nth-child(3) { top: 70%; left: 10%; width: 40px; height: 40px; }
        .icon:nth-child(4) { top: 85%; left: 90%; width: 60px; height: 60px; }
        .icon:nth-child(5) { top: 50%; left: 50%; width: 35px; height: 35px; }
        .icon:nth-child(6) { top: 5%; left: 40%; width: 45px; height: 45px; }
        .icon:nth-child(7) { top: 90%; left: 30%; width: 55px; height: 55px; }
        .icon:nth-child(8) { top: 40%; left: 5%; width: 40px; height: 40px; }
        .icon:nth-child(9) { top: 60%; left: 70%; width: 33px; height: 33px; }
        .icon:nth-child(10) { top: 15%; left: 95%; width: 48px; height: 48px; }

        /* Base Styles */
        body {
            background-color: var(--background-primary);
        }
        
        .stApp {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--background-primary);
            z-index: 1;
        }
        
        /* Hide Streamlit Branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Main Content Area */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1320px;
        }
        
        /* Glassmorphism Header */
        .main-header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(12px) saturate(180%);
            color: var(--text-primary);
            padding: 2.5rem;
            border-radius: var(--radius-lg);
            margin-bottom: 2.5rem;
            text-align: left;
            border: 1px solid var(--border-color);
            box-shadow: var(--shadow-lg);
        }
        
        .main-header h1 {
            font-size: 2.8rem;
            font-weight: 700;
            margin: 0 0 0.5rem 0;
            color: var(--primary-color);
        }
        
        .main-header p {
            font-size: 1.2rem;
            font-weight: 400;
            margin: 0;
            color: var(--text-secondary);
        }
        
        /* Glassmorphism Cards */
        .policy-card, .metric-card, .feature-card {
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px) saturate(150%);
            padding: 1.5rem;
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
            margin: 1rem 0;
            box-shadow: var(--shadow-md);
            transition: all 0.3s ease-in-out;
            position: relative;
            height: 100%;
        }
        
        .policy-card:hover, .metric-card:hover, .feature-card:hover {
            box-shadow: var(--shadow-lg);
            transform: translateY(-5px);
            border-color: var(--primary-color);
        }
        
        .policy-card h3 {
            color: var(--primary-color);
            font-weight: 600;
            margin: 0 0 1rem 0;
            font-size: 1.2rem;
        }

        .feature-card h4 {
            color: var(--primary-color);
            font-weight: 600;
            margin: 0 0 0.75rem 0;
            font-size: 1.1rem;
        }
        
        .policy-card p, .feature-card p {
            color: var(--text-secondary);
            margin: 0.5rem 0;
            line-height: 1.6;
            font-size: 0.95rem;
        }
        
        /* Compact Policy Card */
        .policy-card.compact {
            padding: 1rem;
            font-size: 0.9rem;
        }
        
        /* Status Badges */
        .status-badge {
            display: inline-block;
            padding: 0.3rem 0.8rem;
            border-radius: var(--radius-sm);
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        .status-active {
            background: rgba(16, 185, 129, 0.1);
            color: var(--success-color);
            border: 1px solid var(--success-color);
        }
        
        .status-pending {
            background: rgba(245, 158, 11, 0.1);
            color: var(--warning-color);
            border: 1px solid var(--warning-color);
        }
        
        .status-inactive {
            background: rgba(239, 68, 68, 0.1);
            color: var(--error-color);
            border: 1px solid var(--error-color);
        }
        
        /* Chat Container */
        .chat-container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: var(--radius-lg);
            padding: 1.5rem;
            border: 1px solid var(--border-color);
        }
        
        /* Section Headers */
        .section-header {
            margin-top: 3rem;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--border-color);
        }
        
        .section-header h2 {
            font-size: 1.8rem;
            font-weight: 600;
            color: var(--text-primary);
            margin: 0;
        }
        
        .section-header p {
            font-size: 1rem;
            color: var(--text-secondary);
            margin-top: 0.25rem;
        }
        
        /* Custom Selectbox */
        .stSelectbox > div {
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
            background: var(--background-primary);
        }
        
        /* Custom Metric Styles */
        .stMetric {
            background-color: var(--background-primary);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.5rem;
            text-align: center;
        }
        
        /* Plotly Chart Styling */
        .plotly-chart {
            border-radius: var(--radius-lg);
            overflow: hidden;
        }
        
        /* Info Box */
        .info-box {
            padding: 1.5rem;
            border-radius: var(--radius-md);
            margin: 1rem 0;
            border-left: 5px solid;
        }
        
        .info-box-info {
            background-color: rgba(37, 99, 235, 0.05);
            border-color: var(--primary-color);
        }
        
        .info-box-success {
            background-color: rgba(16, 185, 129, 0.05);
            border-color: var(--success-color);
        }
        
        .info-box-warning {
            background-color: rgba(245, 158, 11, 0.05);
            border-color: var(--warning-color);
        }
        
        .info-box-error {
            background-color: rgba(239, 68, 68, 0.05);
            border-color: var(--error-color);
        }
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(12px);
            border-right: 1px solid var(--border-color);
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
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def render_policy_card(policy: dict, is_compact: bool = False):
    """
    Render a professional policy information card.
    
    Args:
        policy: Policy data dictionary
        is_compact: If True, renders a smaller version for spotlights
    """
    status = policy.get('status', 'unknown').lower()
    status_class = f"status-{status}" if status in ['active', 'pending', 'inactive'] else "status-pending"
    
    card_class = "policy-card compact" if is_compact else "policy-card"

    st.markdown(f"""
    <div class="{card_class}">
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
        "info": {"bg": "rgba(37, 99, 235, 0.05)", "border": "#2563eb", "text": "#1e40af"},
        "success": {"bg": "rgba(16, 185, 129, 0.05)", "border": "#10b981", "text": "#059669"},
        "warning": {"bg": "rgba(245, 158, 11, 0.05)", "border": "#f59e0b", "text": "#d97706"},
        "error": {"bg": "rgba(239, 68, 68, 0.05)", "border": "#ef4444", "text": "#dc2626"}
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
    # This function is now deprecated as Streamlit handles multi-page navigation automatically.
    # The file-based routing in the `pages/` directory is the modern approach.
    # This function can be removed or left for reference.
    st.sidebar.warning("Sidebar navigation is now handled automatically by Streamlit.")
    return pages[0]


def display_page_header(title: str, subtitle: str, icon_name: str = None):
    """
    Displays a styled header for primary pages.
    
    Args:
        title: The main title to display.
        subtitle: A short description of the page's content.
        icon_name: The filename of the icon to display next to the title.
    """
    if icon_name:
        icon_data_uri = get_icon(icon_name)
        st.markdown(f"""
            <div class="main-header">
                <div style="display: flex; align-items: center;">
                    <img src="{icon_data_uri}" style="height: 40px; width: 40px; margin-right: 15px;">
                    <div>
                        <h1>{title}</h1>
                        <p>{subtitle}</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="main-header">
                <h1>{title}</h1>
                <p>{subtitle}</p>
            </div>
        """, unsafe_allow_html=True)


def display_main_header(title: str, subtitle: str, icon_name: str = None):
    """
    Displays a consistent, styled header for the main application page.
    
    Args:
        title: The main title to display.
        subtitle: The subtitle text.
        icon_name: The filename of the icon to display above the title.
    """
    if icon_name:
        icon_data_uri = get_icon(icon_name)
        st.markdown(f"""
            <div class="main-header">
                <div style="display: flex; align-items: center;">
                    <img src="{icon_data_uri}" style="height: 40px; width: 40px; margin-right: 15px;">
                    <div>
                        <h1>{title}</h1>
                        <p>{subtitle}</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="main-header">
                <h1>{title}</h1>
                <p>{subtitle}</p>
            </div>
        """, unsafe_allow_html=True)


def display_info_card(title, content, icon_name=None):
    """
    Displays a card for information with an optional icon.
    
    Args:
        title: The title of the information card.
        content: The main content or data of the card.
        icon_name: Optional name of an icon file from assets.
    """
    icon_html = ""
    if icon_name:
        icon_data_uri = get_icon(icon_name)
        icon_html = f'<img src="{icon_data_uri}" style="height: 24px; width: 24px; margin-right: 10px; vertical-align: middle;">'

    st.markdown(f"""
        <div class="info-box">
            <strong style="font-size: 1.1rem; color: var(--text-primary);">{icon_html}{title}</strong>
            <p style="margin: 0.5rem 0 0 0; color: var(--text-secondary);">{content}</p>
        </div>
    """, unsafe_allow_html=True)


def render_feature_card(title: str, description: str, icon_name: str = None):
    """
    Render a feature card with title, description, and optional icon.
    
    Args:
        title: Card title
        description: Card description
        icon_name: Optional icon filename
    """
    icon_html = ""
    if icon_name:
        icon_data = get_icon(icon_name)
        if icon_data:
            icon_html = f'<img src="{icon_data}" alt="{title}" style="width: 24px; height: 24px; margin-right: 0.5rem; vertical-align: middle;">'
    
    st.markdown(f"""
    <div style="
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-lg);
        padding: 1.5rem;
        margin: 0.5rem 0;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        cursor: pointer;
    " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 25px rgba(0,0,0,0.1)'" 
       onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'">
        <h4 style="
            margin: 0 0 0.5rem 0;
            color: var(--text-primary);
            font-size: 1.1rem;
            font-weight: 600;
        ">{icon_html}{title}</h4>
        <p style="
            margin: 0;
            color: var(--text-secondary);
            font-size: 0.9rem;
            line-height: 1.5;
        ">{description}</p>
    </div>
    """, unsafe_allow_html=True)


def display_interactive_background():
    """Displays the interactive parallax background with SVG icons."""
    
    icon_names = [
        "technology-device-laptop-computer-svgrepo-com.svg",
        "transmission-svgrepo-com.svg",
        "dashboard.svg",
        "trends.svg",
        "policy.svg",
        "cloud-arrow-down-svgrepo-com.svg",
        "data-trends.svg",
        "policy-analysis.svg",
        "technology-tv-svgrepo-com.svg",
        "about.svg"
    ]
    
    icons_html = ""
    for icon_name in icon_names:
        icon_uri = get_icon(icon_name)
        if icon_uri:
            icons_html += f'<div class="icon"><img src="{icon_uri}" alt="icon"></div>'

    background_html = f"""
    <div class="parallax-container" id="parallax-container">
        <div class="parallax-layer" data-depth="0.1">
            {icons_html}
        </div>
    </div>
    <script>
        document.addEventListener('mousemove', function(e) {{
            const container = document.getElementById('parallax-container');
            if (!container) return;

            const width = window.innerWidth;
            const height = window.innerHeight;
            
            const moveX = (e.clientX - width / 2) / width;
            const moveY = (e.clientY - height / 2) / height;

            const layers = container.getElementsByClassName('parallax-layer');
            for (let i = 0; i < layers.length; i++) {{
                const depth = layers[i].getAttribute('data-depth');
                const x = moveX * 100 * depth;
                const y = moveY * 100 * depth;
                layers[i].style.transform = `translate(${{x}}px, ${{y}}px)`;
            }}
        }});
    </script>
    """
    st.markdown(background_html, unsafe_allow_html=True)


def display_page_header(title: str, subtitle: str, icon_name: str = None):
    """
    Displays a styled header for primary pages.
    
    Args:
        title: The main title to display.
        subtitle: A short description of the page's content.
        icon_name: The filename of the icon to display next to the title.
    """
    if icon_name:
        icon_data_uri = get_icon(icon_name)
        st.markdown(f"""
            <div class="main-header">
                <div style="display: flex; align-items: center;">
                    <img src="{icon_data_uri}" style="height: 40px; width: 40px; margin-right: 15px;">
                    <div>
                        <h1>{title}</h1>
                        <p>{subtitle}</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="main-header">
                <h1>{title}</h1>
                <p>{subtitle}</p>
            </div>
        """, unsafe_allow_html=True)
