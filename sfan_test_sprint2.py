from sprint2.sfan_sprint2 import first_cousin_should_not_marry, aunts_and_uncles
import unittest
from geddata import get_inds_fams


class TestSprint2(unittest.TestCase):
    def test_US19(self):
        inds, fams = get_inds_fams('res/US19_20.ged')
        self.assertEqual(first_cousin_should_not_marry(inds, fams),
                         ['ERROR: FAMILY: US19: line139: Couple Bingbao /Xia/ and Xue /Xia/ are first cousins'])

    def test_US20(self):
        inds, fams = get_inds_fams('res/US19_20.ged')
        self.assertEqual(aunts_and_uncles(inds, fams),
                         ['ERROR: FAMILY: US20: line186: Yu /Xia/ marries to his aunt Nanhai /Xia/'])


if __name__ == '__main__':
    unittest.main()
