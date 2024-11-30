import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

try:
    length = int(input("Enter the number of characters for the password: "))
    if length > 0:
        print("Your generated password is:", generate_password(length))
    else:
        print("Please enter a positive number.")
except ValueError:
    print("Please enter a valid number.")
