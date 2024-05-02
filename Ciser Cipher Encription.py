def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text


def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue
        text = input("Enter the text: ")
        shift = int(input("Enter the shift value (0-25): "))

        if choice == 'e':
            encrypted_text = encrypt(text, shift)
            print("Encrypted text:", encrypted_text)
        elif choice == 'd':
            decrypted_text = decrypt(text, shift)
            print("Decrypted text:", decrypted_text)

        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break


if __name__ == "__main__":
    main()
