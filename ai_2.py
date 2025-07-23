import kagglehub
import openai
import streamlit as st
import pandas as pd
import os
from pathlib import Path
# Load OpenAI API key from secrets.toml
openai.api_key = st.secrets[“OPENAI_API_KEY”]
# Download dataset
path = kagglehub.dataset_download(“meleknur/global-internet-usage-by-country-2000-2023")
# Load the CSV file
csv_files = list(Path(path).rglob(“*.csv”))
if not csv_files:
    st.error(“No CSV file found in dataset.“)
    st.stop()
df = pd.read_csv(csv_files[0])
# Clean column names
df.columns = df.columns.str.strip()
# Title and description
st.title(“:scroll: AI Petition Generator”)
st.caption(“Generate petitions based on a country’s digital divide indicators.“)
# Dropdown for country
countries = sorted(df[“Country Name”].dropna().unique())
country = st.selectbox(“:earth_africa: Select a country:“, countries)
# Get internet usage for 2023
raw_value = df.loc[df[“Country Name”] == country, “2023"].values[0]
# Convert safely
try:
    internet_2023 = float(raw_value)
    internet_2023_display = f”{internet_2023:.1f}%”
except (ValueError, TypeError):
    internet_2023 = None
    internet_2023_display = None
# Show usage info if available
st.subheader(f”:bar_chart: Internet Access for {country} (2023)“)
if internet_2023_display:
    st.write(f”Percentage of individuals using the internet: {internet_2023_display}“)
# Input for digital issue
issue = st.text_area(“:speaking_head_in_silhouette: What digital issue should the petition address?“)
# Button to generate petition
if st.button(“:writing_hand: Generate Petition”):
    with st.spinner(“Generating petition...“):
        usage_line = (
            f”The percentage of individuals using the internet in 2023 is {internet_2023_display}. ”
            if internet_2023_display else “”
        )
        prompt = (
            f”Write a compelling policy petition to address the issue of ‘{issue}’ in {country}. ”
            f”{usage_line}Make the language formal and community-driven, suitable for public policy advocacy.”
        )
        try:
            response = openai.ChatCompletion.create(
                model=“gpt-4”,
                messages=[{“role”: “user”, “content”: prompt}],
                max_tokens=600,
                temperature=0.7,
            )
            petition_text = response.choices[0].message.content
            st.subheader(“:page_facing_up: Generated Petition”)
            st.write(petition_text)
        except Exception as e:
            st.error(f”Failed to generate petition: {str(e)}“)