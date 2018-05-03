import unittest
import os
from peewee import *

from trains import db, config

class TestDB(unittest.TestCase):
    def test_create_db_if_file_not_exists(self):
        fi = config.db_file

        if os.path.isfile(fi):
            os.remove(fi)

        db.create()

        assert os.path.isfile(fi)

    def test_create_tables(self):
        db.create()
        assert "volunteer" in db.db.get_tables()

