import datetime

from geddata import get_inds_fams, get_ind_by_id


def less_than_150_years_old(inds):
    results = ''
    for ind in inds:
        if ind['age'].value >= 150:
            results += f"ERROR: INDIVIDUAL: US07: line{ind['age'].line}: {ind['id'].value}: age {ind['age'].value} should less than 150."
    return results


def birth_before_marriage_of_parents(inds, fams):
    results = ''
    for fam in fams:
        marr = fam['marr']
        marr_date = datetime.datetime.strptime(marr.value, '%d %b %Y')
        chils = fam['chil']
        for chil_id in chils:
            chil = get_ind_by_id(chil_id, inds)
            birth_date = chil['birt'].value
            birth_date = datetime.datetime.strptime(birth_date, '%d %b %Y')
            if birth_date < marr_date:
                results += f"ERROR: INDIVIDUAL: US08: line{chil['birt'].line}: {chil['id'].value}: Child birthday {chil['birt'].value} before parents' marriage date {marr.value}\n"
            if 'div' in fam.__dict__.keys():
                div = fam['div']
                div_date = datetime.datetime.strptime(div.value, '%d %b %Y')
                if (birth_date - div_date).days > 270:
                    results += f"ERROR: INDIVIDUAL: US08: line{chil['birt'].line}: {chil['id'].value}: Child birthday {chil['birt'].value} is more than 9 months after parents' divorce date {marr.value}\n"
    return results


if __name__ == '__main__':
    inds, fams = get_inds_fams('../res/US08.ged')
    print(birth_before_marriage_of_parents(inds, fams))
    print()
