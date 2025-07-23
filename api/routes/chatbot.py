from flask import Blueprint, jsonify, request
import os

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/', methods=['GET'])
def chatbot_home():
    return jsonify({
        'message': 'Chatbot API is running. Use POST /api/chatbot/chat to send messages.'
    })

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages from the frontend."""
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400
        
        user_message = data['message']
        message_type = data.get('type', 'chat')
        
        # For now, return a basic response
        # In a full implementation, this would connect to OpenAI or another AI service
        if message_type == 'petition_generation':
            bot_response = generate_petition_response(user_message)
        else:
            bot_response = generate_chat_response(user_message)
        
        return jsonify({
            'bot_response': bot_response,
            'suggestions': get_suggestions_for_message(user_message)
        })
        
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

def generate_chat_response(message: str) -> str:
    """Generate a response for regular chat messages."""
    message_lower = message.lower()
    
    if 'digital divide' in message_lower:
        return "The digital divide refers to the gap between those who have access to modern information and communications technology and those who don't. This includes disparities in internet access, digital literacy, and technology availability across different demographics and regions."
    
    elif 'broadband' in message_lower or 'internet access' in message_lower:
        return "Broadband internet access is crucial for digital equity. Key policies include the Broadband Equity Access and Deployment (BEAD) program, which allocates $42.5 billion to expand broadband infrastructure, and the Affordable Connectivity Program, which provides internet subsidies to low-income households."
    
    elif 'policy' in message_lower or 'policies' in message_lower:
        return "Digital divide policies focus on expanding internet infrastructure, improving affordability, and increasing digital literacy. Major initiatives include federal broadband programs, state-level digital equity plans, and local community technology centers."
    
    elif 'rural' in message_lower:
        return "Rural areas face unique digital divide challenges including limited infrastructure, higher costs, and lower population density. Solutions include targeted funding for rural broadband expansion, satellite internet initiatives, and public-private partnerships."
    
    elif 'education' in message_lower or 'school' in message_lower:
        return "Education is significantly impacted by the digital divide. Students without reliable internet access face challenges with online learning, homework completion, and digital skill development. Programs like E-rate help schools get affordable internet access."
    
    else:
        return f"I understand you're asking about '{message}'. The digital divide involves complex factors including infrastructure, affordability, digital literacy, and policy interventions. Can you tell me more specifically what aspect you'd like to explore?"

def generate_petition_response(prompt: str) -> str:
    """Generate a petition based on the prompt."""
    # Extract key information from prompt
    if 'rural' in prompt.lower():
        focus_area = "rural broadband infrastructure"
        specific_issues = "lack of reliable internet connectivity in rural communities"
    elif 'affordable' in prompt.lower() or 'cost' in prompt.lower():
        focus_area = "internet affordability"
        specific_issues = "high costs of internet service that prevent access"
    elif 'education' in prompt.lower() or 'school' in prompt.lower():
        focus_area = "educational digital equity"
        specific_issues = "digital learning gaps affecting students"
    else:
        focus_area = "digital access and equity"
        specific_issues = "barriers to digital participation"
    
    petition = f"""
PETITION FOR IMPROVED DIGITAL EQUITY

To Whom It May Concern:

We, the undersigned, call for immediate action to address {specific_issues} in our community.

WHEREAS, reliable internet access has become essential for education, healthcare, economic opportunity, and civic participation; and

WHEREAS, significant disparities in {focus_area} create barriers that prevent full participation in the digital economy; and

WHEREAS, these disparities disproportionately affect low-income families, rural communities, and other underserved populations;

WE THEREFORE PETITION for the following actions:

1. Increased investment in broadband infrastructure to ensure universal access
2. Affordable internet service options for low-income households
3. Digital literacy programs to help community members develop necessary skills
4. Support for community technology centers and public internet access points
5. Transparent reporting on progress toward digital equity goals

The digital divide is not just a technology issue—it's an equity issue that affects education, economic opportunity, and quality of life. We urge immediate action to ensure that all community members have the digital access they need to thrive in the 21st century.

Time is of the essence. Every day that passes without action widens the gap and deepens inequality.

We respectfully request your prompt attention to this critical matter.

Sincerely,
[Petition Signers]
"""
    return petition.strip()

def get_suggestions_for_message(message: str) -> list:
    """Get follow-up suggestions based on the message."""
    suggestions = []
    message_lower = message.lower()
    
    if 'digital divide' in message_lower:
        suggestions = [
            "What policies address the digital divide?",
            "How does the digital divide affect education?",
            "What are the main barriers to internet access?"
        ]
    elif 'broadband' in message_lower:
        suggestions = [
            "Tell me about rural broadband programs",
            "How much does broadband expansion cost?",
            "What is the Affordable Connectivity Program?"
        ]
    elif 'policy' in message_lower:
        suggestions = [
            "Compare federal and state digital policies",
            "How effective are current policies?",
            "What new policies are being proposed?"
        ]
    else:
        suggestions = [
            "What is the digital divide?",
            "Tell me about broadband policies",
            "How can communities improve digital access?"
        ]
    
    return suggestions[:3]  # Return max 3 suggestions
