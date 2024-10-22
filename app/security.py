from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# Ensure the key is 16, 24, or 32 bytes (padded to 32 bytes here)
SECRET_KEY = os.getenv('SECRET_KEY', 'my_very_secret_key_12345')
SECRET_KEY = SECRET_KEY[:32].ljust(32).encode('utf-8')  # Ensure it's 32 bytes

def encrypt_password(plain_password: str) -> bytes:
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC)
    iv = cipher.iv  # Initialization Vector
    encrypted_password = cipher.encrypt(pad(plain_password.encode('utf-8'), AES.block_size))
    return iv + encrypted_password  # Return IV + encrypted password


def decrypt_password(encrypted_password: str) -> str:
    # Convert the hexadecimal string to bytes
    encrypted_bytes = bytes.fromhex(encrypted_password[2:])  # Skip the '\\x'

    # Extract IV and the actual encrypted password
    iv = encrypted_bytes[:AES.block_size]  # First 16 bytes (for AES)
    encrypted_data = encrypted_bytes[AES.block_size:]  # Remaining bytes

    # Create AES cipher using the extracted IV
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)

    # Decrypt the encrypted data
    decrypted_password = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    return decrypted_password.decode('utf-8')
