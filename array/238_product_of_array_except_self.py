"""
238. Product of Array Except Self

Description:
    Given an integer array nums, return an array answer such that answer[i]
    is equal to the product of all elements of nums except nums[i].
    Must run in O(n) time without using division.

Approach 1 - Two Arrays (easier to understand):
    Build a left array where left[i] = product of all elements to the left of i.
    Build a right array where right[i] = product of all elements to the right of i.
    answer[i] = left[i] * right[i].
    Time: O(n), Space: O(n) for the two extra arrays.

Approach 2 - One Array (space optimized):
    Use the answer array itself to store left products in the first pass.
    In the second pass, multiply in the right products using a running variable.
    Time: O(n), Space: O(1) extra (excluding the output array).

Tech Stack:
    - Prefix product / Suffix product
    - Two-pass array traversal
"""

# ========== Approach 1: Two Arrays ==========


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left = [1] * n
        right = [1] * n

        # left to right: accumulate left products
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # right to left: accumulate right products
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # left product * right product = product except self
        return [left[i] * right[i] for i in range(n)]


# ========== Approach 2: One Array (Space Optimized) ==========


class SolutionOptimized:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # pass 1: answer[i] = product of all elements to the left
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        # pass 2: multiply in the product of all elements to the right
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer