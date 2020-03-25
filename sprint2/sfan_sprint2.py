from geddata import get_inds_fams, get_name_by_id


def get_children_by_id(id, inds):
    """
    A function to get individual's children by his id
    :param id:
    :param inds:
    :return: a list with individual's children
    """
    childs = []
    for ind in inds:
        if ind['id'].value == id:
            for child in ind['chil']:
                childs.append(child)
    return childs


def first_cousin_should_not_marry(inds, fams):
    """
    A function to judge if first cousin marry to each other
    use another function get_children_by_id
    :param inds:
    :param fams:
    :return:
    """
    marry_error_record = []
    childs = []
    for fam in fams:
        if len(fam['chil']) > 1:
            for child in fam['chil']:
                childs.extend(get_children_by_id(child.value, inds))
            if childs:
                for fam in fams:
                    if fam['husb'].value in [child.value for child in childs]:
                        if fam['wife'].value in [child.value for child in childs]:
                            husb = get_name_by_id(fam['husb'], inds)
                            wife = get_name_by_id(fam['wife'], inds)
                            marry_error_record.append(
                                f"ERROR: FAMILY: US19: line{fam['id'].line}: Couple {husb} and {wife} are first cousins")
                childs.clear()
    if marry_error_record:
        return marry_error_record
    else:
        return 'all right'


def judge_father(adult, child, line, fams, inds):
    """
    judge child marries to his father or uncle
    :param adultid:
    :param childid:
    :return: error message
    """
    record = []
    for fam in fams:
        if child.value in [fam_child.value for fam_child in fam['chil']]:
            if fam['husb'].value == adult.value:
                wife = get_name_by_id(child, inds)
                husb = get_name_by_id(adult, inds)
                record.append(f"ERROR: FAMILY: US17: line{line}: {wife} marries to her father {husb}")
    else:
        wife = get_name_by_id(child, inds)
        husb = get_name_by_id(adult, inds)
        record.append(f"ERROR: FAMILY: US20: line{line}:{wife} marries to her ancle {husb}")

    return record


def judge_mother(adult, child, line, fams, inds):
    """
    judge child marries to his mother or aunt
    :param adultid:
    :param childid:
    :return: error message
    """
    record = []
    for fam in fams:
        if child.value in [fam_child.value for fam_child in fam['chil']]:
            if fam['wife'].value == adult.value:
                wife = get_name_by_id(adult, inds)
                husb = get_name_by_id(child, inds)
                record.append(f"ERROR: FAMILY: US17: line{line}: {husb} marries to his mother {wife}")
    else:
        wife = get_name_by_id(adult, inds)
        husb = get_name_by_id(child, inds)
        record.append(f"ERROR: FAMILY: US20: line{line}: {husb} marries to his aunt {wife}")
    return record


def aunts_and_uncles(inds, fams):
    """

    :param inds:
    :param fams:
    :return:
    """
    marry_error_record = []
    childs = []
    uncles = []
    for fam in fams:
        if len(fam['chil']) > 1:
            for child in fam['chil']:
                uncles.append(child)
                childs.extend(get_children_by_id(child.value, inds))
            for uncle in uncles:
                for fam in fams:
                    if uncle.value == fam['husb'].value:
                        if fam['wife'].value in [child.value for child in childs]:
                            marry_error_record.extend(judge_father(uncle, fam['wife'], fam['id'].line, fams, inds))
                    elif uncle.value == fam['wife'].value:
                        if fam['husb'].value in [child.value for child in childs]:
                            marry_error_record.extend(judge_mother(uncle, fam['husb'], fam['id'].line, fams, inds))
            childs.clear()
            uncles.clear()
    if marry_error_record:
        return marry_error_record
    else:
        return 'all right'


if __name__ == '__main__':
    inds, fams = get_inds_fams('../res/test_sprint2_all.ged')
    print(first_cousin_should_not_marry(inds, fams))
    print(aunts_and_uncles(inds, fams))
