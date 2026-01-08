import user
import sys
from user import *

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

def main_menu_action(all_reminders, all_users):
	liczba = int(get_input("-->"))
	if liczba == 1:
		username = get_input("Nazwa użytkownika\n-->")
		password = get_input("Hasło\n-->")
		err = login_user(username, password, all_users)
		if err:
			print("Nie ma takiego użytkownika lub hasło jest błędne")
			return None
		else:
			return username
	elif liczba == 2:
		username = get_input("Nazwa nowego użytkownika\n-->")
		password1 = get_input("Hasło\n-->")
		password2 = get_input("Potwierdź Hasło\n-->")
		if password1 != password2:
			print("Wprowadzone hasła różnią się\n")
		else:
			register_user(username, password, all_users)
	elif liczba == 3:
		sys.exit(0)
	else:
		print("Wprowadź 1, 2 lub 3")
	return None
