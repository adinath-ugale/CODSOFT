import random
import string

print("_-_- SMIPLE PASSWORD GENERATOR -_-_")

length = int(input("Enter password length: "))

print("Include in password:")
letters = input("Letters? (y/n): ").lower()
digits = input("Numbers? (y/n): ").lower()
symbols = input("Symbols? (y/n): ").lower()

characters = ""

if letters == 'y':
    characters += string.ascii_letters
if digits == 'y':
    characters += string.digits
if symbols == 'y':
    characters += string.punctuation

if characters == "":
    print("Error! Select at least one option.")
else:
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Your Strong Password:", password)
