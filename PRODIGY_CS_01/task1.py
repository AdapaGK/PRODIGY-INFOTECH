#Prodigy Infotech Task-01

#Task-01 : Implement Caesar Cipher

#Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

#Code:

def caesar_cipher(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) + shift * direction - ascii_offset) % 26 + ascii_offset)
        else:
            result += char
    return result

def encrypt(text, shift):
    return caesar_cipher(text, shift, 1)

def decrypt(text, shift):
    return caesar_cipher(text, -shift, 1)

# User input
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

# Encrypt or Decrypt
choice = input("Choose 'encrypt' or 'decrypt': ").lower()
if choice == 'encrypt':
    encrypted_message = encrypt(message, shift)
    print(f"Encrypted message: {encrypted_message}")
elif choice == 'decrypt':
    decrypted_message = decrypt(message, shift)
    print(f"Decrypted message: {decrypted_message}")
else:
    print("Invalid choice.")


def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is an alphabet
            shift_amount = shift % 26
            if char.islower():
                base = ord('a')
                encrypted_text += chr((ord(char) - base + shift_amount) % 26 + base)
            elif char.isupper():
                base = ord('A')
                encrypted_text += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            encrypted_text += char  # Non-alphabetic characters are not changed
    return encrypted_text

# User input for message and shift value
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

# Encrypt or Decrypt
choice = input("Choose 'encrypt' or 'decrypt': ").lower()
if choice == 'encrypt':
    print("Encrypted message:", caesar_cipher(message, shift))
elif choice == 'decrypt':
    print("Decrypted message:", caesar_cipher(message, -shift))
else:
    print("Invalid choice.")

#END...
