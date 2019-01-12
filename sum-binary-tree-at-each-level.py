
"""
Sum a binary tree at each level such that 

            4           ->     4
        /       \
        1       3       ->     4
        /\      /\
        1 2     3 4     ->     10
"""

from random import randint


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def __repr__(self):
        if self.right and self.left:
            return f"<PowerTwoNode(n: {self.data}, left: {self.left}, right: {self.right})>"
        return f"<PowerTwoNode(n: {self.data})"
        

def build_balanced_binary_tree(levels=5):
    data = randint(0, 50)
    node = Node(data)
    if levels - 1 > 0:
        node.left = build_balanced_binary_tree(levels=levels-1)
        node.right = build_balanced_binary_tree(levels=levels-1)
    return node


def sum_binay_tree_levels(node, level=0, collection={}):
    if level in collection.keys():
        collection[level] += node.data
    else:
        collection[level] = node.data
    
    if node.left:
        collection = sum_binay_tree_levels(node.left, level=level+1, collection=collection)
    if node.right:
        collection = sum_binay_tree_levels(node.right, level=level+1, collection=collection)

    return collection


if __name__ == "__main__":
    from random import seed
    seed(1234)
    g = build_balanced_binary_tree(2)
    levels = sum_binay_tree_levels(g)
    assert levels[0] == 49 and levels[1] == 35