from geddata import get_inds_fams, print_inds, print_fams
from sprint1.dcai_sprint1 import dates_before_current_date, birth_before_marriage
from sprint1.sfan_sprint1 import no_marries_to_children, siblings_not_marry
from sprint1.ysun_sprint1 import include_individual_ages, corresponding_entries
from sprint1.zkang_sprint1 import birth_after_death_of_parents, marriage_after_14


def output():
    inds, fams = get_inds_fams('res/test_all_user_stories.ged')
    print_inds(inds)
    print_fams(fams)

    # Danping Cai
    print(dates_before_current_date(inds, fams))
    print(birth_before_marriage(inds, fams))
    # Zihao Kang
    print(birth_after_death_of_parents(fams, inds))
    print(marriage_after_14(fams, inds))
    # Siteng Fan
    print(', '.join(no_marries_to_children(inds, fams)))
    print(', '.join(siblings_not_marry(inds, fams)))
    # Yuning Sun
    print(', '.join(include_individual_ages(inds)))
    print(', '.join(corresponding_entries(inds, fams)))


if __name__ == '__main__':
    output()
