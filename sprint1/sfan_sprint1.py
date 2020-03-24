from geddata import get_inds_fams, get_fams_by_id, get_name_by_id


def no_marries_to_children(inds, fams):
    marry_error_record = []
    for ind in inds:
        if len(ind['chil']) > 1:
            myfams = []
            for id in ind['fams']:
                myfams.append(get_fams_by_id(id, fams))
            for fam in myfams:
                for fam2 in myfams:
                    if fam['husb'] in fam2['chil']:
                        name = get_name_by_id(fam['husb'], inds)
                        marry_error_record.append(
                            f"ERROR: FAMILY: US17: line {fam['id'].line}: {name} marries to his mother {ind['name']}")
                    elif fam['wife'] in fam2['chil']:
                        name = get_name_by_id(fam['wife'], inds)
                        marry_error_record.append(
                            f"ERROR: FAMILY: US17: line {fam['id'].line}: {name} marries to his father {ind['name']}")
    if marry_error_record:
        return marry_error_record


def siblings_not_marry(inds, fams):
    error_record = []
    for fam in fams:
        for ind in inds:
            if len(ind['chil']) > 1:
                if fam['husb'] in ind['chil'] and fam['wife'] in ind['chil']:
                    name1 = get_name_by_id(fam['husb'], inds)
                    name2 = get_name_by_id(fam['wife'], inds)
                    error_record.append(
                        f"ERROR: FAMILY: line {fam['id'].line}US18 :the couple {name1} and {name2} are siblings")
    if error_record:
        return error_record


if __name__ == '__main__':
    inds, fams = get_inds_fams('../res/US17_18.ged')
    print(no_marries_to_children(inds, fams))
    print(siblings_not_marry(inds, fams))
