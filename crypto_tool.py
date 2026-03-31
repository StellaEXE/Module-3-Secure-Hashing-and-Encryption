import hashlib
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

# --- 1. SHA-256 Hashing ---
def generate_sha256(data, is_file=False):
    """Generates SHA-256 hash for a string or a file path."""
    sha256 = hashlib.sha256()
    if is_file:
        if not os.path.exists(data): return "File not found."
        with open(data, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256.update(byte_block)
    else:
        sha256.update(data.encode())
    return sha256.hexdigest()

# --- 2. Caesar Cipher (Substitution) ---
def caesar_cipher(text, shift, mode='encrypt'):
    """Encrypts or decrypts text using a fixed alphabetical shift."""
    if mode == 'decrypt': shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

# --- 3. Digital Signature (Sign/Verify) ---
def simulate_digital_signature(message):
    """Simulates OpenSSL signing/verification using RSA."""
    # Generate keys
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Sign the message
    signature = private_key.sign(
        message.encode(),
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

    # Verify the signature
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return signature.hex(), True
    except Exception:
        return signature.hex(), False

if __name__ == "__main__":
    # Testing
    msg = "Security Assignment 101"
    print(f"SHA-256 Hash: {generate_sha256(msg)}")
    
    encrypted = caesar_cipher(msg, 5, 'encrypt')
    print(f"Caesar Encrypted: {encrypted}")
    print(f"Caesar Decrypted: {caesar_cipher(encrypted, 5, 'decrypt')}")
    
    sig, verified = simulate_digital_signature(msg)
    print(f"Signature Verified: {verified}")
