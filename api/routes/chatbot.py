"""
Chatbot API routes.

Provides endpoints for AI-powered policy questions and interactive conversations.
"""

from flask import Blueprint, jsonify, request
from services.chatbot_service import chatbot_service
from utils.response_helpers import success_response, error_response
from utils.validators import validate_query_params

chatbot_bp = Blueprint('chatbot', __name__)


@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    """
    Process a chat message and return AI response.
    
    Request Body:
        message (str): User's chat message
        conversation_id (str, optional): Conversation identifier for context
    
    Returns:
        JSON response containing bot response and suggestions
    """
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return error_response('Message is required in request body', 400)
        
        message = data.get('message', '').strip()
        if not message:
            return error_response('Message cannot be empty', 400)
        
        conversation_id = data.get('conversation_id')
        
        # Get bot response
        response = chatbot_service.process_message(message, conversation_id)
        
        return success_response({
            'bot_response': response['response'],
            'suggestions': response.get('suggestions', []),
            'conversation_id': response.get('conversation_id'),
            'confidence': response.get('confidence', 0.0)
        })
        
    except Exception as e:
        return error_response(f'Error processing chat message: {str(e)}', 500)


@chatbot_bp.route('/suggestions', methods=['GET'])
def get_suggestions():
    """
    Get suggested questions for starting conversations.
    
    Query Parameters:
        category (str, optional): Category of suggestions ('policies', 'data', 'general')
    
    Returns:
        JSON response containing suggested questions
    """
    try:
        category = request.args.get('category', 'general')
        suggestions = chatbot_service.get_conversation_starters(category)
        
        return success_response({
            'suggestions': suggestions,
            'category': category
        })
        
    except Exception as e:
        return error_response(f'Error retrieving suggestions: {str(e)}', 500)


@chatbot_bp.route('/conversation/<conversation_id>', methods=['GET'])
def get_conversation(conversation_id):
    """
    Retrieve conversation history.
    
    Args:
        conversation_id: Unique conversation identifier
    
    Returns:
        JSON response containing conversation history
    """
    try:
        conversation = chatbot_service.get_conversation_history(conversation_id)
        
        if not conversation:
            return error_response('Conversation not found', 404)
        
        return success_response({
            'conversation_id': conversation_id,
            'messages': conversation['messages'],
            'created_at': conversation['created_at'],
            'last_updated': conversation['last_updated']
        })
        
    except Exception as e:
        return error_response(f'Error retrieving conversation: {str(e)}', 500)


@chatbot_bp.route('/conversation/<conversation_id>', methods=['DELETE'])
def delete_conversation(conversation_id):
    """
    Delete a conversation and its history.
    
    Args:
        conversation_id: Unique conversation identifier
    
    Returns:
        JSON response confirming deletion
    """
    try:
        success = chatbot_service.delete_conversation(conversation_id)
        
        if not success:
            return error_response('Conversation not found', 404)
        
        return success_response({
            'message': 'Conversation deleted successfully',
            'conversation_id': conversation_id
        })
        
    except Exception as e:
        return error_response(f'Error deleting conversation: {str(e)}', 500)


@chatbot_bp.route('/analytics', methods=['GET'])
def get_chat_analytics():
    """
    Get analytics data for chatbot usage.
    
    Returns:
        JSON response containing usage analytics
    """
    try:
        analytics = chatbot_service.get_analytics()
        
        return success_response({
            'analytics': analytics,
            'generated_at': analytics.get('timestamp')
        })
        
    except Exception as e:
        return error_response(f'Error retrieving analytics: {str(e)}', 500)
