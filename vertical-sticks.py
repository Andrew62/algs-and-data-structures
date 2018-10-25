"""
https://www.hackerrank.com/challenges/vertical-sticks/problem

Given an array of integers , we have line segments, such that, the endpoints of segment are
and . Imagine that from the top of each segment a horizontal ray is shot to the left, and
this ray stops when it touches another segment or it hits the y-axis. We construct an array of
integers, , where is equal to length of ray shot from the top of segment . We define .

For example, if we have , then , as shown in the picture below:
"""

from itertools import permutations


def calc_heights(seq):
    heights = []
    for idx, value in enumerate(seq):
        if idx == 0:
            heights.append(1)
        else:
            jdx = idx - 1
            while jdx >= 0:
                if seq[jdx] >= value:
                    break
                jdx -= 1
            heights.append(idx - jdx)
    return heights


def vertical_sticks(y):
    vs = []
    for seq in permutations(y):
        vs.append(sum(calc_heights(seq)))
    return sum(vs)/len(vs)


if __name__ == "__main__":
    a = [1, 2, 3]
    ans = 4.33
    assert round(vertical_sticks(a), 2) == ans

    a = [3, 3, 3]
    ans = 3.00
    assert round(vertical_sticks(a), 2) == ans

    a = [2, 2, 3]
    ans = 4.0
    assert round(vertical_sticks(a), 2) == ans

    a = list(map(int, '10 2 4 4'.split()))
    ans = 6.0
    assert round(vertical_sticks(a), 2) == ans

    a = '10 10 10 5 10'
    ans = 5.8
    g = vertical_sticks(list(map(int, a.split())))
    assert round(g, 2) == ans, "expected {} got {}".format(a, g)

    a = '1 2 3 4 5 6'
    ans = 11.15
    g = vertical_sticks(list(map(int, a.split())))
    assert round(g, 2) == ans, "expected {} got {}".format(a, g)
