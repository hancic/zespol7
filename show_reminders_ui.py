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
	print("8. Wyświetl powiadomienia z danej kategorią")
	print("9. Wyświetl listę swoich kategorii")
	print("wpisz \"help\" aby wyświetlić powyższą listę")

def show_reminders(username, user_reminders):
	show_show_reminders_menu()
	while True:
		res = []
		inp = get_input()
		if inp.lower() == "help":
			show_show_reminders_menu()
			continue
		try:
			liczba = int(inp)
		except ValueError:
			print("To nie jest poprawna opcja! Wpisz cyfrę (0-8) lub 'help'.")
		if liczba == 0:
			return
		elif liczba == 1:
			res = user_reminders
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
		elif liczba == 8:
			category_name = get_input("Wpisz kategorię, którą chcesz wypisać")
			res = get_by_category(user_reminders, username, category_name)
		elif liczba == 9:
			categories = get_unique_categories(user_reminders)
			if categories:
				print("Twoje obecne kategorie")
				for cat in categories:
					print (f"- {cat}")
			else:
				print("Nie masz jeszcze przypisanych żadnych kategorii.")
			continue
			
		
		if res != []:
			a = get_input("Czy chcesz wyświetlić powiadomienia w kolejności chronologicznej? [t/N]")
			if a.lower() == "t":
				res = sort_by_date(res)

		output_reminder_list(res)
