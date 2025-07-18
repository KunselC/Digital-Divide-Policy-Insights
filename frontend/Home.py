"""
Digital Divide Policy Insights - Main Application

A Streamlit frontend for analyzing technology policies and their effectiveness 
in bridging the digital divide. Features interactive dashboards, data visualization,
and an AI-powered chatbot for policy inquiries.
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
    render_header, 
    render_section_header, 
    render_policy_card,
    render_info_box
)
from utils.api_client import api_client


def render_dashboard():
    """Render the main dashboard page."""
    render_section_header("Mission Control", "An overview of digital divide policies and key performance indicators.")

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
        st.metric("Total Policies", total_policies)
    with kpi_cols[1]:
        st.metric("Avg. Effectiveness", f"{avg_effectiveness:.2f}/10")
    with kpi_cols[2]:
        st.metric("Broadband Access", f"{broadband_access:.1f}%")
    with kpi_cols[3]:
        st.metric("Digital Literacy", f"{digital_literacy:.1f}%")


def _render_dashboard_charts(policies_data: dict, indicators_data: dict):
    """Render charts for the dashboard."""
    chart_cols = st.columns(2)
    
    with chart_cols[0]:
        st.subheader("Policy Effectiveness Distribution")
        df = pd.DataFrame(policies_data.get('policies', []))
        if not df.empty:
            fig = px.histogram(df, x="effectiveness_score", nbins=10, title="Policy Effectiveness Scores")
            fig.update_layout(bargap=0.1)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No policy data to display.")

    with chart_cols[1]:
        st.subheader("Key Indicators by State")
        df_indicators = pd.DataFrame(indicators_data.get('indicators_by_state', []))
        if not df_indicators.empty:
            fig = px.bar(df_indicators.head(10), x='state', y=['broadband_access', 'digital_literacy'],
                         title="Top 10 States by Broadband Access", barmode='group')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No indicator data to display.")


def _render_policy_spotlight(policies_data: dict):
    """Render a spotlight on a few key policies."""
    render_section_header("Policy Spotlight", "A closer look at key policies driving change.")
    
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


def main():
    """Main application entry point."""
    configure_app()
    
    render_header(APP_TITLE, APP_SUBTITLE)
    
    # The dashboard is now the home page
    render_dashboard()


if __name__ == "__main__":
    main()
