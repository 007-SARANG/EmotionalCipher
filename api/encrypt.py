from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Import from current directory
from emotion_cipher import EmotionCipher

app = Flask(__name__)
CORS(app)
cipher = EmotionCipher()

def encrypt():
    try:
        data = request.get_json()
        message = data.get('message', '')
        password = data.get('password', 'default_password_123')
        
        if not message:
            return jsonify({"error": "Message is required"}), 400
        
        encrypted_text, emotions = cipher.encrypt_message(message, password)
        
        return jsonify({
            "success": True,
            "encrypted_text": encrypted_text,
            "emotions": emotions,
            "original_length": len(message)
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# Handler for Vercel
def handler(request):
    with app.app_context():
        return encrypt()
