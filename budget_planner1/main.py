from utils.menu import show_menu
from accounts.authentication import authenticate_user

def main():
    print("Welcome to Budget Planner")
    user = authenticate_user()
    if user:
        show_menu(user)

if __name__ == "__main__":
    main()
