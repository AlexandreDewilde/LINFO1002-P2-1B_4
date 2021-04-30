import os
import pathlib
import sys
import unittest
import re


working_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(working_dir), "src"))

from db.db import DB

class TestDB(unittest.TestCase):
    def setUp(self):
        db_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "../src/db/database.db")
        self.db = DB(db_path)
    
    def test_get_all_premature_deaths(self):
        """
        Test the get_all_premature_deaths method
        """
        res = self.db.get_all_premature_deaths()
        self.assertEqual(type(res), list, f"Method from DB class get_all_premature_deaths doesn't return a list but a {type(res)}")

        regex_date = r"[0-3]\d/[0-1]\d/\d\d\d\d$"
        for el in res:
            self.assertEqual(type(el), tuple, f"Method db.get_all_premature_deaths doesn't return a list of tuple but a {type(res)} of {type(el)}")
            self.assertEqual(len(el), 1, f"Method db.get_all_premature_deaths doesn't return a tuple of len 1 but of lenght {len(el)}")
            self.assertEqual(type(el[0]), str, f"Method db.get_all_premature_deaths doesn't return a tuple with one element of type str but an element of type {type(el[0])}")
            self.assertEqual(True, re.match(regex_date, el[0]) != None, f"The return string of db.get_births doesn't match the date format dd:mm:yyyy, it return {el}")
    
    def test_get_births(self):
        """
        Test the get_births method
        """
        res = self.db.get_births()

        self.assertEqual(type(res), list, f"Method db.get_births doesn't return a list but a {type(res)}")
        regex_date = r"[0-3]\d/[0-1]\d/\d\d\d\d$"
        for el in res:
            self.assertEqual(type(el), str, f"Methods db.get_births doesn't return a list of str but a {type(res)} of {type(el)}")
            self.assertEqual(True, re.match(regex_date, el) != None, f"The return string of db.get_births doesn't match the date format dd:mm:yyyy, it return {el}")




if __name__ == "__main__":
    unittest.main()