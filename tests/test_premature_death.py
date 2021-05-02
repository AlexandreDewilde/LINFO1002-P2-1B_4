import os
import pathlib
import sys
import unittest


working_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(working_dir), "src"))

from db.db import DB
from premature_death import list_deces_prematures

class TestPrematureDeath(unittest.TestCase):
    def setUp(self):
        db_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "../src/db/database.db")
        self.db = DB(db_path)

    def test_list_deces_prematures(self):
        """
        Test the list_deces_prematures method
        """
        req = list_deces_prematures(self.db.get_all_premature_deaths())

        self.assertEqual(type(req), list,
                         f"Method list_deces_prematures doesn't return a list but a {type(req)}")

        self.assertEqual(len(req), 12,
                        f"Method list_deces_prematures doesn't return a list of len 12 but of lenght {len(req)}")

        for elem in req:
            self.assertEqual(type(elem), int,
                             f"Method list_deces_prematures doesn't return a list of int but a {type(req)} of {type(elem)}")
            self.assertEqual(True, elem >= 0,
                             f"Method list_deces_prematures doesn't return a int of elem >= 0 but an element {elem}")

if __name__ == "__main__":
    unittest.main()