from gedparser import GEDParser
from gedparser import get_ind_by_id
from gedparser import left_before_right


def birth_after_d_p(fams, inds):
    """
    US09: Child should born before the death of the parent.
    :param fams:
    :param inds:
    :return:
    """
    # print(inds)
    # print(fams)
    for fam in fams:
        father_ind = get_ind_by_id(fam["husb"], inds)
        mother_ind = get_ind_by_id(fam["wife"], inds)
        for child_id in fam['chil']:
            child_ind = get_ind_by_id(child_id, inds)

            try:
                # print("father death :" + father_ind["deat"])
                # print("mother death :" + mother_ind["deat"])
                # print("child birth :" + child_ind["birt"])

                if left_before_right(father_ind["deat"], child_ind["birt"]):
                    return "ERROR: INDIVIDUAL: US09: " + child_ind["id"] + " Child birth after parent death!"

                elif left_before_right(mother_ind["deat"], child_ind["birt"]):
                    return "ERROR: INDIVIDUAL: US09: " + child_ind["id"] + " Child birth after parent death!"
            except KeyError:
                continue
            except TypeError:
                continue


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
                # print(indi["id"])
                # print(indi["birt"])
                # print(marriage_date)
                if int(marriage_date[0:4]) - int(indi["birt"][0:4]) < 14:
                    return "ERROR: FAMILY: US10: " + (indi["id"] + " marriage before 14!")
                elif int(marriage_date[0:4]) - int(indi["birt"][0:4]) == 14:
                    if int(marriage_date[5:7]) - int(indi["birt"][5:7]) > 0:
                        return "ERROR: INDIVIDUAL: US09: " + (indi["id"] + "marriage before 14!")
                    elif int(marriage_date[5:7]) - int(indi["birt"][5:7]) == 0:
                        if int(marriage_date[8:10]) >= int(indi["birt"][8:10]):
                            return "ERROR: INDIVIDUAL: US09: " + (indi["id"] + "marriage before 14!")
            else:
                continue


if __name__ == '__main__':
    p = GEDParser('../res/US09.ged')
    p.parser()
    print(birth_after_d_p(p.fams, p.inds))
