from gedparser import GEDParser
from gedparser import get_ind_by_id


def left_before_right(left, right):
    if int(left[0:4]) < int(right[0:4]):
        return True
    elif int(left[0:4]) == int(right[0:4]):
        if int(left[5:7]) < int(right[5:7]):
            return True
        elif int(left[5:7]) == int(right[5:7]):
            if int(left[8:10]) < int(right[8:10]):
                return True

    return False


def birth_after_d_p(fams, inds):
    print(inds)
    print(fams)
    for fam in fams:
        father_ind = get_ind_by_id(fam["husb"], inds)
        mother_ind = get_ind_by_id(fam["wife"], inds)
        for child_id in fam['chil']:
            child_ind = get_ind_by_id(child_id, inds)

            try:
                print(father_ind["deat"])
                print(mother_ind["deat"])
                print(child_ind["birt"])

                if left_before_right(father_ind["deat"], child_ind["birt"]) or left_before_right(mother_ind["deat"],
                                                                                                 child_ind["birt"]):
                    print("Child birth after parent death!")

            except KeyError:
                continue
            except TypeError:
                continue


if __name__ == '__main__':
    p = GEDParser('C:\\Users\\kzh\\PycharmProjects\\SSW555DSYZ\\res\\ysun.ged')
    p.parser()
    birth_after_d_p(p.fams, p.inds)
