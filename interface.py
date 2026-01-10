import filters
import user
import sys
from user import *
from filters import *

######################################
PROMPT = "-->"
def output_message(prompt):
	if (prompt != ""):
		print(prompt)
def get_input(prompt):
	output_message(prompt)
	return input(PROMPT)
######################################

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

def show_show_reminders_menu():
	print("0. Wyjdź do menu użytkownika")
	print("1. Wyświetl wszystkie swoje powiadomienia")
	print("2. Wyświetl powiadomienia na dzisiaj")
	print("3. Wyświetl powiadomienia na następny tydzień")
	print("4. Wyświetl powiadomienia na następny miesiąc")
	print("5. Wyświetl powiadomienia na dany dzień")
	print("6. Wyświetl zaległe powiadomienia")
	print("7. Wyświetl powiadomienia z daną frazą występującą w komentarzu")
	return int(get_input(""))

def output_reminder(r):
	print(f"kategoria: {r.category}")
	print(f"data: {r.due_date}")
	print(f"komentarz: {r.text}")
	print("---------------")
def output_reminder_list(reminders):
	if reminders == []:
		print("brak takich powiadomień")
	for r in reminders:
		output_reminder(r)

def show_reminders(username, user_reminders):
	while True:
		res = []
		liczba = show_show_reminders_menu()
		if liczba == 0:
			return
		elif liczba == 1:
			res = get_by_user(user_reminders, username)
		elif liczba == 2:
			res = get_today_reminders(user_reminders, username)
		elif liczba == 3:
			res = get_next_week_reminders(user_reminders, username)
		elif liczba == 4:
			res = get_next_month_reminders(user_reminders, username)
		elif liczba == 5:
			#pierdu pierdu z datami + instrukcje dla użytkownika
			print("nie jest to jeszcze gotowe")
			continue
		elif liczba == 6:
			res = get_overdue_reminders(user_reminders, username)
		elif liczba == 7:
			#szukanie frazy + instrukcje dla użytkownika
			print("nie jest to jeszcze gotowe")
			continue
		
		if res != []:
			a = get_input("Czy chcesz wyświetlić powiadomienia w kolejności chronologicznej? [t/N]")
			if a.lower == "t":
				res = sort_by_date(res)

		output_reminder_list(res)

def edit_reminders(username, user_reminders):
	print("nie jest to jeszcze gotowe")

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
