from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    username: str
    password_hash: str

@dataclass
class Reminder:
    id: int
    user: str
    text: str
    category: str
    due_date: datetime