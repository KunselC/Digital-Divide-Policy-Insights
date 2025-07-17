"""
Data processing utilities for Digital Divide Policy Insights.

This module provides functions for data validation, transformation,
and formatting specific to policy and indicator data.
"""

from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import re


class DataValidator:
    """Utility class for data validation operations."""
    
    @staticmethod
    def is_valid_year(year_str: str) -> bool:
        """
        Validate if a string represents a valid year (YYYY format).
        
        Args:
            year_str: String to validate as year
            
        Returns:
            True if valid year format, False otherwise
        """
        if not year_str or not isinstance(year_str, str):
            return False
        
        try:
            year = int(year_str)
            return 1900 <= year <= 2100
        except ValueError:
            return False
    
    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Validate email address format.
        
        Args:
            email: Email address to validate
            
        Returns:
            True if valid email format, False otherwise
        """
        if not email or not isinstance(email, str):
            return False
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def is_valid_percentage(value: Any) -> bool:
        """
        Validate if a value represents a valid percentage (0-100).
        
        Args:
            value: Value to validate
            
        Returns:
            True if valid percentage, False otherwise
        """
        try:
            num_value = float(value)
            return 0 <= num_value <= 100
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def is_valid_effectiveness_score(score: Any) -> bool:
        """
        Validate effectiveness score (0-10 range).
        
        Args:
            score: Score value to validate
            
        Returns:
            True if valid score, False otherwise
        """
        try:
            num_score = float(score)
            return 0 <= num_score <= 10
        except (ValueError, TypeError):
            return False


class DataFormatter:
    """Utility class for data formatting operations."""
    
    @staticmethod
    def format_currency(amount: Union[int, float], decimals: int = 0) -> str:
        """
        Format a number as currency.
        
        Args:
            amount: Numeric amount to format
            decimals: Number of decimal places
            
        Returns:
            Formatted currency string
        """
        try:
            if decimals == 0:
                return f"${amount:,.0f}"
            else:
                return f"${amount:,.{decimals}f}"
        except (ValueError, TypeError):
            return str(amount)
    
    @staticmethod
    def format_percentage(value: Union[int, float], decimals: int = 1) -> str:
        """
        Format a number as percentage.
        
        Args:
            value: Numeric value to format
            decimals: Number of decimal places
            
        Returns:
            Formatted percentage string
        """
        try:
            return f"{value:.{decimals}f}%"
        except (ValueError, TypeError):
            return str(value)
    
    @staticmethod
    def format_large_number(number: Union[int, float]) -> str:
        """
        Format large numbers with appropriate suffixes (K, M, B).
        
        Args:
            number: Number to format
            
        Returns:
            Formatted number string with suffix
        """
        try:
            num = float(number)
            
            if abs(num) >= 1_000_000_000:
                return f"{num / 1_000_000_000:.1f}B"
            elif abs(num) >= 1_000_000:
                return f"{num / 1_000_000:.1f}M"
            elif abs(num) >= 1_000:
                return f"{num / 1_000:.1f}K"
            else:
                return f"{num:.0f}"
        except (ValueError, TypeError):
            return str(number)
    
    @staticmethod
    def format_date(date_str: str, output_format: str = "%B %d, %Y") -> str:
        """
        Format date string to a more readable format.
        
        Args:
            date_str: Date string in ISO format (YYYY-MM-DD)
            output_format: Desired output format
            
        Returns:
            Formatted date string
        """
        try:
            date_obj = datetime.fromisoformat(date_str)
            return date_obj.strftime(output_format)
        except (ValueError, TypeError):
            return date_str


class DataTransformer:
    """Utility class for data transformation operations."""
    
    @staticmethod
    def calculate_trend_direction(values: List[Union[int, float]]) -> str:
        """
        Calculate overall trend direction from a list of values.
        
        Args:
            values: List of numeric values in chronological order
            
        Returns:
            Trend direction: 'increasing', 'decreasing', or 'stable'
        """
        if len(values) < 2:
            return 'stable'
        
        try:
            start_value = float(values[0])
            end_value = float(values[-1])
            difference = end_value - start_value
            
            # Consider changes less than 1% as stable
            threshold = abs(start_value) * 0.01
            
            if difference > threshold:
                return 'increasing'
            elif difference < -threshold:
                return 'decreasing'
            else:
                return 'stable'
        except (ValueError, TypeError):
            return 'stable'
    
    @staticmethod
    def calculate_percentage_change(start: Union[int, float], 
                                  end: Union[int, float]) -> float:
        """
        Calculate percentage change between two values.
        
        Args:
            start: Starting value
            end: Ending value
            
        Returns:
            Percentage change
        """
        try:
            start_val = float(start)
            end_val = float(end)
            
            if start_val == 0:
                return 0.0 if end_val == 0 else float('inf')
            
            return ((end_val - start_val) / start_val) * 100
        except (ValueError, TypeError):
            return 0.0
    
    @staticmethod
    def sanitize_text(text: str, max_length: Optional[int] = None) -> str:
        """
        Sanitize text input by removing unwanted characters.
        
        Args:
            text: Text to sanitize
            max_length: Maximum allowed length
            
        Returns:
            Sanitized text
        """
        if not isinstance(text, str):
            return str(text)
        
        # Remove potentially harmful characters
        sanitized = re.sub(r'[<>"\']', '', text)
        sanitized = sanitized.strip()
        
        if max_length and len(sanitized) > max_length:
            sanitized = sanitized[:max_length].strip()
        
        return sanitized


# Convenience function exports
def validate_year(year_str: str) -> bool:
    """Validate year string format."""
    return DataValidator.is_valid_year(year_str)

def format_metric_value(value: Any, metric_type: str = "auto") -> str:
    """
    Format metric values based on their type.
    
    Args:
        value: Value to format
        metric_type: Type of metric ('currency', 'percentage', 'number', 'auto')
        
    Returns:
        Formatted value string
    """
    if metric_type == "currency":
        return DataFormatter.format_currency(value)
    elif metric_type == "percentage":
        return DataFormatter.format_percentage(value)
    elif metric_type == "large_number":
        return DataFormatter.format_large_number(value)
    else:
        # Auto-detect based on value characteristics
        try:
            num_val = float(value)
            if 0 <= num_val <= 100 and isinstance(value, float):
                return DataFormatter.format_percentage(num_val)
            elif num_val >= 1000:
                return DataFormatter.format_large_number(num_val)
            else:
                return f"{num_val:,.1f}"
        except (ValueError, TypeError):
            return str(value)
