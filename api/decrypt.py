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
            
            encrypted_text = data.get('encrypted_text', '')
            payload = data.get('payload', '')
            
            if not payload or payload == '':
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                error_msg = "Payload is required for decryption. Please encrypt a new message (old messages from before this update won't work)."
                self.wfile.write(json.dumps({"success": False, "error": error_msg}).encode())
                return
            
            # Decode the payload (stateless decryption for Vercel)
            import base64
            payload_json = base64.b64decode(payload.encode()).decode()
            payload_data = json.loads(payload_json)
            
            decrypted_message = payload_data.get('text', '')
            detected_emotions = payload_data.get('emotions', '')
            
            # Convert formatted string to array if needed
            if isinstance(detected_emotions, str):
                if detected_emotions == 'Neutral' or not detected_emotions:
                    emotions = ['Neutral']
                else:
                    emotions = [e.strip() for e in detected_emotions.split('+')]
            else:
                emotions = detected_emotions if detected_emotions else ['Neutral']
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                "success": True,
                "decrypted_message": decrypted_message,
                "emotions": emotions
            }
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
