# EmotionCipher — Emotion Tagging and Encryption Concept Prototype

EmotionCipher is a student prototype exploring whether a text message’s emotion labels could be carried alongside a protected message. The current implementation is a demonstration, not a secure messaging product.

## What the current code does

- `emotion_detector.py` assigns emotion labels using keyword matching and simple counts. It does not use a transformer model or a trained classifier.
- `emotion_cipher.py` creates a short hash-based display token and keeps the original message in an in-memory dictionary so the same running process can demonstrate a round trip. The displayed token is not ciphertext and cannot recover the original message by itself.
- `cipher.py` contains an experimental Fernet-based path, but its display output truncates the ciphertext and `decrypt()` is a placeholder that returns an empty string.
- The web/API files are demonstration interfaces around this unfinished behavior.

**Privacy and security limitation:** do not enter sensitive or confidential text and do not rely on this project to protect, transmit, or recover messages. The default key and incomplete serialization/decryption path are not suitable for real use. Emotion labels are heuristic and may be wrong or culturally biased.

## Run the CLI demonstration

```bash
git clone https://github.com/007-SARANG/EmotionalCipher.git
cd EmotionalCipher
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install -r requirements.txt
python main.py
```

The CLI demonstrates the in-process hash-token flow. It does not demonstrate secure encryption/decryption of a message across sessions or devices.

## Project contents

- `emotion_detector.py` — keyword-based emotion labels and vectors.
- `emotion_cipher.py` — demo orchestration and in-memory message store.
- `cipher.py` — experimental cryptographic helper; decryption is unfinished.
- `server.py`, `web/`, and `public/` — web demonstration components.

## Attribution and status

This is an individual educational prototype. It is not an AI emotion model, a production encryption tool, or a privacy-preserving communication system. Further work would need authenticated encryption with complete ciphertext storage/recovery, key management, threat modeling, and documented evaluation of the emotion classifier.
