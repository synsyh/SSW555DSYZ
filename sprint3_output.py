from geddata import get_inds_fams, print_inds, print_fams
from sprint1.dcai_sprint1 import dates_before_current_date, birth_before_marriage
from sprint1.sfan_sprint1 import no_marries_to_children, siblings_not_marry
from sprint1.ysun_sprint1 import include_individual_ages, corresponding_entries
from sprint1.zkang_sprint1 import birth_after_death_of_parents, marriage_after_14
from sprint2.dcai_sprint2 import birth_before_death, marriage_before_divorce
from sprint2.sfan_sprint2 import first_cousin_should_not_marry, aunts_and_uncles
from sprint2.ysun_sprint2 import check_date_valid
from sprint2.zkang_sprint2 import parents_not_too_old, too_many_siblings
from sprint3.dcai_sprint3 import marriage_before_death, divorce_before_death
from sprint3.sfan_sprint3 import correct_gender, unique_id
from sprint3.zkang_sprint3 import multiple_births, male_last_names
from sprint3.ysun_sprint3 import list_deceased, order_sibling_by_age


def output():
    inds, fams = get_inds_fams('res/test_all_user_stories.ged')
    print_inds(inds)
    print_fams(fams)
    # Sprint1
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
    # Sprint2
    # Danping Cai
    print(','.join(birth_before_death(inds)))
    print(','.join(marriage_before_divorce(fams)))
    # Zihao Kang
    print(parents_not_too_old(fams, inds))
    print(too_many_siblings(fams, inds))
    # Siteng Fan
    print(','.join(first_cousin_should_not_marry(inds, fams)))
    print(','.join(aunts_and_uncles(inds, fams)))
    # Yuning Sun
    try:
        inds, fams = get_inds_fams('res/US42_1.ged')
        for ind in inds:
            check_date_valid(ind, 'ind')
        for fam in fams:
            check_date_valid(fam, 'fam')
    except ValueError as e:
        print(e)
    # Sprint4
    # Danping Cai
    print(','.join(marriage_before_death(inds, fams)))
    print(','.join(divorce_before_death(inds, fams)))
    # Siteng Fan
    print(','.join(correct_gender(inds, fams)))
    print(','.join(unique_id(inds, fams)))
    # Zihao Kang
    print(','.join(multiple_births(fams, inds)))
    print(','.join(male_last_names(fams, inds)))
    # Yuning Sun


if __name__ == '__main__':
    output()
