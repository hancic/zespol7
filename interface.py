import user_interaction
from user_interaction import *
import edit_reminders_ui
import show_reminders_ui
import user
import sys
from user import *
from show_reminders_ui import *
from edit_reminders_ui import *

def show_main_menu():
	print("\n--- SYSTEM PRZYPOMNIEŃ ---")
	print("0. Wyjdź")
	print("1. Zaloguj się")
	print("2. Zarejestruj się")

def show_user_menu(username):
	print(f"\nZalogowany jako: {username}")
	print("0. Wyloguj się")
	print("1. Edytuj listę przypomnień")
	print("2. Wyświetl przypomnienia")


def user_menu_action(username, all_reminders):
	user_reminders = filters.get_by_user(all_reminders, username)
	while True:
		show_user_menu(username)
		liczba = int(get_input(""))
		if liczba == 0:
			return None
		elif liczba == 1:
			edit_reminders(username, user_reminders)
		elif liczba == 2:
			show_reminders(username, user_reminders)

#####################################################################

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
	elif liczba == 0:
		sys.exit(0)
	else:
		print("Wprowadź 0, 1 lub 2")
	return None
