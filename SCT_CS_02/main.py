from PIL import Image
import numpy as np

# Function to load image
def load_image(path):
    image = Image.open(path)
    return image

# Function to encrypt image using XOR
def encrypt_image(image, key):
    image_array = np.array(image)
    encrypted_array = image_array ^ key  # XOR operation
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    return encrypted_image

# Function to decrypt image using XOR (same as encrypt)
def decrypt_image(encrypted_image, key):
    encrypted_array = np.array(encrypted_image)
    decrypted_array = encrypted_array ^ key
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    return decrypted_image

# Main program
def main():
    print("🔐 Image Encryption Tool - SkillCraft Technology")

    # Load original image
    input_path = "sample_images/original.png"
    key = int(input("Enter encryption key (0-255): "))

    image = load_image(input_path)

    # Encrypt image
    encrypted = encrypt_image(image, key)
    encrypted.save("sample_images/encrypted.png")
    print("✅ Image encrypted and saved as 'encrypted.png'")

    # Decrypt image
    decrypted = decrypt_image(encrypted, key)
    decrypted.save("sample_images/decrypted.png")
    print("✅ Decrypted image saved as 'decrypted.png'")

if __name__ == "__main__":
    main()
