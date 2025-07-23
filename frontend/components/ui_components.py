"""
UI styling and component utilities for the Digital Divide Policy frontend.
"""

import streamlit as st
import base64
from pathlib import Path

# --- PATHS ---
ASSETS_PATH = Path(__file__).parent.parent / "assets"
ICONS_PATH = ASSETS_PATH / "icons"
MODELS_PATH = ASSETS_PATH / "models"
JS_PATH = ASSETS_PATH / "js"

def get_asset_path(asset_dir: Path, asset_name: str) -> Path:
    """Constructs and checks the path for an asset."""
    return asset_dir / asset_name

def get_asset_as_base64(asset_path: Path) -> str | None:
    """Reads an asset file and returns its base64 encoded version."""
    if not asset_path.is_file():
        return None
    try:
        with open(asset_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return None

def get_icon(icon_name: str, **kwargs) -> str:
    """Returns the HTML for a styled SVG icon."""
    icon_path = get_asset_path(ICONS_PATH, icon_name)
    icon_svg = ""
    if icon_path.is_file():
        try:
            with open(icon_path, "r") as f:
                icon_svg = f.read()
        except Exception:
            pass

    # Default style - small size to match text
    style = "width: 16px; height: 16px; margin-right: 6px; vertical-align: middle; display: inline-block;"
    
    # Apply overrides from kwargs
    for key, value in kwargs.items():
        style += f" {key.replace('_', '-')}: {value};"

    return f'<span style="{style}">{icon_svg}</span>'

def get_model_as_base64(model_name: str) -> str | None:
    """Returns the base64 encoded data URI for a 3D model."""
    model_path = get_asset_path(MODELS_PATH, model_name)
    b64_model = get_asset_as_base64(model_path)
    if b64_model:
        return f"data:model/gltf-binary;base64,{b64_model}"
    return None

def load_custom_css():
    """Load professional custom CSS styles for the application."""
    st.markdown("""
    <style>
    /* Import Inter font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* CSS Variables */
    :root {
        --primary-color: #2563eb;
        --primary-dark: #1e40af;
        --secondary-color: #64748b;
        --accent-color: #0ea5e9;
        --success-color: #10b981;
        --warning-color: #f59e0b;
        --error-color: #ef4444;
        --text-primary: #0f172a;
        --text-secondary: #475569;
        --text-muted: #94a3b8;
        --background-primary: #ffffff;
        --background-secondary: #f8fafc;
        --background-tertiary: #f1f5f9;
        --border-light: #e2e8f0;
        --border-medium: #cbd5e1;
        --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
        --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
        --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
        --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
        --radius-sm: 0.375rem;
        --radius-md: 0.5rem;
        --radius-lg: 0.75rem;
        --radius-xl: 1rem;
    }

    /* Base Styling */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        color: var(--text-primary);
        background-color: var(--background-secondary);
    }

    /* Main container */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Content boxes */
    .content-box {
        background: var(--background-primary);
        border-radius: var(--radius-lg);
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid var(--border-light);
        box-shadow: var(--shadow-sm);
    }

    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary);
        font-weight: 600;
        line-height: 1.2;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: var(--radius-md);
        font-weight: 500;
        font-size: 0.875rem;
        transition: all 0.2s ease;
        box-shadow: var(--shadow-sm);
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: var(--shadow-md);
        background: linear-gradient(135deg, var(--primary-dark), var(--primary-color));
    }

    /* Remove default Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def display_page_header(title: str, subtitle: str = "", icon_name: str = ""):
    """Display a styled page header with optional icon."""
    icon_html = get_icon(icon_name, width="28px", height="28px") if icon_name else ""
    
    st.markdown(f"""
    <div style="margin-bottom: 2rem;">
        <h1 style="display: flex; align-items: center; margin-bottom: 0.5rem; font-size: 2rem; line-height: 1.2;">
            {icon_html}{title}
        </h1>
        {f'<p style="color: var(--text-secondary); font-size: 1.1rem; margin: 0;">{subtitle}</p>' if subtitle else ''}
    </div>
    """, unsafe_allow_html=True)

def display_interactive_background():
    """Display an interactive background with particles or 3D elements."""
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(-45deg, #f8fafc, #f1f5f9, #e2e8f0, #f8fafc);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>
    """, unsafe_allow_html=True)

def render_metric_card(title: str, value: str, delta: str = None, delta_color: str = "normal"):
    """Render a styled metric card."""
    delta_html = ""
    if delta:
        delta_class = "success" if delta_color == "normal" else "error"
        delta_html = f'<div class="metric-delta {delta_class}">{delta}</div>'
    
    st.markdown(f"""
    <div class="content-box" style="text-align: center;">
        <h3 style="margin: 0 0 0.5rem 0; color: var(--text-secondary); font-size: 0.875rem; font-weight: 500; text-transform: uppercase;">{title}</h3>
        <div style="font-size: 2rem; font-weight: 700; color: var(--text-primary); margin: 0;">{value}</div>
        {delta_html}
    </div>
    """, unsafe_allow_html=True)

def render_policy_card(policy: dict, is_compact: bool = False):
    """Render a policy information card."""
    effectiveness = policy.get('effectiveness_score', 0)
    color = "success" if effectiveness >= 7 else "warning" if effectiveness >= 5 else "error"
    
    st.markdown(f"""
    <div class="content-box">
        <h3 style="margin: 0 0 1rem 0;">{policy.get('name', 'Unknown Policy')}</h3>
        <p style="color: var(--text-secondary); margin: 0 0 1rem 0;">{policy.get('description', '')}</p>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="color: var(--text-muted);">Effectiveness Score</span>
            <span style="font-weight: 600; color: var(--{color}-color);">{effectiveness}/10</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_info_box(content: str, box_type: str = "info"):
    """Render an information box with different types."""
    colors = {
        "info": "var(--primary-color)",
        "success": "var(--success-color)",  
        "warning": "var(--warning-color)",
        "error": "var(--error-color)"
    }
    
    color = colors.get(box_type, colors["info"])
    
    st.markdown(f"""
    <div style="
        background: var(--background-primary);
        border-left: 4px solid {color};
        padding: 1rem;
        border-radius: var(--radius-md);
        margin: 1rem 0;
        box-shadow: var(--shadow-sm);
    ">
        {content}
    </div>
    """, unsafe_allow_html=True)

def render_section_header(title: str, description: str = None):
    """Render a section header with optional description."""
    st.markdown(f"""
    <div style="margin: 2rem 0 1rem 0;">
        <h2 style="margin: 0 0 0.5rem 0;">{title}</h2>
        {f'<p style="color: var(--text-secondary); margin: 0;">{description}</p>' if description else ''}
    </div>
    """, unsafe_allow_html=True)

def display_3d_globe_component():
    """Display the 3D globe component using the submarine cable GLB model."""
    st.info("🌍 Loading interactive 3D globe... This may take a moment due to the detailed model.")
    
    # Load the 3D model as base64
    model_uri = get_model_as_base64("submarine_fiber_optic_cable_network.glb")
    
    if not model_uri:
        st.error("Failed to load 3D model - file not found or too large")
        # Show fallback visualization
        st.markdown("""
        <div style="
            height: 400px; 
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
            font-family: 'Inter', sans-serif;
        ">
            <div>
                <h3 style="margin: 0 0 1rem 0;">3D Globe Temporarily Unavailable</h3>
                <p style="margin: 0;">The 3D model file could not be loaded</p>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.8;">Please check the model file and try again</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Load the HTML template and display the 3D model
    try:
        template_path = ASSETS_PATH / "modern_3d.html"
        
        if not template_path.exists():
            st.error(f"3D template not found: {template_path}")
            return
            
        with open(template_path, 'r', encoding='utf-8') as f:
            html_template = f.read()
        
        # Replace the model URI placeholder
        html_content = html_template.replace("{{MODEL_URI}}", model_uri)
        
        # Display in Streamlit using components
        st.components.v1.html(html_content, height=600, scrolling=False)
        
        # Show model information
        with st.expander("3D Model Information", expanded=False):
            st.info("**Submarine Fiber Optic Cable Network**")
            st.write("This 3D model shows the global network of underwater fiber optic cables that carry internet traffic between continents.")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Model File Size", "9.7 MB", "High detail")
            with col2:
                st.metric("Data Coverage", "Global", "99% of international traffic")
            
            # Check if model is large and show performance note
            if len(model_uri) > 10_000_000:  # 10MB in base64
                st.warning("""
                **Performance Note:** This is a detailed 3D model. If you experience slow loading:
                - The model may take 10-30 seconds to fully load
                - Use mouse to rotate and explore once loaded
                - Refresh the page if the model doesn't appear
                """)
            else:
                st.success("Model size is optimized for web viewing")
                
    except Exception as e:
        st.error(f"Error loading 3D model: {str(e)}")
        st.info("If you continue to see this error, the model file may be corrupted or too large for your browser.")

def display_simple_3d_globe():
    """Display a lightweight 3D globe using Three.js without the heavy model file."""
    st.info("🌍 Interactive 3D Globe - Lightweight Version")
    
    try:
        # Load the simple globe HTML template
        simple_globe_path = ASSETS_PATH / "simple_globe.html"
        
        if simple_globe_path.exists():
            with open(simple_globe_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Display the lightweight 3D globe
            st.components.v1.html(html_content, height=500, scrolling=False)
            
            # Add information about the lightweight version
            st.success("✨ **Lightweight 3D Globe** - Fast loading with interactive features")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Global Internet Users", "5.16B", "4.8%")
            with col2:
                st.metric("Submarine Cables", "450+", "Active worldwide")  
            with col3:
                st.metric("Data Capacity", "15+ Tbps", "Total global capacity")
                
        else:
            st.error(f"Simple globe template not found: {simple_globe_path}")
            
    except Exception as e:
        st.error(f"Error loading simple 3D globe: {str(e)}")

def format_metric_value(value, format_type: str = "auto") -> str:
    """Format metric values for display."""
    if format_type == "percentage":
        return f"{value:.1f}%"
    elif format_type == "currency":
        return f"${value:,.0f}"
    elif format_type == "number":
        return f"{value:,.0f}"
    else:
        return str(value)

def render_feature_card(title: str, description: str, icon_name: str = ""):
    """Render a feature card with icon, title, and description."""
    icon_html = get_icon(icon_name, width="24px", height="24px") if icon_name else ""
    
    st.markdown(f"""
    <div class="content-box" style="margin: 1rem 0;">
        <div style="display: flex; align-items: flex-start; gap: 1rem;">
            {icon_html}
            <div>
                <h4 style="margin: 0 0 0.5rem 0; color: var(--text-primary);">{title}</h4>
                <p style="margin: 0; color: var(--text-secondary); line-height: 1.5;">{description}</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
