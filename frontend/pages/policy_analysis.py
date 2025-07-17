"""
Policy analysis page for Digital Divide Policy Insights.
"""

import streamlit as st
import plotly.graph_objects as go

from utils.api_client import api_client
from components.ui_components import render_policy_card, format_metric_value


def render_policy_analysis():
    """Render detailed policy analysis page."""
    st.header("🏛️ Policy Analysis")
    
    policies_data = api_client.get("/api/policies/")
    
    if not policies_data or not policies_data.get('policies'):
        st.error("Unable to load policy data. Please check API connection.")
        return
    
    policies = policies_data['policies']
    policy_names = [p['name'] for p in policies]
    selected_policy = st.selectbox("Select a policy to analyze:", policy_names)
    
    policy = next(p for p in policies if p['name'] == selected_policy)
    
    _render_policy_details(policy)
    _render_policy_metrics(policy)


def _render_policy_details(policy: dict):
    """Render policy details and effectiveness gauge."""
    col1, col2 = st.columns([2, 1])
    
    with col1:
        render_policy_card(policy)
    
    with col2:
        _render_effectiveness_gauge(policy['effectiveness_score'])


def _render_effectiveness_gauge(effectiveness_score: float):
    """Render effectiveness score gauge chart."""
    st.subheader("Effectiveness Score")
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=effectiveness_score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Score (out of 10)"},
        delta={'reference': 5.0},
        gauge={
            'axis': {'range': [None, 10]},
            'bar': {'color': "#667eea"},
            'steps': [
                {'range': [0, 5], 'color': "lightgray"},
                {'range': [5, 8], 'color': "yellow"},
                {'range': [8, 10], 'color': "green"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 9
            }
        }
    ))
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)


def _render_policy_metrics(policy: dict):
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
