"""
Given an integer N create a function to generate all possible
lists from 0 to N incrementing by powers of 2

example

n = 5

return 
[0, 1, 2, 3, 4, 5] # all deltas 2**0
[0, 1, 3, 5] # mixture of 2**0 and 2**1
...  # results continue

Consider the problem as tree

                5
        /       |       \  
        4       3        1
    /   |   \ 
    3   2   0
    ...
"""

from math import log2

__node_cache__ = {}

__combo_cache__ = {}

class PowerTwoNode(object):
    def __init__(self, n):
        self.n = n
        self.children = []

        # 0 is the basecase for the power2 tree. branches end here
        if self.n > 0:
            self.build_tree()
        
    def __repr__(self):
        return f"<PowerTwoNode(n: {self.n}, children: {len(self.children)})>"

    def build_tree(self):
        """
        Build the power2 tree by identifying the maximum power of 2 less than N. For each 
        level identified, build the subtree combinations 
        """

        # base case is 0. This is the end of the tree so just return a node
        if self.n == 0:
            return PowerTwoNode(0)

        # 2 to what power equals N? Round down and use this max power 
        max_power_2 = int(log2(self.n))

        # for each max power, find the delta from n
        for i in range(max_power_2 + 1):
            next_level = self.n - (2 ** i)
            if next_level < 0:
                break
            # for each delta, build a child node
            if next_level in __node_cache__.keys():
                child = __node_cache__[next_level]
            else:
                child = PowerTwoNode(next_level)
                __node_cache__[next_level] = child

            # add child to current nodes collection
            self.children.append(child)

    def generate_power2_combos(self):
        """
        Generate all combinations of powers of 2 from 0 to N.
        """
        # Base case
        if self.n == 0:
            return [[0]]
        all_lists = []
        # for each child node, generate combinations and return those lists 
        for child in self.children:
            if child.n in __combo_cache__.keys():
                combos = __combo_cache__[child.n]
            else:
                combos = child.generate_power2_combos()
            for combo in combos:
                combo_copy = combo[:]
                combo_copy.append(self.n)
                all_lists.append(combo_copy)
        __combo_cache__[self.n] = all_lists
        return all_lists


if __name__ == "__main__":
    a = PowerTwoNode(10)
    # a.build_tree()
    print("generating combos")
    print(len(a.generate_power2_combos()))
    for l in a.generate_power2_combos():
        print(l)