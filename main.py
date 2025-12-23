import datetime
from models import *
from storage import *
import user
import logic
import filters
import interface

def main():
    # Wczytanie danych z bazy
    #all_reminders = storage.load_data()
    current_user = None
    while True:
        if not current_user:
            interface.show_main_menu()
            # Tu dodasz logikę logowania/rejestracji
            break # Tymczasowe zatrzymanie pętli
        else:
            interface.show_user_menu(current_user)
            # Tu dodasz obsługę komend użytkownika
            break

if __name__ == "__main__":
    main()