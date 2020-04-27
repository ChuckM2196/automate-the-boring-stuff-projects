#! python3
# Goal: Function that uses regular expressions to make sure the password string is strong
import re
# Program will run in a loop until you quit


while True:
    password = input("Input a desired password: ")
    if password == 'q':
        exit()
    elif password == 'quit':
        exit()
    else:
        print("checking password")
# Check password requirements
    # Minimum 8 characters
    if len(password) >= 8:
        print("Password meets the length requirements")

        # Checks for lowercase
        passwordRegex = re.compile(r'[a-z]')
        if passwordRegex.search(password):
            print("Contains atleast one lowercase letter")
        else:
            print("Doesn't contain atleast one lowercase letter")

        # Checks for uppercase
        passwordRegex = re.compile(r'[A-Z]+')
        if passwordRegex.search(password):
            print("Contains atleast one uppercase letter")
        else:
            print("Doesn't contain atleast one uppercase letter")

        # Checks for numbers
        passwordRegex = re.compile(r'[0-9]+')
        if passwordRegex.search(password):
            print("Contains atleast one number")
        else:
            print("Doesn't contain atleast one number")

        # Checks for special characters
        passwordRegex = re.compile(r'[!@#$%^&*()_+]+')
        if passwordRegex.search(password):
            print("Contains atleast one special character")
        else:
            print("Doesn't contain atleast one special character")

    else:
        print("Password is less than 8 characters and does not meet the recommended complexity requirements")
        exit()







