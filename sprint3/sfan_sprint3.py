from geddata import get_inds_fams


def correct_gender(inds, fams):
    """
    husband in family should be male and wife in family should be female
    :param inds:
    :param fams:
    :return: list of error information
    """
    male, female = [], []
    record = []
    for ind in inds:
        if ind['sex'].value == 'M':
            male.append(ind['id'].value)
        else:
            female.append(ind['id'].value)
    for fam in fams:
        if fam['husb'].value in female:
            record.append(f"ERROR: FAMILY: US21: line{fam['husb'].line}: gender of husband in family should be male")
        if fam['wife'].value in male:
            record.append(f"ERROR: FAMILY: US21: line{fam['wife'].line}: gender of wife in family should be female")
    return record


def unique_id(inds, fams):
    record = []
    for ind in inds:
        for ind2 in inds[inds.index(ind)+1:]:
            if ind['id'].value == ind2['id'].value:
                record.append(
                    f"ERROR: INDIVIDUAL: US22: line{ind['id'].line} and line{ind2['id'].line}: These 2 individuals have same id")
    for fam in fams:
        for fam2 in fams[fams.index(fam)+1:]:
            if fam['id'].value == fam2['id'].value:
                record.append(
                    f"ERROR: FAMILY: US22: line{fam['id'].line} and line{fam2['id'].line}: These 2 families have same id")
    return record


if __name__ == '__main__':
    inds, fams = get_inds_fams('../res/US22.ged')
    print(correct_gender(inds, fams))
    print(unique_id(inds, fams))
