"""
https://leetcode.com/problems/find-k-closest-elements/description/

Given a sorted array, two integers k and x, find the k closest elements 
to x in the array. The result should also be sorted in ascending order. 
If there is a tie, the smaller elements are always preferred.
"""


def findClosestElements(arr, k, x):
    # closest means smallest abs dist
    distances = []
    for idx, val in enumerate(arr):
        distances.append((idx, abs(x - val)))
    distances = list(sorted(distances, key=lambda x: x[1], reverse=True))
    idxs = [distances[i][0] for i in range(k)]
    return list(sorted([arr[i] for i in idxs]))


if __name__ == "__moin__":
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 5
    assert findClosestElements(arr, k, x) == [1,2,3,4]

    arr = [1, 2, 3, 4, 5]
    k = 4
    x = -1

    assert findClosestElements(arr, k, x) == [1,2,3,4]