#Prodigy Infotech Task-02

#Task-02 : Pixel Manipulation for Image Encryption

#Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.

#CODE:

from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image, dtype=np.int32)
    
    # Encrypting by adding key and using modulo to keep values within 0-255
    encrypted_pixels = (pixels + key) % 256
    encrypted_pixels = np.clip(encrypted_pixels, 0, 255)
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image, dtype=np.int32)
    
    # Decrypting by subtracting key and using modulo to keep values within 0-255
    decrypted_pixels = (pixels - key) % 256
    decrypted_pixels = np.clip(decrypted_pixels, 0, 255)
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

key = 50  # This is the key for encryption/decryption
input_image = r'C:\Users\sujat\Downloads\cs.png'
encrypted_image = r'C:\Users\sujat\Downloads\encrypted_image.png'
decrypted_image = r'C:\Users\sujat\Downloads\decrypted_image.png'

encrypt_image(input_image, encrypted_image, key)
decrypt_image(encrypted_image, decrypted_image, key)

#END...
