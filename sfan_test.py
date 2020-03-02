import unittest
from sfan import no_marries_to_children, siblings_not_marry
from gedparser import GEDParser


class SfanTest(unittest.TestCase):
    def test_true(self):
        p = GEDParser('res/ysun.ged')
        p.parser()
        self.assertEqual(no_marries_to_children(p), None)
        self.assertEqual(siblings_not_marry(p), None)

    def test_us17_false(self):
        p = GEDParser('res/sfan_test_17_18.ged')
        p.parser()
        self.assertEqual(no_marries_to_children(p),
                         ['ERROR: FAMILY: US17: LI /Fan/ marries to his mother Chloe /Zhang/'])

    def test_us18_false(self):
        p = GEDParser('res/sfan_test_17_18.ged')
        p.parser()
        self.assertEqual(siblings_not_marry(p),
                         ['ERROR: FAMILY: US18 :the couple Stuart /Fan/ and Ally /Jiang/ are siblings'])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
