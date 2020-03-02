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
    print(inds)
    print(fams)
    for fam in fams:
        father_ind = get_ind_by_id(fam["husb"], inds)
        mother_ind = get_ind_by_id(fam["wife"], inds)
        for child_id in fam['chil']:
            child_ind = get_ind_by_id(child_id, inds)

            try:
                print("father death :" + father_ind["deat"])
                print("mother death :" + mother_ind["deat"])
                print("child birth :" + child_ind["birt"])

                if left_before_right(father_ind["deat"], child_ind["birt"]) :
                    raise ValueError(child_ind["id"] + "Child birth after parent death!")

                elif left_before_right(mother_ind["deat"], child_ind["birt"]):
                    raise ValueError(child_ind["id"] + "Child birth after parent death!")

            except KeyError:
                continue
            except TypeError:
                continue


if __name__ == '__main__':
    p = GEDParser('C:\\Users\\kzh\\PycharmProjects\\SSW555DSYZ\\res\\US09.ged')
    p.parser()
    try:
        birth_after_d_p(p.fams, p.inds)
    except ValueError as VE:
        print(VE)