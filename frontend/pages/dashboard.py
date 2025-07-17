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
    """Render the main dashboard with professional overview metrics and charts."""
    # Use professional section header instead of st.header
    from components.ui_components import render_section_header, render_metric_card, render_info_box
    
    render_section_header(
        "Dashboard Overview", 
        "Key metrics and trends in digital divide policy effectiveness"
    )
    
    policies_data = api_client.get("/api/policies/")
    indicators_data = api_client.get("/api/data/indicators")
    
    if not policies_data or not indicators_data:
        render_info_box(
            "Unable to load dashboard data. Please check API connection and try again.",
            "error"
        )
        return
    
    _render_overview_metrics(policies_data, indicators_data)
    _render_dashboard_charts(policies_data, indicators_data)


def _render_overview_metrics(policies_data: dict, indicators_data: dict):
    """Render professional overview metrics cards."""
    from components.ui_components import render_metric_card
    
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
            avg_effectiveness = sum(p.get('effectiveness_score', 0) for p in policies) / len(policies)
            st.metric(
                label="Avg Effectiveness",
                value=f"{avg_effectiveness:.1f}/10",
                delta="+0.3 improvement"
            )
    
    with col3:
        # Calculate broadband access trend
        indicators = indicators_data.get('data', {}).get('indicators', {}).get('indicators', {})
        broadband_data = indicators.get('broadband_access', [])
        if len(broadband_data) >= 2:
            latest = broadband_data[-1].get('percentage', 0)
            previous = broadband_data[-2].get('percentage', 0)
            change = latest - previous
            st.metric(
                label="Broadband Access",
                value=f"{latest:.1f}%",
                delta=f"{change:+.1f}%"
            )
    
    with col4:
        # Calculate total data points
        total_points = indicators_data.get('data', {}).get('indicators', {}).get('total_points', 0)
        st.metric(
            label="Data Points",
            value=f"{total_points:,}",
            delta="Real-time"
        )


def _render_dashboard_charts(policies_data: dict, indicators_data: dict):
    """Render professional dashboard charts with improved styling."""
    from components.ui_components import render_section_header
    
    render_section_header(
        "Digital Divide Trends", 
        "Historical data showing progress in key digital equity indicators"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        _render_policy_effectiveness_chart(policies_data)
    
    with col2:
        _render_broadband_trend_chart(indicators_data)


def _render_policy_effectiveness_chart(policies_data: dict):
    """Render professional policy effectiveness comparison chart."""
    policies = policies_data.get('policies', [])
    if not policies:
        st.warning("No policy data available.")
        return
    
    df_policies = pd.DataFrame(policies)
    
    # Professional color scheme
    colors = ['#2563eb', '#0ea5e9', '#059669', '#d97706', '#dc2626']
    
    fig = px.bar(
        df_policies, 
        x='name', 
        y='effectiveness_score',
        title="Policy Effectiveness Scores",
        color='effectiveness_score',
        color_continuous_scale='blues',
        text='effectiveness_score'
    )
    
    # Professional styling
    fig.update_layout(
        title_font_size=16,
        title_font_color='#0f172a',
        xaxis_tickangle=-45,
        xaxis_title="Policy",
        yaxis_title="Effectiveness Score (out of 10)",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_family="Inter",
        showlegend=False
    )
    
    fig.update_traces(
        texttemplate='%{text:.1f}',
        textposition='outside',
        marker_line_color='rgba(0,0,0,0)',
        marker_line_width=0
    )
    
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor='#e2e8f0', gridwidth=1)
    
    st.plotly_chart(fig, use_container_width=True)


def _render_broadband_trend_chart(indicators_data: dict):
    """Render professional broadband access trend chart."""
    # Get nested indicators data
    indicators = indicators_data.get('data', {}).get('indicators', {}).get('indicators', {})
    broadband_data = indicators.get('broadband_access', [])
    
    if not broadband_data:
        st.warning("No broadband access data available.")
        return
    
    df_broadband = pd.DataFrame(broadband_data)
    df_broadband['date'] = pd.to_datetime(df_broadband['date'])
    
    fig = go.Figure()
    
    # Professional color scheme
    colors = {
        'percentage': '#2563eb',
        'rural': '#059669', 
        'urban': '#0ea5e9'
    }
    
    # Add traces for different categories
    traces = [
        ('percentage', 'Overall', colors['percentage']),
        ('rural', 'Rural', colors['rural']),
        ('urban', 'Urban', colors['urban'])
    ]
    
    for column, name, color in traces:
        if column in df_broadband.columns:
            fig.add_trace(go.Scatter(
                x=df_broadband['date'],
                y=df_broadband[column],
                mode='lines+markers',
                name=name,
                line=dict(color=color, width=3),
                marker=dict(size=6, color=color),
                hovertemplate=f'<b>{name}</b><br>Date: %{{x}}<br>Access: %{{y:.1f}}%<extra></extra>'
            ))
    
    # Professional styling
    fig.update_layout(
        title="Broadband Access Trends Over Time",
        title_font_size=16,
        title_font_color='#0f172a',
        xaxis_title="Date",
        yaxis_title="Access Percentage (%)",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_family="Inter",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        hovermode='x unified'
    )
    
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor='#e2e8f0', gridwidth=1)
    
    st.plotly_chart(fig, use_container_width=True)
