import random
import string

def generate_password(min_length = 7, max_length = 16, numbers = True, special_characters = True):
    # populate variables with associated ASCII characters
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    characters = letters
    #conditionals to decide what characters are required/allowed for the password
    if numbers:
        characters += digits
    if special_characters:
        characters += specials

    #initalizing variables to create password string render the checks on the criteria given
    password = ""
    meets_requirements = False
    has_number = False
    has_special = False

    while not meets_requirements or len(password) < min_length:
        new_char = random.choice(characters)
        if new_char in digits:
            has_number = True
        elif new_char in specials:
            has_special = True
        meets_requirements = True

        if numbers:
            meets_requirements = has_number
        if special_characters:
            meets_requirements = meets_requirements and has_special




