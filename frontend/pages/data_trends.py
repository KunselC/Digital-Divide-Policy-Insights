"""
Data trends analysis page for Digital Divide Policy Insights.
"""

import streamlit as st
import pandas as pd
import plotly.express as px

from utils.api_client import api_client


def render_data_trends():
    """Render data trends and correlation analysis page."""
    st.header("📊 Data Trends & Analysis")
    
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
    st.subheader("Trend Analysis (2020-2023)")
    
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
        direction_emoji = "📈" if trend['trend_direction'] == "increasing" else "📉"
        st.metric(
            label="Trend",
            value=f"{direction_emoji} {trend['trend_direction'].title()}"
        )


def _render_demographics_analysis(demographics_data: dict):
    """Render demographics analysis charts."""
    st.subheader("Demographics Analysis")
    
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
    """Render income level analysis chart."""
    st.subheader("Digital Access by Income Level")
    
    income_df = pd.DataFrame(income_data).T.reset_index()
    income_df.columns = ['Income Level'] + list(income_df.columns[1:])
    
    # Ensure we have the expected columns
    if 'broadband_access' in income_df.columns and 'digital_literacy' in income_df.columns:
        fig = px.bar(
            income_df,
            x='Income Level',
            y=['broadband_access', 'digital_literacy'],
            title="Digital Access by Income Level",
            barmode='group',
            labels={'value': 'Percentage', 'variable': 'Metric'}
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Income data does not contain expected metrics.")


def _render_geographic_analysis(geographic_data: dict):
    """Render geographic analysis chart."""
    st.subheader("Digital Access by Geographic Region")
    
    geo_df = pd.DataFrame(geographic_data).T.reset_index()
    geo_df.columns = ['Region'] + list(geo_df.columns[1:])
    
    if 'broadband_access' in geo_df.columns:
        fig = px.bar(
            geo_df,
            x='Region',
            y='broadband_access',
            title="Broadband Access by Geographic Region",
            color='broadband_access',
            color_continuous_scale='viridis'
        )
        st.plotly_chart(fig, use_container_width=True)


def _render_age_analysis(age_data: dict):
    """Render age group analysis chart."""
    st.subheader("Digital Literacy by Age Group")
    
    age_df = pd.DataFrame(age_data).T.reset_index()
    age_df.columns = ['Age Group'] + list(age_df.columns[1:])
    
    if 'digital_literacy' in age_df.columns:
        fig = px.line(
            age_df,
            x='Age Group',
            y='digital_literacy',
            title="Digital Literacy by Age Group",
            markers=True
        )
        st.plotly_chart(fig, use_container_width=True)


def _render_correlation_analysis(correlation_data: dict):
    """Render correlation analysis."""
    st.subheader("Policy Correlation Analysis")
    
    correlations = correlation_data.get('correlations', {})
    if correlations:
        for metric, correlation in correlations.items():
            st.metric(
                label=f"{metric.replace('_', ' ').title()} Correlation",
                value=f"{correlation:.3f}"
            )
    else:
        st.info("No correlation data available.")
