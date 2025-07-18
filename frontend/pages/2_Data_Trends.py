"""
Data trends analysis page for Digital Divide Policy Insights.
"""

import streamlit as st
import pandas as pd
import plotly.express as px

from utils.api_client import api_client
from components.ui_components import render_section_header


def render_data_trends_page():
    """Render data trends and correlation analysis page."""
    render_section_header("Data Trends & Analysis", "Explore trends, demographics, and correlations in digital divide data.")
    
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
        st.metric(
            label="Trend",
            value=f"{trend['trend_direction'].title()}"
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
    
    fig = px.bar(income_df, x='Income Level', y='internet_access', 
                 title="Internet Access by Income Level",
                 labels={'internet_access': 'Internet Access (%)'})
    st.plotly_chart(fig, use_container_width=True)


def _render_geographic_analysis(geo_data: dict):
    """Render geographic analysis chart."""
    st.subheader("Digital Access by Geographic Location")
    
    geo_df = pd.DataFrame(geo_data).T.reset_index()
    geo_df.columns = ['Location'] + list(geo_df.columns[1:])
    
    fig = px.pie(geo_df, names='Location', values='broadband_penetration', 
                 title="Broadband Penetration by Location",
                 hole=0.3)
    st.plotly_chart(fig, use_container_width=True)


def _render_age_analysis(age_data: dict):
    """Render age group analysis chart."""
    st.subheader("Digital Literacy by Age Group")
    
    age_df = pd.DataFrame(age_data).T.reset_index()
    age_df.columns = ['Age Group'] + list(age_df.columns[1:])
    
    fig = px.funnel(age_df, x='Age Group', y='digital_literacy_rate',
                    title="Digital Literacy Rate by Age Group")
    st.plotly_chart(fig, use_container_width=True)


def _render_correlation_analysis(correlation_data: dict):
    """Render correlation analysis heatmap."""
    st.subheader("Correlation Analysis")
    
    corr_matrix = correlation_data.get('correlation_matrix')
    if not corr_matrix:
        st.warning("No correlation data available.")
        return
        
    df = pd.DataFrame(corr_matrix)
    
    fig = px.imshow(df, text_auto=True, aspect="auto",
                    title="Correlation Matrix of Digital Divide Indicators")
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    from components.ui_components import load_custom_css
    st.set_page_config(layout="wide", page_title="Data Trends - Digital Divide Policy Insights", page_icon="frontend/assets/icons/trends.svg")
    load_custom_css()
    render_data_trends_page()
