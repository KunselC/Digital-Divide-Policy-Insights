"""
Policy Analysis Page
"""

import streamlit as st
import plotly.graph_objects as go
import sys
import os

# Add the parent directory to the Python path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.api_client import api_client
from components.ui_components import (
    render_policy_card, 
    format_metric_value, 
    display_page_header, 
    load_custom_css,
    display_interactive_background
)


def render_policy_analysis_page():
    """Render detailed policy analysis page."""
    display_page_header(
        title="Policy Analysis", 
        subtitle="Dig into the details of each policy.",
        icon_name="policy-analysis.svg"
    )
    
    policies_data = api_client.get("/api/policies/")
    
    if not policies_data or not policies_data.get('policies'):
        st.error("Couldn't load policy data. Is the API running?")
        return
    
    policies = policies_data['policies']
    policy_names = [p['name'] for p in policies]
    selected_policy = st.selectbox("Which policy do you want to explore?", policy_names)
    
    policy = next(p for p in policies if p['name'] == selected_policy)
    
<<<<<<< HEAD
    _render_policy_details(policy)
    _render_policy_metrics(policy)
=======
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    _render_policy_details(policy)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    _render_policy_metrics(policy)
    st.markdown('</div>', unsafe_allow_html=True)
>>>>>>> origin/main


def _render_policy_details(policy: dict):
    """Render policy details and effectiveness gauge."""
    col1, col2 = st.columns([2, 1])
    
    with col1:
        render_policy_card(policy)
    
    with col2:
        _render_effectiveness_gauge(policy['effectiveness_score'])


def _render_effectiveness_gauge(effectiveness_score: float):
    """Render effectiveness score gauge chart."""
<<<<<<< HEAD
    st.subheader("Effectiveness Score")
    
=======
>>>>>>> origin/main
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=effectiveness_score,
        domain={'x': [0, 1], 'y': [0, 1]},
<<<<<<< HEAD
        title={'text': "Score (out of 10)"},
        gauge={
            'axis': {'range': [None, 10]},
            'bar': {'color': "var(--primary-color)"},
            'steps': [
                {'range': [0, 5], 'color': "#2D3748"},
                {'range': [5, 8], 'color': "#007EA7"},
            ],
        }
    ))
    fig.update_layout(height=300, paper_bgcolor="rgba(0,0,0,0)", font_color="white")
=======
        title={'text': "Effectiveness Score", 'font': {'size': 20}},
        gauge={
            'axis': {'range': [None, 10], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "var(--primary-color)"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 5], 'color': "rgba(239, 68, 68, 0.1)"},
                {'range': [5, 8], 'color': "rgba(245, 158, 11, 0.1)"},
                {'range': [8, 10], 'color': "rgba(16, 185, 129, 0.1)"}
            ],
        }
    ))
    fig.update_layout(
        height=250, 
        paper_bgcolor="rgba(0,0,0,0)", 
        font={'color': "var(--text-primary)", 'family': "Inter"}
    )
>>>>>>> origin/main
    st.plotly_chart(fig, use_container_width=True)


def _render_policy_metrics(policy: dict):
<<<<<<< HEAD
    """Render policy key metrics."""
    st.subheader("Key Metrics")
    
    metrics = policy.get('metrics', {})
    if not metrics:
        st.info("No metrics available for this policy.")
        return
    
    metric_columns = st.columns(len(metrics))
    
    for i, (metric_name, metric_value) in enumerate(metrics.items()):
        with metric_columns[i]:
            formatted_name = metric_name.replace('_', ' ').title()
            formatted_value = format_metric_value(metric_value)
            st.metric(label=formatted_name, value=formatted_value)

def main():
    """Main function to set up and render the page."""
    from components.ui_components import load_custom_css, display_interactive_background
    
=======
    """Render policy metrics in styled cards."""
    st.subheader("Key Performance Indicators")
    
    kpis = policy.get('kpis', {})
    if not kpis:
        st.info("No specific KPIs are available for this policy.")
        return
        
    # Display KPIs in a grid
    cols = st.columns(len(kpis))
    for i, (kpi, data) in enumerate(kpis.items()):
        with cols[i]:
            render_metric_card(
                title=kpi.replace('_', ' ').title(),
                value=format_metric_value(data['value'], data.get('format')),
                delta=data.get('change', '')
            )

def main():
    """Main function to set up and render the page."""
>>>>>>> origin/main
    st.set_page_config(
        page_title="Policy Analysis - NetEquity",
        layout="wide"
    )
    load_custom_css()
    display_interactive_background()
    render_policy_analysis_page()

if __name__ == "__main__":
    main()
