from gedparser import GEDParser
from sprint1.sfan_sprint1 import no_marries_to_children, siblings_not_marry
from sprint1.ysun_sprint1 import corresponding_entries, include_individual_ages
from sprint1.dcai_sprint1 import dates_before_current_date, birth_before_marriage
from sprint1.zkang_sprint1 import birth_after_d_p, marriage_after_14


def output():
    p = GEDParser('res/test_sprint1_all.ged')
    p.parser()
    print(p.print_fams())

    for item in no_marries_to_children(p):
        print(item)
    for item in siblings_not_marry(p):
        print(item)
    for item in corresponding_entries(p):
        print(item)
    for item in dates_before_current_date(p):
        print(item)
    print(birth_before_marriage(p))
    print(birth_after_d_p(p.fams, p.inds))
    print(marriage_after_14(p.fams, p.inds))
    print(p.print_indi())

if __name__ == '__main__':
    output()
