"""
ssw555tmDSYZ2020spring-geddata by Yuning Sun
1:55 PM 3/3/20
Module documentation: 
"""
import prettytable

from geddate import get_age, check_date_valid
from gedparser2 import GEDParser, GEDNode


class GEDAttribute:
    def __init__(self, value: object = 'NA', line: object = 0):
        self.value = value
        self.line = line

    def __str__(self):
        if self.value:
            return str(self.value)
        else:
            return 'NA'

    def add(self, node):
        if isinstance(node.value, list):
            self.value += node.value
            self.line += node.line
        else:
            self.value.append(node.value)
            self.line.append(node.line)


class GEDItem:
    def __init__(self):
        self.attributes = []
        self.date_attributes = []
        self.set_attributes = []

    def __setitem__(self, key, node):
        if isinstance(node, GEDNode):
            self.__dict__[key] = GEDAttribute(node.value, node.line)
        else:
            self.__dict__[key] = node

    def __getitem__(self, item):
        if item in self.__dict__.keys():
            return self.__dict__[item]
        else:
            return GEDAttribute('NA', -1)

    def node_parser(self, ged_node: GEDNode):
        self['id'] = ged_node
        for node in ged_node.nodes:
            tag = node.tag.lower()
            if tag in self.attributes:
                if tag in self.date_attributes:
                    self[tag] = node.nodes[0]
                elif tag in self.set_attributes:
                    self[tag].append(GEDAttribute(node.value, node.line))
                else:
                    self[tag] = node


class GEDFamily(GEDItem):
    def __init__(self):
        super().__init__()
        self['chil'] = []
        self.attributes = ['id', 'marr', 'div', 'husb', 'wife', 'chil']
        self.date_attributes = ['marr', 'div']
        self.set_attributes = ['chil']

    def set_spouse_name(self, inds):
        try:
            husb = get_ind_by_id(self['husb'], inds)
            wife = get_ind_by_id(self['wife'], inds)
        except ValueError:
            self['husb_name'] = GEDAttribute('NA', -1)
            self['wife_name'] = GEDAttribute('NA', -1)
        else:
            self['husb_name'] = GEDAttribute(husb['name'].value, husb['name'].line)
            self['wife_name'] = GEDAttribute(wife['name'].value, wife['name'].line)


class GEDIndividual(GEDItem):
    def __init__(self):
        super().__init__()
        self['famc'] = []
        self['fams'] = []
        self['chil'] = []
        self.attributes = ['id', 'name', 'sex', 'birt', 'deat', 'famc', 'fams']
        self.date_attributes = ['birt', 'deat']
        self.set_attributes = ['famc', 'fams']

    def set_age(self):
        if self['birt'].value == 'NA':
            pass
        else:
            if self['deat'].value == 'NA':
                self['age'] = GEDAttribute(get_age(self['birt'], date_format='%d %b %Y'), self['birt'].line)
                self['alive'] = GEDAttribute('True', self['birt'].line)
            else:
                self['age'] = GEDAttribute(get_age(self['birt'], self['deat'], date_format='%d %b %Y'),
                                           self['birt'].line)
                self['alive'] = GEDAttribute('False', self['deat'].line)


def print_fams(fams):
    pt = prettytable.PrettyTable(
        ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children'])
    for fam in fams:
        chil = ', '.join(i.value for i in fam['chil'])
        pt.add_row(
            [fam['id'], fam['marr'], fam['div'], fam['husb'], fam['husb_name'], fam['wife'], fam['wife_name'], chil])
    print(pt)


def print_inds(inds):
    pt = prettytable.PrettyTable(['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse'])
    for ind in inds:
        chil = ', '.join(i.value for i in ind['chil'])
        fams = ', '.join(i.value for i in ind['fams'])
        pt.add_row(
            [ind['id'], ind['name'], ind['sex'], ind['birt'], ind['age'], ind['alive'], ind['deat'], chil, fams])
    print(pt)


def set_child(inds, fams):
    for fam in fams:
        try:
            husb = get_ind_by_id(fam['husb'], inds)
            wife = get_ind_by_id(fam['wife'], inds)
        except ValueError:
            continue
        else:
            husb['chil'] += fam['chil']
            wife['chil'] += fam['chil']


def get_ind_by_id(ind_id, inds):
    for ind in inds:
        if ind['id'].value == ind_id.value:
            return ind
    else:
        raise ValueError(
            f'ERROR: INDIVIDUAL: US26: {ind_id.line}: {ind_id.value}: {ind_id.value} does not have corresponding entry.')


def get_fams_by_id(fam_id, fams):
    for fam in fams:
        if fam['id'].value == fam_id.value:
            return fam
    return None


def get_name_by_id(ind_id, inds):
    for ind in inds:
        if ind['id'].value == ind_id.value:
            return ind['name'].value
    return None


def get_inds_fams(file_name):
    p = GEDParser(file_name)
    p.parser()
    inds = []
    fams = []
    for node in p.tree.tree:
        if node.tag == 'INDI':
            ind = GEDIndividual()
            ind.node_parser(node)
            check_date_valid(ind, 'ind')
            ind.set_age()
            inds.append(ind)
        elif node.tag == 'FAM':
            fam = GEDFamily()
            fam.node_parser(node)
            check_date_valid(fam, 'fam')
            fam.set_spouse_name(inds)
            fams.append(fam)
    set_child(inds, fams)
    return inds, fams


if __name__ == '__main__':
    inds, fams = get_inds_fams('res/test_sprint2_all.ged')
    print_inds(inds)
    print_fams(fams)
