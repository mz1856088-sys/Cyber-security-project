import re

def analyze_password(password):
    score = 0
    suggestions = []

    # Length
    if len(password) >= 12:
        score += 25
    else:
        suggestions.append("Use at least 12 characters")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 20
    else:
        suggestions.append("Add uppercase letters")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 20
    else:
        suggestions.append("Add lowercase letters")

    # Numbers
    if re.search(r"\d", password):
        score += 15
    else:
        suggestions.append("Add numbers")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        suggestions.append("Add special characters")

    if score < 40:
        strength = "Weak"
    elif score < 70:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "score": score,
        "strength": strength,
        "suggestions": suggestions
    }