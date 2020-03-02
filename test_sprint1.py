"""
ssw555tmDSYZ2020spring-test_sprint1 by Yuning Sun
11:29 AM 3/2/20
Module documentation: 
"""
import unittest

from gedparser import GEDParser
from sprint1.dcai_sprint1 import dates_before_current_date, birth_before_marriage
from sprint1.sfan_sprint1 import siblings_not_marry, no_marries_to_children
from sprint1.ysun_sprint1 import include_individual_ages, corresponding_entries
from sprint1.zkang_sprint1 import marriage_after_14, birth_after_d_p


class TestSprint1(unittest.TestCase):
    def test_true(self):
        p = GEDParser('./res/ysun.ged')
        p.parser()
        self.assertEqual(dates_before_current_date(p), None)
        self.assertEqual(birth_before_marriage(p), None)
        self.assertEqual(birth_after_d_p(p.fams, p.inds), None)
        self.assertEqual(marriage_after_14(p.fams, p.inds), None)
        self.assertEqual(no_marries_to_children(p), None)
        self.assertEqual(siblings_not_marry(p), None)
        self.assertEqual(corresponding_entries(p), None)
        self.assertEqual(include_individual_ages(p), None)

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

    def test_US09(self):
        p = GEDParser('res/US09.ged')
        p.parser()
        self.assertEqual(birth_after_d_p(p.fams, p.inds),
                         'ERROR: INDIVIDUAL: US09: @I6000000120666859850@ Child birth after parent death!')

    def test_US10(self):
        p = GEDParser('res/US10.ged')
        p.parser()
        self.assertEqual(marriage_after_14(p.fams, p.inds),
                         'ERROR: FAMILY: US10: @I6000000120666500951@ marriage before 14!')

    def test_US17(self):
        p = GEDParser('res/US17_18.ged')
        p.parser()
        self.assertEqual(no_marries_to_children(p),
                         ['ERROR: FAMILY: US17: LI /Fan/ marries to his mother Chloe /Zhang/'])

    def test_US18(self):
        p = GEDParser('res/US17_18.ged')
        p.parser()
        self.assertEqual(siblings_not_marry(p),
                         ['ERROR: FAMILY: US18 :the couple Stuart /Fan/ and Ally /Jiang/ are siblings'])

    def test_US26(self):
        p = GEDParser('res/US26.ged')
        p.parser()
        self.assertEqual(corresponding_entries(p),
                         ['ERROR: INDIVIDUAL: US26: @I6000000120667216833@ cannot find corresponding '
                          'families.',
                          'ERROR: FAMILY: US26: @I6000000120666859777@,@I6000000120667216824@ cannot '
                          'find corresponding individual information.'])

    def test_US27(self):
        p = GEDParser('res/US27.ged')
        p.parser()
        self.assertEqual(include_individual_ages(p),
                         'ERROR: INDIVIDUAL: US27: @I6000000120666859777@ have no age information.')


if __name__ == '__main__':
    unittest.main()
