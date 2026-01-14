import user_interaction
import logic
from user_interaction import *
from logic import *

def show_edit_reminders_menu():
	print("0. Wyjdź do menu użytkownika")
	print("1. Dodaj przypomnienie")
	print("2. Usuń przypomnienia")
	print("3. Edytuj przypomnienie")

def edit_reminders(username, user_reminders, all_reminders):
	while True:
		show_edit_reminders_menu()
		liczba = int(get_input())
		if liczba == 0:
			return
		if liczba == 1:
			print("Wpisz dane nowego przypomnienia (zostaw puste aby nie dodawać")
			r = get_reminder_from_input(username)
			add_reminder(all_reminders, r.text, r.due_date, r.category, username)
		elif liczba == 2:
			to_delete_list = list(map(int, get_input("Wpisz id przypomnień do usunięcia po spacji").split()))
			for reminder_id in to_delete_list:
				delete_reminder(all_reminders, reminder_id)
		elif liczba == 3:
			reminder_id = int(get_input("Wpisz id przypomnienia do edycji"))
			print("Wpisz nowe dane (zostaw puste aby nie zmieniać)")
			r = get_reminder_from_input(username, reminder_id)
			edit_reminder(all_reminders, r.id, r.text, r.due_date, r.category)
