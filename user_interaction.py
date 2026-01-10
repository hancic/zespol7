######################################
PROMPT = "-->"
def output_message(prompt):
	if (prompt != ""):
		print(prompt)
def get_input(prompt):
	output_message(prompt)
	return input(PROMPT)
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
######################################

