import hashlib
from models import *

def hash_password(password: str) -> str:
    """Zamienia jawne hasło na bezpieczny skrót (hash)."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password, users_list):
    for user in users_list:
        if user.username == username: #użytkownik o tej nazwie już istnieje
            return []
    password_hashed = hash_password(password)
    user = User(
        username=username,
        password_hash=password_hashed
    )
    users_list.append(user)
    return users_list

def login_user(username, password, users_list):
    user = None
    for u in users_list:
        if u.username == username:
            user = u
            break
    if user == None: #nie znaleziono użytkownika o tej nazwie
        return False
    elif hash_password(password) == user.password_hash:
            return True
    return False