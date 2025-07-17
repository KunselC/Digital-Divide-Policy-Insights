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
            st.error(f"API Error: {str(e)}")
            return None
    
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
            st.error(f"API Error: {str(e)}")
            return None


# Global API client instance
api_client = APIClient()
