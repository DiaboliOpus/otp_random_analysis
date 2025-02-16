# otp_random_analysis
One-Time Pad (OTP) &amp; RNG Security Analysis
One-Time Pad (OTP) & RNG Security Analysis

Overview

This project demonstrates:

One-Time Pad (OTP) encryption and decryption for secure communication.

Comparison of standard PRNG (random) vs cryptographic CSPRNG (secrets, os.urandom) to highlight security differences.

An example attack on PRNG (random) by predicting its sequence when the seed is known.


Features

Secure OTP Encryption: Uses XOR with a truly random key.

PRNG vs CSPRNG Analysis: Demonstrates predictable vs secure randomness.

PRNG Attack Simulation: Shows how an attacker can predict outputs of random if the seed is exposed.


Installation

Clone the repository:

git clone https://github.com/otp_random_analysis/otp-rng-security.git
cd otp-rng-security


Usage

Run the script to see encryption, randomness comparisons, and the PRNG attack demo:

python otp_random_analysis.py


Security Considerations

OTP is only secure if the key is truly random, as long as the message, and never reused.

PRNGs like random are not suitable for cryptographic purposes.

Always use CSPRNGs (secrets, os.urandom) for secure applications.


License

This project is licensed under the MIT License.
