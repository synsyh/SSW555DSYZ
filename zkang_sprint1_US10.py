from gedparser import GEDParser


def marriage_after_14(fams, inds):
    """
    US10: Marriage date should be at least 14 years after birth date for a person
    :param fams:
    :param inds:
    :return:
    """
    for item in fams:
        marriage_date = item["marr"]
        hus_id = item["husb"]
        wife_id = item["wife"]
        for indi in inds:
            if indi["id"] == hus_id or indi["id"] == wife_id:
                print(indi["id"])
                print(indi["birt"])
                print(marriage_date)
                if int(marriage_date[0:4]) - int(indi["birt"][0:4]) < 14:
                    raise ValueError(indi["id"] + "marriage before 14!")
                elif int(marriage_date[0:4]) - int(indi["birt"][0:4]) == 14:
                    if int(marriage_date[5:7]) - int(indi["birt"][5:7]) > 0:
                        raise ValueError(indi["id"] + "marriage before 14!")
                    elif int(marriage_date[5:7]) - int(indi["birt"][5:7]) == 0:
                        if int(marriage_date[8:10]) >= int(indi["birt"][8:10]):
                            raise ValueError(indi["id"] + "marriage before 14!")
            else:
                continue
# def marriage_before_14():
#     p = gedparser.GEDParser('C:\\Users\\kzh\\PycharmProjects\\SSW555DSYZ\\res\\temp.ged')
#     inds = p.inds
#     fams = p.fams


if __name__ == '__main__':
    p = GEDParser('C:\\Users\\kzh\\PycharmProjects\\SSW555DSYZ\\res\\US10.ged')
    p.parser()
    try:
        marriage_after_14(p.fams, p.inds)
    except ValueError as VE:
        print(VE)