from utils.hashing import hash_password, verify_password
from accounts.user_data import load_users, save_users
from colorama import init, Fore

init()

def authenticate_user():
    users = load_users()
    while True:
        print(Fore.MAGENTA +"__________________________________________________________________")
        print(Fore.BLUE +"\n            * Welcome to Budget Planner *"+ Fore.RESET)
        print(Fore.MAGENTA +"\n1. Login\n2. Register\n3. Exit"+ Fore.RESET)
        choice = input(Fore.GREEN +"Choose an option: "+ Fore.RESET)

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            user = users.get(username)
            if user and verify_password(password, user["password"]):
                print(Fore.GREEN +"")
                print(f"Welcome back, {username} .")
                print(""+ Fore.RESET)
                return username
            else:
                print(Fore.RED +"Invalid credentials. Please try again."+ Fore.RESET)

        elif choice == "2":
            username = input("Choose a username: ")
            if username in users:
                print(Fore.RED +"Username already exists!"+ Fore.RESET)
            else:
                password = input("Choose a password: ")
                users[username] = {"password": hash_password(password)}
                save_users(users)
                print(Fore.GREEN +"Registration successful! You can now log in."+ Fore.RESET)
        
        elif choice == "3":
            print(Fore.MAGENTA +"Goodbye see you next time ."+ Fore.RESET)
            exit()
        else:
            print(Fore.RED +"Invalid option. Please try again."+ Fore.RESET)
