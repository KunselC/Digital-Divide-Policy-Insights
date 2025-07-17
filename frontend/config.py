"""
Configuration settings for the Digital Divide Policy Insights frontend.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
API_BASE_URL = os.getenv('API_BASE_URL', 'http://localhost:5001')

# App Configuration
APP_TITLE = "Digital Divide Policy Insights"
APP_ICON = "📊"
APP_SUBTITLE = "Analyzing Technology Policies and Their Effectiveness in Bridging the Digital Divide"

# Theme Configuration
THEME_CONFIG = {
    "primary_color": "#2563eb",
    "background_color": "#ffffff", 
    "secondary_background_color": "#f8fafc",
    "text_color": "#0f172a",
    "accent_color": "#0ea5e9"
}

# Page Configuration
PAGES = [
    "Dashboard",
    "Policy Analysis", 
    "Data Trends",
    "AI Chatbot",
    "About"
]

# Streamlit Configuration
STREAMLIT_CONFIG = {
    "page_title": APP_TITLE,
    "page_icon": APP_ICON,
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "menu_items": {
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
}

# Quick questions for chatbot
CHATBOT_SUGGESTIONS = [
    "What is the Digital Equity Act?",
    "How effective are the policies?",
    "Compare all policies",
    "Show policy statistics"
]
