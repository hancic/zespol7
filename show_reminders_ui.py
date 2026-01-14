import filters
import user_interaction
import filters
from filters import *
from user_interaction import *
from filters import *

def show_show_reminders_menu():
	print("0. Wyjdź do menu użytkownika")
	print("1. Wyświetl wszystkie swoje powiadomienia")
	print("2. Wyświetl powiadomienia na dzisiaj")
	print("3. Wyświetl powiadomienia na następny tydzień")
	print("4. Wyświetl powiadomienia na następny miesiąc")
	print("5. Wyświetl powiadomienia na dany dzień")
	print("6. Wyświetl zaległe powiadomienia")
	print("7. Wyświetl powiadomienia z daną frazą występującą w komentarzu")
	print("wpisz \"help\" aby wyświetlić powyższą listę")

def show_reminders(username, user_reminders):
	user_reminders = filters.get_by_user(all_reminders, username)
	show_show_reminders_menu()
	while True:
		res = []
		inp = get_input()
		while inp.lower() == "help":
			show_show_reminders_menu()
			inp = get_input()
		liczba = int(inp)
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
			due_date = get_date("Data w formacie DD-MM-RRRR")
			day = due_date.date()
			res = get_day_reminders(user_reminders, username, day)
		elif liczba == 6:
			res = get_overdue_reminders(user_reminders, username)
		elif liczba == 7:
			pattern = get_input("Wpisz frazę, której szukasz")
			res = search_reminders(user_reminders, username, pattern)
		
		if res != []:
			a = get_input("Czy chcesz wyświetlić powiadomienia w kolejności chronologicznej? [t/N]")
			if a.lower() == "t":
				res = sort_by_date(res)

		output_reminder_list(res)
