"""
ssw555tmDSYZ2020spring-ysun_sprint1 by Yuning Sun
15:36 2020/2/17
Module documentation: 
"""
from geddata import get_inds_fams
from gedparser import GEDParser


def include_individual_ages(p):
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
    if missed_aged_ind:
        return 'ERROR: INDIVIDUAL: US27: ' + ', '.join(missed_aged_ind) + ' have no age information.'


def corresponding_entries(inds, fams):
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
    results = []
    for fam in fams:
        ind_in_fam.add(fam['wife'])
        ind_in_fam.add(fam['husb'])
        for i in range(len(fam['chil'].value)):
            ind_in_fam.add(fam['chil'].value[i])
    for ind in inds:
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
        results.append('ERROR: INDIVIDUAL: US26: ' + ','.join(missed_ind_id) + ' cannot find corresponding families.')
    if missed_fam_id:
        missed_fam_id.sort()
        results.append(
            'ERROR: FAMILY: US26: ' + ','.join(missed_fam_id) + ' cannot find corresponding individual information.')
    if results:
        return results


if __name__ == '__main__':
    inds, fams = get_inds_fams('../res/US26.ged')
    corresponding_entries(inds, fams)
