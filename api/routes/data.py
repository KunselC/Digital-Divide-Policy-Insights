"""
Data API routes.

Provides RESTful endpoints for data analytics, trends, and digital divide indicators.
"""

from flask import Blueprint, jsonify, request
from services.data_service import data_service
from utils.response_helpers import success_response, error_response

data_bp = Blueprint('data', __name__)


@data_bp.route('/indicators', methods=['GET'])
def get_indicators():
    """
    Retrieve digital divide indicators and timeline data.
    
    Returns:
        JSON response containing indicator timeline data
    """
    try:
        indicators = data_service.get_indicators_data()
        return success_response({'indicators': indicators})
    except Exception as e:
        return error_response(f'Error retrieving indicators: {str(e)}', 500)


@data_bp.route('/trends', methods=['GET'])
def get_trends():
    """
    Retrieve trend analysis for digital divide metrics.
    
    Query Parameters:
        start_year: Starting year for trend analysis (YYYY)
        end_year: Ending year for trend analysis (YYYY)
    
    Returns:
        JSON response containing trend analysis data
    """
    try:
        start_year = request.args.get('start_year')
        end_year = request.args.get('end_year')
        
        trends = data_service.calculate_trends(start_year=start_year, end_year=end_year)
        return success_response({'trends': trends})
    except Exception as e:
        return error_response(f'Error calculating trends: {str(e)}', 500)


@data_bp.route('/demographics', methods=['GET'])
def get_demographics():
    """
    Retrieve demographic breakdown data for digital divide metrics.
    
    Returns:
        JSON response containing demographic analysis
    """
    try:
        demographics = data_service.get_demographics_data()
        return success_response({'demographics': demographics})
    except Exception as e:
        return error_response(f'Error retrieving demographics: {str(e)}', 500)


@data_bp.route('/correlation', methods=['GET'])
def get_correlation():
    """
    Retrieve correlation analysis between policies and digital divide metrics.
    
    Returns:
        JSON response containing correlation data
    """
    try:
        correlations = data_service.calculate_policy_correlations()
        return success_response({'correlations': correlations})
    except Exception as e:
        return error_response(f'Error calculating correlations: {str(e)}', 500)


@data_bp.route('/export/<format>', methods=['GET'])
def export_data(format):
    """
    Export data in various formats.
    
    Args:
        format: Export format ('csv', 'json', 'xlsx')
    
    Returns:
        Exported data file or error response
    """
    try:
        if format not in ['csv', 'json', 'xlsx']:
            return error_response('Invalid export format. Use csv, json, or xlsx.', 400)
        
        export_data = data_service.export_data(format)
        return success_response({
            'format': format,
            'data': export_data,
            'message': f'Data exported successfully in {format} format'
        })
    except Exception as e:
        return error_response(f'Error exporting data: {str(e)}', 500)
