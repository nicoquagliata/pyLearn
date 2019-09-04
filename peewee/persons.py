from peewee import *
from datetime import date

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db

def create_and_connect():
    db.connect()
    db.create_tables([Person, Pet], safe=True)

def create_family_members():
    uncle_tommy = Person(name="tommy", birthday=date(2000,4,22), is_relative=True)
    uncle_tommy.save()

    grandma_ana = Person.create(name="ana", birthday=date(1940,6,21),is_relative=False)

create_and_connect()
create_family_members()