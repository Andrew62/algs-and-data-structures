"""
https://leetcode.com/problems/range-addition-ii/description/

Given an m * n matrix M initialized with all 0's and several update operations.

Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.

You need to count and return the number of maximum integers in the matrix after performing all the operations.
"""


def maxCount(m, n, ops):
    """
    :type m: int
    :type n: int
    :type ops: List[List[int]]
    :rtype: int
    """
    mat = [[0] * n for _ in range(m)]
    max_val = 0
    max_val_count = 0

    for n_rows, n_cols in ops:
        for r in range(n_rows):
            for c in range(n_cols):
                mat[r][c] += 1
                if mat[r][c] == max_val:
                    max_val_count += 1
                if mat[r][c] > max_val:
                    max_val = mat[r][c]
                    max_val_count = 1
    return max_val_count


if __name__ == "__main__":
    m = 3
    n = 3
    operations = [[2,2], [3, 3]]

    assert maxCount(m, n, operations) == 4