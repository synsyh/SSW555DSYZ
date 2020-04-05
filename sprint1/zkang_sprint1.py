import geddata
from geddata import get_ind_by_id
import datetime


def birth_after_death_of_parents(fams, inds):
    """
    US09: Child should born before the death of the parent.
    """
    for fam in fams:
        father_ind = get_ind_by_id(fam["husb"], inds)
        if str(father_ind['deat']) == 'NA':
            fa_year_death = 9999
        else:
            fa_year_death = datetime.datetime.strptime(str(father_ind['deat']), '%d %b %Y').year
        mother_ind = get_ind_by_id(fam["wife"], inds)
        if str(mother_ind['deat']) == 'NA':
            ma_year_death = 9999
        else:
            ma_year_death = datetime.datetime.strptime(str(mother_ind['deat']), '%d %b %Y').year
        for child_id in fam['chil']:
            # print('child:')
            # print(child_id)
            child_ind = get_ind_by_id(child_id, inds)
            # print(child_ind['birt'])
            if 'birt' not in child_ind.__dict__.keys():
                continue
            ch_year_birth = datetime.datetime.strptime(str(child_ind['birt']), '%d %b %Y').year
            if (ma_year_death - ch_year_birth) < 0 or (fa_year_death - ch_year_birth) < 0:
                return f"ERROR: INDIVIDUAL: {child_ind['birt'].line}: US09: Child birth after parent death!"


def marriage_after_14(fams, inds):
    """
    US10: Marriage date should be at least 14 years after birth date for a person
    """
    for fam in fams:
        father_ind = get_ind_by_id(fam["husb"], inds)
        if 'birt' not in father_ind.__dict__.keys():
            continue
        fa_year_birth = datetime.datetime.strptime(str(father_ind['birt']), '%d %b %Y').year

        mother_ind = get_ind_by_id(fam["wife"], inds)
        if 'birt' not in mother_ind.__dict__.keys():
            continue
        ma_year_birth = datetime.datetime.strptime(str(mother_ind['birt']), '%d %b %Y').year

        marr_date = datetime.datetime.strptime(str(fam['marr']), '%d %b %Y').year

        if (marr_date - fa_year_birth) < 14 or (marr_date - ma_year_birth) < 14:
            return f"ERROR: FAMILY: {fam['marr'].line}: US10: Parents less than 14 years old!"


if __name__ == '__main__':
    inds, fams = geddata.get_inds_fams('../res/test_sprint2_all.ged')

    print(birth_after_death_of_parents(fams, inds))

    print(marriage_after_14(fams, inds))
