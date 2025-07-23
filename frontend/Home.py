"""
NetEquity: Digital Divide Policy Insights

This is the main entry point for the Streamlit application.
"""

import streamlit as st
import sys
import os
import pandas as pd
import plotly.express as px

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import STREAMLIT_CONFIG, APP_TITLE, APP_SUBTITLE
from components.ui_components import (
    load_custom_css, 
    display_page_header,
    display_interactive_background,
    render_metric_card,
    render_policy_card,
    render_info_box,
    render_section_header
)
from utils.api_client import api_client


def render_dashboard():
    """Render the main dashboard page."""
    display_page_header(
        title="Dashboard", 
        subtitle="A quick look at the policies and key metrics shaping digital equity.",
        icon_name="dashboard.svg"
    )

    # Fetch data from API
    policies_data = api_client.get("/api/policies/")
    indicators_data = api_client.get("/api/data/indicators")

    if not policies_data or not indicators_data:
        st.error("Failed to load dashboard data. Please ensure the API is running.")
        return

    # Render key performance indicators
    _render_kpis(policies_data, indicators_data)
    
    # Render charts
    _render_dashboard_charts(policies_data, indicators_data)

    # Render policy spotlight
    _render_policy_spotlight(policies_data)


def _render_kpis(policies_data: dict, indicators_data: dict):
    """Render key performance indicators."""
    total_policies = len(policies_data.get('policies', []))
    avg_effectiveness = policies_data.get('average_effectiveness_score', 0)
    broadband_access = indicators_data.get('national_broadband_access', 0)
    digital_literacy = indicators_data.get('national_digital_literacy', 0)

    kpi_cols = st.columns(4)
    with kpi_cols[0]:
        render_metric_card("Total Policies", str(total_policies))
    with kpi_cols[1]:
        render_metric_card("Avg. Effectiveness", f"{avg_effectiveness:.2f}/10")
    with kpi_cols[2]:
        render_metric_card("Broadband Access", f"{broadband_access:.1f}%")
    with kpi_cols[3]:
        render_metric_card("Digital Literacy", f"{digital_literacy:.1f}%")


def _render_dashboard_charts(policies_data: dict, indicators_data: dict):
    """Render charts for the dashboard."""
    chart_cols = st.columns(2)
    
    with chart_cols[0]:
        render_section_header("Policy Effectiveness", "How do current policies score?")
        df = pd.DataFrame(policies_data.get('policies', []))
        if not df.empty:
            fig = px.histogram(df, x="effectiveness_score", nbins=10)
            fig.update_layout(bargap=0.1, yaxis_title="Number of Policies", xaxis_title="Effectiveness Score")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No policy data to display.")

    with chart_cols[1]:
        render_section_header("State-Level Data", "Which states are leading in digital access?")
        df_indicators = pd.DataFrame(indicators_data.get('indicators_by_state', []))
        if not df_indicators.empty:
            fig = px.bar(df_indicators.head(10), x='state', y=['broadband_access', 'digital_literacy'],
                         barmode='group', labels={'value': 'Percentage', 'state': 'State', 'variable': 'Indicator'})
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No indicator data to display.")


def _render_policy_spotlight(policies_data: dict):
    """Render a spotlight on a few key policies."""
    render_section_header("Policy Spotlight", "A closer look at some key policies.")
    
    policies = policies_data.get('policies', [])
    if not policies:
        st.info("No policies available to display.")
        return

    # Sort by effectiveness and feature top 3
    top_policies = sorted(policies, key=lambda p: p.get('effectiveness_score', 0), reverse=True)[:3]

    spotlight_cols = st.columns(len(top_policies))
    for i, policy in enumerate(top_policies):
        with spotlight_cols[i]:
            render_policy_card(policy, is_compact=True)


def configure_app():
    """Configure Streamlit app settings."""
    st.set_page_config(**STREAMLIT_CONFIG, page_icon="frontend/assets/icons/dashboard.svg")
    load_custom_css()

from config import STREAMLIT_CONFIG, APP_TITLE
from components.ui_components import (
    load_custom_css, 
    display_interactive_background
)

def main():
    """Main function to run the Streamlit application."""
    st.set_page_config(**STREAMLIT_CONFIG)
    load_custom_css()
    display_interactive_background()
    
    render_dashboard()

    render_info_box(
        "About This Platform",
        "This dashboard helps you explore policies related to the digital divide. "
        "It uses a mix of real and sample data to show what's possible."
    )

    st.title(f"Welcome to {APP_TITLE}")
    st.markdown("Select a page from the sidebar to explore digital divide policies and data.")
    st.sidebar.success("Select a page above.")

if __name__ == "__main__":
    main()
