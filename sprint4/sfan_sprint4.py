from geddata import get_inds_fams


def unique_name_and_birth(inds,fams):
    recordind = []
    record = []
    for ind in inds:
        if ind['name'].value in [rind['name'].value for rind in recordind]:
            if ind['birt'].value in [rind['birt'].value for rind in recordind]:
                line2 = [rind['name'].line for rind in recordind if rind['name'].value == ind['name'].value][0]
                record.append(
                    f"ERROR: INDIVIDUAL: US23: line{ind['name'].line} and line {line2}: these two guys have same name and birthday")
        else:
            recordind.append(ind)
    return record


def unique_families_by_spouse(inds, fams):
    recordfam = []
    recordmarr = []
    record = []
    for fam in fams:
        if [fam['husb'].value, fam['wife'].value] in recordfam:
            if fam['marr'].value in [rmar.value for rmar in recordmarr]:
                line2 = [rmar.line for rmar in recordmarr if rmar.value == fam['marr'].value][0]
                record.append(
                    f"ERROR: INDIVIDUAL: US23: line{fam['marr'].line} and line {line2}: these two families have same spouses and marry date")
        else:
            recordfam.append([fam['husb'].value, fam['wife'].value])
            recordmarr.append(fam['marr'])
    return record


if __name__ == '__main__':
    inds, fams = get_inds_fams('../res/US24.ged')
    print(unique_name_and_birth(inds,fams))
    print(unique_families_by_spouse(inds, fams))
