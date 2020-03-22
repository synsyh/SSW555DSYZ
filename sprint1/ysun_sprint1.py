"""
ssw555tmDSYZ2020spring-ysun_sprint1 by Yuning Sun
15:36 2020/2/17
Module documentation: 
"""
from geddata import get_inds_fams
from gedparser import GEDParser


def include_individual_ages(inds):
    """
    US27: Include person's current age when listing individuals
    @param inds:
    @return:
    """
    missed_aged_ind = []
    results = []
    for ind in inds:
        if 'age' not in ind.__dict__.keys():
            missed_aged_ind.append(ind['id'])
    if missed_aged_ind:
        for ind in missed_aged_ind:
            results.append(f'ERROR: INDIVIDUAL: US27: {ind.line}: {ind.value}: {ind.value} have no age information.')
    return results


def corresponding_entries(inds, fams):
    """
    US26: All family roles (spouse, child) specified in an individual record should have corresponding entries in the
    corresponding family records. Likewise, all individual roles (spouse, child) specified in family records should
    have corresponding entries in the corresponding  individual's records.  I.e. the information in the individual and
    family records should be consistent.
    @param inds:
    @param fams:
    @return:
    """
    ind_in_fam = set()
    ind_in_ind = set()
    results = []
    for fam in fams:
        ind_in_fam.add(fam['wife'])
        ind_in_fam.add(fam['husb'])
        for i in range(len(fam['chil'])):
            ind_in_fam.add(fam['chil'][i])
    for ind in inds:
        ind_in_ind.add(ind['id'])
    missed_ind = []
    for i in ind_in_ind:
        for j in ind_in_fam:
            if i.value == j.value:
                break
        else:
            missed_ind.append(i)
    if missed_ind:
        for ind in missed_ind:
            results.append(
                f'ERROR: INDIVIDUAL: US26: {ind.line}: {ind.value}: {ind.value} cannot find corresponding families.')
    if results:
        return results


if __name__ == '__main__':
    inds, fams = get_inds_fams('../res/US26.ged')
    print(corresponding_entries(inds, fams))
