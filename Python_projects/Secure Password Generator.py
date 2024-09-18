import random
import string

def generate_password(length=12, include_numbers=True, include_symbols=True, include_uppercase=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the desired password length: "))
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, include_numbers, include_symbols, include_uppercase)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
