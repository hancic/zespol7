from datetime import datetime
import uuid

from models import Reminder
from storage import save_reminders


def add_reminder(reminders_list, text, date_str, category, username):
    """Zadanie: Stwórz i dodaj nowe przypomnienie do listy."""
    due_date = datetime.fromisoformat(date_str)

    reminder = Reminder(
        id=str(uuid.uuid4()),
        user=username,
        text=text,
        category=category,
        due_date=due_date
    )

    reminders_list.append(reminder)
    save_reminders(reminders_list)
    return reminder

def delete_reminder(reminders_list, reminder_id):
    """Zadanie: Usuń wybrane przypomnienie z listy."""
    for i, r in enumerate(reminders_list):
        if r.id == reminder_id:
            removed = reminders_list.pop(i)
            save_reminders(reminders_list)
            return removed
    return None

def edit_reminder(reminders_list, reminder_id, new_text=None, new_date=None, new_category=None):
    """
    Zadanie:
    1. Znajdź w liście przypomnienie o konkretnym ID.
    2. Jeśli użytkownik podał nową treść (new_text nie jest None), zaktualizuj pole w obiekcie.
    3. To samo zrób dla daty i kategorii.
    """
    for r.id == reminder.id:
        if new_text is not None:
            r.text = new_text

        if new_date is not None:
            r.due_date = datetime.fromisoformat(new_date)

        if new_category is not None:
            r.category = new_category

        save_reminders(reminders_list)
        return r
   return None
