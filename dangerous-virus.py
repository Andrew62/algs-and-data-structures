"""
https://www.hackerrank.com/challenges/extremely-dangerous-virus/problem

A recent lab accident resulted in the creation of an extremely dangerous virus that replicates so rapidly it's hard to predict exactly how many cells it will contain after a given period of time. However, a lab technician made the following observations about its growth per millisecond:

    The probability of the number of virus cells growing by a factor of is .
    The probability of the number of virus cells growing by a factor of is .

Given , , and knowing that initially there is only a single cell of virus, calculate the expected number of virus cells after milliseconds. As this number can be very large, print your answer modulo .

Input Format

A single line of three space-separated integers denoting the respective values of (the first growth factor), (the second growth factor), and (the time you want to know the expected number of cells for).

Constraints

    it is guaranteed that expected value is integer

Output Format

Print the expected number of virus cells after milliseconds modulo .
"""


def dangerous_virus(a, b, t):
    return ((a + b) / 2) ** t % (10 ** 9 + 7)


assert dangerous_virus(2, 4, 1) == 3