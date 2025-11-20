import random
import string

def generate_password():
    print("--- Random Password Generator ---")

    while True:
        try:
            length = int(input("Enter password length (min 4): "))
            if length >= 4:
                break
            print("Length must be at least 4.")
        except ValueError:
            print("Please enter a valid number.")


    use_upper = input("Include Uppercase letters? (y/n): ").lower().startswith('y')
    use_lower = input("Include Lowercase letters? (y/n): ").lower().startswith('y')
    use_digits = input("Include Numbers? (y/n): ").lower().startswith('y')
    use_symbols = input("Include Symbols? (y/n): ").lower().startswith('y')

    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        print("\n[!] Error: You must select at least one character type.")
        return

    password = []
    
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(char_pool))

    random.shuffle(password)
    
    final_password = "".join(password)

    print(f"\nGenerated Password: {final_password}")
    print("-" * 30)

if __name__ == "__main__":
    generate_password()