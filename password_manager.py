import password_generator
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
    pwd = input("Password: ")
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














