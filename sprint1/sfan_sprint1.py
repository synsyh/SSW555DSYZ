from gedparser import GEDParser, get_fam_by_id, get_name_by_id


def no_marries_to_children(p):
    marry_error_record = []
    for ind in p.inds:
        if 'chil' in ind:
            myfams = []
            for id in ind['fams']:
                myfams.append(get_fam_by_id(id, p.fams))
            for fam in myfams:
                for fam2 in myfams:
                    if fam['husb'] in fam2['chil']:
                        name = get_name_by_id(fam['husb'], p.inds)
                        marry_error_record.append(f"ERROR: FAMILY: US17: {name} marries to his mother {ind['name']}")
                    elif fam['wife'] in fam2['chil']:
                        name = get_name_by_id(fam['wife'], p.inds)
                        marry_error_record.append(f"ERROR: FAMILY: US17: {name} marries to his father {ind['name']}")
    if marry_error_record:
        return marry_error_record


def siblings_not_marry(p):
    error_record = []
    for fam in p.fams:
        for ind in p.inds:
            if ('chil' in ind) and len(ind['chil']) > 1:
                if fam['husb'] in ind['chil'] and fam['wife'] in ind['chil']:
                    name1 = get_name_by_id(fam['husb'], p.inds)
                    name2 = get_name_by_id(fam['wife'], p.inds)
                    error_record.append(f"ERROR: FAMILY: US18 :the couple {name1} and {name2} are siblings")
    if error_record:
        return error_record


if __name__ == '__main__':
    p = GEDParser('../res/US17_18.ged')
    p.parser()
    print(no_marries_to_children(p))
    print(siblings_not_marry(p))
