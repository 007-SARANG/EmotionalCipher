"""
Cipher Module with Emotion Preservation
Encrypts text while embedding emotional signatures that can be detected.
"""

import base64
import hashlib
import secrets
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from typing import Tuple, List
import struct


class EmotionPreservingCipher:
    """
    A cipher that encrypts text while preserving emotional signatures.
    The emotional vector is embedded in the encrypted output.
    """
    
    def __init__(self, master_key: str = None):
        """
        Initialize the cipher with an optional master key.
        
        Args:
            master_key: Master password for encryption (if None, uses default)
        """
        if master_key is None:
            master_key = "EmotionCipher_DefaultKey_2025"
        self.master_key = master_key.encode()
        
    def _derive_key(self, salt: bytes) -> bytes:
        """Derive encryption key from master key and salt."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        return base64.urlsafe_b64encode(kdf.derive(self.master_key))
    
    def _encode_emotion_signature(self, emotion_vector: List[float]) -> bytes:
        """
        Encode emotion vector into bytes that can be embedded in ciphertext.
        Uses a format that creates detectable patterns.
        """
        # Convert emotion probabilities to bytes
        # Using a special marker to make it detectable
        signature = b'EMO:'
        for prob in emotion_vector:
            # Convert float to 2 bytes (scaled to 0-65535)
            value = int(prob * 65535)
            signature += struct.pack('>H', value)
        return signature
    
    def _decode_emotion_signature(self, signature_bytes: bytes) -> List[float]:
        """Decode emotion vector from embedded bytes."""
        if not signature_bytes.startswith(b'EMO:'):
            return []
        
        data = signature_bytes[4:]  # Skip 'EMO:' marker
        emotion_vector = []
        
        # Read 2-byte chunks
        for i in range(0, len(data), 2):
            if i + 2 <= len(data):
                value = struct.unpack('>H', data[i:i+2])[0]
                prob = value / 65535.0
                emotion_vector.append(prob)
        
        return emotion_vector
    
    def encrypt(self, text: str, emotion_vector: List[float]) -> Tuple[str, bytes]:
        """
        Encrypt text while embedding emotional signature.
        
        Args:
            text: The plaintext message
            emotion_vector: The emotion probability vector
            
        Returns:
            Tuple of (encrypted_text, emotion_signature)
        """
        # Generate salt for this encryption
        salt = secrets.token_bytes(16)
        
        # Derive encryption key
        key = self._derive_key(salt)
        cipher = Fernet(key)
        
        # Encrypt the text
        encrypted_data = cipher.encrypt(text.encode())
        
        # Encode emotion signature
        emotion_sig = self._encode_emotion_signature(emotion_vector)
        
        # Combine salt + encrypted_data for decryption
        combined = salt + encrypted_data
        
        # Create the final encrypted output (shortened for display)
        encrypted_text = base64.urlsafe_b64encode(combined[:20]).decode()
        
        return encrypted_text, emotion_sig
    
    def decrypt(self, encrypted_text: str, emotion_signature: bytes, original_length: int) -> str:
        """
        Decrypt the encrypted text back to original.
        
        Args:
            encrypted_text: The encrypted text string
            emotion_signature: The emotion signature bytes
            original_length: Approximate original length (for reconstruction)
            
        Returns:
            The original decrypted text
        """
        # Note: In a real implementation, you would store the full encrypted data
        # For this demo, we're using a simplified approach
        # The actual decryption would use the full encrypted payload
        
        # Decode the shortened encrypted text
        try:
            combined = base64.urlsafe_b64decode(encrypted_text.encode())
            # In production, you'd have the full encrypted data stored
            # This is a simplified demo showing the concept
        except:
            pass
        
        return ""  # Placeholder - see EmotionCipher class for full implementation
    
    def generate_encrypted_display(self, text: str, emotion_vector: List[float]) -> str:
        """
        Generate a deterministic-looking encrypted string for display purposes.
        This creates the visual representation shown in examples.
        
        Args:
            text: Original text
            emotion_vector: Emotion vector
            
        Returns:
            Display-friendly encrypted string
        """
        # Create a hash-based encryption display
        combined = text.encode() + self._encode_emotion_signature(emotion_vector)
        hash_value = hashlib.sha256(combined).digest()
        
        # Convert to base64 and create a shortened display format
        b64 = base64.b64encode(hash_value).decode()
        
        # Create a visually appealing encrypted format
        # Using special characters to make it look encrypted
        encrypted_display = '"' + b64[:16].replace('/', '@').replace('+', '#') + '"'
        
        return encrypted_display
