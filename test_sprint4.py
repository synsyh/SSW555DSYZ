"""
ssw555tmDSYZ2020spring-test_sprint4 by Yuning Sun
1:58 PM 4/19/20
Module documentation: 
"""
import unittest

from geddata import get_inds_fams
from sprint4.dcai_sprint4 import less_than_150_years_old, birth_before_marriage_of_parents
from sprint4.sfan_sprint4 import unique_name_and_birth, unique_families_by_spouse
from sprint4.ysun_sprint4 import list_living_married, list_living_single, list_multiple_births, list_orphans
from sprint4.zkang_sprint4 import no_bigamy, siblings_spacing


class TestSprint3(unittest.TestCase):
    def test_US07(self):
        inds, fams = get_inds_fams('res/US07.ged')
        self.assertEqual(less_than_150_years_old(inds),
                         'ERROR: INDIVIDUAL: US07: LINE: 80: @I7@: age 167 should less than 150.')

    def test_US08(self):
        inds, fams = get_inds_fams('res/US08.ged')
        self.assertEqual(birth_before_marriage_of_parents(inds, fams),
                         """ERROR: INDIVIDUAL: US08: line20: @I1@: Child birthday 12 MAY 1993 before parents' marriage date 12 DEC 1993
ERROR: INDIVIDUAL: US08: line130: @I12@: Child birthday 3 AUG 2003 is more than 9 months after parents' divorce date 12 DEC 1993
ERROR: INDIVIDUAL: US08: line31: @I2@: Child birthday 19 DEC 1969 before parents' marriage date 7 JUL 1972
ERROR: INDIVIDUAL: US08: line42: @I3@: Child birthday 3 MAR 1970 before parents' marriage date 13 MAR 1974
""")

    def test_US11(self):
        inds, fams = get_inds_fams('res/US11.ged')
        self.assertEqual(no_bigamy(fams, inds),
                         'ERROR: INDIVIDUAL: line24 US11: Marriage should not occur during marriage to another spouse!')

    def test_US13(self):
        inds, fams = get_inds_fams('res/US13.ged')
        self.assertEqual(siblings_spacing(fams, inds),
                         'ERROR: FAMILY: @F3@ US13: Birth dates of siblings should be more than 8 months apart or less than 2 days apart!')

    def test_US23(self):
        inds, fams = get_inds_fams('res/US23.ged')
        self.assertEqual(unique_name_and_birth(inds, fams),
                         ['ERROR: INDIVIDUAL: US23: line140 and line 130: these two guys have same name and birthday'])

    def test_US24(self):
        inds, fams = get_inds_fams('res/US24.ged')
        self.assertEqual(unique_families_by_spouse(inds, fams), [
            'ERROR: INDIVIDUAL: US24: line196 and line 190: these two families have same spouses and marry date'])

    def test_US30(self):
        inds, fams = get_inds_fams('res/US30.ged')
        lml = list_living_married(inds, fams)
        id_list = sorted([ind['id'].value for ind in lml])
        self.assertEqual(id_list, ['@I2@', '@I3@', '@I6@'])

    def test_US31(self):
        inds, fams = get_inds_fams('res/US31.ged')
        lsl = list_living_single(inds, fams)
        id_list = sorted([ind['id'].value for ind in lsl])
        self.assertEqual(id_list, ['@I12@'])

    def test_US32(self):
        inds, fams = get_inds_fams('res/US32.ged')
        mbl = list_multiple_births(inds, fams)
        id_list = sorted([ind['id'].value for ind in mbl])
        self.assertEqual(id_list, ['@I12@', '@I4@'])

    def test_US33(self):
        inds, fams = get_inds_fams('res/US33.ged')
        lo = list_orphans(inds, fams)
        id_list = sorted([ind['id'].value for ind in lo])
        self.assertEqual(id_list, ['@I47@'])


if __name__ == '__main__':
    unittest.main()
