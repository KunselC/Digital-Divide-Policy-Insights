"""
Chatbot service module.

Handles natural language processing, intent detection, and response generation
for policy-related queries.
"""

import re
from typing import Dict, List, Optional, Tuple
from datetime import datetime


class ChatbotService:
    """Service class for chatbot functionality and natural language processing."""
    
    def __init__(self):
        """Initialize chatbot with knowledge base and intent patterns."""
        self._policy_knowledge = {
            "digital equity act": {
                "description": "The Digital Equity Act is federal legislation aimed at ensuring equitable access to digital technologies and bridging the digital divide.",
                "effectiveness": "The act has shown strong effectiveness with a 7.5/10 rating, leading to 15.2% increase in broadband access and 12.8% improvement in digital literacy.",
                "implementation": "Implemented on November 15, 2021, and currently active.",
                "impact": "Particularly effective in rural areas with 22.1% boost in connectivity."
            },
            "affordable connectivity program": {
                "description": "A program providing discounted internet service to eligible households to make broadband more accessible.",
                "effectiveness": "Highly effective with 8.2/10 rating, serving 14.5 million households with 45% cost reduction.",
                "implementation": "Launched on December 31, 2021, and currently active.",
                "impact": "Strong rural participation at 68.3% rate, making internet affordable for low-income families."
            },
            "rural digital opportunity fund": {
                "description": "An FCC program designed to bring broadband infrastructure to underserved rural areas.",
                "effectiveness": "Moderately effective with 6.8/10 rating, covering 5.2 million areas with 85.7% speed improvement.",
                "implementation": "Started October 29, 2020, currently in progress with 42.1% completion rate.",
                "impact": "Focuses specifically on rural broadband infrastructure development."
            }
        }
        
        self._intent_keywords = {
            "effectiveness": ["effective", "effectiveness", "impact", "success", "results", "outcome"],
            "implementation": ["when", "implemented", "started", "launched", "timeline", "date"],
            "description": ["what", "describe", "about", "explain", "overview"],
            "comparison": ["compare", "versus", "vs", "difference", "better", "best"],
            "statistics": ["stats", "numbers", "data", "metrics", "percentage"]
        }
    
    def process_message(self, message: str) -> Dict:
        """
        Process user message and generate appropriate response.
        
        Args:
            message: User's input message
            
        Returns:
            Dictionary containing response data
        """
        message = self._sanitize_message(message)
        
        if not message:
            return self._get_empty_message_response()
        
        policy_name = self._extract_policy_name(message)
        intent = self._detect_intent(message)
        
        response_data = self._generate_response(policy_name, intent, message)
        
        return {
            'user_message': message,
            'bot_response': response_data['response'],
            'detected_policy': policy_name,
            'detected_intent': intent,
            'suggestions': response_data.get('suggestions', []),
            'timestamp': datetime.now().isoformat(),
            'confidence': response_data.get('confidence', 0.8)
        }
    
    def get_available_policies(self) -> List[Dict]:
        """
        Get list of available policies for chatbot queries.
        
        Returns:
            List of policy information dictionaries
        """
        policies = []
        for policy_key, policy_info in self._policy_knowledge.items():
            policies.append({
                'name': policy_key.title(),
                'key': policy_key,
                'description': policy_info.get('description', ''),
                'available_intents': list(self._intent_keywords.keys())
            })
        
        return policies
    
    def get_conversation_starters(self) -> List[str]:
        """
        Get list of suggested conversation starters.
        
        Returns:
            List of suggested questions
        """
        return [
            "What is the Digital Equity Act?",
            "How effective is the Affordable Connectivity Program?",
            "Compare all digital divide policies",
            "When was the Rural Digital Opportunity Fund implemented?",
            "Show me statistics on broadband access improvements",
            "Which policy has been most successful?"
        ]
    
    def _sanitize_message(self, message: str) -> str:
        """
        Clean and sanitize user message.
        
        Args:
            message: Raw user message
            
        Returns:
            Sanitized message string
        """
        if not message:
            return ""
        
        # Remove excessive whitespace and normalize
        sanitized = re.sub(r'\s+', ' ', message.strip())
        
        # Remove potentially harmful characters while preserving meaning
        sanitized = re.sub(r'[<>\"\'`]', '', sanitized)
        
        return sanitized
    
    def _extract_policy_name(self, query: str) -> Optional[str]:
        """
        Extract policy name from user query using pattern matching.
        
        Args:
            query: User query string
            
        Returns:
            Policy key or None if not found
        """
        query_lower = query.lower()
        
        # Direct matches first
        for policy_key in self._policy_knowledge.keys():
            if policy_key in query_lower:
                return policy_key
        
        # Partial matches with specific patterns
        if "digital equity" in query_lower or "equity act" in query_lower:
            return "digital equity act"
        elif "affordable" in query_lower and "connectivity" in query_lower:
            return "affordable connectivity program"
        elif "rural" in query_lower and ("opportunity" in query_lower or "fund" in query_lower):
            return "rural digital opportunity fund"
        
        return None
    
    def _detect_intent(self, query: str) -> str:
        """
        Detect user intent from query using keyword matching.
        
        Args:
            query: User query string
            
        Returns:
            Detected intent string
        """
        query_lower = query.lower()
        intent_scores = {}
        
        for intent, keywords in self._intent_keywords.items():
            score = sum(1 for keyword in keywords if keyword in query_lower)
            if score > 0:
                intent_scores[intent] = score
        
        if intent_scores:
            return max(intent_scores, key=intent_scores.get)
        
        return "description"  # Default intent
    
    def _generate_response(self, policy_name: Optional[str], intent: str, query: str) -> Dict:
        """
        Generate chatbot response based on policy and intent.
        
        Args:
            policy_name: Detected policy name
            intent: Detected intent
            query: Original user query
            
        Returns:
            Dictionary containing response and metadata
        """
        if not policy_name:
            return self._get_no_policy_response()
        
        policy_info = self._policy_knowledge.get(policy_name, {})
        
        if intent == "effectiveness":
            response = f"Regarding the effectiveness of the {policy_name.title()}: {policy_info.get('effectiveness', 'No effectiveness data available.')}"
        elif intent == "implementation":
            response = f"Implementation details for the {policy_name.title()}: {policy_info.get('implementation', 'No implementation data available.')}"
        elif intent == "comparison":
            response = self._generate_comparison_response()
        elif intent == "statistics":
            response = f"Key statistics for the {policy_name.title()}: {policy_info.get('impact', 'No statistical data available.')}"
        else:  # description
            response = f"About the {policy_name.title()}: {policy_info.get('description', 'No description available.')}"
        
        return {
            'response': response,
            'policy': policy_name.title(),
            'intent': intent,
            'suggestions': self._get_follow_up_suggestions(policy_name, intent),
            'confidence': 0.9 if policy_name else 0.6
        }
    
    def _get_no_policy_response(self) -> Dict:
        """Generate response when no policy is detected."""
        return {
            'response': "I can help you learn about these digital divide policies: Digital Equity Act, Affordable Connectivity Program, and Rural Digital Opportunity Fund. What would you like to know?",
            'suggestions': [
                "Tell me about the Digital Equity Act",
                "How effective is the Affordable Connectivity Program?",
                "When was the Rural Digital Opportunity Fund implemented?"
            ],
            'confidence': 0.7
        }
    
    def _get_empty_message_response(self) -> Dict:
        """Generate response for empty or invalid messages."""
        return {
            'user_message': '',
            'bot_response': "I'm here to help you learn about digital divide policies. Please ask me a question!",
            'detected_policy': None,
            'detected_intent': None,
            'suggestions': self.get_conversation_starters()[:3],
            'timestamp': datetime.now().isoformat(),
            'confidence': 0.5
        }
    
    def _generate_comparison_response(self) -> str:
        """Generate comparison response for all policies."""
        return """Here's a comparison of the three main digital divide policies:

1. **Affordable Connectivity Program** (8.2/10 effectiveness) - Most effective overall, serving 14.5M households
2. **Digital Equity Act** (7.5/10 effectiveness) - Strong rural impact with 22.1% connectivity boost  
3. **Rural Digital Opportunity Fund** (6.8/10 effectiveness) - Infrastructure-focused, 42.1% completion rate

The Affordable Connectivity Program has the highest effectiveness score, while the Rural Digital Opportunity Fund focuses specifically on infrastructure development."""
    
    def _get_follow_up_suggestions(self, policy_name: str, current_intent: str) -> List[str]:
        """
        Generate relevant follow-up question suggestions.
        
        Args:
            policy_name: Current policy being discussed
            current_intent: Current conversation intent
            
        Returns:
            List of follow-up suggestions
        """
        suggestions = []
        policy_title = policy_name.title()
        
        if current_intent != "effectiveness":
            suggestions.append(f"How effective is the {policy_title}?")
        if current_intent != "implementation":
            suggestions.append(f"When was the {policy_title} implemented?")
        if current_intent != "statistics":
            suggestions.append(f"Show me statistics for the {policy_title}")
        
        suggestions.append("Compare all policies")
        return suggestions[:3]


# Global service instance
chatbot_service = ChatbotService()
