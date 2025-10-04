from flask import jsonify
from app import app

@app.route('/')
def hello():
    """Root endpoint that greets the user"""
    return jsonify({
        'message': 'Welcome to REST API!',
    }), 200
