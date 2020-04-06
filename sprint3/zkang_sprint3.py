import geddata
from geddata import get_ind_by_id
import datetime


def multiple_births(fams, inds):
    """
    US14: Multiple births.
    No more than five siblings should be born at the same time
    """
    for fam in fams:
        if len(fam['chil']) >= 5:
            for child_id in fam['chil']:
                child_birth_year_list = []
                child_birth_year_set = set()
                child_ind = get_ind_by_id(child_id, inds)
                if 'birt' not in child_ind.__dict__.keys():
                    continue
                ch_birth_year_month = datetime.datetime.strptime(str(child_ind['birt']), '%d %b %Y').year * 10 + datetime.datetime.strptime(str(child_ind['birt']), '%d %b %Y').month
                child_birth_year_list.append(ch_birth_year_month)
                child_birth_year_set.add(ch_birth_year_month)
                if len(child_birth_year_list) - len(child_birth_year_set) < 5:
                    return f"ERROR: FAMILY: LINE: {child_ind['birt'].line} US12: more than five siblings born at the same time!"


def male_last_names(fams, inds):
    """
    US16: Male last names
    All male members of a family should have the same last name
    """
    for fam in fams:
        father_ind = get_ind_by_id(fam["husb"], inds)
        if 'sex' not in father_ind.__dict__.keys():
            continue
        fa_name = str(father_ind['name'])
        for child_id in fam['chil']:
            # print('child:')
            # print(child_id)
            child_ind = get_ind_by_id(child_id, inds)
            ch_name = str(child_ind['name'])
            ch_gender = str(child_ind['sex'])
            # print(str(ch_name)[-3:])
            # print(ch_gender == 'M')
            if 'sex' not in child_ind.__dict__.keys():
                continue
            if ch_gender == 'M' and fa_name[-3:] != ch_name[-3:]:
                return f"ERROR: FAMILY: LINE: {child_ind['name'].line} US16: All male members of a family should have the same last name!"


if __name__ == '__main__':
    inds, fams = geddata.get_inds_fams('../res/US16.ged')
    print(male_last_names(fams, inds))
    inds, fams = geddata.get_inds_fams('../res/US15.ged')
    print(multiple_births(fams, inds))

