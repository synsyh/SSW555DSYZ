import unittest
import geddata
from zkang_sprint2 import too_many_siblings
from zkang_sprint2 import parents_not_too_old


class TestSprint1(unittest.TestCase):
    def test_US12(self):
        inds, fams = geddata.get_inds_fams('res/US12.ged')
        self.assertEqual(parents_not_too_old(fams, inds), 'ERROR: line 31 US12: Parents too old!')

    def test_US15(self):
        inds, fams = geddata.get_inds_fams('res/US15.ged')
        self.assertEqual(too_many_siblings(fams, inds), 'ERROR: line 151 US15: too many siblings!')


if __name__ == '__main__':
    unittest.main()