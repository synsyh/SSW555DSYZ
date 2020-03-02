"""
ssw555tmDSYZ2020spring-gedparser1 by Yuning Sun
12:02 PM 2/27/20
Module documentation: 
"""
import prettytable

from geddate import date_transit, get_age
from gedparser import get_ind_by_id


class GEDParser:
    def __init__(self, file_name):
        # create initial variables
        self.file_name = file_name
        self.indis, self.fams, self.oths = [], [], []

    def parser(self):
        item_type, item_type1 = '', ''
        line_num = 0
        item = dict()
        with open(self.file_name, encoding='UTF-8-sig') as f:
            line = f.readline()
            line_num += 1
            words = line.strip().split(' ', maxsplit=2)
            while line:
                if words[0] == '0':
                    if item:
                        if item_type == 'INDI':
                            self.indis.append(item)
                        elif item_type == 'FAM':
                            self.fams.append(item)
                        else:
                            self.oths.append(item)
                    item = dict()
                    item_type = words[-1]
                    item[item_type] = {item_type: words[1], 'LINE': line_num}
                elif words[0] == '1':
                    # if next line has same tag as last line. For example, double lines for FAMS
                    if words[1] == item_type1:
                        if 0 in item[item_type1].keys():
                            item[item_type1][list(item[item_type1].keys())[-1] + 1] = {item_type1: words[-1],
                                                                                       'LINE': line_num}
                        else:
                            tmp_item = dict()
                            tmp_item[0] = item[item_type1]
                            tmp_item[1] = {item_type1: words[-1], 'LINE': line_num}
                            item[item_type1] = tmp_item
                    else:
                        item_type1 = words[1]
                        item[item_type1] = {item_type1: words[-1], 'LINE': line_num}
                elif words[0] == '2':
                    item_type2 = words[1]
                    item[item_type1][item_type2] = {item_type2: words[-1], 'LINE': line_num}
                elif words[0] == '3':
                    item_type3 = words[1]
                    item[item_type1][item_type2][item_type3] = {item_type3: words[-1], 'LINE': line_num}
                line = f.readline()
                line_num += 1
                words = line.strip().split(' ', maxsplit=2)
        print()


def indi_info(raw_indis, raw_fams):
    indis, fams = [], []
    for raw_indi in raw_indis:
        indi = {}
        indi['id'] = raw_indi['INDI']['INDI']
        indi['name'] = raw_indi['NAME']['NAME']
        indi['sex'] = raw_indi['SEX']['SEX']
        indi['birt'] = date_transit(raw_indi['BIRT']['DATE']['DATE'])
        if 'DEAT' in raw_indi.keys():
            indi['deat'] = date_transit(raw_indi['DEAT']['DATE']['DATE'])
            indi['age'] = get_age(indi['birt'], indi['deat'])
            indi['alive'] = 'True'
        else:
            indi['deat'] = 'NA'
            indi['age'] = get_age(indi['birt'])
            indi['alive'] = 'False'
        indi['fams'] = set()
        if 'FAMS' in raw_indi.keys():
            if 0 in raw_indi['FAMS'].keys():
                for item in raw_indi['FAMS'].values():
                    indi['fams'].add(item['FAMS'])
            else:
                indi['fams'] = {raw_indi['FAMS']['FAMS']}
        indi['chil'] = set()
        indis.append(indi)
    for raw_fam in raw_fams:
        fam = {}
        fam['id'] = raw_fam['FAM']['FAM']
        fam['marr'] = date_transit(raw_fam['MARR']['DATE']['DATE'])
        if 'DIV' in raw_fam.keys():
            fam['divorced'] = date_transit(raw_fam['DIV']['DATE']['DATE'])
        else:
            fam['divorced'] = 'False'
        if 'HUSB' in raw_fam.keys():
            fam['husb'] = raw_fam['HUSB']['HUSB']
            fam['husb_name'] = get_ind_by_id(fam['husb'], indis)['name']
        else:
            fam['husb'] = 'NA'
            fam['husb_name'] = 'NA'
        if 'WIFE' in raw_fam.keys():
            fam['wife'] = raw_fam['WIFE']['WIFE']
            fam['wife_name'] = get_ind_by_id(fam['wife'], indis)['name']
        else:
            fam['wife'] = 'NA'
            fam['wife_name'] = 'NA'
        fam['chil'] = set()
        if 'CHIL' in raw_fam.keys():
            if 0 in raw_fam['CHIL'].keys():
                for chil in raw_fam['CHIL'].values():
                    fam['chil'].add(chil['CHIL'])
            else:
                fam['chil'] = {raw_fam['CHIL']['CHIL']}
            husb = get_ind_by_id(fam['husb'], indis)
            if husb:
                husb['chil'] = husb['chil'].union(fam['chil'])
            wife = get_ind_by_id(fam['wife'], indis)
            if wife:
                wife['chil'] = wife['chil'].union(fam['chil'])
        fams.append(fam)
    return indis, fams


def print_fams(fams):
    pt = prettytable.PrettyTable(
        ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children'])
    for fam in fams:
        pt.add_row(
            [fam['id'], fam['marr'], fam['divorced'], fam['husb'], fam['husb_name'], fam['wife'], fam['wife_name'],
             fam['chil']])
    print(pt)


def print_inds(inds):
    pt = prettytable.PrettyTable(['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse'])
    for ind in inds:
        pt.add_row(
            [ind['id'], ind['name'], ind['sex'], ind['birt'], ind['age'], ind['alive'], ind['deat'], str(ind['chil']),
             str(ind['fams'])])
    print(pt)


if __name__ == '__main__':
    p = GEDParser('res/ysun.ged')
    p.parser()
    inds, fams = indi_info(p.indis, p.fams)
    print_fams(fams)
    print_inds(inds)
    print()
