#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:08:08 2016

@author: awoizesko
"""

import json


def create_binary_tree(depth):
    if depth == 1:
        # make the final node the same type for ease
        return {'left':[], 'right':[]}
    tree = {'left':create_binary_tree(depth-1),
            'right':create_binary_tree(depth-1)}
    return tree

    
def invert_binary_tree(tree):
    left, right = 'left', 'right'
    # this assumes the tree is balanced
    if len(tree[left]) > 0:
        inv_tree = dict(right=invert_binary_tree(tree[right]),
                        left=invert_binary_tree(tree[left]))
    else:
        inv_tree = dict(right=[], left=[])
    return inv_tree
    
    
def get_tree_depth(tree, depth=1):
    level_max = 0
    k_max = None
    for k, v in tree.items():
        if len(v) > level_max:
            level_max = len(v)
            k_max = k
    if level_max > 0:
        depth = get_tree_depth(tree[k_max], depth + 1)
    return depth
    

    
    
    
test = create_binary_tree(3)
inv = invert_binary_tree(test)
print(json.dumps(inv, indent=2))
