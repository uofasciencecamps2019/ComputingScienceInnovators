#!/usr/bin/env python3

"""
File: caesar_template.py
Name:

Description:
Sources:

** The only functions you should be modifying are encrypt() and decrypt() **
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"


def main():
    original = input("Enter a message to encrypt: ")
    n = 5

    ciphertext = encrypt(n, original)
    plaintext = decrypt(n, ciphertext)

    print()
    print("Original message:", original)
    print("Encoded message: ", ciphertext)
    print("Decoded message: ", plaintext)
    print()


# Iterate through the plaintext and call shift() on each character to encode
# Parameters: n (value to shift by), plaintext (decoded text to encode)
# Return: ciphertext (encoded text)
def encrypt(n, plaintext):
    # Code here


# Iterate through the plaintext and call shift() on each character to decode
# Parameters: n (value to shift by), ciphertext (encoded text to decode)
# Return: plaintext (decoded text)
def decrypt(n, ciphertext):
    # Code here


# Takes a string of a single character and encodes or decodes it according to it's index in <key>
# Parameters: char (string of single character), n (value to shift by), mode (e for encode, d for decode)
def shift(char, n, mode):
    if mode.lower().startswith("e"):
        try:
            return alphabet[(alphabet.index(char) + n) % 26]
        except ValueError:
            return char

    elif mode.lower().startswith("d"):
        try:
            return alphabet[(alphabet.index(char) - n) % 26]
        except ValueError:
            return char

    else:
        print("ERROR: Invalid mode selected")


if __name__ == "__main__":
    main()
