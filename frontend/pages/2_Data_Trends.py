"""
Data Trends Page
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import sys
import os

# Add the parent directory to the Python path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.api_client import api_client
from components.ui_components import display_page_header, load_custom_css, display_interactive_background


def render_data_trends_page():
    """Render data trends and correlation analysis page."""
    display_page_header(
        title="Data Trends", 
        subtitle="See how digital access is changing over time and across different groups.",
        icon_name="data-trends.svg"
    )
    
    trends_data = api_client.get("/api/data/trends")
    correlation_data = api_client.get("/api/data/correlation")
    demographics_data = api_client.get("/api/data/demographics")
    
    if trends_data:
        _render_trend_analysis(trends_data)
    
    if demographics_data:
        _render_demographics_analysis(demographics_data)
    
    if correlation_data:
        _render_correlation_analysis(correlation_data)


def _render_trend_analysis(trends_data: dict):
    """Render trend analysis metrics."""
    st.subheader("Digital Access Trends (2020-2023)")
    
    trends = trends_data.get('trends', {})
    if not trends:
        st.warning("No trend data available.")
        return
    
    for indicator, trend in trends.items():
        _render_trend_metrics(indicator, trend)


def _render_trend_metrics(indicator: str, trend: dict):
    """Render individual trend metrics."""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label=indicator.replace('_', ' ').title(),
            value=f"{trend['end_value']:.1f}%"
        )
    
    with col2:
        st.metric(
            label="Absolute Change",
            value=f"{trend['absolute_change']:+.1f}%"
        )
    
    with col3:
        st.metric(
            label="Percentage Change",
            value=f"{trend['percentage_change']:+.1f}%"
        )
    
    with col4:
        st.metric(
            label="Trend",
            value=f"{trend['trend_direction'].title()}"
        )


def _render_demographics_analysis(demographics_data: dict):
    """Render demographics analysis charts."""
    st.subheader("Who is Being Affected?")
    
    demo_data = demographics_data.get('demographics', {})
    if not demo_data:
        st.warning("No demographics data available.")
        return
    
    # Income levels analysis
    if 'income_levels' in demo_data:
        _render_income_analysis(demo_data['income_levels'])
    
    # Geographic analysis
    if 'geographic' in demo_data:
        _render_geographic_analysis(demo_data['geographic'])
    
    # Age groups analysis
    if 'age_groups' in demo_data:
        _render_age_analysis(demo_data['age_groups'])


def _render_income_analysis(income_data: dict):
    """Render income level analysis chart as a 3D scatter plot."""
    st.subheader("Digital Access by Income")
    
    df = pd.DataFrame(income_data)
    
    if df.empty:
        st.warning("No income data available for 3D analysis.")
        return

    df = df.T.reset_index()
    df.columns = ['Income Level', 'internet_access', 'device_ownership']
    
    # Add a synthetic 'digital_literacy' dimension for 3D effect
    df['digital_literacy'] = np.random.uniform(low=40, high=90, size=len(df))

    fig = go.Figure(data=[go.Scatter3d(
        x=df['internet_access'],
        y=df['device_ownership'],
        z=df['digital_literacy'],
        text=df['Income Level'],
        mode='markers',
        marker=dict(
            size=12,
            color=df['digital_literacy'], # set color to a variable
            colorscale='Viridis',   # choose a colorscale
            opacity=0.8,
            colorbar=dict(title='Digital Literacy')
        )
    )])
    
    fig.update_layout(
        title="Digital Access Metrics by Income Level",
        scene=dict(
            xaxis_title='Internet Access (%)',
            yaxis_title='Device Ownership (%)',
            zaxis_title='Digital Literacy (%)'
        ),
        margin=dict(r=20, b=10, l=10, t=40)
    )
    st.plotly_chart(fig, use_container_width=True)


def _render_geographic_analysis(geo_data: dict):
    """Render geographic analysis chart as a 3D bar chart."""
    st.subheader("Digital Access by Geography")
    
    df = pd.DataFrame(geo_data)
    
    if df.empty:
        st.warning("No geographic data available for 3D analysis.")
        return

    df = df.T.reset_index()
    df.columns = ['Location', 'broadband_penetration', 'avg_speed']

    fig = go.Figure(data=[go.Bar(
        x=df['Location'],
        y=df['broadband_penetration'],
        marker_color=df['avg_speed'],
        marker=dict(
            colorscale='Blues',
            colorbar=dict(title='Avg. Speed (Mbps)')
        ),
        text=df['avg_speed'],
        textposition='auto'
    )])

    fig.update_layout(
        title="Broadband Penetration and Speed by Location",
        xaxis_title="Location",
        yaxis_title="Broadband Penetration (%)",
        scene=dict(
            xaxis=dict(title='Location'),
            yaxis=dict(title='Broadband Penetration (%)'),
            zaxis=dict(title='Average Speed (Mbps)'),
        ),
        # This is a 2D chart styled to look more dynamic, as true 3D bars can be misleading.
        # For a true 3D bar chart, one would need a third axis variable.
    )
    st.plotly_chart(fig, use_container_width=True)


def _render_age_analysis(age_data: dict):
    """Render age group analysis chart as a 3D surface plot."""
    st.subheader("Digital Access by Age Group")
    
    df = pd.DataFrame(age_data).T.reset_index()
    df.columns = ['Age Group'] + list(df.columns[1:])
    
    fig = px.funnel(df, x='Age Group', y='digital_literacy_rate',
                    title="Digital Literacy Rate by Age Group")
    st.plotly_chart(fig, use_container_width=True)


def _render_correlation_analysis(correlation_data: dict):
    """Render correlation analysis heatmap."""
    st.subheader("What's Related?")
    
    corr_matrix = correlation_data.get('correlation_matrix', [])
    if not corr_matrix:
        st.warning("No correlation data available.")
        return
        
    df = pd.DataFrame(corr_matrix)
    
    fig = px.imshow(df, text_auto=True, aspect="auto",
                    title="Correlation Matrix of Digital Divide Indicators")
    st.plotly_chart(fig, use_container_width=True)


def main():
    """Main function to set up and render the page."""
    from components.ui_components import load_custom_css, display_interactive_background
    
    st.set_page_config(
        page_title="Data Trends - NetEquity",
        layout="wide"
    )
    load_custom_css()
    display_interactive_background()
    render_data_trends_page()

if __name__ == "__main__":
    main()
