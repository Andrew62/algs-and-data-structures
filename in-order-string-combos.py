"""
Given some string, can you generate all in order combinations such that

my_str = 'abcd'

combos = [
    ('a', 'b', 'c', 'd'),
    ('a', 'b', 'cd'),
    ('a', 'bc', 'd')
    ('a', 'bcd'),
    ...
]
  
"""

class Node(object):
    def __init__(self, data, parent=None):
        self.data = data
        self.children = []

    def __repr__(self):
        return "<Node {} (chidren: {})>".format(self.data, self.children)


class ComboBuilder(object):
    def __init__(self):
        self.nodes = []
        self.combos = []

    def in_order_string_combos(self, in_str, parent=None):
        for idx in range(len(in_str)):
            current = in_str[:idx + 1]
            if parent:
                node = Node(current)
                parent.children.append(node)
            else:
                node = Node(current, parent=parent)
                self.nodes.append(node)
            self.in_order_string_combos(in_str[idx + 1:], node)
    
    def build_combos(self, in_str):
        self.in_order_string_combos(in_str)
        self.dfs()
        return(self.combos)

    def dfs(self, nodes=None, depth=[]):
        if not nodes:
            nodes = self.nodes
        for node in nodes:
            n_depth = depth + [node.data]
            if node.children:
                self.dfs(node.children, n_depth)
            else:
                self.combos.append(n_depth)

def in_order_string_combos(s):
    cb = ComboBuilder()
    return cb.build_combos(s)

if __name__ == "__main__":
    for combo in in_order_string_combos('abcde'):
        print(combo)
