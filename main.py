import models
import storage
import user
import logic
import filters
import interface

def main():
	# Wczytanie danych z bazy
	all_reminders = storage.load_reminders()
	all_users = storage.load_users()
	current_user = None
	# Wczytanie danych z bazy
	all_reminders = storage.load_reminders()
	all_users = storage.load_users()
	current_user = None

	while True:
		if not current_user:
			interface.show_main_menu()
			# Tu dodasz logikę logowania/rejestracji
			current_user = interface.main_menu_action(all_reminders, all_users)
		else:
			current_user = interface.user_menu_action(current_user, all_reminders)

if __name__ == "__main__":
	main()
