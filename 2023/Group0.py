import re
   # Function to check password strength 
def check_password_strength(password):
    strength = 0
   # To check length of password is > 8
    if len(password) < 8:
        print("Password is weak. It must be at least 8 characters long.")
        return strength
   # To check password has numeric characters
    if not re.search('[0-9]', password):
        print("Password is weak. It must contain numeric characters.")
        return strength
   # To check password for lower and uppercase characters
    if not re.search('[A-Z]', password) or not re.search('[a-z]', password):
        print("Password is moderate. It should contain both uppercase and lowercase characters.")
        strength = 1
    else:
        strength = 2

    # Return strength score
    return strength

while True:
    password = input("Enter password: ")
    strength = check_password_strength(password)

    if strength == 2:
        print("Password is strong!")
        break
    # If password is not strong enough 
    print("Try again!")
