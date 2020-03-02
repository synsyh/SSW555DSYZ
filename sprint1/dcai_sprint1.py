import datetime

from gedparser import GEDParser


def dates_before_current_date(para):
    """
    US01: Dates (birth, marriage, divorce, death) should not be after the current date
    @param para:
    @return:
    """
    inds = para.inds
    fams = para.fams
    today = datetime.datetime.today()
    results = []
    for ind in inds:
        birt = ind['birt']
        birt = datetime.datetime.strptime(birt, '%Y-%m-%d')
        if today < birt:
            results.append(f'ERROR: INDIVIDUAL: US01: Birthday {birt} is after today')
        try:
            deat = ind['deat']
        except KeyError:
            continue
        if deat == 'NA':
            continue
        else:
            deat = datetime.datetime.strptime(deat, '%Y-%m-%d')
            if today < deat:
                results.append(f'ERROR: INDIVIDUAL: US01: Death {deat} day is after today')

    for fam in fams:
        marr = fam['marr']
        marr = datetime.datetime.strptime(marr, '%Y-%m-%d')
        if today < marr:
            results.append(f'ERROR: FAMILY: US01: Marriage date {marr} is after today')

        divorced = fam['divorced']
        if divorced == 'False':
            continue
        else:
            divorced = datetime.datetime.strptime(divorced, '%Y-%m-%d')
            if today < divorced:
                results.append(f'ERROR: FAMILY: US01: Divorce date {divorced} is after today')
    if len(results) == 1:
        return results[0]
    elif results:
        return results


def birth_before_marriage(para):
    """
    US02: Birth should occur before marriage of an individual
    @param para:
    @return:
    """
    inds = para.inds
    fams = para.fams

    for ind in inds:
        ids_fam_by_ind = ind['fams']
        for id_fam_by_ind in ids_fam_by_ind:
            for fam in fams:
                id_fam_by_fam = fam['id']
                if id_fam_by_fam == id_fam_by_ind:
                    marr = fam['marr']
                    marr = datetime.datetime.strptime(marr, '%Y-%m-%d')
                    birt = ind['birt']
                    birt = datetime.datetime.strptime(birt, '%Y-%m-%d')
                    if not birt < marr:
                        if ind['sex'] == 'F':
                            return f"ERROR: FAMILY: US02: Husband's birthday {birt} is after marriage date {marr}"
                        else:
                            return f"ERROR: FAMILY: US02: Wife's birthday {birt} is after marriage date {marr}"


def main():
    p = GEDParser('res/US01_02.ged')
    p.parser()
    print(dates_before_current_date(p))
    print(birth_before_marriage(p))


if __name__ == '__main__':
    main()
