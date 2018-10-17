"""
We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the
maximum array element in that subarray is at least L and at most R.

Example :
Input:
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

Note:

    L, R  and A[i] will be an integer in the range [0, 10^9].
    The length of A will be in the range of [1, 50000].

https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
"""
from typing import List


class Solution(object):

    @staticmethod
    def check_bounds(val: int, lower: int, upper: int) -> bool:
        return lower <= val <= upper

    @staticmethod
    def check_array(a: List[int], lower: int, upper: int) -> bool:
        return Solution.check_bounds(min(a), lower, upper) and Solution.check_bounds(max(a), lower, upper)

    def numSubarrayBoundedMax(self, a: List[int], l: int, r: int) -> int:
        """
        :type a: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        num_sub_arrays = 0
        for i in range(len(a)):
            for j in range(i + 1, len(a) + 1):
                if Solution.check_array(a[i:j], l, r):
                    num_sub_arrays += 1
                else:
                    # exit this sub loop and increment
                    break
        return num_sub_arrays


if __name__ == "__main__":
    A = [2, 1, 4, 3]
    L = 2
    R = 3
    solution = Solution()
    ans = solution.numSubarrayBoundedMax(A, L, R)
    assert ans == 2, f"expected 3 got {ans}"

    a = [4, 5, 6, 3, 19, 4, 5]
    l = 4
    r = 7
    ans = solution.numSubarrayBoundedMax(a, l, r)
    assert ans == 9, f"expected 9 got {ans}"
