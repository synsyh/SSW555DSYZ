"""
ssw555tmDSYZ2020spring-ysun_sprint1 by Yuning Sun
15:36 2020/2/17
Module documentation: 
"""
from gederror import GEDError
from gedparser import GEDParser


def unique_first_name(p):
    """
    US27: Include person's current age when listing individuals
    @param p:
    @return:
    """
    p.print_indi()
    p.print_fams()
    missed_aged_ind = []
    for ind in p.inds:
        if 'age' not in ind.keys():
            missed_aged_ind.append(ind['id'])
    raise GEDError('Individual: ' + ', '.join(missed_aged_ind) + ' have no age information.')


def corresponding_entries(p):
    """
    US26: All family roles (spouse, child) specified in an individual record should have corresponding entries in the
    corresponding family records. Likewise, all individual roles (spouse, child) specified in family records should
    have corresponding entries in the corresponding  individual's records.  I.e. the information in the individual and
    family records should be consistent.
    @param p:
    @return:
    """
    ind_in_fam = set()
    ind_in_ind = set()
    for fam in p.fams:
        ind_in_fam.add(fam['wife'])
        ind_in_fam.add(fam['husb'])
        for child in fam['chil']:
            ind_in_fam.add(child)
    for ind in p.inds:
        ind_in_ind.add(ind['id'])
    ind_in_fam.remove('NA')
    missed_ind_id = []
    missed_fam_id = []
    for ind_id in ind_in_ind:
        if ind_id not in ind_in_fam:
            missed_ind_id.append(ind_id)
    for ind_id in ind_in_fam:
        if ind_id not in ind_in_ind:
            missed_fam_id.append(ind_id)
    if missed_ind_id:
        raise GEDError('Individual: ' + ','.join(missed_ind_id) + ' cannot find corresponding families.')
    if missed_fam_id:
        raise GEDError(
            'Individual: ' + ','.join(missed_fam_id) + ' cannot find corresponding individual information.')


if __name__ == '__main__':
    p = GEDParser('res/US27.ged')
    p.parser()
    unique_first_name(p)
