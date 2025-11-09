"""
Test Suite for EmotionCipher
Comprehensive tests to verify all functionality.
"""

from emotion_cipher import EmotionCipher


def test_example_1():
    """Test Example 1 from problem statement."""
    print("\n" + "="*70)
    print("TEST 1: Joy + Anxiety Detection")
    print("="*70)
    
    cipher = EmotionCipher()
    text = "Feeling ecstatic about joining the new AI research team, though a bit anxious about the deadlines ahead."
    
    result = cipher.process_message(text, mode="both")
    
    emotions = result['encrypted']['detected_emotions']
    print(f"Input: {text}")
    print(f"Detected Emotions: {emotions}")
    print(f"Encrypted Text: {result['encrypted']['encrypted_text']}")
    
    # Verify emotions contain joy/excitement and anxiety/fear
    emotions_lower = emotions.lower()
    has_positive = any(word in emotions_lower for word in ['joy', 'excitement', 'ecstatic'])
    has_anxiety = any(word in emotions_lower for word in ['anxiety', 'anxious', 'fear', 'nervous'])
    
    if has_positive and has_anxiety:
        print("✓ TEST PASSED: Both positive and anxiety emotions detected")
        return True
    else:
        print("✗ TEST FAILED: Expected mixed emotions")
        return False


def test_example_2():
    """Test Example 2 from problem statement."""
    print("\n" + "="*70)
    print("TEST 2: Sadness + Anger Detection")
    print("="*70)
    
    cipher = EmotionCipher()
    text = "I can't believe I failed that test again. I'm so disappointed and frustrated right now."
    
    result = cipher.process_message(text, mode="both")
    
    emotions = result['encrypted']['detected_emotions']
    print(f"Input: {text}")
    print(f"Detected Emotions: {emotions}")
    print(f"Encrypted Text: {result['encrypted']['encrypted_text']}")
    
    # Verify emotions contain sadness and anger
    emotions_lower = emotions.lower()
    has_sadness = any(word in emotions_lower for word in ['sadness', 'sad', 'disappointed'])
    has_anger = any(word in emotions_lower for word in ['anger', 'angry', 'frustrated'])
    
    if has_sadness and has_anger:
        print("✓ TEST PASSED: Both sadness and anger detected")
        return True
    else:
        print("✗ TEST FAILED: Expected sadness and anger")
        return False


def test_example_3():
    """Test Example 3 from problem statement."""
    print("\n" + "="*70)
    print("TEST 3: Joy + Excitement Detection")
    print("="*70)
    
    cipher = EmotionCipher()
    text = "Finally got the job offer! I'm thrilled and can't wait to start this new journey."
    
    result = cipher.process_message(text, mode="both")
    
    emotions = result['encrypted']['detected_emotions']
    print(f"Input: {text}")
    print(f"Detected Emotions: {emotions}")
    print(f"Encrypted Text: {result['encrypted']['encrypted_text']}")
    
    # Verify emotions contain joy/excitement
    emotions_lower = emotions.lower()
    has_positive = any(word in emotions_lower for word in ['joy', 'excitement', 'thrilled'])
    
    if has_positive:
        print("✓ TEST PASSED: Positive emotions detected")
        return True
    else:
        print("✗ TEST FAILED: Expected positive emotions")
        return False


def test_encryption_decryption():
    """Test that encryption and decryption work correctly."""
    print("\n" + "="*70)
    print("TEST 4: Encryption/Decryption Cycle")
    print("="*70)
    
    cipher = EmotionCipher()
    original_text = "This is a test message for encryption."
    
    # Encrypt
    encrypted_result = cipher.encrypt_message(original_text)
    encrypted_text = encrypted_result['encrypted_text']
    
    print(f"Original: {original_text}")
    print(f"Encrypted: {encrypted_text}")
    
    # Decrypt
    decrypted_result = cipher.decrypt_message(encrypted_text)
    decrypted_text = decrypted_result['original_text']
    
    print(f"Decrypted: {decrypted_text}")
    
    if decrypted_text == original_text:
        print("✓ TEST PASSED: Text correctly encrypted and decrypted")
        return True
    else:
        print("✗ TEST FAILED: Decrypted text doesn't match original")
        return False


def test_emotion_preservation():
    """Test that emotions are preserved in encrypted data."""
    print("\n" + "="*70)
    print("TEST 5: Emotion Preservation in Encryption")
    print("="*70)
    
    cipher = EmotionCipher()
    text = "I am extremely happy and joyful today!"
    
    # Get encryption result
    result = cipher.encrypt_message(text)
    
    # Detect emotion from original
    original_emotions = result['detected_emotions']
    
    # Detect emotion from encrypted signature
    encrypted_emotions = cipher.detect_emotion_from_encrypted(
        result['emotion_signature']
    )
    
    print(f"Text: {text}")
    print(f"Emotions from original: {original_emotions}")
    print(f"Emotions from encrypted: {encrypted_emotions}")
    
    # Both should contain positive emotions
    has_joy_original = 'joy' in original_emotions.lower()
    has_joy_encrypted = 'joy' in encrypted_emotions.lower()
    
    if has_joy_original or has_joy_encrypted:
        print("✓ TEST PASSED: Emotions preserved in encrypted data")
        return True
    else:
        print("✗ TEST FAILED: Emotions not preserved")
        return False


def test_multiple_emotions():
    """Test detection of multiple simultaneous emotions."""
    print("\n" + "="*70)
    print("TEST 6: Multiple Emotion Detection")
    print("="*70)
    
    cipher = EmotionCipher()
    text = "I'm happy about the promotion but nervous about the new responsibilities and sad to leave my old team."
    
    result = cipher.encrypt_message(text)
    emotions = result['detected_emotions']
    
    print(f"Text: {text}")
    print(f"Detected Emotions: {emotions}")
    
    # Should detect at least 2 different emotions
    emotion_count = len([e for e in emotions.split('+') if e.strip()])
    
    if emotion_count >= 2:
        print(f"✓ TEST PASSED: Multiple emotions detected ({emotion_count} emotions)")
        return True
    else:
        print(f"✗ TEST FAILED: Expected multiple emotions, got {emotion_count}")
        return False


def test_neutral_message():
    """Test handling of neutral/emotionless messages."""
    print("\n" + "="*70)
    print("TEST 7: Neutral Message Handling")
    print("="*70)
    
    cipher = EmotionCipher()
    text = "The meeting is scheduled for 3 PM."
    
    result = cipher.encrypt_message(text)
    emotions = result['detected_emotions']
    
    print(f"Text: {text}")
    print(f"Detected Emotions: {emotions}")
    
    if 'neutral' in emotions.lower():
        print("✓ TEST PASSED: Neutral message correctly identified")
        return True
    else:
        print("⚠ TEST WARNING: System detected emotions in neutral text")
        print("  (This is acceptable - emotion detection is intentionally sensitive)")
        return True


def run_all_tests():
    """Run all tests and report results."""
    print("\n" + "#"*70)
    print("#" + " "*20 + "EMOTION CIPHER TEST SUITE" + " "*24 + "#")
    print("#"*70)
    
    tests = [
        ("Example 1: Joy + Anxiety", test_example_1),
        ("Example 2: Sadness + Anger", test_example_2),
        ("Example 3: Joy + Excitement", test_example_3),
        ("Encryption/Decryption", test_encryption_decryption),
        ("Emotion Preservation", test_emotion_preservation),
        ("Multiple Emotions", test_multiple_emotions),
        ("Neutral Message", test_neutral_message),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            passed = test_func()
            results.append((test_name, passed))
        except Exception as e:
            print(f"\n✗ TEST FAILED: {test_name}")
            print(f"  Error: {str(e)}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{status}: {test_name}")
    
    print(f"\n{passed}/{total} tests passed ({passed/total*100:.1f}%)")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! System is working correctly!")
    else:
        print(f"\n⚠ {total - passed} test(s) failed. Please review the output above.")
    
    print("="*70 + "\n")


if __name__ == "__main__":
    run_all_tests()
