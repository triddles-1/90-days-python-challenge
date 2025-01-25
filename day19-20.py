from cryptography.fernet import Fernet

# Generate a key for encryption/decryption
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt(data):
    return cipher.encrypt(data.encode())

def decrypt(encrypted_data):
    return cipher.decrypt(encrypted_data).decode()

# Example usage
if __name__ == "__main__":
    message = input("Type your secret secret message!: ")
    encrypted = encrypt(message)
    decrypted = decrypt(encrypted)

    print(f"Original: {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")