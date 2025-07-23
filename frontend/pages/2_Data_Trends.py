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
import matplotlib.pyplot as plt

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
    # --- Custom Internet Access Trend Plot ---
    col_header1, col_header2 = st.columns(2)
    
    usage_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ml_data/internet_usage.csv'))
    profile_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ml_data/country_profile_variables.csv'))
    if os.path.exists(usage_path) and os.path.exists(profile_path):
        usage = pd.read_csv(usage_path)
        profile = pd.read_csv(profile_path)
        # ...existing code...
        # --- Animated Choropleth Map: Internet Usage Change by Country ---
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("Internet Usage Change by Country (2000–2023)")
        df_long = pd.melt(usage, id_vars=["Country Name", "Country Code"], var_name="Year", value_name="Value")
        df_long["Year"] = df_long["Year"].astype(int)
        # Clean up non-numeric values for choropleth
        df_long["Value"] = pd.to_numeric(df_long["Value"], errors="coerce")
        vmin = df_long["Value"].min()
        vmax = df_long["Value"].max()
        fig = px.choropleth(
            df_long,
            locations="Country Code",
            color="Value",
            hover_name="Country Name",
            animation_frame="Year",
            color_continuous_scale="Viridis",
            range_color=[vmin, vmax],
            projection="natural earth"
        )
        fig.update_traces(zmin=vmin, zmax=vmax, selector=dict(type='choropleth'))
        fig.update_layout(
            coloraxis_colorbar=dict(title="Change (%)"),
            title="Internet Usage Change by Country (2000–2023)"
        )
        st.plotly_chart(fig, use_container_width=True)
    
<<<<<<< HEAD
=======
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    
>>>>>>> origin/main
    # --- Custom Internet Access Trend Plot ---
    col_header1, col_header2 = st.columns(2)
    with col_header1:
        st.markdown('<span style="color:#0F172A; font-size:25.6px; font-family:Source Sans Pro, sans-serif; font-weight:bold; display:inline-block;">Internet Access Trends by Country</span>', unsafe_allow_html=True)
    with col_header2:
        st.markdown('<span style="color:#0F172A; font-size:25.6px; font-family:Source Sans Pro, sans-serif; font-weight:bold; display:inline-block;">Average Internet Access by Continent</span>', unsafe_allow_html=True)
    usage_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ml_data/internet_usage.csv'))
    profile_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ml_data/country_profile_variables.csv'))
    if os.path.exists(usage_path) and os.path.exists(profile_path):
        usage = pd.read_csv(usage_path)
        profile = pd.read_csv(profile_path)
        # Merge on country name
        merged = usage.merge(profile[['country', 'Region']], left_on='Country Name', right_on='country', how='left')
        # Map region names to continents
        region_to_continent = {
            # Africa
            'NorthernAfrica': 'Africa', 'MiddleAfrica': 'Africa', 'EasternAfrica': 'Africa', 'WesternAfrica': 'Africa', 'SouthernAfrica': 'Africa',
            # Asia
            'WesternAsia': 'Asia', 'SouthernAsia': 'Asia', 'South-easternAsia': 'Asia', 'EasternAsia': 'Asia', 'CentralAsia': 'Asia',
            # Europe
            'WesternEurope': 'Europe', 'EasternEurope': 'Europe', 'SouthernEurope': 'Europe', 'NorthernEurope': 'Europe',
            # Americas
            'NorthernAmerica': 'North America', 'CentralAmerica': 'North America', 'Caribbean': 'North America', 'SouthAmerica': 'South America',
            # Oceania
            'Oceania': 'Oceania', 'Polynesia': 'Oceania', 'Melanesia': 'Oceania', 'Micronesia': 'Oceania'
        }
        merged['Continent'] = merged['Region'].map(region_to_continent)
        country_list = merged['Country Name'].dropna().unique().tolist()
        provided_countries = country_list
        col1, col2 = st.columns(2)
        with col1:
            country_name = st.selectbox("Select Country", provided_countries, index=provided_countries.index("Ethiopia") if "Ethiopia" in provided_countries else 0)
            country_data = merged[merged['Country Name'] == country_name]
            if not country_data.empty:
                year_data = country_data.iloc[0, 2:len(usage.columns)].replace(['..', '...', 'N/A', 'n/a'], np.nan)
                year_values = pd.to_numeric(year_data, errors='coerce').values
                years = list(range(2000, 2000 + len(year_values)))
                pct_change = pd.Series(year_values).pct_change() * 100
                fig, ax1 = plt.subplots(figsize=(8, 5))
                fig.patch.set_facecolor('#f7fbfc')
                ax1.set_facecolor('#f7fbfc')
                ax1.plot(years, year_values, marker='o', color='#0074D9', label='Percent Internet Access', linewidth=3, markersize=10)
                ax1.set_xlabel('Year', color='#0074D9', fontsize=13)
                ax1.set_ylabel('Total Internet Access (%)', color='#0074D9', fontsize=13)
                ax1.tick_params(axis='y', labelcolor='#0074D9', labelsize=12)
                ax1.tick_params(axis='x', colors='#0074D9', labelsize=12)
                ax1.grid(True, alpha=0.2, color='#DDDDDD')
                ax2 = ax1.twinx()
                ax2.set_facecolor('#f7fbfc')
                ax2.plot(years, pct_change, marker='o', color='#FF4136', label='% Year-over-Year Change', linewidth=3, markersize=10)
                ax2.set_ylabel('% Change', color='#FF4136', fontsize=13)
                ax2.tick_params(axis='y', labelcolor='#FF4136', labelsize=12)
                ax2.tick_params(axis='x', colors='#0074D9', labelsize=12)
                # Add legends
                lines1, labels1 = ax1.get_legend_handles_labels()
                lines2, labels2 = ax2.get_legend_handles_labels()
                ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=12, facecolor='#f7fbfc')
                plt.title(f'{country_name} - Internet Access and Year-over-Year % Change', color='#0074D9', fontsize=16, weight='bold')
                fig.tight_layout()
                st.pyplot(fig)
            else:
                st.warning(f"No data available for {country_name}.")
        with col2:
            continent_names = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
            selected_continent = st.selectbox("Select Continent", continent_names, index=continent_names.index("Africa") if "Africa" in continent_names else 0, key="continent_selectbox_col2")
            df_continent = merged[merged['Continent'] == selected_continent]
            MIN_COUNTRIES = 5
            year_means_continent = {}
            for year in usage.columns.tolist()[2:]:
                df_continent[year] = pd.to_numeric(df_continent[year], errors='coerce')
                values = df_continent[year].values
                clean_values = values[np.isfinite(values)]
                if len(clean_values) >= MIN_COUNTRIES:
                    year_means_continent[year] = np.mean(clean_values)
                else:
                    year_means_continent[year] = np.nan
            df_mean_continent = pd.DataFrame([year_means_continent])
            fig3, ax3 = plt.subplots(figsize=(8, 5))
            fig3.patch.set_facecolor('#f7fbfc')
            ax3.set_facecolor('#f7fbfc')
            years_cont = df_mean_continent.columns.tolist()
            means = df_mean_continent.iloc[0].values
            ax3.plot(years_cont, means, marker='o', linewidth=3, markersize=10, color='#2ECC40', label='Average Internet Access')
            ax3.set_title(f'Average Internet Access Over Time - {selected_continent}', color='#2ECC40', fontsize=16, weight='bold')
            ax3.set_xlabel('Year', color='#2ECC40', fontsize=13)
            ax3.set_ylabel('Average Internet Access (%)', color='#2ECC40', fontsize=13)
            ax3.grid(True, alpha=0.2, color='#DDDDDD')
            ax3.tick_params(axis='x', colors='#2ECC40', labelsize=12)
            ax3.tick_params(axis='y', colors='#2ECC40', labelsize=12)
            plt.xticks(rotation=45, color='#2ECC40')
            ax3.legend(loc='upper left', fontsize=12, facecolor='#f7fbfc')
            fig3.tight_layout()
            st.pyplot(fig3)
        # --- Continent Mean Plot ---
        # ...removed duplicate continent plot and selectbox...
    else:
        st.error("internet_usage.csv or country_profile_variables.csv not found in ml_data folder.")
<<<<<<< HEAD

    # --- Existing API-based sections removed as requested ---


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
    
=======
    
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    """Main function to set up and render the page."""
>>>>>>> origin/main
    st.set_page_config(
        page_title="Data Trends - NetEquity",
        layout="wide"
    )
    load_custom_css()
    display_interactive_background()
    render_data_trends_page()

if __name__ == "__main__":
    main()
