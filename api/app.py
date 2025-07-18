"""
Digital Divide Policy Insights API

A Flask API providing endpoints for policy data, analytics, and chatbot functionality.
"""

import os
import sys
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

def create_app():
    """Application factory pattern for Flask app creation."""
    app = Flask(__name__)
    
    # Configuration
    app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.config['API_PORT'] = int(os.getenv('API_PORT', 5001))
    
    # CORS configuration
    CORS(app, origins=['http://localhost:8501', 'http://127.0.0.1:8501'])
    
    # Register blueprints
    register_blueprints(app)
    
    # Register error handlers
    register_error_handlers(app)
    
    return app

def register_blueprints(app):
    """Register all application blueprints."""
    from routes.policies import policies_bp
    from routes.data import data_bp
    
    app.register_blueprint(policies_bp, url_prefix='/api/policies')
    app.register_blueprint(data_bp, url_prefix='/api/data')

def register_error_handlers(app):
    """Register global error handlers."""
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Endpoint not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500

# Create app instance
app = create_app()

@app.route('/')
def index():
    """API root endpoint with service information."""
    return jsonify({
        'service': 'Digital Divide Policy Insights API',
        'version': '1.0.0',
        'status': 'operational',
        'endpoints': {
            'policies': '/api/policies',
            'data': '/api/data',
            'health': '/health'
        }
    })

@app.route('/health')
def health_check():
    """Health check endpoint for monitoring services."""
    return jsonify({
        'status': 'healthy',
        'service': 'api',
        'message': 'Service is operational'
    })

if __name__ == '__main__':
    port = app.config['API_PORT']
    debug = app.config['DEBUG']
    
    print(f"Starting Digital Divide Policy Insights API on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug)
