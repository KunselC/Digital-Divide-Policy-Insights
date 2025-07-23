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
                # Use built-in AI responses when API is unavailable
                return _get_local_ai_response(prompt)
        except Exception as e:
            # Use built-in AI responses when API fails
            return _get_local_ai_response(prompt)


def _get_local_ai_response(prompt: str) -> str:
    """Generate local AI responses when API is unavailable."""
    prompt_lower = prompt.lower()
    
    if 'digital divide' in prompt_lower:
        return "The digital divide refers to the gap between those who have access to modern information and communications technology and those who don't. This includes disparities in internet access, digital literacy, and technology availability across different demographics and regions."
    
    elif 'broadband' in prompt_lower or 'internet access' in prompt_lower:
        return "Broadband internet access is crucial for digital equity. Key policies include the Broadband Equity Access and Deployment (BEAD) program, which allocates $42.5 billion to expand broadband infrastructure, and the Affordable Connectivity Program, which provides internet subsidies to low-income households."
    
    elif 'policy' in prompt_lower or 'policies' in prompt_lower:
        return "Digital divide policies focus on expanding internet infrastructure, improving affordability, and increasing digital literacy. Major initiatives include federal broadband programs, state-level digital equity plans, and local community technology centers."
    
    elif 'rural' in prompt_lower:
        return "Rural areas face unique digital divide challenges including limited infrastructure, higher costs, and lower population density. Solutions include targeted funding for rural broadband expansion, satellite internet initiatives, and public-private partnerships."
    
    elif 'education' in prompt_lower or 'school' in prompt_lower:
        return "Education is significantly impacted by the digital divide. Students without reliable internet access face challenges with online learning, homework completion, and digital skill development. Programs like E-rate help schools get affordable internet access."
    
    elif 'affordability' in prompt_lower or 'cost' in prompt_lower:
        return "Internet affordability is a major barrier to digital equity. The Affordable Connectivity Program provides up to $30/month discount for eligible households. Other solutions include municipal broadband, competition among ISPs, and device subsidy programs."
    
    elif 'data' in prompt_lower or 'statistics' in prompt_lower:
        return "According to recent data, about 87% of Americans have broadband access, but significant gaps remain. Rural areas have lower access rates (78%), and low-income households are less likely to have reliable internet. The platform provides detailed analytics on these trends."
    
    else:
        return f"I understand you're asking about '{prompt}'. The digital divide involves complex factors including infrastructure, affordability, digital literacy, and policy interventions. Can you tell me more specifically what aspect you'd like to explore?"


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
                    # Generate intelligent petition when API is not available
                    st.success("Generated Policy Petition")
                    st.markdown("---")
                    
                    petition_text = _generate_local_petition(country, audience, issue, internet_display)
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
                    
            except Exception as e:
                # Generate intelligent petition when API fails
                st.success("Generated Policy Petition")
                st.markdown("---")
                
                petition_text = _generate_local_petition(country, audience, issue, internet_display)
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


def _generate_local_petition(country: str, audience: str, issue: str, internet_display: str) -> str:
    """Generate an intelligent petition based on the inputs."""
    
    # Analyze the issue to provide specific recommendations
    issue_lower = issue.lower()
    specific_demands = []
    
    if 'rural' in issue_lower or 'remote' in issue_lower:
        specific_demands.extend([
            "Establish rural broadband infrastructure grants with targeted funding for underserved areas",
            "Create satellite internet access programs for remote communities",
            "Implement tax incentives for ISPs to expand rural coverage"
        ])
    
    if 'afford' in issue_lower or 'cost' in issue_lower or 'price' in issue_lower:
        specific_demands.extend([
            "Expand affordable internet subsidy programs for low-income households",
            "Regulate internet pricing to prevent excessive costs",
            "Create community internet access points in public facilities"
        ])
    
    if 'education' in issue_lower or 'school' in issue_lower or 'student' in issue_lower:
        specific_demands.extend([
            "Ensure all schools have high-speed broadband access",
            "Provide devices and internet access for remote learning",
            "Establish digital literacy training programs in educational institutions"
        ])
    
    if 'literacy' in issue_lower or 'skill' in issue_lower:
        specific_demands.extend([
            "Fund comprehensive digital literacy training programs",
            "Create multilingual digital skills resources",
            "Establish community technology centers with training programs"
        ])
    
    # Default demands if no specific category is identified
    if not specific_demands:
        specific_demands = [
            "Invest in comprehensive digital infrastructure development",
            "Implement affordable internet access programs for all citizens",
            "Establish digital inclusion initiatives targeting underserved communities"
        ]
    
    # Add common demands
    specific_demands.extend([
        "Create public-private partnerships to accelerate digital equity",
        "Establish monitoring and evaluation systems to track progress",
        "Ensure equitable access across all demographic groups"
    ])
    
    # Format demands
    demands_text = "\n".join([f"{i+1}. {demand}" for i, demand in enumerate(specific_demands[:6])])
    
    # Generate context-aware impact statement
    if internet_display != "Data not available":
        try:
            access_rate = float(internet_display.replace('%', ''))
            if access_rate < 30:
                urgency = "critical"
                impact_desc = "severely limiting economic opportunities, educational access, and social participation"
            elif access_rate < 60:
                urgency = "significant"
                impact_desc = "creating substantial barriers to full participation in the digital economy and society"
            else:
                urgency = "important"
                impact_desc = "preventing optimal economic growth and leaving some citizens behind"
        except:
            urgency = "important"
            impact_desc = "affecting economic development and social equity"
    else:
        urgency = "critical"
        impact_desc = "hindering national development and citizen welfare"
    
    petition_text = f"""**PETITION FOR DIGITAL EQUITY IN {country.upper()}**

**To: {audience}**

We, the undersigned citizens and stakeholders, respectfully petition for immediate and comprehensive action to address the {urgency} digital divide issue of "{issue}" in {country}.

**Current Digital Landscape:**
Our analysis reveals that internet access in {country} stands at {internet_display}, {impact_desc}. This digital inequality undermines our nation's potential and violates the principle of equal opportunity for all citizens.

**Specific Policy Demands:**

{demands_text}

**Expected Impact and Benefits:**

The implementation of these measures will result in:
- **Economic Growth**: Enhanced GDP through increased digital participation and e-commerce
- **Educational Advancement**: Improved learning outcomes and digital skill development
- **Healthcare Access**: Better telemedicine and health information services
- **Social Inclusion**: Reduced inequality and increased civic participation
- **Innovation Ecosystem**: Stronger foundation for technological advancement and entrepreneurship

**Call for Immediate Action:**

We urge {audience} to treat digital equity as a fundamental infrastructure priority, equivalent to roads, electricity, and water systems. The digital divide is not merely a technological challenge—it is a barrier to human dignity, economic opportunity, and democratic participation.

We respectfully request:
- **Timeline**: Implementation of these measures within the next 18 months
- **Funding**: Adequate budget allocation for sustainable digital infrastructure
- **Accountability**: Regular progress reports and community engagement in the implementation process
- **Collaboration**: Multi-stakeholder approach involving government, private sector, and civil society

The time for action is now. Every day we delay addressing this issue, we widen the gap between the digitally connected and disconnected, perpetuating inequality and limiting our nation's potential.

We stand ready to collaborate and support these essential initiatives for the digital future of {country}.

**Respectfully submitted,**
[Citizens and Organizations of {country}]

---
*This petition is generated based on digital divide data and policy analysis to support evidence-based advocacy for digital equity.*"""

    return petition_text


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
