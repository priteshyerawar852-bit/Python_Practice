users ={}

def register():
    username=input("enter a username: ")

    if username in users:
        print("user already exits!")

    else:
        password=input("enter a password: ")
        users[username]=password
        print("succesfull")

def login():
    username = input("enter a username: ")
    password=input("enter a password: ")

    if username in users and users[username]==password:
        print("login successful")

    else:
        print("Inavalid Username or password")

while True:
    print("\n----- MENU -----")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = int(input("enter a choice: "))

    if choice ==1:
        register()
    elif choice ==2:
        login()
    elif choice==3:
        print("thankyu")

    else:
        print("invalid choice")
        