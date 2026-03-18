"""
1. Two Sum

Description:
    Given an array of integers `nums` and an integer `target`,
    return indices of the two numbers such that they add up to `target`.
    Each input has exactly one solution, and the same element cannot be used twice.

Approach:
    Use a hash map to store seen values and their indices.
    For each number, check if its complement (target - num) already exists in the map.
    This avoids the brute-force O(n^2) nested loop.

Tech Stack:
    - Hash Map (dictionary)

Complexity:
    Time:  O(n) - single pass, hash map lookup is O(1)
    Space: O(n) - hash map stores up to n elements
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i