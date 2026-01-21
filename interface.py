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
	print("3. Usuń konto")


def user_menu_action(username, all_reminders, all_users):
	while True:
		user_reminders = filters.get_by_user(all_reminders, username)
		show_user_menu(username)
		liczba = get_int_input()
		if liczba == 0:
			return None
		elif liczba == 1:
			edit_reminders(username, user_reminders, all_reminders)
		elif liczba == 2:
			show_reminders(username, user_reminders)
		elif liczba == 3:
			potwierdzenie = get_input("Czy na pewno chcesz usunąć konto? Wszystkie dane znikną! (t/N)")
			if potwierdzenie.lower() == 't':
				delete_all_user_reminders(all_reminders, username)
				delete_user(username, all_users)
				print(f"Konto użytkownika {username} zostało usunięte.")
				return None

#####################################################################

def main_menu_action(all_reminders, all_users):
	liczba = get_int_input()
	if liczba == 1:
		username = get_input("Nazwa użytkownika")
		password = get_input("Hasło")
		err = login_user(username, password, all_users)
		if err == None:
			print("Nie ma takiego użytkownika lub hasło jest błędne")
			return None
		else:
			return username
	elif liczba == 2:
		username = get_input("Nazwa nowego użytkownika")
		if any(u.username == username for u in all_users):
			print("Nazwa użytkownika jest już zajęta. Wybierz inną")
			return None
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
