from flask import Flask, request, jsonify
from flask_cors import CORS
from emotion_cipher import EmotionCipher

app = Flask(__name__)
CORS(app)
cipher = EmotionCipher()

def decrypt():
    try:
        data = request.get_json()
        encrypted_text = data.get('encrypted_text', '')
        password = data.get('password', 'default_password_123')
        
        if not encrypted_text:
            return jsonify({"error": "Encrypted text is required"}), 400
        
        decrypted_message, emotions = cipher.decrypt_message(encrypted_text, password)
        
        return jsonify({
            "success": True,
            "decrypted_message": decrypted_message,
            "emotions": emotions
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# Handler for Vercel
def handler(request):
    with app.app_context():
        return decrypt()
