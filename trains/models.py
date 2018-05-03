"""
Stores database models
"""
from peewee import *

from trains.db import db

class Volunteer(Model):
    bsa_id = CharField()
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    district = CharField()
    council = CharField()
    unit_type = CharField()
    unit = IntegerField()

    class Meta:
        database = db
