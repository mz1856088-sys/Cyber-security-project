# 🔐 Password Strength Analyzer

A simple Python-based cybersecurity project that analyzes the strength of a password and provides a score along with improvement suggestions.

---

## 📌 Features

- Checks password length
- Detects uppercase and lowercase letters
- Checks for numbers
- Checks for special characters
- Generates a strength score (0–100)
- Classifies password as:
  - Weak
  - Medium
  - Strong
- Provides improvement suggestions

---

## 🧠 How It Works

The tool evaluates a password based on security rules:

| Criteria              | Points |
|----------------------|--------|
| Length ≥ 12          | 25     |
| Uppercase letters    | 20     |
| Lowercase letters    | 20     |
| Numbers              | 15     |
| Special characters   | 20     |

Final score determines password strength.

---

## 📂 Project Structure

```text id="structure1"
password_strength_analyzer/
│
├── main.py
└──analyzer.py



