"""
Handles database and table connect, creation, etc.
"""
from peewee import *
import os

db_file = 'trains/data/trains.db'

if not os.path.isfile(db_file):
    open(db_file, 'w')

db = SqliteDatabase(db_file)
db.connect()
