"""
Emotion Detection Module
Uses rule-based and keyword analysis to detect emotions in text.
"""

import re
from typing import List, Dict
from collections import defaultdict


class EmotionDetector:
    """Detects emotions from text using keyword analysis and patterns."""
    
    def __init__(self):
        """Initialize the emotion detection model."""
        print("Loading emotion detection model...")
        
        # Emotion keyword dictionary
        self.emotion_keywords = {
            'joy': [
                'happy', 'joy', 'joyful', 'delighted', 'pleased', 'glad', 'cheerful',
                'ecstatic', 'thrilled', 'excited', 'elated', 'wonderful', 'great',
                'fantastic', 'amazing', 'love', 'enjoy', 'blessed', 'grateful'
            ],
            'sadness': [
                'sad', 'unhappy', 'depressed', 'miserable', 'sorrowful', 'gloomy',
                'disappointed', 'down', 'blue', 'heartbroken', 'grief', 'crying',
                'tears', 'hopeless', 'lonely', 'failed', 'fail', 'failure', 'devastated'
            ],
            'anger': [
                'angry', 'furious', 'rage', 'mad', 'irritated', 'annoyed', 'frustrated',
                'outraged', 'upset', 'aggravated', 'hostile', 'bitter', 'resentful',
                'hate', 'can\'t believe', 'disgusted'
            ],
            'fear': [
                'afraid', 'scared', 'frightened', 'terrified', 'anxious', 'worried',
                'nervous', 'panic', 'fearful', 'alarmed', 'concerned', 'dread',
                'uneasy', 'tense', 'stress', 'stressed'
            ],
            'surprise': [
                'surprised', 'amazed', 'astonished', 'shocked', 'stunned', 'startled',
                'unexpected', 'suddenly', 'wow', 'can\'t believe'
            ],
            'excitement': [
                'excited', 'thrilled', 'eager', 'enthusiastic', 'pumped', 'energized',
                'can\'t wait', 'looking forward', 'anticipating'
            ],
            'anxiety': [
                'anxious', 'nervous', 'worried', 'stressed', 'tense', 'uneasy',
                'concerned', 'restless', 'deadline', 'deadlines'
            ]
        }
        
        print("Emotion detection model loaded successfully!")
        
    def detect_emotions(self, text: str, threshold: float = 0.3) -> List[str]:
        """
        Detect emotions in the given text.
        
        Args:
            text: The input text to analyze
            threshold: Minimum confidence threshold for emotion detection
            
        Returns:
            List of detected emotions
        """
        if not text or not text.strip():
            return []
        
        text_lower = text.lower()
        emotion_scores = defaultdict(float)
        
        # Count keyword matches for each emotion
        for emotion, keywords in self.emotion_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    emotion_scores[emotion] += 1
        
        # Normalize scores
        total = sum(emotion_scores.values())
        if total == 0:
            return ['Neutral']
        
        # Calculate probabilities
        emotion_probs = {
            emotion: score / total 
            for emotion, score in emotion_scores.items()
        }
        
        # Filter emotions above threshold
        detected_emotions = [
            emotion.capitalize() 
            for emotion, prob in emotion_probs.items() 
            if prob >= threshold
        ]
        
        # Sort by score (descending)
        detected_emotions.sort(
            key=lambda e: emotion_probs[e.lower()],
            reverse=True
        )
        
        return detected_emotions if detected_emotions else ['Neutral']
    
    def get_emotion_vector(self, text: str) -> List[float]:
        """
        Get the emotion probability vector for the text.
        This can be used as an emotional signature for encryption.
        
        Args:
            text: The input text to analyze
            
        Returns:
            List of emotion probabilities (7 emotions)
        """
        if not text or not text.strip():
            return [0.0] * 7
        
        text_lower = text.lower()
        emotion_scores = {}
        
        # Get scores for all emotions
        for emotion, keywords in self.emotion_keywords.items():
            score = 0
            for keyword in keywords:
                if keyword in text_lower:
                    score += 1
            emotion_scores[emotion] = score
        
        # Normalize to probabilities
        total = sum(emotion_scores.values())
        if total == 0:
            return [1.0/7] * 7  # Uniform distribution for neutral
        
        # Return in consistent order
        emotion_order = ['anger', 'anxiety', 'fear', 'joy', 'sadness', 'surprise', 'excitement']
        vector = [emotion_scores.get(e, 0) / total for e in emotion_order]
        
        return vector
    
    def format_emotions(self, emotions: List[str]) -> str:
        """
        Format the list of emotions for display.
        
        Args:
            emotions: List of detected emotions
            
        Returns:
            Formatted string of emotions
        """
        if not emotions or emotions == ['Neutral']:
            return "Neutral"
        return " + ".join(emotions)
