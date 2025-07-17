"""
Input validation utilities for API endpoints.

Provides common validation functions for request parameters.
"""

import re
from datetime import datetime
from typing import Any, List, Optional


class QueryParamValidators:
    """Collection of query parameter validation methods."""
    
    @staticmethod
    def is_valid_year(year_str: str) -> bool:
        """
        Validate year format (YYYY).
        
        Args:
            year_str: Year string to validate
            
        Returns:
            True if valid year format, False otherwise
        """
        if not year_str:
            return False
        
        try:
            year = int(year_str)
            return 1900 <= year <= datetime.now().year + 10
        except ValueError:
            return False
    
    @staticmethod
    def is_valid_status(status: str, valid_statuses: List[str]) -> bool:
        """
        Validate status value against allowed options.
        
        Args:
            status: Status string to validate
            valid_statuses: List of valid status values
            
        Returns:
            True if status is valid, False otherwise
        """
        return status in valid_statuses if status else True
    
    @staticmethod
    def is_valid_page(page_str: str) -> bool:
        """
        Validate page number parameter.
        
        Args:
            page_str: Page number string to validate
            
        Returns:
            True if valid page number, False otherwise
        """
        if not page_str:
            return True  # Optional parameter
        
        try:
            page = int(page_str)
            return page > 0
        except ValueError:
            return False
    
    @staticmethod
    def is_valid_per_page(per_page_str: str, max_per_page: int = 100) -> bool:
        """
        Validate per_page parameter.
        
        Args:
            per_page_str: Per page string to validate
            max_per_page: Maximum allowed items per page
            
        Returns:
            True if valid per_page value, False otherwise
        """
        if not per_page_str:
            return True  # Optional parameter
        
        try:
            per_page = int(per_page_str)
            return 1 <= per_page <= max_per_page
        except ValueError:
            return False
    
    @staticmethod
    def is_valid_date_format(date_str: str, date_format: str = '%Y-%m-%d') -> bool:
        """
        Validate date string format.
        
        Args:
            date_str: Date string to validate
            date_format: Expected date format
            
        Returns:
            True if valid date format, False otherwise
        """
        if not date_str:
            return True  # Optional parameter
        
        try:
            datetime.strptime(date_str, date_format)
            return True
        except ValueError:
            return False


class DataValidators:
    """Collection of data validation methods for request bodies."""
    
    @staticmethod
    def validate_policy_data(policy_data: dict) -> tuple[bool, Optional[str]]:
        """
        Validate policy data structure.
        
        Args:
            policy_data: Dictionary containing policy data
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        required_fields = ['name', 'description', 'implementation_date', 'status']
        
        for field in required_fields:
            if field not in policy_data:
                return False, f"Missing required field: {field}"
        
        # Validate date format
        if not QueryParamValidators.is_valid_date_format(
            policy_data['implementation_date']
        ):
            return False, "Invalid implementation_date format. Use YYYY-MM-DD"
        
        # Validate status
        valid_statuses = ['active', 'inactive', 'in_progress', 'planned']
        if policy_data['status'] not in valid_statuses:
            return False, f"Invalid status. Must be one of: {valid_statuses}"
        
        return True, None
    
    @staticmethod
    def sanitize_search_query(query: str) -> str:
        """
        Sanitize search query string.
        
        Args:
            query: Raw search query
            
        Returns:
            Sanitized query string
        """
        if not query:
            return ""
        
        # Remove excessive whitespace and special characters
        sanitized = re.sub(r'[^\w\s-]', '', query.strip())
        return re.sub(r'\s+', ' ', sanitized)


# Create instances for easy importing
validate_query_params = QueryParamValidators()
validate_data = DataValidators()
