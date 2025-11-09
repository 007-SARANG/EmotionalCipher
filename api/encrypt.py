from http.server import BaseHTTPRequestHandler
import json
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

try:
    from emotion_cipher import EmotionCipher
    cipher = EmotionCipher()
except Exception as e:
    print(f"Import error: {e}")
    cipher = None

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            if cipher is None:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": "Cipher module failed to load"}).encode())
                return
            
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            message = data.get('message', '')
            
            if not message:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Message is required"}).encode())
                return
            
            result = cipher.encrypt_message(message)
            encrypted_text = result['encrypted_text']
            detected_emotions = result.get('detected_emotions', '')
            
            # Convert formatted string to array if needed
            if isinstance(detected_emotions, str):
                if detected_emotions == 'Neutral' or not detected_emotions:
                    emotions = ['Neutral']
                else:
                    emotions = [e.strip() for e in detected_emotions.split('+')]
            else:
                emotions = detected_emotions if detected_emotions else ['Neutral']
            
            # Encode full data for stateless decryption (Vercel serverless)
            import base64
            full_payload = {
                'text': message,
                'emotions': detected_emotions
            }
            payload_json = json.dumps(full_payload)
            encoded_payload = base64.b64encode(payload_json.encode()).decode()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                "success": True,
                "encrypted_text": encrypted_text,
                "emotions": emotions,
                "original_length": len(message),
                "payload": encoded_payload  # Full data for decryption
            }
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            print(f"Error in encrypt: {error_details}")
            
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({
                "success": False, 
                "error": str(e),
                "details": error_details
            }).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
