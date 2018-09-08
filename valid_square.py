"""
https://leetcode.com/problems/valid-square/description/

Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

Note:

    All the input integers are in the range [-10000, 10000].
    A valid square has four equal sides with positive length and four equal angles (90-degree angles).
    Input points have no order.
"""

import math
from itertools import permutations
from timeit import timeit
from functools import lru_cache
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

@lru_cache()
def euclid_dist(p1: Point, p2: Point):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def is_right_angle(corner: Point, p1: Point, p2: Point):
    hypot = euclid_dist(p1, p2)
    corner_to_p1 = euclid_dist(corner, p1)
    corner_to_p2 = euclid_dist(corner, p2)
    return corner_to_p1 == corner_to_p2 and hypot == math.sqrt(corner_to_p1**2 + corner_to_p2**2)

def validSquare(*args):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        # constant runtime b/c there are always 4 points
        points = map(lambda x: Point(*x), args)
        for ul, ur, lr, ll in permutations(points, 4):
            if all([is_right_angle(ul, ll, ur), is_right_angle(ur, ul, lr), is_right_angle(lr, ur, ll), is_right_angle(ll, ul, lr)]):
                if euclid_dist(ul, ur) == euclid_dist(ur, lr) == euclid_dist(lr, ll) == euclid_dist(ll, ul):
                    return True
        return False
            

if __name__ == "__main__":
    ll = Point(0, 0)
    ul = Point(0, 2)
    lr = Point(2, 0)
    assert euclid_dist(ll, ul) == 2
    assert euclid_dist(ll, lr) == 2
    assert is_right_angle(ll, ul, lr)

    p1 = [0,0]
    p2 = [1,1]
    p3 = [1,0]
    p4 = [0,1]
    assert validSquare(p1, p2, p3, p4)
    assert validSquare(p1, p2, [6, 6], p4) is False
    print("pass")