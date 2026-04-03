"""
15. 3Sum

Description:
    Given an integer array nums, return all unique triplets
    [nums[i], nums[j], nums[k]] such that i != j != k and
    nums[i] + nums[j] + nums[k] == 0. No duplicate triplets allowed.

Approach:
    Sort the array, then for each element nums[i], use two pointers
    (left and right) on the remaining part to find pairs that sum to
    -nums[i]. This reduces 3Sum to a 2Sum problem.
    Deduplication at two levels:
    1. Outer loop: skip if nums[i] == nums[i-1].
    2. Inner loop: after finding a triplet, skip duplicate left/right values.

Tech Stack:
    - Sorting + Two Pointers
    - Deduplication by skipping adjacent equal values

Complexity:
    - Time: O(n^2), sort O(n log n) + outer loop O(n) * two pointers O(n)
    - Space: O(1), excluding the result array
"""


class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            # skip duplicate i values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            target = -nums[i]

            while left < right:
                total = nums[left] + nums[right]

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    # found a triplet
                    result.append([nums[i], nums[left], nums[right]])

                    # move pointers first, then skip duplicates
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result