import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def generate_key():
    return AESGCM.generate_key(bit_length=256)

def encrypt(key: bytes, plaintext: str) -> bytes:
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)          # 96-bit nonce for GCM
    ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), None)
    return nonce + ciphertext       # prepend nonce for decryption

def decrypt(key: bytes, data: bytes) -> str:
    aesgcm = AESGCM(key)
    nonce, ciphertext = data[:12], data[12:]
    return aesgcm.decrypt(nonce, ciphertext, None).decode()