import unittest
import geddata
from zkang_sprint2 import too_many_siblings
from zkang_sprint2 import parents_not_too_old
from sprint1.zkang_sprint1 import birth_after_death_of_parents
from sprint1.zkang_sprint1 import marriage_after_14


class TestSprint1(unittest.TestCase):
    def test_US09(self):
        inds, fams = geddata.get_inds_fams('res/US09.ged')
        self.assertEqual(birth_after_death_of_parents(fams, inds), 'ERROR: INDIVIDUAL: line: 42 US09: Child birth after parent death!')

    def test_US10(self):
        inds, fams = geddata.get_inds_fams('res/US10.ged')
        self.assertEqual(marriage_after_14(fams, inds), 'ERROR: line: 156 US10: Parents less than 14 years old!')

    def test_US12(self):
        inds, fams = geddata.get_inds_fams('res/US12.ged')
        self.assertEqual(parents_not_too_old(fams, inds), 'ERROR: line 31 US12: Parents too old!')

    def test_US15(self):
        inds, fams = geddata.get_inds_fams('res/US15.ged')
        self.assertEqual(too_many_siblings(fams, inds), 'ERROR: line 151 US15: too many siblings!')


if __name__ == '__main__':
    unittest.main()