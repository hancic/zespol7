from datetime import datetime
import uuid

from models import Reminder
from storage import save_reminders


def add_reminder(reminders_list, text, due_date_obj, category, username):
    """Tworzy, dodaje i zapisuje nowe przypomnienie do listy."""

    if not reminders_list:
        new_id = 1
    else:
        new_id = max(int(r.id) for r in reminders_list) + 1

    reminder = Reminder(
        id=new_id,
        user=username,
        text=text,
        category=category,
        due_date=due_date_obj
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

def edit_reminder(reminders_list, reminder_id, new_text=None, new_date_obj=None, new_category=None):
    """Aktualizuje pola już istniejącego przyomnienia, a więc tekst, datę i kategorię."""
    for r in reminders_list:
        if r.id == reminder_id:
           if new_text is not None:
              r.text = new_text
           if new_date_obj is not None:
              r.due_date = new_date_obj
           if new_category is not None:
              r.category = new_category

           save_reminders(reminders_list)
           return r
    return None
