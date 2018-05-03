import unittest
import os
from peewee import *
from peewee import SqliteDatabase

from trains import db

class TestDB(unittest.TestCase):
    def test_create_db_file(self):
        assert type(db.db) is SqliteDatabase
