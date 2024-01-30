import random
import string
from random import seed
from random import randint
def generate_password(reqs):
    min_length = reqs[0]
    max_length = reqs[1]
    numbers = reqs[2]
    special_characters = reqs[3]
    length = random.randint(min_length, max_length)
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
    meets_requirements = False
    has_number = False
    has_special = False
    num = randint(min_length, max_length)
    counter = 0
    while True:
        password = ""
        for i in range(num):
            new_char = random.choice(characters)
            password += new_char
        if numbers and special_characters:
            for i in range(num):
                if password[i] in digits:
                    has_number = True
                if password[i] in specials:
                    has_special = True
            if has_number and has_special:
                meets_requirements = True
        elif numbers:
            for i in range(num):
                if password[i] in digits:
                    has_number = True
                    meets_requirements = True
        elif special_characters:
            for i in range(num):
                if password[i] in specials:
                    has_special = True
                    meets_requirements = True
        else:
            meets_requirements = True
        if meets_requirements:
            break
    return password



# min_length, max_length, numbers, specials
def get_pwd_requirements():
    while True:
        try:
            min = int(input("Enter an integer for MIN length of password : "))
            break
        except ValueError:
            print("Invalid Character Type. Please Try Again")
    while True:
        try:
            max = int(input("Enter an integer for MAX length of password : "))
            break
        except ValueError:
            print("Invalid Character Type. Please Try Again")

    while True:
        nums_in_pwd = input("Would you like to have numbers in the password (y/n): ")
        if (nums_in_pwd == 'y'):
            nums = True
            break
        elif (nums_in_pwd == 'n'):
            nums = False
            break
        else:
            print("Type 'y' or 'n'. Please Try Again")
    while True:
        special_in_pwd = input("Would you like to have special characters in the password (y/n): ")
        if (special_in_pwd == 'y'):
            specials = True
            break
        elif (special_in_pwd == 'n'):
            specials = False
            break
        else:
            print("Type 'y' or 'n'. Please Try Again")
    return [min, max, nums, specials]

seed(1)

reqs = get_pwd_requirements()

password = generate_password(reqs)
print()
print("Password: " + str(password))

