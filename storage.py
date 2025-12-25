import json
import os
from models import *

REMINDERS_PATH = "reminders.jsonl"
USERS_PATH = "users.jsonl"

def load_reminders():
    if not os.path.exists(REMINDERS_PATH) or os.path.getsize(REMINDERS_PATH) == 0:
        return []
    reminders_list = []
    with open(REMINDERS_PATH, "r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue
            item = json.loads(line)
            date_str = item.get("due_date")
            due_date_obj = datetime.fromisoformat(date_str)
            new_reminder = Reminder(
                id=item.get("id"),
                user=item.get("user"),
                text=item.get("text"),
                category=item.get("category"),
                due_date=due_date_obj
            )
            reminders_list.append(new_reminder)
    return reminders_list

def load_users():
    if not os.path.exists(USERS_PATH) or os.path.getsize(USERS_PATH) == 0:
        return []
    users_list = []
    with open(USERS_PATH, "r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue
            item = json.loads(line)
            user = User(
                username=item.get("username"),
                password_hash=item.get("password_hash")
            )
            users_list.append(user)
    return users_list

def save_users(users_list):
    with open(USERS_PATH, "w", encoding="utf-8") as file:
        for u in users_list:
            data = {
                "username": users_list.username,
                "password_hash": users_list.password_hash,
            }
            file.write(json.dumps(data, ensure_ascii=False) + "\n")


def save_reminders(reminders_list):
    """Nadpisuje cały plik (używane przy usuwaniu/edycji)"""
    with open(REMINDERS_PATH, "w", encoding="utf-8") as file:
        for r in reminders_list:
            data = {
                "id": r.id,
                "user": r.user,
                "text": r.text,
                "category": r.category,
                "due_date": r.due_date.isoformat() if r.due_date else None
            }
            file.write(json.dumps(data, ensure_ascii=False) + "\n")
