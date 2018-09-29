"""
https://leetcode.com/problems/remove-element/description/

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""


def removeElement(nums, val):
    total = len(nums)
    for i in nums:
        if i == val:
            total -= 1
    return total
    

if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    assert removeElement(nums, val) == 5

    nums = [3,2,2,3]
    val = 3
    assert removeElement(nums, val) == 2