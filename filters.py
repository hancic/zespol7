from datetime import datetime, timedelta

def get_by_user(reminders_list, username):
    """Filtruje przypomnienia należące do konkretnego użytkownika."""
    return [r for r in reminders_list if r.user == username]

def get_today_reminders(user_reminders):
    """Zadanie: Zwróć tylko dzisiejsze przypomnienia."""
    pass