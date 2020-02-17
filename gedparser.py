"""
ssw555tmDSYZ2020spring-gedparser by Yuning Sun
18:04 2020/2/7
Module documentation: Parser to parser ged file and save information
"""

import prettytable

from geddate import date_transit, get_age


def get_name_by_id(name_id, inds):
    """
    Get individual's name by his id
    @param name_id: ind['id']
    @param inds: GEDParser.inds
    @return: ind's name
    """
    for ind in inds:
        if ind['id'] == name_id:
            return ind['name']
    return 'not found'


class GEDParser:
    def __init__(self, file_name):
        # create initial variables
        self.file_name = file_name
        self.inds, self.fams = [], []

    def parser(self):
        ind, fam = {}, {}
        ind['famc'], ind['fams'] = set(), set()
        fam['chil'] = set()
        with open(self.file_name) as f:
            line = f.readline()
            while line:
                words = line.strip().split(' ', maxsplit=2)
                if len(words) <= 2 or words[2] not in ['INDI', 'FAM']:
                    line = f.readline()
                else:
                    # if tag is indi, parser indi
                    if words[2] == 'INDI':
                        ind['id'] = words[1]
                        line = next(f)
                        while not line.startswith('0'):
                            words = line.strip().split(' ', maxsplit=2)
                            if words[1] == 'NAME':
                                ind['name'] = words[2]
                            elif words[1] == 'SEX':
                                ind['sex'] = words[2]
                            elif words[1] == 'BIRT':
                                # transit date type
                                ind['birt'] = date_transit(next(f).strip().split(' ', maxsplit=2)[2])
                            elif words[1] == 'DEAT':
                                ind['deat'] = date_transit(next(f).strip().split(' ', maxsplit=2)[2])
                            elif words[1] == 'FAMC':
                                ind['famc'].add(words[2])
                            elif words[1] == 'FAMS':
                                ind['fams'].add(words[2])
                            line = next(f)
                        # complete indi's data
                        if 'deat' in ind.keys():
                            ind['age'] = get_age(ind['birt'], ind['deat'])
                            ind['alive'] = 'False'
                        else:
                            ind['deat'] = 'NA'
                            ind['alive'] = 'True'
                            ind['age'] = get_age(ind['birt'])
                        if 'famc' not in ind.keys() or len(ind['famc']) == 0:
                            ind['famc'] = 'NA'
                        if 'fams' not in ind.keys() or len(ind['fams']) == 0:
                            ind['fams'] = 'NA'
                        self.inds.append(ind)
                        ind = dict()
                        ind['famc'] = set()
                        ind['fams'] = set()

                    elif words[2] == 'FAM':
                        fam['id'] = words[1]
                        line = next(f)
                        while not line.startswith('0'):
                            words = line.strip().split(' ', maxsplit=2)
                            if words[1] == 'HUSB':
                                fam['husb'] = words[2]
                            elif words[1] == 'WIFE':
                                fam['wife'] = words[2]
                            elif words[1] == 'CHIL':
                                fam['chil'].add(words[2])
                            elif words[1] == 'MARR':
                                fam['marr'] = date_transit(next(f).strip().split(' ', maxsplit=2)[2])
                            elif words[1] == 'DIV':
                                fam['div'] = date_transit(next(f).strip().split(' ', maxsplit=2)[2])
                            line = next(f)
                        if 'div' in fam.keys():
                            fam['divorced'] = fam['div']
                        else:
                            fam['divorced'] = 'False'
                        if len(fam['chil']) == 0:
                            fam['chil'] = 'NA'
                        # TODO: if in ged file, FAM parts are before INDI parts, this gonna be wrong
                        if 'husb' in fam.keys():
                            fam['husb_name'] = get_name_by_id(fam['husb'], self.inds)
                        else:
                            fam['husb_name'] = 'NA'
                            fam['husb'] = 'NA'
                        if 'wife' in fam.keys():
                            fam['wife_name'] = get_name_by_id(fam['wife'], self.inds)
                        else:
                            fam['wife_name'] = 'NA'
                            fam['wife'] = 'NA'
                        self.fams.append(fam)
                        fam = {}
                        fam['chil'] = set()
        # sort the list according to id number
        self.inds.sort(key=lambda ind: ind['id'])
        self.fams.sort(key=lambda fam: fam['id'])

    def print_indi(self):
        # create pretty table
        pt = prettytable.PrettyTable(['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse'])
        for ind in self.inds:
            pt.add_row(
                [ind['id'], ind['name'], ind['sex'], ind['birt'], ind['age'], ind['alive'], ind['deat'],
                 str(ind['famc']),
                 str(ind['fams'])])
        print(pt)

    def print_fams(self):
        pt = prettytable.PrettyTable(
            ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children'])
        for fam in self.fams:
            pt.add_row(
                [fam['id'], fam['marr'], fam['divorced'], fam['husb'], fam['husb_name'], fam['wife'], fam['wife_name'],
                 fam['chil']])
        print(pt)


if __name__ == '__main__':
    p = GEDParser('res/ysun.ged')
    p.parser()
    p.print_fams()
    p.print_indi()
