import re
import hashlib

# Function to check password strength
def check_password_strength(password):
    strength = 0
    remarks = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Increase length to at least 8 characters.")

    # Check uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        remarks.append("Add at least one uppercase letter.")

    # Check lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        remarks.append("Add at least one lowercase letter.")

    # Check numbers
    if re.search(r'\d', password):
        strength += 1
    else:
        remarks.append("Include at least one number.")

    # Check special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        remarks.append("Use at least one special character (!@#$%^&*).")

    # Determine strength
    strength_levels = ["Weak ❌", "Moderate ⚠️", "Strong ✅"]
    colors = ["#e74c3c", "#f39c12", "#2ecc71"]

    strength_level = ""
    color = ""
    if strength == 5:
        strength_level = strength_levels[2]
        color = colors[2]
    elif strength >= 3:
        strength_level = strength_levels[1]
        color = colors[1]
    else:
        strength_level = strength_levels[0]
        color = colors[0]

    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    return strength_level, color, remarks, hashed_password[:20] + "..."
