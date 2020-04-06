from datetime import datetime

from geddata import get_inds_fams, get_ind_by_id


def marriage_before_death(inds, fams):
    """
    Marriage should occur before death of either spouse
    @param inds:
    @param fams:
    @return:
    """
    results = []
    for fam in fams:
        marr = fam['marr']
        marr_time = datetime.strptime(marr.value, '%d %b %Y')
        husb = get_ind_by_id(fam['husb'], inds)
        wife = get_ind_by_id(fam['wife'], inds)
        if 'deat' in husb.__dict__.keys():
            deat_husb = datetime.strptime(husb['deat'].value, '%d %b %Y')
            if marr_time > deat_husb:
                results.append(
                    f"ERROR: FAMILY: US05: {marr.line}: {husb['id'].value}: Marriage {marr.value} is after death.")
        if 'deat' in wife.__dict__.keys():
            deat_wife = datetime.strptime(wife['deat'].value, '%d %b %Y')
            if marr_time > deat_wife:
                results.append(
                    f"ERROR: FAMILY: US05: {marr.line}: {wife['id'].value}: Marriage {marr.value} is after death.")
    return results


def divorce_before_death(inds, fams):
    """
    Divorce can only occur before death of both spouses
    @param inds:
    @param fams:
    @return:
    """
    results = []
    for fam in fams:
        if 'div' in fam.__dict__.keys():
            div = fam['div']
            div_time = datetime.strptime(div.value, '%d %b %Y')
        else:
            continue
        husb = get_ind_by_id(fam['husb'], inds)
        wife = get_ind_by_id(fam['wife'], inds)
        if 'deat' in husb.__dict__.keys():
            deat_husb = datetime.strptime(husb['deat'].value, '%d %b %Y')
            if div_time > deat_husb:
                results.append(
                    f"ERROR: FAMILY: US06: {div.line}: {husb['id'].value}: Divorce {div.value} is after death.")
        if 'deat' in wife.__dict__.keys():
            deat_wife = datetime.strptime(wife['deat'].value, '%d %b %Y')
            if div_time > deat_wife:
                results.append(
                    f"ERROR: FAMILY: US06: {div.line}: {wife['id'].value}: Divorce {div.value} is after death.")
    return results


if __name__ == '__main__':
    inds, fams = get_inds_fams('../res/US06.ged')
    print(marriage_before_death(inds,fams))
    print(divorce_before_death(inds, fams))
