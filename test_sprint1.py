"""
ssw555tmDSYZ2020spring-test_sprint1 by Yuning Sun
11:29 AM 3/2/20
Module documentation: 
"""
import unittest

from geddata import get_inds_fams
from gedparser import GEDParser
from sprint1.dcai_sprint1 import dates_before_current_date, birth_before_marriage
from sprint1.sfan_sprint1 import siblings_not_marry, no_marries_to_children
from sprint1.ysun_sprint1 import include_individual_ages, corresponding_entries
from sprint1.zkang_sprint1 import marriage_after_14, birth_after_death_of_parents


class TestSprint1(unittest.TestCase):
    def test_true(self):
        inds, fams = get_inds_fams('res/valid.ged')
        self.assertEqual(dates_before_current_date(inds, fams), None)
        self.assertEqual(birth_before_marriage(inds, fams), None)
        self.assertEqual(birth_after_death_of_parents(fams, inds), None)
        self.assertEqual(marriage_after_14(fams, inds), None)
        self.assertEqual(no_marries_to_children(inds, fams), None)
        self.assertEqual(siblings_not_marry(inds, fams), None)
        self.assertEqual(corresponding_entries(inds, fams), None)
        self.assertEqual(include_individual_ages(inds), [])

    def test_US01(self):
        inds, fams = get_inds_fams('res/US01_02.ged')
        self.assertEqual(dates_before_current_date(inds, fams),
                         ['ERROR: INDIVIDUAL: US01: 82: @I7@: Death 2022-09-14 00:00:00 day is after '
                          'today',
                          'ERROR: FAMILY: US01: 133: @F1@: Divorce date 2022-08-12 00:00:00 is after '
                          'today']
                         )

    def test_US02(self):
        inds, fams = get_inds_fams('res/US01_02.ged')
        self.assertEqual(birth_before_marriage(inds, fams),
                         "ERROR: FAMILY: US02: 140: @F2@: Wife's birthday 1969-12-19 00:00:00 is after marriage date 1969-06-06 00:00:00")

    def test_US09(self):
        inds, fams = get_inds_fams('res/US09.ged')
        self.assertEqual(birth_after_death_of_parents(fams, inds),
                         'ERROR: INDIVIDUAL: line: 42 US09: Child birth after parent death!')

    def test_US10(self):
        inds, fams = get_inds_fams('res/US10.ged')
        self.assertEqual(marriage_after_14(fams, inds),
                         'ERROR: line: 156 US10: Parents less than 14 years old!')

    # def test_US17(self):
    #     inds, fams = get_inds_fams('res/US17_18.ged')
    #     self.assertEqual(no_marries_to_children(inds, fams),
    #                      ['ERROR: FAMILY: US17: LI /Fan/ marries to his mother Chloe /Zhang/'])
    #
    # def test_US18(self):
    #     inds, fams = get_inds_fams('res/US17_18.ged')
    #
    #     self.assertEqual(siblings_not_marry(inds, fams),
    #                      ['ERROR: FAMILY: US18 :the couple Stuart /Fan/ and Ally /Jiang/ are siblings'])

    def test_US26(self):
        inds, fams = get_inds_fams('res/US26.ged')
        self.assertEqual(corresponding_entries(inds, fams),
                         ['ERROR: INDIVIDUAL: US26: 126: @I12@: @I12@ cannot find corresponding families.'])

    def test_US27(self):
        inds, fams = get_inds_fams('res/US27.ged')
        self.assertEqual(include_individual_ages(inds),
                         ['ERROR: INDIVIDUAL: US27: 42: @I6000000120666859777@: @I6000000120666859777@ have no age information.'])


if __name__ == '__main__':
    unittest.main()
