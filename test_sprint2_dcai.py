import unittest

from dcai_sprint2 import birth_before_death
from dcai_sprint2 import marriage_before_divorce


def test_US03(self):
    p = GEDParser('res/US03.ged')
    p.parser()
    self.assertEqual(birth_before_death(p),
                     'ERROR: INDIVIDUAL: US03: birthday should occur before the death of a person')


def test_US04(self):
    p = GEDParser('res/US04.ged')
    p.parser()
    self.assertEqual(marriage_before_divorce(p),
                     "ERROR: FAMILY: US04: marriage should occur before divorce of spouses")



if __name__ == '__main__':
    unittest.main()