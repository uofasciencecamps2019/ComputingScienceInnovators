#!/usr/bin/env python3

"""
File: substitution_template.py
Name:

Description:
Sources:
"""

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"


def main():
    key = make_key(alphabet)
    
    original = input("Enter word or phrase to encrypt: ").lower()
    ciphertext = encrypt(original, key)
    plaintext = decrypt(ciphertext, key)

    print()
    print("Original text: ", original)
    print("Encrypted text:", ciphertext)
    print("Decrypted text:", plaintext)
    print()

# Takes a plaintext message and a key and encodes it
# Parameters: text (plaintext message), key (what you're encoding according to)
# Return: ciphertext (encoded message)
def encrypt(text, key):
    # Code here


# Takes a ciphertext message and a key and decodes it
# Parameters: text (ciphertext message), key (what you're decoding according to)
# Return: plaintext (decoded message)
def decrypt(text, key):
    # Code here


# Shuffling the alphabet to make a random key
# Parameter: alphabet (the alphabet in a string)
# Return: the randomly shuffled alphabet to be used as a key
def make_key(alphabet):
    shuffled = list(alphabet)
    random.shuffle(shuffled)
    return ''.join(shuffled)


if __name__ == "__main__":
    main()
