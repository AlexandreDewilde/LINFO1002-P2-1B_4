import os
import sys
import unittest

working_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(working_dir), "src"))

from moon_phases import moon_phases_by_years
from moon_phase import moon_phase_dict


class TestMoonPhases(unittest.TestCase):

    def setUp(self):

        self.samples = {"06/01/2021": 6, "20/01/2021": 2, "14/06/2022": 4}
        self.samples_result_by_years = {2021: [0] * len(moon_phase_dict), 2022: [0] * len(moon_phase_dict)}

        for k, val in self.samples.items():
            self.samples_result_by_years[int(k.split('/')[-1])][val] += 1

    def test_moon_phases_by_years(self):
        res = moon_phases_by_years(list(self.samples.keys()))
        
        self.assertEqual(type(res), dict, "Function moon_phases_by_years not return a dict")

        for k, val in res.items():
            self.assertEqual(type(k), int, f"Function moon_phases_by_years not return a dict of key of int but a {type(res)} of key of {type(k)}")
            self.assertEqual(type(val), list, f"Function moon_phases_by_years not returning a dict of value of type list but value of type {type(val)}")
            for i, phase in enumerate(val):
                self.assertEqual(type(phase), int, f"Function moon_phases_by_years not returning a dict of value list of element of type int but of type {type(phase)}")
                return_val = self.samples_result_by_years[k][i]
                self.assertEqual(return_val, phase, f"Function moon_phases_by_years return {phase} instead of {return_val}")
        


if __name__ == "__main__":
    unittest.main()

        
        



