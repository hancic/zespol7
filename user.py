import hashlib

def hash_password(password: str) -> str:
    """Zamienia jawne hasło na bezpieczny skrót (hash)."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password, users_list):
    """
    Zadanie:
    1. Sprawdź, czy użytkownik już istnieje w users_list.
    2. Jeśli nie, stwórz hash hasła używając hash_password().
    3. Stwórz obiekt User i dodaj go do listy.
    """
    pass

def login_user(username, password, users_list):
    """
    Zadanie:
    1. Znajdź użytkownika o podanym username.
    2. Zahashuj podane przez niego hasło.
    3. Sprawdź, czy wygenerowany hash jest taki sam jak ten zapisany w obiekcie User.
    """
    return False