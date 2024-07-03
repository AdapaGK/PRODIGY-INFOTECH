#Prodigy Infotech Task-03

#Task-03 : Password Complexity Checker

#Build a tool that assesses the strength of a password based on criteria such as length,presence of uppercase and lowercase letters , numbers,and special characters. Provide feedback to users on the password's strength.

#CODE :

import re

def password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Calculate strength score
    score = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_char_criteria])

    # Provide feedback based on score
    if score == 5:
        feedback = "Very Strong"
    elif score == 4:
        feedback = "Strong"
    elif score == 3:
        feedback = "Moderate"
    elif score == 2:
        feedback = "Weak"
    else:
        feedback = "Very Weak"

    return feedback

password = input("Enter a password to check its strength: ")
print(f"Password strength: {password_strength(password)}")

#END...
