import password_generator


pwd = input("What is the master password? ")
mode = input("Do you want to add password or view existing ones (view/add)? [Press q to quit.] ").lower()

def view():
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            data = print(line.rstrip())
            username, password, website = data.split("|")
            print("Website/Company: "+ website + "Username:" + username +"\n" + "Password: " + password)
def add():
    company = input("Name of Company: ")
    username = input("Username: ")
    pwd = input("Password")

    with open("passwords.txt", "a") as file:
        file.write(username + "|" + pwd + + company + "\n")


while True:
    if mode == "q":
        break
    elif mode == "pass":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid Mode. Please try again.")
        continue
    m_username = input("Master Username: ")
    m_pwd = input("Master Password: ")












