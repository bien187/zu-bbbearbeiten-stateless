from dataclasses import dataclass
import datetime

items = []

@dataclass
class Item:
    text: str
    date: datetime.date
    isCompleted: bool = False

def add(text, date):
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    items.append(Item(text, date_obj))

def get_all():
    return items

def get(index):
    return items[index]

def update(index):
    items[index].isCompleted = not items[index].isCompleted
