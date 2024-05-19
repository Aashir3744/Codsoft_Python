import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    while True:
        print("\nPassword Generator")
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer value.")
            continue

        password = generate_password(length)
        print(f"Generated Password: {password}")

        # Ask the user if they want to generate another password
        choice = input("Do you want to generate another password? (yes/no): ").lower()
        if choice != 'yes':
            print("Exiting Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
