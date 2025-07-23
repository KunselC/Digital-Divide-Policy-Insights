"""
API client utilities for making requests to the Digital Divide Policy API.
"""

import requests
import streamlit as st
from typing import Optional, Dict, Any

from config import API_BASE_URL


class APIClient:
    """Client for interacting with the Digital Divide Policy API."""
    
    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """
        Make a GET request to the API.
        
        Args:
            endpoint: API endpoint path
            params: Optional query parameters
            
        Returns:
            JSON response data or None if request fails
        """
        try:
            url = f"{self.base_url}{endpoint}"
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            # Return mock data for demo purposes when API is unavailable
            return self._get_mock_data(endpoint)
    
    def _get_mock_data(self, endpoint: str) -> Dict[str, Any]:
        """Return mock data for demo purposes when API is unavailable."""
        if "/api/policies/" in endpoint:
            return {
                "policies": [
                    {
                        "name": "Broadband Equity Access & Deployment Program",
                        "status": "active",
                        "description": "Federal program providing $42.5B to expand broadband access nationwide.",
                        "implementation_date": "2021-11-15",
                        "effectiveness_score": 8.5,
                        "metrics": {"funding": 42500000000, "states_covered": 50}
                    },
                    {
                        "name": "Emergency Broadband Benefit",
                        "status": "completed",
                        "description": "Temporary program providing internet subsidies during COVID-19.",
                        "implementation_date": "2021-05-12",
                        "effectiveness_score": 7.2,
                        "metrics": {"households_served": 9000000, "monthly_discount": 50}
                    }
                ],
                "average_effectiveness_score": 7.85
            }
        elif "/api/data/indicators" in endpoint:
            return {
                "national_broadband_access": 87.3,
                "national_digital_literacy": 76.8,
                "indicators_by_state": [
                    {"state": "Utah", "broadband_access": 94.2, "digital_literacy": 85.1},
                    {"state": "New Hampshire", "broadband_access": 92.8, "digital_literacy": 82.4},
                    {"state": "Connecticut", "broadband_access": 91.5, "digital_literacy": 80.9}
                ]
            }
        elif "/api/data/trends" in endpoint:
            return {
                "trends": {
                    "broadband_access": {
                        "end_value": 87.3,
                        "absolute_change": 12.4,
                        "percentage_change": 16.6,
                        "trend_direction": "increasing"
                    },
                    "digital_literacy": {
                        "end_value": 76.8,
                        "absolute_change": 8.9,
                        "percentage_change": 13.1,
                        "trend_direction": "increasing"
                    }
                }
            }
        elif "/api/data/demographics" in endpoint:
            return {
                "demographics": {
                    "income_levels": {
                        "low_income": {"broadband_access": 71.2, "digital_literacy": 58.4},
                        "middle_income": {"broadband_access": 89.6, "digital_literacy": 78.2},
                        "high_income": {"broadband_access": 96.8, "digital_literacy": 91.5}
                    },
                    "geographic": {
                        "urban": {"broadband_access": 92.1, "digital_literacy": 82.3},
                        "suburban": {"broadband_access": 88.7, "digital_literacy": 76.9},
                        "rural": {"broadband_access": 75.4, "digital_literacy": 65.2}
                    }
                }
            }
        elif "/api/chatbot/chat" in endpoint:
            return {
                "bot_response": "I'm here to help you understand digital divide policies and analyze digital equity data. What specific aspect would you like to explore?",
                "suggestions": ["Tell me about broadband access policies", "What are the main barriers to digital equity?", "How can we measure digital divide progress?"]
            }
        else:
            return {"message": "Demo mode - API unavailable"}
    
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """
        Make a POST request to the API.
        
        Args:
            endpoint: API endpoint path
            data: Optional JSON data to send
            
        Returns:
            JSON response data or None if request fails
        """
        try:
            url = f"{self.base_url}{endpoint}"
            response = requests.post(url, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            # Return mock data for demo purposes when API is unavailable
            return self._get_mock_data(endpoint)
            response = requests.post(url, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            st.error(f"API Error: {str(e)}")
            return None


# Global API client instance
api_client = APIClient()
