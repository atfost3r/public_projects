#! python3

# This script should take the input from the user and then check for strength

import pyperclip, re

# Get up strong Password Regex Tests
alphaRegex = re.compile(r"[a-z]")
alphaCapitalRegex = re.compile(r"[A-Z]")
numRegex = re.compile(r"[0-9]")

# Get password
# TODO: Possibly add an option to type in the password
password = str(pyperclip.paste())
strong = [
    False,
    False,
    False,
]  # This set up a test where as each criteria is met, the value will be flipped to True

# Check that password is strong
if len(password) >= 8:
    if alphaRegex.findall(password) != []:  # Test for lowercase letters
        strong[0] = True
    else:
        print("Your password needs some lowercase letters.")

    if alphaCapitalRegex.findall(password) != []:  # Test for capital letters
        strong[1] = True
    else:
        print("Your password needs a capital letter.")

    if numRegex.findall(password) != []:  # Test for numbers
        strong[2] = True
    else:
        print("Your password needs a number.")

else:
    print("Your password is not long enough.")


# Tell the user that their password sucks or not
if all(strong) == True:
    print("This is one strong password!")
else:
    print("Your password does not meet the above criteria.")
