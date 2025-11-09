# Setup and Testing Guide

## Quick Setup Instructions

### Step 1: Install Dependencies

```bash
cd d:\PROJECT\EmotionCipher
pip install -r requirements.txt
```

Expected output:
```
Collecting cryptography>=41.0.0
...
Successfully installed cryptography-X.X.X
```

### Step 2: Test with Demo Examples

```bash
python main.py --demo
```

This will run all 3 provided examples and show:
- Encrypted text
- Detected emotions
- Emotion detection from encrypted data
- Decrypted original message

### Step 3: Try Interactive Mode

```bash
python main.py
```

Choose option 1 to encrypt your own messages.

### Step 4: Quick Single Message Test

```bash
python main.py "I love this project!"
```

---

## Verification Checklist

After installation, verify:

- [ ] No import errors when running
- [ ] All 3 examples execute successfully
- [ ] Emotions are correctly detected
- [ ] Text is encrypted into gibberish
- [ ] Emotions visible from encrypted data
- [ ] Decryption recovers original text
- [ ] Interactive mode works

---

## Expected Example Outputs

### Example 1:
**Input**: "Feeling ecstatic about joining the new AI research team, though a bit anxious about the deadlines ahead."

**Expected Emotions**: Anxiety + Joy (or similar combinations with Fear)

### Example 2:
**Input**: "I can't believe I failed that test again. I'm so disappointed and frustrated right now."

**Expected Emotions**: Sadness + Anger

### Example 3:
**Input**: "Finally got the job offer! I'm thrilled and can't wait to start this new journey."

**Expected Emotions**: Excitement + Joy

---

## Common Issues and Solutions

### Issue 1: Module Not Found
**Error**: `ModuleNotFoundError: No module named 'cryptography'`

**Solution**:
```bash
pip install cryptography
```

### Issue 2: Python Version
**Error**: Syntax errors or compatibility issues

**Solution**: Ensure Python 3.7+ is installed:
```bash
python --version
```

### Issue 3: Permission Errors
**Solution**: Run terminal as administrator or use:
```bash
pip install --user cryptography
```

---

## Testing Different Emotions

Try these test messages to verify emotion detection:

**Joy/Happiness**:
```bash
python main.py "I am so happy and grateful for this wonderful opportunity!"
```

**Sadness**:
```bash
python main.py "I feel so lonely and heartbroken after the breakup."
```

**Anger**:
```bash
python main.py "I am furious and frustrated with this situation!"
```

**Fear/Anxiety**:
```bash
python main.py "I'm terrified and anxious about the upcoming exam."
```

**Mixed Emotions**:
```bash
python main.py "I'm excited but also nervous about moving to a new city."
```

---

## Performance Expectations

- **Startup Time**: < 1 second
- **Encryption Time**: < 0.1 seconds per message
- **Memory Usage**: < 50 MB
- **Dependencies**: Just cryptography library (~3 MB)

---

## File Structure Verification

Ensure all files exist:

```
EmotionCipher/
├── main.py                 ✓
├── emotion_cipher.py       ✓
├── emotion_detector.py     ✓
├── cipher.py              ✓
├── requirements.txt       ✓
├── README.md             ✓
├── .gitignore            ✓
├── VIDEO_SCRIPT.md       ✓
└── SETUP_GUIDE.md        ✓
```

---

## Ready for Submission?

Checklist:

- [ ] All files created
- [ ] Dependencies installed
- [ ] Demo runs successfully
- [ ] All 3 examples work correctly
- [ ] Interactive mode tested
- [ ] Code is well-documented
- [ ] README is comprehensive
- [ ] Video recorded and uploaded
- [ ] GitHub repository created
- [ ] Repository is public
- [ ] Video link added to README

---

## GitHub Repository Setup

1. Initialize git (if not already):
```bash
cd d:\PROJECT\EmotionCipher
git init
```

2. Add all files:
```bash
git add .
```

3. Commit:
```bash
git commit -m "Initial commit: EmotionCipher - Empathy Encryption System"
```

4. Create repository on GitHub (via web interface)

5. Add remote and push:
```bash
git remote add origin https://github.com/YOUR_USERNAME/EmotionCipher.git
git branch -M main
git push -u origin main
```

---

## Submission

1. **Video**: Upload to YouTube (public or unlisted)
2. **GitHub**: Push all code to repository
3. **Portal**: Submit GitHub link (manually typed!)
4. **Video Link**: Include in repository README

---

**Good luck with your submission! 🚀**
