from datetime import datetime
import uuid

from models import Reminder
from storage import save_reminders


def add_reminder(reminders_list, text, date_str, category, username):
    """Tworzy, dodaje i zapisuje nowe przypomnienie do listy."""
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
    """Usuwa przypomnienie z listy po ID."""
    for i, r in enumerate(reminders_list):
        if r.id == reminder_id:
            removed = reminders_list.pop(i)
            save_reminders(reminders_list)
            return removed
    return None

def edit_reminder(reminders_list, reminder_id, new_text=None, new_date=None, new_category=None):
    """Aktualizuje pola już istniejącego przyomnienia, a więc tekst, datę i kategorię."""
    for r in reminders_list:
        if r.id == reminder_id:
           if new_text is not None:
              r.text = new_text
           if new_date is not None:
              r.due_date = datetime.fromisoformat(new_date)
           if new_category is not None:
              r.category = new_category

           save_reminders(reminders_list)
           return r
    return None
