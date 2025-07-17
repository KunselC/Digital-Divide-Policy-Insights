"""
Policy API routes.

Provides RESTful endpoints for policy data management and analysis.
"""

from flask import Blueprint, jsonify, request
from services.policy_service import policy_service
from utils.validators import validate_query_params
from utils.response_helpers import success_response, error_response

policies_bp = Blueprint('policies', __name__)


@policies_bp.route('/', methods=['GET'])
def get_all_policies():
    """
    Retrieve all policies with optional filtering.
    
    Query Parameters:
        status: Filter by policy status (active, inactive, in_progress)
        year: Filter by implementation year (YYYY format)
    
    Returns:
        JSON response containing policies list and metadata
    """
    try:
        status = request.args.get('status')
        year = request.args.get('year')
        
        # Validate query parameters
        if year and not validate_query_params.is_valid_year(year):
            return error_response('Invalid year format. Use YYYY format.', 400)
        
        policies = policy_service.get_all_policies(status=status, year=year)
        
        return success_response({
            'policies': policies,
            'total': len(policies),
            'filters_applied': {
                'status': status,
                'year': year
            }
        })
        
    except Exception as e:
        return error_response(f'Error retrieving policies: {str(e)}', 500)


@policies_bp.route('/<int:policy_id>', methods=['GET'])
def get_policy(policy_id):
    """
    Retrieve a specific policy by ID.
    
    Args:
        policy_id: Integer ID of the policy
        
    Returns:
        JSON response containing policy data or error message
    """
    try:
        policy = policy_service.get_policy_by_id(policy_id)
        
        if not policy:
            return error_response('Policy not found', 404)
        
        return success_response(policy)
        
    except Exception as e:
        return error_response(f'Error retrieving policy: {str(e)}', 500)


@policies_bp.route('/effectiveness', methods=['GET'])
def get_effectiveness_data():
    """
    Retrieve effectiveness metrics for all policies.
    
    Returns:
        JSON response containing effectiveness data and statistics
    """
    try:
        effectiveness_data = policy_service.get_effectiveness_data()
        return success_response(effectiveness_data)
        
    except Exception as e:
        return error_response(f'Error retrieving effectiveness data: {str(e)}', 500)


@policies_bp.route('/timeline', methods=['GET'])
def get_policy_timeline():
    """
    Retrieve policy timeline data sorted by implementation date.
    
    Returns:
        JSON response containing chronological policy data
    """
    try:
        timeline_data = policy_service.get_timeline_data()
        return success_response(timeline_data)
        
    except Exception as e:
        return error_response(f'Error retrieving timeline data: {str(e)}', 500)


@policies_bp.route('/search', methods=['GET'])
def search_policies():
    """
    Search policies by name or description.
    
    Query Parameters:
        q: Search query string (required)
        
    Returns:
        JSON response containing search results
    """
    try:
        query = request.args.get('q', '').strip()
        
        if not query:
            return error_response('Search query parameter "q" is required', 400)
        
        if len(query) < 2:
            return error_response('Search query must be at least 2 characters', 400)
        
        results = policy_service.search_policies(query)
        
        return success_response({
            'results': results,
            'query': query,
            'total': len(results)
        })
        
    except Exception as e:
        return error_response(f'Error searching policies: {str(e)}', 500)
