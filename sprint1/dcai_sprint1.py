import datetime

from geddata import get_inds_fams


def dates_before_current_date(inds, fams):
    """
    US01: Dates (birth, marriage, divorce, death) should not be after the current date
    @param para:
    @return:
    """
    today = datetime.datetime.today()
    results = []
    for ind in inds:
        if 'birt' not in ind.__dict__.keys():
            continue
        birt = ind['birt'].value
        birt = datetime.datetime.strptime(birt, '%d %b %Y')
        if today < birt:
            results.append(
                f'ERROR: INDIVIDUAL: US01: {ind["birt"].line}: {ind["id"].value}: Birthday {birt} is after today')
        if 'deat' in ind.__dict__.keys():
            deat = ind['deat']
            deat = datetime.datetime.strptime(deat.value, '%d %b %Y')
            if today < deat:
                results.append(
                    f'ERROR: INDIVIDUAL: US01: {ind["deat"].line}: {ind["id"].value}: Death {deat} day is after today')

    for fam in fams:
        if 'marr' not in fam.__dict__.keys():
            continue
        marr = fam['marr'].value
        marr = datetime.datetime.strptime(marr, '%d %b %Y')
        if today < marr:
            results.append(
                f'ERROR: FAMILY: US01: {fam["marr"].line}: {fam["id"].value}: Marriage date {marr} is after today')
        if 'div' in fam.__dict__.keys():
            divorced = datetime.datetime.strptime(fam['div'].value, '%d %b %Y')
            if today < divorced:
                results.append(
                    f'ERROR: FAMILY: US01: {fam["div"].line}: {fam["id"].value}: Divorce date {divorced} is after today')
    if len(results) == 1:
        return results[0]
    elif results:
        return results


def birth_before_marriage(inds, fams):
    """
    US02: Birth should occur before marriage of an individual
    @param para:
    @return:
    """
    for ind in inds:
        ids_fam_by_ind = ind['fams']
        for id_fam_by_ind in ids_fam_by_ind:
            for fam in fams:
                id_fam_by_fam = fam['id'].value
                if id_fam_by_fam == id_fam_by_ind.value:
                    if 'birt' not in ind.__dict__.keys() or 'marr' not in fam.__dict__.keys():
                        continue
                    marr = fam['marr'].value
                    marr = datetime.datetime.strptime(marr, '%d %b %Y')
                    birt = ind['birt'].value
                    birt = datetime.datetime.strptime(birt, '%d %b %Y')
                    if not birt < marr:
                        if ind['sex'].value == 'F':
                            return f"ERROR: FAMILY: US02: {fam['marr'].line}: {fam['id'].value}: Husband's birthday {birt} is after marriage date {marr}"
                        else:
                            return f"ERROR: FAMILY: US02: {fam['marr'].line}: {fam['id'].value}: Wife's birthday {birt} is after marriage date {marr}"


def main():
    inds, fams = get_inds_fams('../res/test_sprint2_all.ged')
    print(dates_before_current_date(inds, fams))
    print(birth_before_marriage(inds, fams))
    # print(birth_before_marriage(p))


if __name__ == '__main__':
    main()
