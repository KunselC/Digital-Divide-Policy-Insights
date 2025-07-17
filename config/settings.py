"""
Configuration settings for Digital Divide Policy Insights.

This module manages all application configuration including environment variables,
database settings, API keys, and validation logic.
"""

import os
from typing import List
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration manager."""
    
    # Flask Configuration
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    API_PORT = int(os.getenv('API_PORT', 5001))
    
    # Database Configuration
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///policy_data.db')
    
    # External API Keys
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '')
    
    # Frontend Configuration
    STREAMLIT_PORT = int(os.getenv('STREAMLIT_PORT', 8501))
    API_BASE_URL = os.getenv('API_BASE_URL', f'http://localhost:{API_PORT}')
    
    # Data Management
    DATA_UPDATE_INTERVAL = int(os.getenv('DATA_UPDATE_INTERVAL', 3600))
    
    # Security and CORS
    CORS_ORIGINS = [
        f'http://localhost:{STREAMLIT_PORT}',
        f'http://127.0.0.1:{STREAMLIT_PORT}'
    ]
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Feature Flags
    ENABLE_CHATBOT = os.getenv('ENABLE_CHATBOT', 'True').lower() == 'true'
    ENABLE_DATA_CACHING = os.getenv('ENABLE_DATA_CACHING', 'True').lower() == 'true'
    
    @classmethod
    def validate_config(cls) -> List[str]:
        """
        Validate configuration settings and return list of issues.
        
        Returns:
            List of configuration issues or empty list if valid
        """
        issues = []
        
        # Validate API keys
        if cls.ENABLE_CHATBOT and not cls.OPENAI_API_KEY:
            issues.append("OPENAI_API_KEY is required when chatbot is enabled")
        
        # Validate port ranges
        if not cls._is_valid_port(cls.API_PORT):
            issues.append(f"API_PORT {cls.API_PORT} is not in valid range (1024-65535)")
        
        if not cls._is_valid_port(cls.STREAMLIT_PORT):
            issues.append(f"STREAMLIT_PORT {cls.STREAMLIT_PORT} is not in valid range (1024-65535)")
        
        # Validate URLs
        if not cls.API_BASE_URL.startswith(('http://', 'https://')):
            issues.append("API_BASE_URL must start with http:// or https://")
        
        # Check for production security
        if cls.FLASK_ENV == 'production':
            if cls.SECRET_KEY == 'dev-secret-key-change-in-production':
                issues.append("SECRET_KEY must be changed for production use")
            
            if cls.FLASK_DEBUG:
                issues.append("FLASK_DEBUG should be False in production")
        
        return issues
    
    @staticmethod
    def _is_valid_port(port: int) -> bool:
        """Check if port number is in valid range."""
        return 1024 <= port <= 65535
    
    @classmethod
    def get_config_summary(cls) -> dict:
        """
        Get a summary of current configuration (safe for logging).
        
        Returns:
            Dictionary with non-sensitive configuration values
        """
        return {
            'environment': cls.FLASK_ENV,
            'debug_mode': cls.FLASK_DEBUG,
            'api_port': cls.API_PORT,
            'streamlit_port': cls.STREAMLIT_PORT,
            'chatbot_enabled': cls.ENABLE_CHATBOT,
            'caching_enabled': cls.ENABLE_DATA_CACHING,
            'has_openai_key': bool(cls.OPENAI_API_KEY),
            'has_google_key': bool(cls.GOOGLE_API_KEY)
        }
