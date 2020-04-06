"""
ssw555tmDSYZ2020spring-ysun_sprint3 by Yuning Sun
4:36 PM 4/4/20
Module documentation: 
"""
import datetime

from geddata import get_inds_fams, get_ind_by_id, GEDAttribute


def order_sibling_by_age(inds, fams):
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


def list_deceased(inds, fams):
    id_inds_deceased = set()
    for fam in fams:
        if 'div' in fam.__dict__.keys():
            id_inds_deceased.add(fam['husb'].value)
            id_inds_deceased.add(fam['wife'].value)
    inds_deceased = [get_ind_by_id(ind_id, inds) for ind_id in id_inds_deceased]
    return inds_deceased




if __name__ == '__main__':
    inds, fams = get_inds_fams('../res/test_all_user_stories.ged')
    for ind in list_deceased(inds, fams):
        print(ind['name'].value)
    order_sibling_by_age(inds, fams)
    record_all = []
    for fam in fams:
        record = []
        for child in fam['chil']:
            child_ind = get_ind_by_id(child,inds)
            record.append(child_ind['age'].value)
            record_all.extend([record])
    print(record_all)
