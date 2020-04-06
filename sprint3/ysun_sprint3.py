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
    results = ''
    for fam in fams:
        if 'chil' in fam.__dict__.keys() and len(fam['chil']) != 0:
            results += f"Family ID: {fam['id'].value}, Family Sibling ordered by age: {', '.join([c.value for c in fam['chil']])} \n"
    return results


def list_deceased(inds):
    """
    US 29
    List all deceased individuals in a GEDCOM file
    @param inds:
    @return:
    """
    deceased_inds = [ind['id'].value for ind in inds if 'deat' in ind.__dict__.keys()]
    return 'All deceased individuals in the GEDCOM file: ' + ', '.join(deceased_inds)


if __name__ == '__main__':
    inds, fams = get_inds_fams('../res/US28.ged')
    print(order_sibling_by_age(inds, fams))
