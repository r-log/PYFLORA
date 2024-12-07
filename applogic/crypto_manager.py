from cryptography.fernet import Fernet
import json

class CryptoManager:
    def __init__(self):
        # Generate a key for encryption (should be kept secure)
        self.encryption_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.encryption_key)

    def encrypt_data(self, data):
        encrypted_data = self.cipher_suite.encrypt(json.dumps(data).encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        decrypted_data = json.loads(self.cipher_suite.decrypt(encrypted_data).decode())
        return decrypted_data
