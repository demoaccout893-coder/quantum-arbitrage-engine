from cryptography.fernet import Fernet

class KeyVault:
    def __init__(self, key: bytes):
        self.cipher = Fernet(key)

    def encrypt(self, message: str) -> bytes:
        return self.cipher.encrypt(message.encode())

    def decrypt(self, encrypted_message: bytes) -> str:
        return self.cipher.decrypt(encrypted_message).decode()