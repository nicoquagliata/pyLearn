from peewee import *
import datetime
import sys
from collections import OrderedDict

db = SqliteDatabase('diary.db')


class Entry(Model):
    #content
    #timestamp
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def create_and_connect():
    """Connects to the database and creates tables"""
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show menu """

    choice = None

    while choice != 'q':
        print("Press 'q' to quit")
        for key,value in menu.items():
            print("{}) {}".format(key,value.__doc__))
        choice = input("Action: ").lower().strip()
        if choice in menu:
            menu[choice]()

    print("thanks for using diary!")

    


def add_entry():
    """Add Entry"""
    print("Enter your thoughts. Press ctrl + Z to finish")
    data= sys.stdin.read().strip()

    if data:
        if input("Do you want to save your entry? [y|n]").lower().strip() != 'n':
            Entry.create(content=data)
            print("Your entry was created succesfully")

def view_entries():
    """View all entries"""

def delete_entry():
    """Delete an Entry"""





menu = OrderedDict([
    ('a', add_entry ),
    ('v', view_entries),
    ('d', delete_entry)
])


if __name__ == '__main__':
    create_and_connect()
    menu_loop()