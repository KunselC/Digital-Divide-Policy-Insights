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
    
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    
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
    
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    """Main function to set up and render the page."""
    st.set_page_config(
        page_title="Data Trends - NetEquity",
        layout="wide"
    )
    load_custom_css()
    display_interactive_background()
    render_data_trends_page()

if __name__ == "__main__":
    main()
