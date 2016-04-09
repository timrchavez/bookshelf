from peewee import *

db = SqliteDatabase('bookshelf.db')

class Book(Model):
    title = CharField(unique=True)
    isbn = CharField(null=True)
    width = FloatField(default=15.0)
    height = FloatField(default=23.0)
    thickness = FloatField(default=2.5)


    class Meta:
        database = db
