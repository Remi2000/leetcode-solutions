"""
Description:
    Given an integer array nums and a target, find three integers in nums
    such that the sum is closest to target. Return the sum.
    The answer is guaranteed to be unique.

Approach:
    Sort the array, then fix one element and use two pointers to find the
    closest sum for the remaining two. Store the closest sum directly (not
    the difference) by initializing closest to float('inf') and comparing
    abs(total - target) < abs(closest - target) at each step.
    If the sum equals target exactly, return immediately.

Tech Stack:
    - Sorting to enable two pointer traversal
    - Two pointers (l, r) to scan remaining pairs in O(n) per outer iteration

Complexity:
    Time:  O(n^2) - outer loop O(n), two pointers O(n) per iteration
    Space: O(1)   - only constant extra variables used
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')  # stores the closest sum seen so far (not the difference)

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                # update if current sum is closer to target than previous best
                if abs(total - target) < abs(closest - target):
                    closest = total

                if total < target:
                    l += 1      # sum too small, move left pointer right
                elif total > target:
                    r -= 1      # sum too large, move right pointer left
                else:
                    return total  # exact match

        return closest