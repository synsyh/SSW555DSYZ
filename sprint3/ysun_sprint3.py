"""
ssw555tmDSYZ2020spring-ysun_sprint3 by Yuning Sun
4:36 PM 4/4/20
Module documentation: 
"""
import datetime

from geddata import get_inds_fams, get_ind_by_id


def order_sibling_by_age(inds, fams):
    """
    US 28
    List siblings in families by decreasing age, i.e. oldest siblings first
    @param inds:
    @param fams:
    @return:
    """
    for fam in fams:
        chils = [get_ind_by_id(chil, inds) for chil in fam['chil']]
        chils = [ind if 'birt' in ind.__dict__.keys() else None for ind in chils]
        try:
            chils.remove(None)
        except ValueError:
            pass
        chils = sorted(chils, key=lambda ind: datetime.datetime.strptime(ind['birt'].value, '%d %b %Y').timestamp())
        fam['chil'] = [chil['id'] for chil in chils]
    return fams


def list_deceased(inds):
    """
    US 29
    List all deceased individuals in a GEDCOM file
    @param inds:
    @return:
    """
    return [ind for ind in inds if 'deat' in ind.__dict__.keys()]


if __name__ == '__main__':
    inds, fams = get_inds_fams('../res/US29.ged')
    deceased_inds = list_deceased(inds)
    for ind in deceased_inds:
        print(ind['id'].value)
