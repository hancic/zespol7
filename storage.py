import json
import os
from models import *

REMINDERS_PATH = "reminders.jsonl"


def load_reminders():
    if not os.path.exists(REMINDERS_PATH) or os.path.getsize(REMINDERS_PATH) == 0:
        return []
    reminders_list = []
    with open(REMINDERS_PATH, "r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue
            item = json.loads(line)
            new_reminder = Reminder(
                id=item.get("id"),
                user=item.get("user"),
                text=item.get("text"),
                category=item.get("category"),
                due_date=item.get("due_date")
            )
            reminders_list.append(new_reminder)
    return reminders_list

def save_reminder(new_reminder):
    with open(REMINDERS_PATH, "a", encoding="utf-8") as file:
        data = {
            "id": new_reminder.id,
            "user": new_reminder.user,
            "text": new_reminder.text,
            "category": new_reminder.category,
            "due_date": new_reminder.due_date.isoformat()
        }
        file.write(json.dumps(data, ensure_ascii=False) + "\n")