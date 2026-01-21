from datetime import datetime, timedelta



def get_by_user(reminders_list, username):
    """Filtruje przypomnienia należące do konkretnego użytkownika."""
    result=[] #tworzenie listy wynikowej
    for r in reminders_list:
        if r.user == username:
            result.append(r)
   
    return result



def get_today_reminders(user_reminders, username):
    """Zadanie: Zwróć tylko dzisiejsze przypomnienia."""
    today=datetime.now().date() #ustawianie today jako dzisiejszej daty
    result=[] #tworzenie listy wynikowej
    for r in user_reminders:
        if r.due_date.date() == today and r.user == username: #jeśli ta data to dzisiaj, to dodaj ją do naszej listy
            result.append(r)

    return result


def get_next_week_reminders(user_reminders, username):
    """Zadanie: Zwróć tylko przypomnienia na kolejny tydzień."""
    today = datetime.now().date() #ustawianie today jako dzisiejszej daty
    week_later = today + timedelta(days=7) #ustawienie daty tydzień później
    result=[] #tworzenie listy wynikowej
    for r in user_reminders:
        if today <= r.due_date.date() <= week_later and r.user == username: #jeśli ta data jest pomiędzy dzisiaj a datą tydzień późniejszą
            result.append(r)

    return result


def get_next_month_reminders(user_reminders, username):
    """Filtruje przypomnienia dla następny miesiąc (30 dni)."""
    today = datetime.now().date() #ustawianie today jako dzisiejszej daty
    month_later = today + timedelta(days=30) #ustawienie daty miesiąc później
    result=[] #tworzenie listy wynikowej
    for r in user_reminders:
        if today <= r.due_date.date() <= month_later and r.user == username: #jeśli ta data jest pomiędzy dzisiaj a datą tydzień późniejszą
            result.append(r)

    return result


def get_day_reminders (user_reminders, username, day):
    """Zwraca przypomnienia z konkretnego dnia."""
    result=[] #tworzenie listy wynikowej
    for r in user_reminders:
        if r.due_date.date() == day and r.user == username: 
            result.append(r)
    
    return result



def get_overdue_reminders(user_reminders, username):
    """Zwraca przypomnienia, których termin już minął."""
    today = datetime.now().date()
    result=[]
    for r in user_reminders:
        if r.due_date.date() < today and r.user==username: #jeśli termin minął
            result.append(r)
    return result


#nie jestem pewna czy będziemy mieć te kategorie, w razie czego zakomentować
def get_by_category(user_reminders, username, category_name):
    """Zwraca przypomnienia z konkretnej kategorii."""
    result=[]
    for r in user_reminders:
        if r.category == category_name and r.user==username: #jeśli jest ta sama kategoria
            result.append(r)
    return result



def search_reminders(user_reminders, username, query):
    """Wyszukuje przypomnienia zawierające konkretną frazę w treści."""
    result=[]
    for r in user_reminders:
        #.lower() zamienia na małe litery
        if r.text == None: #AttributeError: 'NoneType' object has no attribute 'lower' :)
            continue
        if query.lower() in r.text.lower() and r.user==username:
            result.append(r)
   
    return result


def sort_by_date(user_reminders):
    """Sortuje przypomnienia chronologicznie."""
    return sorted(user_reminders, key=lambda r: r.due_date.date())


