"""
On a table are N cards, with a positive integer printed on the front and back of each card (possibly different).

We flip any number of cards, and after we choose one card.

If the number X on the back of the chosen card is not on the front of any card, then this number X is good.

What is the smallest number that is good?  If no number is good, output 0.

Here, fronts[i] and backs[i] represent the number on the front and back of card i.

A flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.

Example:

Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: 2
Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the backs are [1,2,4,1,3].
We choose the second card, which has number 2 on the back, and it isn't on the front of any card, so 2 is good.

https://leetcode.com/problems/card-flipping-game/
"""
from typing import List


class Solution(object):
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """

        flips = []
        for idx in range(len(fronts)):
            if backs[idx] not in fronts:
                flips.append(fronts[idx])
                fronts[idx], backs[idx] = backs[idx], fronts[idx]
        return min(flips)


if __name__ == "__main__":
    fronts = [1, 2, 4, 4, 7]
    backs = [1, 3, 4, 1, 3]

    solution = Solution()
    ans = solution.flipgame(fronts, backs)
    assert ans == 2, f"expected 2 received {ans}"
