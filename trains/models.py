"""
Stores database models
"""
import os
import sys

from peewee import *

try:
    from trains.db import db
except ImportError:
    from db import db


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

    @staticmethod
    def populate(data_file):
        """
        Pulls data from CSV source file and writes Volunteer models to db
        """
        with open(data_file, 'r') as fi:
            keys = fi.readline().strip().lower().split(',')
            for row in fi.readlines()[1:]:
                values = row.strip().split(',')
                vol = dict(zip(keys, values)) # Dictionary of volunteer data
                if not vol['unit']:
                    vol['unit_type'] = 0
                    vol['unit'] = 0
                else:
                    vol['unit_type'] = vol['unit'].split()[0]
                    vol['unit'] = vol['unit'].split()[1]

                Volunteer(
                    bsa_id=vol['memberid'],
                    first_name=vol['first_name'],
                    last_name=vol['last_name'],
                    email=vol['email'],
                    district=vol['district'],
                    council=vol['council'],
                    unit_type=vol['unit_type'],
                    unit=int(vol['unit'])
                ).save()

def create_tables():
    db_file = 'trains/data/trains.db'

    if not os.path.isfile(db_file):
        open(db_file, 'w')
    Volunteer.create_table(True)

if __name__ == '__main__':
    create_tables()
