import user_interaction
import filters
from filters import *
from user_interaction import *

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
			pattern = get_input("Wpisz frazę, której szukasz")
			res = search_reminders(user_reminders, username, pattern)
		
		if res != []:
			a = get_input("Czy chcesz wyświetlić powiadomienia w kolejności chronologicznej? [t/N]")
			if a.lower == "t":
				res = sort_by_date(res)

		output_reminder_list(res)

