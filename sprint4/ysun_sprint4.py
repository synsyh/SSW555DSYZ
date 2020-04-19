"""
ssw555tmDSYZ2020spring-ysun_sprint4 by Yuning Sun
3:41 PM 4/17/20
Module documentation: 
"""
from geddata import get_inds_fams, get_ind_by_id, print_inds


def list_living_married(inds, fams):
    """
    US 30
    List all living married people in a GEDCOM file
    @param inds:
    @param fams:
    @return:
    """
    living_married_list = []
    id_inds = set()
    for fam in fams:
        if 'div' in fam.__dict__.keys():
            continue
        else:
            id_inds.add(fam['husb'].value)
            id_inds.add(fam['wife'].value)
    for id_ind in id_inds:
        ind = get_ind_by_id(id_ind, inds)
        if 'deat' in ind.__dict__.keys():
            continue
        living_married_list.append(ind)
    return living_married_list


def list_living_single(inds, fams):
    """
    US 31
    List all living people over 30 who have never been married in a GEDCOM file
    @param inds:
    @param fams:
    @return:
    """
    married_ids = set()
    living_single_list = []
    for fam in fams:
        married_ids.add(fam['husb'].value)
        married_ids.add(fam['wife'].value)
    for ind in inds:
        if ind['alive'].value == 'True':
            if ind['age'].value > 30:
                if ind['id'].value not in married_ids:
                    living_single_list.append(ind)
    return living_single_list


def list_multiple_births(inds, fams):
    """
    US 32
    List all multiple births in a GEDCOM file
    @param inds:
    @param fams:
    @return:
    """
    multiple_births_list = []
    multiple_births_ids = set()
    for fam in fams:
        if len(fam['chil']) > 1:
            for id_chil in fam['chil']:
                multiple_births_ids.add(id_chil)
    for mb_id in multiple_births_ids:
        ind = get_ind_by_id(mb_id, inds)
        multiple_births_list.append(ind)
    return multiple_births_list


def list_orphans(inds, fams):
    """
    US 33
    List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file
    @param inds:
    @param fams:
    @return:
    """
    orphans_list = []
    for fam in fams:
        husb = get_ind_by_id(fam['husb'].value, inds)
        if husb['alive'].value == 'True':
            continue
        wife = get_ind_by_id(fam['wife'].value, inds)
        if wife['alive'].value == 'True':
            continue
        for chil in fam['chil']:
            chil = get_ind_by_id(chil, inds)
            if chil['age'].value != 'NA':
                if int(chil['age'].value) < 18:
                    orphans_list.append(chil)
    return orphans_list


def list_large_age_differences():
    pass


def list_recent_births(inds):
    pass


if __name__ == '__main__':
    # inds, fams = get_inds_fams('../res/US30.ged')
    # lml = list_living_married(inds, fams)
    # print([ind['id'].value for ind in lml])
    # inds, fams = get_inds_fams('../res/US31.ged')
    # lsl = list_living_single(inds, fams)
    # print(sorted([ind['id'].value for ind in lsl]))
    # inds, fams = get_inds_fams('../res/US32.ged')
    # mbl = list_multiple_births(inds, fams)
    # print(sorted([ind['id'].value for ind in mbl]))
    inds, fams = get_inds_fams('../res/test_all_user_stories.ged')
    lo = list_orphans(inds, fams)
    print(sorted([ind['id'].value for ind in lo]))

    # print_inds(lml)
    print()
