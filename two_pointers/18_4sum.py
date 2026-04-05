"""
Description:
    Given an integer array nums and a target, return all unique quadruplets
    [a, b, c, d] such that a + b + c + d == target.

Approach:
    Sort the array, then fix two elements with nested loops and use two pointers
    for the remaining two. Skip duplicate elements at each level to avoid
    duplicate quadruplets in the result.

Tech Stack:
    - Sorting to enable two pointer traversal and deduplication
    - Two pointers (l, r) to scan remaining pairs in O(n) per outer iteration

Complexity:
    Time:  O(n^3) - two outer loops O(n^2), two pointers O(n) per iteration
    Space: O(1)   - not counting the output array
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            # skip duplicates at the first level
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # skip duplicates at the second level
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l, r = j + 1, n - 1

                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]

                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        # skip duplicates at the two pointer level
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif total < target:
                        l += 1      # sum too small, move left pointer right
                    else:
                        r -= 1      # sum too large, move right pointer left

        return res