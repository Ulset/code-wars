"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""


def find_it(seq):
    nums = {}
    for num in seq:
        try:
            nums[num] = nums[num] + 1
        except KeyError:
            nums[num] = 1
    for numKey in nums:
        if (nums[numKey] % 2 != 0):
            return numKey
