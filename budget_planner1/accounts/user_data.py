import os

USER_DATA_FILE = "data/users.txt"

def load_users():
    
    if not os.path.exists("data"):
        os.makedirs("data")
    
    
    if not os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "w") as file:
            pass  
    
    users = {}
    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            username, hashed_password = line.strip().split(":")
            users[username] = {"password": hashed_password}
    return users

def save_users(users):
    with open(USER_DATA_FILE, "w") as file:
        for username, data in users.items():
            file.write(f"{username}:{data['password']}\n")
