# Module-3-Secure-Hashing-and-Encryption

This app provides basic cryptographic functions, including hashing, symmetric substitution, and asymmetric digital signatures.

## Functionality
- **SHA-256 Generator**: Uses the standard `hashlib` to process raw strings or binary file streams.
- **Caesar Cipher**: A classic substitution cipher that shifts characters by a user-defined integer.
- **Digital Signature**: Utilizes the `cryptography` library to simulate OpenSSL behavior (RSA keys with SHA-256 padding) to ensure message integrity and authenticity.

## Requirements
`pip install cryptography`

## Usage
Run `python crypto_tool.py` to see the demonstration of all three components.
