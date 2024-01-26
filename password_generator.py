import random
import string

def generate_password(min_length, max_length = 16, numbers = True, special_characters = True):
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

