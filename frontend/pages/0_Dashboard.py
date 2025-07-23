"""
NetEquity Dashboard

This page displays key performance indicators and policy recommendations.
"""

import streamlit as st
import sys
import os
import plotly.graph_objects as go

# Add the parent directory to the Python path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.api_client import api_client
from components.ui_components import (
    display_page_header,
    render_metric_card,
    render_policy_card,
    format_metric_value,
    load_custom_css,
    display_interactive_background,
    display_3d_globe_component
)

def render_dashboard_tab():
    """Renders the content for the dashboard tab."""
    display_page_header(
        title="Dashboard",
        subtitle="An overview of the digital divide and policy impact.",
        icon_name="dashboard.svg"
    )
    
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    
    # Fetch data from API
    kpi_data = api_client.get("/api/kpis")
    recommendations_data = api_client.get("/api/policies/recommendations")

    if kpi_data:
        st.subheader("Key Performance Indicators")
        kpis = kpi_data.get('kpis', {})
        if kpis:
            cols = st.columns(len(kpis))
            for i, (kpi, data) in enumerate(kpis.items()):
                with cols[i]:
                    render_metric_card(
                        title=kpi.replace('_', ' ').title(),
                        value=format_metric_value(data['value'], data.get('format')),
                        description=f"Change: {data['delta']}%"
                    )
        else:
            st.warning("Could not load KPIs.")
    else:
        st.error("Failed to fetch KPI data from the API.")

    if recommendations_data:
        st.subheader("Top Policy Recommendations")
        recommendations = recommendations_data.get('recommendations', [])
        if recommendations:
            for rec in recommendations:
                render_policy_card(rec)
        else:
            st.warning("No policy recommendations available.")
    else:
        st.error("Failed to fetch policy recommendations from the API.")

    st.markdown('</div>', unsafe_allow_html=True)

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
    st.set_page_config(
        page_title="Dashboard - NetEquity",
        layout="wide"
    )
    load_custom_css()
    display_interactive_background()

    tab1, tab2 = st.tabs(["Dashboard", "3D Globe"])

    with tab1:
        render_dashboard_tab()
    
    with tab2:
        render_globe_tab()


if __name__ == "__main__":
    main()
