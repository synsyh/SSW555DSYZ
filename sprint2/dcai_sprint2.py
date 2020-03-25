"""
ssw555tmDSYZ2020spring-dcai_sprint2 by Yuning Sun
11:27 PM 3/22/20
Module documentation: 
"""
import datetime

from geddata import get_inds_fams


def birth_before_death(inds):
    results = []
    for ind in inds:
        if 'deat' in ind.__dict__.keys():
            birt = datetime.datetime.strptime(ind['birt'].value, '%d %b %Y')
            deat = datetime.datetime.strptime(ind['deat'].value, '%d %b %Y')
            if birt > deat:
                results.append(
                    f"ERROR: INDIVIDUAL: US03: {ind['birt'].line}: {ind['id'].value}: Birthday {birt} is after death.")
    return results


def marriage_before_divorce(fams):
    results = []
    for fam in fams:
        if 'div' in fam.__dict__.keys():
            if 'marr' in fam.__dict__.keys():
                marr = datetime.datetime.strptime(fam['marr'].value, '%d %b %Y')
                div = datetime.datetime.strptime(fam['div'].value, '%d %b %Y')
                if marr > div:
                    results.append(
                        f'ERROR: FAMILY: US04: {fam["div"].line}: {fam["id"].value}: Marriage should occur before divorce of spouses')
            else:
                results.append(
                    f'ERROR: FAMILY: US04: {fam["div"].line}: {fam["id"].value}: Divorce can only occur after marriage')
    return results


if __name__ == '__main__':
    inds, fams = get_inds_fams('../res/test_sprint2_all.ged')
    print(birth_before_death(inds))
    print(marriage_before_divorce(fams))
