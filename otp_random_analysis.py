import os
import random
import secrets
import struct

"""
One-Time Pad (OTP) Encryption & Random Number Generator (RNG) Analysis

This script demonstrates:
1. One-Time Pad (OTP) encryption and decryption.
2. Comparison of standard PRNG (`random`) vs cryptographic CSPRNG (`secrets`, `os.urandom`).
3. An example attack on `random` (predicting sequence if seed is known).
"""

# ======================
# 1. One-Time Pad (OTP) Implementation
# ======================
def generate_key(length):
    """Generates a one-time pad key using a cryptographically secure RNG."""
    return os.urandom(length)

def otp_encrypt_decrypt(message: bytes, key: bytes) -> bytes:
    """Encrypts/decrypts a message using a one-time pad (XOR operation)."""
    return bytes([m ^ k for m, k in zip(message, key)])

message = b"SecretMessage"  # Original message
key = generate_key(len(message))  # Generate key
ciphertext = otp_encrypt_decrypt(message, key)  # Encrypt

decrypted_message = otp_encrypt_decrypt(ciphertext, key)  # Decrypt
print(f"Original Message: {message}")
print(f"Encrypted: {ciphertext}")
print(f"Decrypted: {decrypted_message}")

# ======================
# 2. PRNG vs CSPRNG Analysis
# ======================
print("\nPRNG vs CSPRNG:")
random.seed(42)  # Fix seed for reproducibility
print("random.randint(0, 255):", [random.randint(0, 255) for _ in range(5)])
print("secrets.randbelow(256):", [secrets.randbelow(256) for _ in range(5)])
print("os.urandom(5):", list(os.urandom(5)))

# ======================
# 3. PRNG Attack Demonstration (Mersenne Twister)
# ======================
def predict_next_random():
    """Demonstration of PRNG attack (predicting output of random module)."""
    random.seed(12345)  # Set a known seed
    observed_values = [random.randint(0, 100) for _ in range(5)]
    
    # If the seed is known, the sequence can be predicted
    random.seed(12345)  # Reset the seed
    predicted_values = [random.randint(0, 100) for _ in range(5)]
    
    print("\nPRNG Attack:")
    print("Observed Values:", observed_values)
    print("Predicted Values:", predicted_values)
    print("Match:", observed_values == predicted_values)

predict_next_random()

if __name__ == "__main__":
    print("\nThis script demonstrates OTP encryption and RNG analysis. Use responsibly!")
