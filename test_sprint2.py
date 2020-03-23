"""
ssw555tmDSYZ2020spring-test_sprint2 by Yuning Sun
4:22 PM 3/23/20
Module documentation: 
"""
import unittest

import geddata
from sprint1.zkang_sprint1 import birth_after_death_of_parents, marriage_after_14
from sprint2.dcai_sprint2 import birth_before_death, marriage_before_divorce
from sprint2.sfan_sprint2 import first_cousin_should_not_marry, aunts_and_uncles
from sprint2.zkang_sprint2 import parents_not_too_old, too_many_siblings


class TestSprint2(unittest.TestCase):

    def test_US03(self):
        inds, fams = geddata.get_inds_fams('res/US03.ged')
        self.assertEqual(birth_before_death(inds),
                         ['ERROR: INDIVIDUAL: US03: 80: @I7@: Birthday 1945-08-11 00:00:00 is after death.'])

    def test_US04(self):
        inds, fams = geddata.get_inds_fams('res/US04.ged')
        self.assertEqual(marriage_before_divorce(fams),
                         ['ERROR: FAMILY: US04: 133: @F1@: Marriage should occur before divorce of spouses'])

    def test_US09(self):
        inds, fams = geddata.get_inds_fams('res/US09.ged')
        self.assertEqual(birth_after_death_of_parents(fams, inds),
                         'ERROR: INDIVIDUAL: line: 42 US09: Child birth after parent death!')

    def test_US10(self):
        inds, fams = geddata.get_inds_fams('res/US10.ged')
        self.assertEqual(marriage_after_14(fams, inds), 'ERROR: line: 156 US10: Parents less than 14 years old!')

    def test_US12(self):
        inds, fams = geddata.get_inds_fams('res/US12.ged')
        self.assertEqual(parents_not_too_old(fams, inds), 'ERROR: line 31 US12: Parents too old!')

    def test_US15(self):
        inds, fams = geddata.get_inds_fams('res/US15.ged')
        self.assertEqual(too_many_siblings(fams, inds), 'ERROR: line 151 US15: too many siblings!')

    def test_US19(self):
        inds, fams = geddata.get_inds_fams('res/US19_20.ged')
        self.assertEqual(first_cousin_should_not_marry(inds, fams),
                         ['ERROR: FAMILY: US19: line139: Couple Bingbao /Xia/ and Xue /Xia/ are first cousins'])

    def test_US20(self):
        inds, fams = geddata.get_inds_fams('res/US19_20.ged')
        self.assertEqual(aunts_and_uncles(inds, fams),
                         ['ERROR: FAMILY: US20: line186: Yu /Xia/ marries to his aunt Nanhai /Xia/'])

    def test_US42(self):
        with self.assertRaises(ValueError):
            inds, fams = geddata.get_inds_fams('../res/US42_1.ged')


if __name__ == '__main__':
    unittest.main()
