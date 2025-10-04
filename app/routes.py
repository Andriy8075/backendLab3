from flask import jsonify
from app import app
from datetime import datetime

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    """Healthcheck endpoint that returns current date and service status"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat() + 'Z',
    }), 200

@app.route('/')
def hello():
    """Root endpoint that greets the user"""
    return jsonify({
        'message': 'Welcome to REST API!',
    }), 200
