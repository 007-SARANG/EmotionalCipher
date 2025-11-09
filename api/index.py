from flask import Flask, request, jsonify
from flask_cors import CORS
from emotion_cipher import EmotionCipher

app = Flask(__name__)
CORS(app)

# Initialize the cipher
cipher = EmotionCipher()

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "EmotionCipher API is running!",
        "endpoints": ["/encrypt", "/decrypt"]
    })

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.get_json()
        message = data.get('message', '')
        password = data.get('password', 'default_password_123')
        
        if not message:
            return jsonify({"error": "Message is required"}), 400
        
        # Encrypt the message
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

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.get_json()
        encrypted_text = data.get('encrypted_text', '')
        password = data.get('password', 'default_password_123')
        
        if not encrypted_text:
            return jsonify({"error": "Encrypted text is required"}), 400
        
        # Decrypt the message
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

# For local testing
if __name__ == '__main__':
    app.run(debug=True, port=5000)

# Vercel serverless function handler
# The app variable is automatically used by Vercel
