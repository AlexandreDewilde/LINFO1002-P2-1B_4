import os
import sys
import pathlib
import unittest

working_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(working_dir), "src"))

from fam_pre import list_family
from typing import List
from db.db import DB

class TestListFamily(unittest.TestCase):

    def setUp(self):
        db_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "../src/db/database.db")
        self.db = DB(db_path)
        self.families: List[tuple] = self.db.get_families()
        self.families_ids: List[int] = [family[0] for family in self.families]
        self.samples = [(68,), (164,), (26,), (164,), (68,), (68,), (61,), (25,), (81,), (7,)]

    def test_list_family(self):
        res = list_family(self.families_ids, self.samples)
        
        self.assertEqual(type(res), list, f"Function list_family not return a list")

        self.assertEqual(len(res), 165, f"Function list_family doesn't return a list of len 165 but of lenght {len(res)}")

        for val in res:
            self.assertEqual(type(val), int, f"Function list_family not returning an int value but value of type {type(val)}")

if __name__ == "__main__":
    unittest.main()