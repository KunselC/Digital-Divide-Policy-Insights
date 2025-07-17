"""
Dashboard page for Digital Divide Policy Insights.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.api_client import api_client
from components.ui_components import format_metric_value


def render_dashboard():
    """Render the main dashboard with overview metrics and charts."""
    st.header("📈 Dashboard Overview")
    
    policies_data = api_client.get("/api/policies/")
    indicators_data = api_client.get("/api/data/indicators")
    
    if not policies_data or not indicators_data:
        st.error("Unable to load dashboard data. Please check API connection.")
        return
    
    _render_overview_metrics(policies_data, indicators_data)
    _render_dashboard_charts(policies_data, indicators_data)


def _render_overview_metrics(policies_data: dict, indicators_data: dict):
    """Render overview metrics cards."""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Policies",
            value=policies_data.get('total', 0),
            delta="3 Active"
        )
    
    with col2:
        policies = policies_data.get('policies', [])
        if policies:
            avg_effectiveness = sum(p['effectiveness_score'] for p in policies) / len(policies)
            st.metric(
                label="Avg Effectiveness",
                value=f"{avg_effectiveness:.1f}/10",
                delta="0.3 improvement"
            )
    
    with col3:
        st.metric(
            label="Broadband Access",
            value="87.9%",
            delta="14.7% since 2020"
        )
    
    with col4:
        st.metric(
            label="Digital Literacy",
            value="76.8%",
            delta="18.5% since 2020"
        )


def _render_dashboard_charts(policies_data: dict, indicators_data: dict):
    """Render dashboard charts."""
    col1, col2 = st.columns(2)
    
    with col1:
        _render_policy_effectiveness_chart(policies_data)
    
    with col2:
        _render_broadband_trend_chart(indicators_data)


def _render_policy_effectiveness_chart(policies_data: dict):
    """Render policy effectiveness comparison chart."""
    st.subheader("Policy Effectiveness Scores")
    
    policies = policies_data.get('policies', [])
    if not policies:
        st.warning("No policy data available.")
        return
    
    df_policies = pd.DataFrame(policies)
    fig = px.bar(
        df_policies, 
        x='name', 
        y='effectiveness_score',
        title="Policy Effectiveness Comparison",
        color='effectiveness_score',
        color_continuous_scale='viridis'
    )
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)


def _render_broadband_trend_chart(indicators_data: dict):
    """Render broadband access trend chart."""
    st.subheader("Broadband Access Trend")
    
    broadband_data = indicators_data.get('indicators', {}).get('broadband_access')
    if not broadband_data:
        st.warning("No broadband access data available.")
        return
    
    df_broadband = pd.DataFrame(broadband_data)
    df_broadband['date'] = pd.to_datetime(df_broadband['date'])
    
    fig = go.Figure()
    
    # Add traces for different categories
    traces = [
        ('Overall', 'percentage', '#667eea', 3),
        ('Rural', 'rural', '#28a745', 2),
        ('Urban', 'urban', '#dc3545', 2)
    ]
    
    for name, column, color, width in traces:
        fig.add_trace(go.Scatter(
            x=df_broadband['date'],
            y=df_broadband[column],
            mode='lines+markers',
            name=name,
            line=dict(color=color, width=width)
        ))
    
    fig.update_layout(
        title="Broadband Access Over Time",
        xaxis_title="Date",
        yaxis_title="Access Percentage",
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)
