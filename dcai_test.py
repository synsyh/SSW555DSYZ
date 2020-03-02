import unittest

from gedparser import GEDParser
from sprint1.dcai_sprint1 import dates_before_current_date, birth_before_marriage


class TestSprint1(unittest.TestCase):
    def test_US01(self):
        p = GEDParser('res/US01_02.ged')
        p.parser()
        self.assertEqual(dates_before_current_date(p),
                         'ERROR: INDIVIDUAL: US01: Birthday 2069-12-19 00:00:00 is after today')

    def test_US02(self):
        p = GEDParser('res/US01_02.ged')
        p.parser()
        self.assertEqual(birth_before_marriage(p),
                         "ERROR: FAMILY: US02: Wife's birthday 2069-12-19 00:00:00 is after marriage date 2005-06-06 00:00:00")


if __name__ == '__main__':
    unittest.main()
