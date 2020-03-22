import geddata
from geddata import get_ind_by_id
import datetime


def parents_not_too_old(fams, inds):
    """
    US12: Parents not too old.
    Mother should be less than 60 years older than her children and father should be less than 80 years older than his children
    """
    for fam in fams:
        # print('husb"')
        # print(fam['husb'])
        # print('wife:')
        # print(fam['wife'])
        father_ind = get_ind_by_id(fam["husb"], inds)
        fa_year_birth = datetime.datetime.strptime(str(father_ind['birt']), '%d %b %Y').year
        print(fa_year_birth)
        mother_ind = get_ind_by_id(fam["wife"], inds)
        ma_year_birth = datetime.datetime.strptime(str(mother_ind['birt']), '%d %b %Y').year
        for child_id in fam['chil']:
            print('child:')
            print(child_id)
            child_ind = get_ind_by_id(child_id, inds)
            print(child_ind['birt'])
            ch_year_birth = datetime.datetime.strptime(str(child_ind['birt']), '%d %b %Y').year
            if (ma_year_birth - ch_year_birth) > 60 or (fa_year_birth - ch_year_birth) > 80:
                return f"ERROR: line ", child_ind["birt"].line, "US12: Parents too old!"


def too_many_siblings(fams, inds):
    """
    US15: Fewer than 15 siblings
    There should be fewer than 15 siblings in a family
    """
    for fam in fams:
        child_num = 0
        for child in fam['chil']:
            child_num += 1
        if child_num >= 15:
            return f"ERROR: line ", fam.line, "US15: too many siblings!"
    # for fam in fams:
    #     father_ind = get_ind_by_id(fam["husb"], inds)
    #     mother_ind = get_ind_by_id(fam["wife"], inds)
    #     for child_id in fam['chil']:
    #         child_ind = get_ind_by_id(child_id, inds)
    #
    #         try:
    #             # print("father death :" + father_ind["deat"])
    #             # print("mother death :" + mother_ind["deat"])
    #             # print("child birth :" + child_ind["birt"])
    #
    #             if left_before_right(father_ind["deat"], child_ind["birt"]):
    #                 return "ERROR: INDIVIDUAL: US09: " + child_ind["id"] + " Child birth after parent death!"


if __name__ == '__main__':
    inds, fams = geddata.get_inds_fams('res/valid.ged')
    # print(inds)
    # print(fams)
    # print(fams[0])

    print(parents_not_too_old(fams, inds))
    # print(parents_not_too_old(fams, inds))

