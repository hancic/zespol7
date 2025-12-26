from datetime import datetime, timedelta

def get_by_user(reminders_list, username):
    """Filtruje przypomnienia należące do konkretnego użytkownika."""
    return [r for r in reminders_list if r.user == username] #pętla po nazwach użytkownika jeśli jest równa naszemu użytkownikowi to zwróć ten punkt

def get_today_reminders(user_reminders, username):
    """Zadanie: Zwróć tylko dzisiejsze przypomnienia."""
    today=datetime.now().date() #ustawianie today jako dzisiejszej daty
    result=[] #tworzenie listy wynikowej
    for r in user_reminders:
        if r.date.date() == today and r.user == username: #jeśli ta data to dzisiaj, to dodaj ją do naszej listy
            result.append(r)
    if not result:
        print(f"Użytkowniku {username}, nie masz przypomnień na dzisiaj")

    return result

def get_next_week_reminders(user_reminders, username):
    """Zadanie: Zwróć tylko przypomnienia na kolejny tydzień."""
    today = datetime.now().date() #ustawianie today jako dzisiejszej daty
    week_later = today + timedelta(days=7) #ustawienie daty tydzień później
    result=[] #tworzenie listy wynikowej
    for r in user_reminders:
        if today <= r.date.date() <= week_later and r.user == username: #jeśli ta data jest pomiędzy dzisiaj a datą tydzień późniejszą
            result.append(r)
    if not result:
        print(f"Użytkowniku {username}, nie masz przypomnień na najbliższy tydzień")

    return result


def get_reminders_by_month(user_reminders, username):
    """Filtruje przypomnienia dla obecnego miesiąca."""

def get_overdue_reminders(user_reminders, username):
    """Zwraca przypomnienia, których termin już minął."""

def get_by_category(user_reminders, username, category_name):
    """Zwraca przypomnienia z konkretnej kategorii (np. 'Praca', 'Dom')."""

def get_summary(user_reminders, username):
    """Wypisuje krótkie podsumowanie dla użytkownika."""

def get_day_reminders (user_reminders, username, day)
    """Zwraca przypomnienia z konkretnego dnia."""
