"""
ssw555tmDSYZ2020spring-test by Yuning Sun
1:03 PM 3/3/20
Module documentation: 
"""
from collections import defaultdict


class GEDTree:
    def __init__(self):
        self.tree = []

    def add_tree(self):
        root_node = GEDNode()
        self.tree.append(root_node)
        return root_node


class GEDNode:
    def __init__(self):
        self.value = ''
        self.tag = ''
        self.line = -1
        self.nodes = []

    def add_node(self):
        node = GEDNode()
        self.nodes.append(node)
        return node

    def set_value(self, value, tag, line):
        self.value = value
        self.tag = tag
        self.line = line


class GEDParser:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tree = GEDTree()

    def parser(self):
        line_num = 0
        with open(self.file_name, encoding='UTF-8-sig') as f:
            line = True
            while line:
                line = f.readline()
                line_num += 1
                words = line.strip().split(' ', maxsplit=2)
                if words[0] == '0':
                    node = self.tree.add_tree()
                    node.set_value(words[1], words[-1], line_num)
                elif words[0] == '1':
                    node1 = node.add_node()
                    node1.set_value(words[-1], words[1], line_num)
                elif words[0] == '2':
                    node2 = node1.add_node()
                    node2.set_value(words[-1], words[1], line_num)
                elif words[0] == '3':
                    node3 = node2.add_node()
                    node3.set_value(words[-1], words[1], line_num)


if __name__ == '__main__':
    p = GEDParser('res/ysun.ged')
    p.parser()
    print()
