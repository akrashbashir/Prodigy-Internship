from PIL import Image
import os


def encrypt_image():
    try:
        # Get the path to the image to encrypt
        image_path = input("Enter the path to the image to encrypt: ").strip('"')
        if not os.path.exists(image_path):
            print("Error: Image file not found.")
            return

        # Open the image
        img = Image.open(image_path)

        # Get the dimensions of the image
        width, height = img.size

        # Convert the image to RGB mode (if not already)
        img = img.convert("RGB")

        # Ask for encryption key
        key = int(input("Enter the encryption key (an integer value): "))

        # Iterate through each pixel and perform encryption
        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))  # Get pixel value
                # Perform encryption (for example, swapping pixel values)
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                img.putpixel((x, y), (r, g, b))  # Update pixel value

        # Save the encrypted image
        encrypted_image_path = os.path.splitext(image_path)[0] + "_encrypted.png"
        img.save(encrypted_image_path)
        print("Image encrypted successfully!")
        print("Encrypted image saved as:", encrypted_image_path)

        # Display the encrypted image
        img.show()

        return encrypted_image_path
    except Exception as e:
        print("Error encrypting image:", str(e))
        return None


def decrypt_image(encrypted_image_path):
    try:
        # Open the encrypted image
        img = Image.open(encrypted_image_path)

        # Get the dimensions of the image
        width, height = img.size

        # Convert the image to RGB mode (if not already)
        img = img.convert("RGB")

        # Ask for decryption key
        key = int(input("Enter the decryption key (an integer value): "))

        # Iterate through each pixel and perform decryption
        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))  # Get pixel value
                # Perform decryption (opposite operation of encryption)
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                img.putpixel((x, y), (r, g, b))  # Update pixel value

        # Save the decrypted image
        decrypted_image_path = encrypted_image_path.rsplit('_encrypted', 1)[0] + "_decrypted.png"
        img.save(decrypted_image_path)
        print("Image decrypted successfully!")
        print("Decrypted image saved as:", decrypted_image_path)

        # Display the decrypted image
        img.show()

        return decrypted_image_path
    except Exception as e:
        print("Error decrypting image:", str(e))
        return None


def main():
    while True:
        print("\n--- Image Encryption Tool ---")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            encrypted_image_path = encrypt_image()
            if encrypted_image_path:
                print("Encrypted image saved as:", encrypted_image_path)
        elif choice == '2':
            encrypted_image_path = input("Enter the path to the encrypted image to decrypt: ").strip('"')
            if not os.path.exists(encrypted_image_path):
                print("Error: Encrypted image file not found.")
                continue
            decrypted_image_path = decrypt_image(encrypted_image_path)
            if decrypted_image_path:
                print("Decrypted image saved as:", decrypted_image_path)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
