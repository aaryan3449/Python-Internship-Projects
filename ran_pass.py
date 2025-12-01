import random
import string

print("---- Password Generator ----")

try:
    length = int(input("Enter password length: "))

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    print("Your Password:", password)

except:
    print("Please enter a valid number.")
