"""
ssw555tmDSYZ2020spring-ysun_sprint2 by Yuning Sun
2:37 PM 3/22/20
Module documentation: 
"""
import datetime

from geddata import get_inds_fams
from geddate import check_date_valid


def reject_illegitimate_dates():
    """
    All dates should be legitimate dates for the months specified (e.g., 2/30/2015 is not legitimate)
    @return:
    """
    try:
        # inds, fams = get_inds_fams('../res/US42.ged')
        inds, fams = get_inds_fams('../res/US42_1.ged')
        for ind in inds:
            check_date_valid(ind, 'ind')
        for fam in fams:
            check_date_valid(fam, 'fam')
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    reject_illegitimate_dates()
