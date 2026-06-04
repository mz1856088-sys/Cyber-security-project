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
```





# 🚀 How to Run

## 1. Clone the repository
git clone https://github.com/mz1856088-sys/Cyber-security-project.git
## 2. Go to project folder
cd password-strength-analyzer
## 3. Run the program
python main.py
🧪 Example Output
Enter Password: hello123

Results
----------------------------------------
Strength : Medium
Score    : 55/100

Suggestions:
- Use at least 12 characters
- Add uppercase letters
- Add special characters
## 📦 Requirements

No external libraries required. Uses Python standard library only.

requirements.txt is empty or optional




