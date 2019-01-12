"""
https://leetcode.com/problems/combinations/description/

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
"""


def combine(n, k, start_val=1):
    if k == 1:
        return [[val] for val in range(start_val, n + 1)]
    collection = []
    for val in range(start_val, n + 1):
        for sub in combine(n, k - 1, val + 1):
            collection.append([val] + sub)
    return collection


if __name__ == "__main__":
    n = 4
    k = 2
    output = [
        [2,4],
        [3,4],
        [2,3],
        [1,2],
        [1,3],
        [1,4],
    ]
    test = combine(n, k)
    assert all(map(lambda x: x in output, test)) and len(output) == len(test)