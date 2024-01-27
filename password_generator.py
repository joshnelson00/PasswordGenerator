import random
import string

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
    password = ""
    meets_requirements = False
    has_number = False
    has_special = False

    while not meets_requirements or len(password) != length:
        new_char = random.choice(characters)
        password += new_char
        if new_char in digits:
            has_number = True
        elif new_char in specials:
            has_special = True
        meets_requirements = True

        if numbers:
            meets_requirements = has_number
        if special_characters:
            meets_requirements = meets_requirements and has_special

        if meets_requirements:
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


reqs = get_pwd_requirements()


password = generate_password(reqs)
print(password)

