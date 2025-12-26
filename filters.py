from datetime import datetime, timedelta

def get_by_user(reminders_list, username):
    """Filtruje przypomnienia należące do konkretnego użytkownika."""
    return [r for r in reminders_list if r.user == username] #pętla po nazwach użytkownika jeśli jest równa naszemu użytkownikowi to zwróć ten punkt

def get_today_reminders(user_reminders):
    """Zadanie: Zwróć tylko dzisiejsze przypomnienia."""
    today=datetime.now().date() #ustawianie today jako dzisiejszej daty
    result=[] #tworzenie listy wynikowej
    for r in user_reminders:
        if r.date.date() == today: #jeśli ta data to dzisiaj, to dodaj ją do naszej listy
            result.append(r)

    return result
