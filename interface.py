def show_main_menu():
    print("\n--- SYSTEM PRZYPOMNIEŃ ---")
    print("1. Zaloguj się")
    print("2. Zarejestruj się")
    print("3. Wyjdź")

def show_user_menu(username):
    print(f"\nZalogowany jako: {username}")
    print("1. Dodaj przypomnienie")
    print("2. Wyświetl dzisiejsze")
    print("3. Wyświetl wszystkie")
    print("4. Instrukcja (Help)")
    print("5. Wyloguj")

def get_input(prompt):
    return input(prompt)