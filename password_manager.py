from password_generator import get_pwd_reqs
from password_generator import generate_password
from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
def view():
    with open("passwords.txt", "r") as file:
        counter = 1
        for line in file.readlines():
            data = line.rstrip()
            company, username, password = data.split("|")
            print(str(counter) + ". " + company + "\n" + "Username:" + username + "\n" + "Password: " + str(fer.decrypt(password.encode()).decode()))
            counter += 1
def add():
    company = input("Name of Company: ")
    username = input("Username: ")
    while True:
        user_choice = input("Would you like to generate or input an entry (generate/input)?: ")
        if user_choice == "generate":
            pwd = generate_password(get_pwd_reqs())
            break
        elif user_choice == "input":
            pwd = input("Password: ")
            break
        else:
            print("Invalid option. Please try again.")
            continue
    with open("passwords.txt", "a") as file:
        file.write(company + "|" + username + "|" + str(fer.encrypt(pwd.encode()).decode()) + "\n")

#set password here
m_password = "password"
while True:
    m_check = input("Master Password: ")
    if m_password == m_check:
        print("Password Accepted.")
        break
    else:
        print("Wrong Password. Please Try Again")

key = load_key() + m_password.encode()
fer = Fernet(key)

while True:
    mode = input("Do you want to add a password, view existing ones, or delete a password (view/add/delete)? [Press q to quit]: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode. Please try again.")
        continue














