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
    """
    Returns the HTML for a styled SVG icon.
    """
    icon_path = get_asset_path(ICONS_PATH, icon_name)
    icon_svg = ""
    if icon_path.is_file():
        with open(icon_path, "r", encoding="utf-8") as f:
            icon_svg = f.read()

    # Default style
    style = "width: 24px; height: 24px; margin-right: 8px; vertical-align: middle;"
    
    # Apply overrides from kwargs
    for key, value in kwargs.items():
        css_key = key.replace('_', '-')
        style += f" {css_key}: {value};"

    return f'<span style="{style}">{icon_svg}</span>'

def get_model_as_base64(model_name: str) -> str | None:
    """Returns the base64 encoded data URI for a 3D model."""
    model_path = get_asset_path(MODELS_PATH, model_name)
    b64_model = get_asset_as_base64(model_path)
    if b64_model:
        return f"data:application/octet-stream;base64,{b64_model}"
    return None

def get_js_as_base64(js_name: str) -> str | None:
    """Returns the base64 encoded data URI for a JavaScript file."""
    js_path = get_asset_path(JS_PATH, js_name)
    b64_js = get_asset_as_base64(js_path)
    if b64_js:
        return f"data:application/javascript;base64,{b64_js}"
    return None


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
        }

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
        
        /* Content Box for wrapping sections */
        .content-box {
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px) saturate(150%);
            padding: 1.5rem;
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
            margin: 1rem 0;
            box-shadow: var(--shadow-md);
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
        icon_html = get_icon(icon_name, width="40px", height="40px", margin_right="15px")
        st.markdown(f"""
            <div class="main-header">
                <div style="display: flex; align-items: center;">
                    {icon_html}
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
        icon_html = get_icon(icon_name, width="40px", height="40px", margin_right="15px")
        st.markdown(f"""
            <div class="main-header">
                <div style="display: flex; align-items: center;">
                    {icon_html}
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


def render_feature_card(title: str, content: str, icon_name: str = None):
    """
    Renders a feature card with optional icon.
    
    Args:
        title: Card title
        content: Card content
        icon_name: Optional name of an icon file from assets
    """
    icon_html = ""
    if icon_name:
        icon_html = get_icon(icon_name)

    card_html = f"""
        <div class="feature-card">
            <h4>{icon_html}{title}</h4>
            <p>{content}</p>
        </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)


def display_3d_globe_component():
    """
    Renders an interactive 3D globe using Three.js in a Streamlit component.
    """
    st.info("Loading 3D model... This may take a moment for the detailed submarine cable network.")
    
    model_base64 = get_model_as_base64("submarine_fiber_optic_cable_network.glb")
    
    if not model_base64:
        st.error("3D model file not found or could not be loaded.")
        return

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ margin: 0; background-color: transparent; }}
            canvas {{ display: block; width: 100%; height: 100%; }}
            #loading {{
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                color: #2563eb;
                font-family: Inter, sans-serif;
                font-size: 18px;
            }}
        </style>
    </head>
    <body>
        <div id="loading">Loading 3D submarine cable network...</div>
        <script type="importmap">
        {{
            "imports": {{
                "three": "https://unpkg.com/three@0.164.1/build/three.module.js",
                "three/addons/": "https://unpkg.com/three@0.164.1/examples/jsm/"
            }}
        }}
        </script>
        <script type="module">
            import * as THREE from 'three';
            import {{ OrbitControls }} from 'three/addons/controls/OrbitControls.js';
            import {{ GLTFLoader }} from 'three/addons/loaders/GLTFLoader.js';

            let scene, camera, renderer, controls;

            function base64ToArrayBuffer(base64) {{
                const binaryString = atob(base64.split(',')[1]);
                const len = binaryString.length;
                const bytes = new Uint8Array(len);
                for (let i = 0; i < len; i++) {{
                    bytes[i] = binaryString.charCodeAt(i);
                }}
                return bytes.buffer;
            }}

            function hideLoading() {{
                const loading = document.getElementById('loading');
                if (loading) loading.style.display = 'none';
            }}

            function init() {{
                // Scene
                scene = new THREE.Scene();
                scene.background = null; // Transparent background

                // Camera
                camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                camera.position.set(0, 0, 3);

                // Renderer
                const canvas = document.createElement('canvas');
                document.body.appendChild(canvas);
                renderer = new THREE.WebGLRenderer({{ canvas: canvas, alpha: true, antialias: true }});
                renderer.setSize(window.innerWidth, 500);

                // Controls
                controls = new OrbitControls(camera, renderer.domElement);
                controls.enableDamping = true;
                controls.dampingFactor = 0.05;
                controls.screenSpacePanning = false;
                controls.minDistance = 1;
                controls.maxDistance = 10;
                controls.autoRotate = true;
                controls.autoRotateSpeed = 0.5;

                // Lighting
                const ambientLight = new THREE.AmbientLight(0xffffff, 1.2);
                scene.add(ambientLight);
                const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
                directionalLight.position.set(10, 10, 5);
                scene.add(directionalLight);

                // GLTF Loader
                const loader = new GLTFLoader();
                
                // Convert base64 to ArrayBuffer and load
                try {{
                    const arrayBuffer = base64ToArrayBuffer('{model_base64}');
                    loader.parse(arrayBuffer, '', function (gltf) {{
                        const model = gltf.scene;
                        
                        // Center and scale the model
                        const box = new THREE.Box3().setFromObject(model);
                        const center = box.getCenter(new THREE.Vector3());
                        model.position.sub(center);
                        
                        const size = box.getSize(new THREE.Vector3());
                        const maxDim = Math.max(size.x, size.y, size.z);
                        const scale = 2 / maxDim;
                        model.scale.set(scale, scale, scale);
                        
                        scene.add(model);
                        hideLoading();
                        animate(); // Start animation loop after model loads
                    }}, function (progress) {{
                        console.log('Loading progress:', progress);
                    }}, function (error) {{
                        console.error('An error happened while parsing the model:', error);
                        hideLoading();
                        // Fallback: create a simple wireframe sphere
                        const geometry = new THREE.SphereGeometry(1, 32, 32);
                        const material = new THREE.MeshBasicMaterial({{ color: 0x2563eb, wireframe: true }});
                        const sphere = new THREE.Mesh(geometry, material);
                        scene.add(sphere);
                        animate();
                    }});
                }} catch (error) {{
                    console.error('Error loading model:', error);
                    hideLoading();
                    // Fallback: create a simple wireframe sphere
                    const geometry = new THREE.SphereGeometry(1, 32, 32);
                    const material = new THREE.MeshBasicMaterial({{ color: 0x2563eb, wireframe: true }});
                    const sphere = new THREE.Mesh(geometry, material);
                    scene.add(sphere);
                    animate();
                }}

                // Handle window resize
                window.addEventListener('resize', onWindowResize, false);
            }}

            function onWindowResize() {{
                camera.aspect = window.innerWidth / 500;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, 500);
            }}

            function animate() {{
                requestAnimationFrame(animate);
                controls.update();
                renderer.render(scene, camera);
            }}

            init();
        </script>
    </body>
    </html>
    """
    st.components.v1.html(html_content, height=520, scrolling=False)


def display_interactive_background():
    """
    Injects HTML and JavaScript for a subtle professional background effect.
    """
    background_html = """
    <style>
        .stApp {
            background: #f8fafc;
        }
    </style>
    """
    st.markdown(background_html, unsafe_allow_html=True)

def display_custom_css():
    """
    Displays the custom CSS for the application.
    """
    css_uri = get_js_as_base64("styles.css")
    if not css_uri:
        st.warning("Could not load the custom CSS file.")
        return

    st.markdown(f'<link href="{css_uri}" rel="stylesheet">', unsafe_allow_html=True)
