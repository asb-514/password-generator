#!/usr/bin/env ipython

import string
import random


def generate_password(
    length=12,
    include_digits=True,
    include_punctuation=True,
    include_uppercase=True,
    include_lowercase=True,
):
    characters = ""
    if include_digits:
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase

    if not characters:
        raise ValueError("At least one character type must be included.")

    password = "".join(random.choice(characters) for _ in range(length))
    return password


# User prompts and interaction
print("Welcome to the Secure Password Generator!")
print("Let's create a custom password based on your preferences.")

length = int(input("Enter the desired length of the password: "))
include_digits = input("Include digits? (y/n): ").lower() == "y"
include_punctuation = input("Include punctuation? (y/n): ").lower() == "y"
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"

try:
    generated_password = generate_password(
        length=length,
        include_digits=include_digits,
        include_punctuation=include_punctuation,
        include_uppercase=include_uppercase,
        include_lowercase=include_lowercase,
    )
    print("Generated Password:", generated_password)
except ValueError as e:
    print("Error:", str(e))
