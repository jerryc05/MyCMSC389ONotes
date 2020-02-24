# Given an array of size n, where the values are between 1 and n inclusive and
# each value may at most appear twice, return a List of all the duplicate
# elements. All tests have duplicates occur in ascending order (i.e. a duplicate
# 1 would occur before a duplicate 2, etc), so your output MUST have the
# duplicates in ascending order!


from typing import List


def findDuplicates(nums: List[int]) -> List[int]:
    """
    A set is used to check for duplicate in the array. If a duplicate is found, add it
    to a list (since order of duplicates are guaranteed in ascending order).

    Time complexity: O(n)
    Space complexity: O(n)

    :param nums: array of unordered ints where duplicates are sorted
    :return: a list containing duplicates in ascending order
    """
    s = set()  # the set containing checked ints, space: O(n)
    d = []  # the list containing duplicates to return (ordered), space: O(n)

    for x in nums:  # iterate over the array, time: O(n)
        # if `x` is a duplicate, add to list
        if x in s:  # time: O(1) since `s` is a hashset
            d.append(x)  # time: O(1) since elements are appended to a list
        else:
            s.add(x)  # time: O(1) since `s` is a hashset
    return d