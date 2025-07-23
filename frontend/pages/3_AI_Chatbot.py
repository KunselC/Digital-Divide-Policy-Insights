"""
AI Chatbot Page
"""

import streamlit as st
from typing import List, Dict
import sys
import os
import pandas as pd
from pathlib import Path

# Add the parent directory to the Python path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.api_client import api_client
from config import CHATBOT_SUGGESTIONS
from components.ui_components import display_page_header, load_custom_css, display_interactive_background


def render_chatbot_page():
    """Render AI-powered policy chatbot page."""
    display_page_header(
        title="AI Policy Assistant", 
        subtitle="Chat with AI or generate policy petitions based on digital divide data.",
        icon_name="chatbot.svg"
    )
    
    # Initialize chat session
    _initialize_chat_session()
    
    # Create tabs for different AI functionalities  
    tab1, tab2 = st.tabs(["AI Chatbot", "Petition Generator"])
    
    with tab1:
        _render_chat_display()
        _render_sidebar_suggestions()
    
    with tab2:
        _render_petition_generator()
    
    # Chat input must be outside tabs
    if prompt := st.chat_input("What do you want to know?"):
        _handle_user_message(prompt)


def _initialize_chat_session():
    """Initialize chat session state."""
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I'm here to help you understand digital divide policies. What would you like to know?"}
        ]


def _render_chat_display():
    """Display existing chat messages."""
    # Display existing chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def _render_chat_interface():
    """Render the main chat interface."""
    _render_chat_display()
    
    # Chat input handling is now moved to main function outside tabs


def _handle_user_message(prompt: str):
    """
    Handle new user message and generate bot response.
    
    Args:
        prompt: User's input message
    """
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display bot response
    with st.chat_message("assistant"):
        response_text = _get_bot_response(prompt)
        st.markdown(response_text)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response_text})


def _get_bot_response(prompt: str) -> str:
    """
    Get response from the chatbot API.
    
    Args:
        prompt: User's input message
        
    Returns:
        Bot response text
    """
    with st.spinner("Thinking..."):
        try:
            response_data = api_client.post("/api/chatbot/chat", {"message": prompt})
            
            if response_data:
                bot_response = response_data.get('bot_response', 
                                               "Sorry, I couldn't find an answer to that.")
                
                # Handle suggestions if available
                suggestions = response_data.get('suggestions', [])
                if suggestions:
                    _render_response_suggestions(suggestions)
                
                return bot_response
            else:
                return "Sorry, the AI service is currently unavailable. This is a demo platform - in a real deployment, this would connect to an AI service for data analysis."
        except Exception as e:
            return f"The AI chatbot service is currently in demo mode. In a full deployment, this would provide intelligent responses about digital divide data and analysis."


def _render_response_suggestions(suggestions: List[str]):
    """
    Render suggestion buttons for follow-up questions.
    
    Args:
        suggestions: List of suggested follow-up questions
    """
    st.markdown("**Here are some other questions you could ask:**")
    
    for i, suggestion in enumerate(suggestions):
        button_key = f"suggestion_{len(st.session_state.messages)}_{i}_{hash(suggestion) % 10000}"
        if st.button(suggestion, key=button_key):
            _handle_user_message(suggestion)


def _render_sidebar_suggestions():
    """Render sidebar with suggested conversation starters."""
    with st.sidebar:
        st.subheader("Don't know where to start?")
        st.write("Try one of these conversation starters:")
        
        for i, suggestion in enumerate(CHATBOT_SUGGESTIONS):
            if st.button(suggestion, key=f"sidebar_{i}_{hash(suggestion) % 10000}"):
                _handle_user_message(suggestion)


def _render_petition_generator():
    """Render the AI petition generator interface."""
    st.subheader("AI Policy Petition Generator")
    st.caption("Generate compelling policy petitions based on a country's digital divide indicators.")
    
    # Load internet usage data
    try:
        data_path = Path(__file__).parent.parent.parent / "ml_data" / "internet_usage.csv"
        if not data_path.exists():
            st.error("Internet usage data not found. Please ensure the data file is available.")
            return
        
        df = pd.read_csv(data_path)
        df.columns = df.columns.str.strip()
        
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return
    
    # Country selection
    countries = sorted(df["Country Name"].dropna().unique())
    country = st.selectbox("Select a country:", countries, key="petition_country")
    
    # Get internet usage for 2023 (or latest available year)
    country_data = df[df["Country Name"] == country]
    if not country_data.empty:
        # Try to get 2023 data, fall back to latest available
        internet_2023 = None
        internet_display = "Data not available"
        
        for year in ["2023", "2022", "2021", "2020"]:
            if year in df.columns:
                raw_value = country_data[year].values[0]
                try:
                    if pd.notna(raw_value) and raw_value != "..":
                        internet_2023 = float(raw_value)
                        internet_display = f"{internet_2023:.1f}%"
                        break
                except (ValueError, TypeError):
                    continue
    
    # Display internet access info
    col1, col2 = st.columns([2, 1])
    with col1:
        st.info(f"**Internet Access in {country}**: {internet_display}")
    with col2:
        if internet_2023 is not None:
            if internet_2023 < 25:
                st.error("Low access")
            elif internet_2023 < 50:
                st.warning("Moderate access") 
            else:
                st.success("Good access")
    
    # Issue input
    st.subheader("Define the Digital Issue")
    issue = st.text_area(
        "What digital divide issue should the petition address?",
        placeholder="e.g., Lack of affordable internet access in rural areas, Digital literacy gaps in education, Limited mobile infrastructure...",
        height=100,
        key="petition_issue"
    )
    
    # Target audience
    audience = st.selectbox(
        "Who should this petition target?",
        [
            "Government/Ministry of Communications",
            "Local Government/Municipal Authorities", 
            "Internet Service Providers",
            "Educational Institutions",
            "International Organizations",
            "Private Sector/Tech Companies"
        ],
        key="petition_audience"
    )
    
    # Generate petition button
    if st.button("Generate Policy Petition", type="primary", key="generate_petition"):
        if not issue.strip():
            st.error("Please describe the digital issue first.")
            return
            
        with st.spinner("Generating petition..."):
            # Create petition prompt
            usage_info = f"The percentage of individuals using the internet is {internet_display}" if internet_display != "Data not available" else "Internet usage data is limited"
            
            prompt = f"""Write a compelling policy petition to address the digital divide issue of '{issue}' in {country}. 

Context: {usage_info}.

The petition should:
1. Be addressed to {audience}
2. Use formal, professional language suitable for policy advocacy
3. Include specific, actionable demands
4. Mention the broader impact on society and economy
5. Be between 300-500 words
6. Include a clear call to action

Make it community-driven and emphasize the urgency of addressing digital inequalities."""

            try:
                # Use the API client to generate the petition
                response_data = api_client.post("/api/chatbot/chat", {
                    "message": prompt,
                    "type": "petition_generation"
                })
                
                if response_data and 'bot_response' in response_data:
                    petition_text = response_data['bot_response']
                    
                    st.subheader("Generated Policy Petition")
                    st.markdown("---")
                    st.markdown(petition_text)
                    st.markdown("---")
                    
                    # Add download button
                    petition_filename = f"petition_{country.replace(' ', '_').lower()}.txt"
                    st.download_button(
                        label="Download Petition",
                        data=petition_text,
                        file_name=petition_filename,
                        mime="text/plain",
                        key="download_petition"
                    )
                    
                else:
                    # Fallback template since API is not available
                    st.info("AI service in demo mode - showing template petition:")
                    _show_template_petition(country, audience, issue, internet_display)
                    
            except Exception as e:
                st.info("AI service currently unavailable - showing template petition:")
                _show_template_petition(country, audience, issue, internet_display)


def _show_template_petition(country: str, audience: str, issue: str, internet_display: str):
    """Show a template petition when AI service is unavailable."""
    template_petition = f"""
**PETITION FOR DIGITAL EQUITY IN {country.upper()}**

To: {audience}

We, the undersigned citizens and stakeholders, respectfully petition for immediate action to address the critical digital divide issue of {issue} in {country}.

**Current Situation:**
The current internet access rate is {internet_display}, highlighting significant disparities in digital access and opportunities across our nation.

**Our Demands:**
1. Immediate investment in digital infrastructure development
2. Implementation of affordable internet access programs
3. Establishment of digital literacy training initiatives
4. Creation of public-private partnerships to expand connectivity
5. Development of targeted support for underserved communities

**Impact:**
Addressing this digital divide is essential for:
- Economic growth and competitiveness
- Educational opportunities for all citizens
- Healthcare access and telemedicine services
- Social inclusion and democratic participation
- Sustainable development goals achievement

**Call to Action:**
We urge {audience} to prioritize digital equity initiatives and allocate necessary resources to bridge the digital divide within the next fiscal year.

The digital divide is not just a technological issue—it's a matter of social justice and economic necessity. We call for swift, decisive action to ensure no citizen is left behind in our digital future.

Respectfully submitted,
[Your Organization/Community Group]
"""
    st.markdown(template_petition)
    
    # Add download button for template
    petition_filename = f"petition_{country.replace(' ', '_').lower()}.txt"
    st.download_button(
        label="Download Template Petition",
        data=template_petition,
        file_name=petition_filename,
        mime="text/plain",
        key="download_template_petition"
    )


def main():
    """Main function to set up and render the page."""
    from components.ui_components import load_custom_css, display_interactive_background
    
    st.set_page_config(
        page_title="AI Chatbot - NetEquity",
        layout="wide"
    )
    load_custom_css()
    display_interactive_background()
    render_chatbot_page()

if __name__ == "__main__":
    main()
