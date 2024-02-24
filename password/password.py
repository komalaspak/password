import random
import string

def generate_password(length):
    # Define characters for password generation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user for password length
        length = int(input("Enter the desired length of the password: "))

        # Check if the length is valid
        if length <= 0:
            print("Password length should be a positive integer.")
            return

        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
