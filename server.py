"""
Flask Server for EmotionCipher Web GUI
Provides REST API endpoints for the web interface.
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from emotion_cipher import EmotionCipher
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for web requests

# Initialize EmotionCipher
cipher = EmotionCipher()

@app.route('/')
def index():
    """Serve the main HTML page."""
    return send_from_directory('web', 'index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    """
    Encrypt a message and detect emotions.
    
    Request JSON:
        {
            "text": "Your message here"
        }
    
    Response JSON:
        {
            "encrypted_text": "...",
            "emotions": ["Joy", "Anxiety"],
            "emotion_signature": "..."
        }
    """
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Encrypt the message
        result = cipher.encrypt_message(text)
        
        # Parse emotions
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
    """
    Decrypt a message and recover emotions.
    
    Request JSON:
        {
            "encrypted_text": "..."
        }
    
    Response JSON:
        {
            "original_text": "...",
            "emotions": ["Joy", "Anxiety"]
        }
    """
    try:
        data = request.get_json()
        encrypted_text = data.get('encrypted_text', '')
        
        if not encrypted_text:
            return jsonify({'error': 'No encrypted text provided'}), 400
        
        # Decrypt the message
        result = cipher.decrypt_message(encrypted_text)
        
        if result.get('error'):
            return jsonify({'error': result['error']}), 404
        
        # Parse emotions
        emotions_str = result['detected_emotions']
        emotions = [e.strip() for e in emotions_str.split('+')]
        
        return jsonify({
            'original_text': result['original_text'],
            'emotions': emotions
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/demo/<int:example_num>', methods=['GET'])
def demo(example_num):
    """
    Get one of the demo examples.
    
    URL Parameter:
        example_num: 1, 2, or 3
    
    Response JSON:
        {
            "text": "Example message"
        }
    """
    examples = {
        1: "Feeling ecstatic about joining the new AI research team, though a bit anxious about the deadlines ahead.",
        2: "I can't believe I failed that test again. I'm so disappointed and frustrated right now.",
        3: "Finally got the job offer! I'm thrilled and can't wait to start this new journey."
    }
    
    if example_num not in examples:
        return jsonify({'error': 'Invalid example number'}), 400
    
    return jsonify({'text': examples[example_num]})

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'EmotionCipher API',
        'version': '1.0'
    })

def main():
    """Start the Flask server."""
    print("\n" + "="*70)
    print("🔐 EmotionCipher Web Server Starting...")
    print("="*70)
    print("\n📡 Server running on: http://localhost:5000")
    print("🌐 Open your browser to: http://localhost:5000")
    print("\n💡 Press Ctrl+C to stop the server")
    print("="*70 + "\n")
    
    # Run the server
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    main()
