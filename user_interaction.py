from datetime import datetime
from models import Reminder

PROMPT = "-->"
def output_message(prompt):
	if (prompt != ""):
		print(prompt)
def get_input(prompt = ""):
	output_message(prompt)
	return input(PROMPT)
def get_int_input(prompt = ""):
    """Pobiera liczbę od użytkownika, dopóki nie poda on poprawnej wartości."""
    while True:
        try:
            # Próbujemy zamienić tekst na liczbę
            return int(get_input(prompt))
        except ValueError:
            # Jeśli się nie uda (np. wpisano literę), wyświetlamy komunikat
            print("To nie jest liczba! Wprowadź cyfrę odpowiadającą opcji w menu.")

def get_date(prompt = ""):
    """Pobiera datę i prosi o ponowienie, jeśli format jest błędny."""
    while True:
        due_date_str = get_input(prompt)
        if due_date_str == "":
            return None
        try:
            # Sprawdzamy, czy format pasuje do DD-MM-RRRR
            due_date = datetime.strptime(due_date_str, "%d-%m-%Y")
            return due_date
        except ValueError:
            # Jeśli format jest zły (np. kropki zamiast myślników), nie crashujemy programu
            print("Błędny format daty! Proszę użyć formatu DD-MM-RRRR (np. 21-01-2026).")
def get_reminder_from_input(username, id = 0):
	r = Reminder(id, username, None, None, None)
	r.text = get_input("Komentarz")
	r.category = get_input("Kategoria")
	r.due_date = get_date("Data w formacie DD-MM-RRRR")
	if r.text == "":
		r.text = None
	if r.category == "":
		r.category = None
	return r
def output_reminder(r):
	print(f"id: {r.id}")
	print(f"kategoria: {r.category}")
	print(f"data: {r.due_date.strftime('%d-%m-%Y')}")
	print(f"komentarz: {r.text}")
	print("---------------")
def output_reminder_list(reminders):
	if reminders == [] :
		print("brak takich powiadomień")
	for r in reminders:
		output_reminder(r)
