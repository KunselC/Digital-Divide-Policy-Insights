"""
Response helper utilities for API endpoints.

Provides standardized response formatting for success and error cases.
"""

from flask import jsonify
from typing import Any, Dict


def success_response(data: Any, message: str = None, status_code: int = 200) -> tuple:
    """
    Create a standardized success response.
    
    Args:
        data: The response data
        message: Optional success message
        status_code: HTTP status code (default: 200)
        
    Returns:
        Tuple of (JSON response, status code)
    """
    response = {
        'success': True,
        'data': data
    }
    
    if message:
        response['message'] = message
    
    return jsonify(response), status_code


def error_response(message: str, status_code: int = 400, 
                  error_code: str = None) -> tuple:
    """
    Create a standardized error response.
    
    Args:
        message: Error message
        status_code: HTTP status code
        error_code: Optional error code for client handling
        
    Returns:
        Tuple of (JSON response, status code)
    """
    response = {
        'success': False,
        'error': {
            'message': message,
            'status_code': status_code
        }
    }
    
    if error_code:
        response['error']['code'] = error_code
    
    return jsonify(response), status_code


def paginated_response(data: list, page: int, per_page: int, 
                      total: int, **kwargs) -> Dict:
    """
    Create a paginated response structure.
    
    Args:
        data: List of items for current page
        page: Current page number
        per_page: Items per page
        total: Total number of items
        **kwargs: Additional metadata
        
    Returns:
        Dictionary with paginated data structure
    """
    return {
        'data': data,
        'pagination': {
            'page': page,
            'per_page': per_page,
            'total': total,
            'pages': (total + per_page - 1) // per_page,
            'has_next': page * per_page < total,
            'has_prev': page > 1
        },
        **kwargs
    }
