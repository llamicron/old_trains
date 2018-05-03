"""
Handles database and table connect, creation, etc.
"""
from peewee import *
import config
import os

db = SqliteDatabase(config.db_file)
db.connect()

def create():
    if not os.path.isfile(config.db_file):
        open(config.db_file, 'w')

    from models import Volunteer
    Volunteer.create_table(True)
