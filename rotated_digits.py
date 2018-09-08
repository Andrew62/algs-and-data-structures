"""
X is a good number if after rotating each digit individually by 180 degrees, 
we get a valid number that is different from X.  Each digit must be 
rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, 
and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 r
otate to each other, and the rest of the numbers do not rotate to any 
other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Note:

    N  will be in range [1, 10000].

"""

def rotatedDigits(N):
    """
    :type N: int
    :rtype: int
    """
    rotations = {
        "0": "0",
        "1": "1",
        "8": "8",
        "2": "5",
        "5": "2", 
        "6": "9",
        "9": "6"
    }
    count = 0
    for num in range(N + 1):
        str_num = str(num)
        is_new_valid_num = True
        new_num = ''
        for char in str_num:
            if char in rotations.keys():
                new_num += rotations[char]
            else:
                is_new_valid_num = False
                break
        if is_new_valid_num and new_num != str_num:
            count += 1
    return count


if __name__ == "__main__":
    print(rotatedDigits(10))