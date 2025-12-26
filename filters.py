from datetime import datetime, timedelta

def get_by_user(reminders_list, username):
    """Filtruje przypomnienia należące do konkretnego użytkownika."""
    result=[] #tworzenie listy wynikowej
    for r in user_reminders:
        if r.user == username:
            result.append(r)
    if not result: #jeśli lista jest pusta to zwracamy komunikat
        print(f"Użytkowniku {username}, nie masz żadnych przypomnień\n")

    return result

    

def get_today_reminders(user_reminders, username):
    """Zadanie: Zwróć tylko dzisiejsze przypomnienia."""
    today=datetime.now().date() #ustawianie today jako dzisiejszej daty
    result=[] #tworzenie listy wynikowej
    for r in user_reminders:
        if r.date.date() == today and r.user == username: #jeśli ta data to dzisiaj, to dodaj ją do naszej listy
            result.append(r)
    if not result:
        print(f"Użytkowniku {username}, nie masz przypomnień na dzisiaj\n")

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
        print(f"Użytkowniku {username}, nie masz przypomnień na najbliższy tydzień\n")

    return result


def get_next_month_reminders(user_reminders, username):
    """Filtruje przypomnienia dla następny miesiąc (30 dni)."""
    today = datetime.now().date() #ustawianie today jako dzisiejszej daty
    month_later = today + timedelta(days=30) #ustawienie daty miesiąc później
    result=[] #tworzenie listy wynikowej
    for r in user_reminders:
        if today <= r.date.date() <= month_later and r.user == username: #jeśli ta data jest pomiędzy dzisiaj a datą tydzień późniejszą
            result.append(r)
    if not result:
        print(f"Użytkowniku {username}, nie masz przypomnień na najbliższy miesiąc\n")

    return result


def get_day_reminders (user_reminders, username, day):
    """Zwraca przypomnienia z konkretnego dnia."""
    result=[] #tworzenie listy wynikowej
    for r in user_reminders:
        if r.date.date() == day and r.user == username: 
            result.append(r)
    if not result:
        print(f"Użytkowniku {username}, nie masz przypomnień na dzień {day}\n")

    return result



def get_overdue_reminders(user_reminders, username):
    """Zwraca przypomnienia, których termin już minął."""
    today = datetime.now().date()
    result=[]
    for r in user_reminders:
        if r.date.date() < today and r.user==username: #jeśli termin minął
            result.append(r)
    if not result:
        print(f"Użytkowniku {username}, nie masz żadnych zaległych przypomnień\n")

    return result


#nie jestem pewna czy będziemy mieć te kategorie, w razie czego zakomentować
def get_by_category(user_reminders, username, category_name):
    """Zwraca przypomnienia z konkretnej kategorii."""
    result=[]
    for r in user_reminders:
        if r.category == category_name and r.user==username: #jeśli jest ta sama kategoria
            result.append(r)
    if not result:
        print(f"Użytkowniku {username}, nie masz żadnych przypomnień tej kategorii\n")

    return result



def get_summary(user_reminders, username):
    """Wypisuje krótkie podsumowanie dla użytkownika."""
    today_reminders = get_today_reminders(user_reminders, username)
    overdue_reminders_reminders = get_overdue_reminders(user_reminders, username)
    print(f"Użytkowniku {username}, masz {len(today_reminders)} przypomnień do wykonania\n")
    print(f"Użytkowniku {username}, masz {len(overdue_reminders)} zaległych przypomnień\n")
    if overdue_reminders:
        print("Masz zaległości! Sprawdź, co powinieneś nadrobić\n")


