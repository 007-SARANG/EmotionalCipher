"""
EmotionCipher - Main Integration Module
Combines emotion detection with encryption to create an empathy-preserving cipher.
"""

from emotion_detector import EmotionDetector
from cipher import EmotionPreservingCipher
from typing import Dict, List


class EmotionCipher:
    """
    Main class that integrates emotion detection with encryption.
    Encrypts messages while preserving emotional signatures for AI detection.
    """
    
    def __init__(self, master_key: str = None):
        """
        Initialize the EmotionCipher system.
        
        Args:
            master_key: Optional master key for encryption
        """
        self.emotion_detector = EmotionDetector()
        self.cipher = EmotionPreservingCipher(master_key)
        
        # Store encrypted messages for decryption
        self.message_store = {}
        
    def encrypt_message(self, text: str) -> Dict:
        """
        Encrypt a message while preserving its emotional signature.
        
        Args:
            text: The original text message
            
        Returns:
            Dictionary containing encrypted text and detected emotions
        """
        # Step 1: Detect emotions in the original text
        emotions = self.emotion_detector.detect_emotions(text, threshold=0.2)
        emotion_vector = self.emotion_detector.get_emotion_vector(text)
        
        # Step 2: Encrypt the text with emotion embedding
        encrypted_text = self.cipher.generate_encrypted_display(text, emotion_vector)
        emotion_signature = self.cipher._encode_emotion_signature(emotion_vector)
        
        # Step 3: Store the message for decryption
        message_id = encrypted_text
        self.message_store[message_id] = {
            'original_text': text,
            'emotion_vector': emotion_vector,
            'emotion_signature': emotion_signature
        }
        
        # Step 4: Return the encrypted result
        return {
            'encrypted_text': encrypted_text,
            'detected_emotions': self.emotion_detector.format_emotions(emotions),
            'emotion_signature': emotion_signature,
            'emotion_vector': emotion_vector
        }
    
    def decrypt_message(self, encrypted_text: str, emotion_signature: bytes = None) -> Dict:
        """
        Decrypt a message and recover the original text and emotions.
        
        Args:
            encrypted_text: The encrypted text
            emotion_signature: The emotion signature bytes (optional)
            
        Returns:
            Dictionary containing original text and detected emotions
        """
        # Retrieve from message store
        if encrypted_text in self.message_store:
            stored_data = self.message_store[encrypted_text]
            original_text = stored_data['original_text']
            emotion_vector = stored_data['emotion_vector']
            
            # Re-detect emotions to verify
            emotions = self.emotion_detector.detect_emotions(original_text, threshold=0.2)
            
            return {
                'original_text': original_text,
                'detected_emotions': self.emotion_detector.format_emotions(emotions),
                'emotion_vector': emotion_vector
            }
        else:
            return {
                'original_text': None,
                'detected_emotions': "Unknown",
                'error': 'Message not found in store'
            }
    
    def detect_emotion_from_encrypted(self, emotion_signature: bytes) -> str:
        """
        Detect emotions from the encrypted message's signature.
        This demonstrates that AI can still understand emotions even when text is encrypted.
        
        Args:
            emotion_signature: The embedded emotion signature
            
        Returns:
            Formatted emotion string
        """
        # Decode the emotion vector from signature
        emotion_vector = self.cipher._decode_emotion_signature(emotion_signature)
        
        if not emotion_vector:
            return "Neutral"
        
        # Map emotion vector back to labels
        # The model uses these emotion labels in order
        emotion_labels = ['Anger', 'Disgust', 'Fear', 'Joy', 'Neutral', 'Sadness', 'Surprise']
        
        # Get top emotions above threshold
        emotions = []
        threshold = 0.2
        for i, prob in enumerate(emotion_vector):
            if prob >= threshold:
                emotions.append((emotion_labels[i], prob))
        
        # Sort by probability
        emotions.sort(key=lambda x: x[1], reverse=True)
        
        # Format output
        emotion_names = [e[0] for e in emotions]
        return " + ".join(emotion_names) if emotion_names else "Neutral"
    
    def process_message(self, text: str, mode: str = "both") -> Dict:
        """
        Process a message: encrypt it and optionally decrypt it back.
        
        Args:
            text: The input message
            mode: "encrypt", "decrypt", or "both"
            
        Returns:
            Dictionary with processing results
        """
        result = {}
        
        if mode in ["encrypt", "both"]:
            encrypted_result = self.encrypt_message(text)
            result['encrypted'] = encrypted_result
        
        if mode in ["decrypt", "both"] and 'encrypted' in result:
            decrypted_result = self.decrypt_message(
                result['encrypted']['encrypted_text'],
                result['encrypted']['emotion_signature']
            )
            result['decrypted'] = decrypted_result
        
        return result
    
    def demo_example(self, text: str) -> None:
        """
        Run a complete demo showing encryption, emotion detection, and decryption.
        
        Args:
            text: The input message to demonstrate
        """
        print(f"\n{'='*70}")
        print(f"Input Message: \"{text}\"")
        print(f"{'='*70}")
        
        # Encrypt
        result = self.process_message(text, mode="both")
        
        # Display encrypted output
        print(f"\n{'Encrypted Output:':^70}")
        print(f"{'-'*70}")
        print(f"Encrypted Text: {result['encrypted']['encrypted_text']}")
        print(f"Detected Emotion: {result['encrypted']['detected_emotions']}")
        
        # Demonstrate that emotion can be detected from encrypted data
        detected_from_encrypted = self.detect_emotion_from_encrypted(
            result['encrypted']['emotion_signature']
        )
        print(f"\n{'AI Detection (from encrypted):':^70}")
        print(f"Emotion visible to AI: {detected_from_encrypted}")
        
        # Display decrypted output
        print(f"\n{'Decrypted Output:':^70}")
        print(f"{'-'*70}")
        if result['decrypted']['original_text']:
            print(f"Original Message: \"{result['decrypted']['original_text']}\"")
            print(f"Detected Emotion: {result['decrypted']['detected_emotions']}")
        else:
            print("Decryption failed")
        
        print(f"{'='*70}\n")
