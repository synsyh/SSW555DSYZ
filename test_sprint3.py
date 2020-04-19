import unittest
from geddata import get_inds_fams, get_ind_by_id
from sprint3.sfan_sprint3 import unique_id, correct_gender
from sprint3.dcai_sprint3 import divorce_before_death, marriage_before_death
from sprint3.ysun_sprint3 import list_deceased, order_sibling_by_age
from sprint3.zkang_sprint3 import multiple_births, male_last_names


class Testsprint3(unittest.TestCase):

    def test_US05(self):
        inds, fams = get_inds_fams('res/US05.ged')
        self.assertEqual(marriage_before_death(inds, fams),
                         ['ERROR: FAMILY: US05: 156: @I7@: Marriage 7 JUL 1972 is after death.'])

    def test_US06(self):
        inds, fams = get_inds_fams('res/US06.ged')
        self.assertEqual(divorce_before_death(inds, fams),
                         ['ERROR: FAMILY: US06: 149: @I8@: Divorce 1 OCT 2000 is after death.'])

    def test_US14(self):
        inds, fams = get_inds_fams('res/US14.ged')
        self.assertEqual(multiple_births(fams, inds),
                         'ERROR: FAMILY: LINE: 31 US14: more than five siblings born at the same time!')

    def test_US16(self):
        inds, fams = get_inds_fams('res/US16.ged')
        self.assertEqual(male_last_names(fams, inds),
                         'ERROR: FAMILY: LINE: 47 US16: All male members of a family should have the same last name!')

    def test_US21(self):
        inds, fams = get_inds_fams('res/US21.ged')
        self.assertEqual(correct_gender(inds, fams),
                         ['ERROR: FAMILY: US21: line146: gender of husband in family should be male',
                          'ERROR: FAMILY: US21: line147: gender of wife in family should be female',
                          'ERROR: FAMILY: US21: line153: gender of husband in family should be male',
                          'ERROR: FAMILY: US21: line172: gender of wife in family should be female'])

    def test_US22(self):
        inds, fams = get_inds_fams('res/US22.ged')
        self.assertEqual(unique_id(inds, fams),
                         ['ERROR: INDIVIDUAL: US22: line14 and line35: These 2 individuals have same id',
                          'ERROR: INDIVIDUAL: US22: line120 and line129: These 2 individuals have same id',
                          'ERROR: FAMILY: US22: line170 and line186: These 2 families have same id'])

    def test_US28(self):
        inds, fams = get_inds_fams('res/US28.ged')
        ordered_fams = order_sibling_by_age(inds, fams)
        self.assertEqual([chil.value for chil in ordered_fams[3]['chil']], ['@I6@', '@I2@', '@I13@'])

    def test_US29(self):
        inds, _ = get_inds_fams('res/US29.ged')
        deceased_inds = list_deceased(inds)
        self.assertEqual([ind['id'].value for ind in deceased_inds], ['@I7@', '@I8@', '@I10@', '@I11@'])


if __name__ == '__main__':
    unittest.main()
