"""
https://leetcode.com/problems/distinct-subsequences/description/

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining 
characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
"""


class Solution(object):
    def __init__(self):
        self.count = 0

    def _num_distinct(self, s, t):
        n_elements = len(t)
        if n_elements == 0:
            self.count += 1
            return
        if len(s) == 0 and n_elements > 0:
            return 
        for s_idx, char in enumerate(s):
            if char == t[0]:
                self.numDistinct(s[s_idx + 1:], t[1:])

    def numDistinct(self, s, t):
        self._num_distinct(s, t)
        return self.count
        

if __name__ == "__main__":
    S = "rabbbit"
    T = "rabbit"
    s = Solution()
    assert s.numDistinct(S, T) == 3

    S = "babgbag"
    T = "bag"
    s = Solution()
    assert s.numDistinct(S, T) == 5