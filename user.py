import hashlib
from models import *

def hash_password(password: str) -> str:
    """Zamienia jawne hasło na bezpieczny skrót (hash)."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password, users_list):
    for user in users_list:
        if user.username == username: #użytkownik o tej nazwie już istnieje
            return False
    password_hashed = hash_password(password)
    user = User(
        username=username,
        password_hash=password_hashed
    )
    users_list.append(user)
    return True

def login_user(username, password, users_list):
    for user in users_list:
        if user.username == username:
            if hash_password(password) == user.password_hash:
                return user
            else:
                return None
    return None