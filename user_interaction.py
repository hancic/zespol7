from models import Reminder

PROMPT = "-->"
def output_message(prompt):
	if (prompt != ""):
		print(prompt)
def get_input(prompt = ""):
	output_message(prompt)
	return input(PROMPT)
def get_date(prompt = ""):
	print("wczytywanie daty nie jest jeszcze wspierane")
	return None
def get_reminder_from_input(username, id = 0):
	r = Reminder(id, username, None, None, None)
	r.text = get_input("Komentarz")
	r.category = get_input("Kategoria")
	r.due_date = get_date("Data")
	if r.text == "":
		r.text = None
	if r.category == "":
		r.category = None
	return r
def output_reminder(r):
	print(f"id: {r.id}")
	print(f"kategoria: {r.category}")
	print(f"data: {r.due_date}")
	print(f"komentarz: {r.text}")
	print("---------------")
def output_reminder_list(reminders):
	if reminders == []:
		print("brak takich powiadomień")
	for r in reminders:
		output_reminder(r)
