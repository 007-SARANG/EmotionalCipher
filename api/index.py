"""
Vercel Serverless Function for EmotionCipher
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from emotion_cipher import EmotionCipher

app = Flask(__name__)
CORS(app)

# Initialize EmotionCipher
cipher = EmotionCipher()

@app.route('/')
def index():
    """Serve the main HTML page."""
    html_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'web', 'index.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/encrypt', methods=['POST'])
def encrypt():
    """Encrypt a message and detect emotions."""
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        result = cipher.encrypt_message(text)
        emotions_str = result['detected_emotions']
        emotions = [e.strip() for e in emotions_str.split('+')]
        
        return jsonify({
            'encrypted_text': result['encrypted_text'],
            'emotions': emotions,
            'emotion_signature': result['emotion_signature'].hex()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/decrypt', methods=['POST'])
def decrypt():
    """Decrypt a message and recover emotions."""
    try:
        data = request.get_json()
        encrypted_text = data.get('encrypted_text', '')
        
        if not encrypted_text:
            return jsonify({'error': 'No encrypted text provided'}), 400
        
        result = cipher.decrypt_message(encrypted_text)
        
        if result.get('error'):
            return jsonify({'error': result['error']}), 404
        
        emotions_str = result['detected_emotions']
        emotions = [e.strip() for e in emotions_str.split('+')]
        
        return jsonify({
            'original_text': result['original_text'],
            'emotions': emotions
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'EmotionCipher API',
        'version': '1.0'
    })

# Vercel serverless function handler
def handler(request):
    with app.request_context(request.environ):
        return app.full_dispatch_request()
