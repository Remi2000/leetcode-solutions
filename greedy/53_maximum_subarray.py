"""
53. Maximum Subarray

Description:
    Given an integer array nums, find the contiguous subarray
    with the largest sum and return its sum.

Approach:
    Kadane's Algorithm (greedy):
    Walk through the array, maintaining a running sum (curr_sum).
    At each element, decide: is the previous accumulation helping or hurting?
    - If curr_sum is negative, discard it and start fresh from current element.
    - If curr_sum is non-negative, keep adding the current element.
    Track the global maximum (max_sum) throughout the process.

Tech Stack:
    - Greedy / Kadane's Algorithm
    - Single pass array traversal

Complexity:
    - Time: O(n), one pass through the array
    - Space: O(1), only two variables
"""


class Solution:
    def maxSubArray(self, nums):
        curr_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            # if previous sum is negative, start fresh; otherwise keep adding
            if curr_sum < 0:
                curr_sum = num
            else:
                curr_sum += num

            # update global max
            max_sum = max(max_sum, curr_sum)

        return max_sum