import user
import sys
from user import *

PROMPT = "-->"

def show_main_menu():
    print("\n--- SYSTEM PRZYPOMNIEŃ ---")
    print("1. Zaloguj się")
    print("2. Zarejestruj się")
    print("3. Wyjdź")

def show_user_menu(username):
    print(f"\nZalogowany jako: {username}")
    print("0. Wyloguj się")
	print("1. Edytuj listę przypomnień")
	print("2. Wyświetl przypomnienia")

######################################
def output_message(prompt):
	if (prompt != ""):
		print(prompt)
def get_input(prompt):
	output_message(prompt)
	return input(PROMPT)
######################################

def main_menu_action(all_reminders, all_users):
	liczba = int(get_input(""))
	if liczba == 1:
		username = get_input("Nazwa użytkownika")
		password = get_input("Hasło")
		err = login_user(username, password, all_users)
		if err:
			print("Nie ma takiego użytkownika lub hasło jest błędne")
			return None
		else:
			return username
	elif liczba == 2:
		username = get_input("Nazwa nowego użytkownika")
		password1 = get_input("Hasło")
		password2 = get_input("Potwierdź Hasło")
		if password1 != password2:
			print("Wprowadzone hasła różnią się")
		else:
			register_user(username, password1, all_users)
	elif liczba == 3:
		sys.exit(0)
	else:
		print("Wprowadź 1, 2 lub 3")
	return None

def user_menu_action(username):
	show_user_menu(username)
	#costam dalej
