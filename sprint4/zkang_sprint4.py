import geddata
from geddata import get_ind_by_id
import datetime


def no_bigamy(fams, inds):
    """
    US11: No bigamy
    Marriage should not occur during marriage to another spouse
    """
    pass


def siblings_spacing(fams, inds):
    """
    US13: Siblings spacing
    Birth dates of siblings should be more than 8 months apart or less than 2 days apart
    """
    for fam in fams:
        child_birth_date_list = []
        for child_id in fam['chil']:
            child_ind = get_ind_by_id(child_id, inds)
            child_birth_date = datetime.datetime.strptime(str(child_ind['birt']), '%d %b %Y')
            # print(child_birth_date)
            child_birth_date_list.append(child_birth_date)
            # print(child_birth_date_list)
        for date1 in child_birth_date_list:
            for date2 in child_birth_date_list:
                time_diff = date2 - date1
                if datetime.timedelta(days=240) > time_diff > datetime.timedelta(days=2):
                    return f"ERROR: FAMILY: {fam['id']} US13: Birth dates of siblings should be more than 8 months apart or less than 2 days apart!"


if __name__ == '__main__':
    inds, fams = geddata.get_inds_fams('../res/US13.ged')
    print(siblings_spacing(fams, inds))
    # child_birth_date_list = []
    # for fam in fams:
    #     for child_id in fam['chil']:
    #         child_ind = get_ind_by_id(child_id, inds)
    #         child_birth_date = datetime.datetime.strptime(str(child_ind['birt']), '%d %b %Y')
    #         print(child_birth_date)
    #         child_birth_date_list.append(child_birth_date)
    #         print(child_birth_date_list)
    #         for date1 in child_birth_date_list:
    #             for date2 in child_birth_date_list:
    #                 time_diff = date2 - date1
    #                 print(time_diff > datetime.timedelta(days=244))