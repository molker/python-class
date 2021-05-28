# Exercise Password Validation

import re


def checkStrength(password):
    noSymbol = re.compile(r"[$%#@]+").search(password) is None
    noCaps = re.compile(r"[A-Z]+").search(password) is None
    if noSymbol:
        print('\tNo special characters detected.')
    if noCaps:
        print('\tNo capital letters detected.')
    if not noCaps and not noSymbol:
        print('Good job! You\'ve picked a strong password')
    else:
        print('\tConsider adding some to strengthen your password.')


# at least 8 char long
# contains any sort letters, numbers, $%#@
# if you want to make sure it ends with a number, put \d after {8,}
pattern = re.compile(r"^[a-zA-Z0-9$%#@]{8,}$")
guess = input('Please enter your desired password:\t')

if pattern.search(guess) is not None:
    print('valid password')
    # Suggestions
    checkStrength(guess)
else:
    # Reasons it could've been rejected
    if len(guess) < 8:
        print('Password must be at least 8 characters long')
    else:
        print('Password contained illegal symbols')
