import unittest

from trains import models
from trains.db import db

class TestModels(unittest.TestCase):
    def test_create_tables(self):
        models.create_tables()

        assert 'volunteer' in db.get_tables()

    def test_populate_volunteers(self):
        models.Volunteer.populate('trains/data/volunteers.csv')
        assert type(models.Volunteer.get()) is models.Volunteer
