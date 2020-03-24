from geddata import get_inds_fams, print_fams, print_inds
from sprint2.sfan_sprint2 import aunts_and_uncles, first_cousin_should_not_marry
from sprint2.dcai_sprint2 import marriage_before_divorce, birth_before_death
from sprint2.zkang_sprint2 import too_many_siblings, parents_not_too_old


def output_03():
    inds, fams = get_inds_fams('res/US03.ged')
    print_inds(inds)
    print_fams(fams)
    return birth_before_death(inds)


def output_04():
    inds, fams = get_inds_fams('res/US04.ged')
    print_inds(inds)
    print_fams(fams)
    return marriage_before_divorce(fams)


def output_15():
    inds, fams = get_inds_fams('res/US15.ged')
    print_inds(inds)
    print_fams(fams)
    return too_many_siblings(inds, fams)


def output_12():
    inds, fams = get_inds_fams('res/US12.ged')
    print_fams(fams)
    print_inds(inds)
    return parents_not_too_old(fams, inds)


def output_19_20():
    record = []
    inds, fams = get_inds_fams('res/US19_20.ged')
    print_inds(inds)
    print_fams(fams)
    record.extend(aunts_and_uncles(inds, fams))
    record.extend(first_cousin_should_not_marry(inds, fams))
    return record


if __name__ == '__main__':
    for item in output_03():
        print(item)
    for item in output_04():
        print(item)
    print(output_15())
    print(output_12())
    for item in output_19_20():
        print(item)
