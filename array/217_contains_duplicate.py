"""
217. Contains Duplicate

Description:
    Given an integer array nums, return True if any value appears
    at least twice in the array, and False if every element is distinct.

Approach:
    Use a set to track seen numbers. Iterate through the array:
    if the current number is already in the set, return True (duplicate found).
    Otherwise, add it to the set and continue.
    Early termination on first duplicate found.

Tech Stack:
    - Hash set for O(1) lookup and insertion

Complexity:
    - Time: O(n), single pass through the array
    - Space: O(n), set stores up to n elements in the worst case
"""


class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            # already seen this number → duplicate
            if num in seen:
                return True
            # first time seeing this number → add to set
            seen.add(num)
        return False