"""
128. Longest Consecutive Sequence

Description:
    Given an unsorted array of integers, return the length of the
    longest consecutive elements sequence. Must run in O(n) time.

Approach:
    Use a set for O(1) lookups. For each number, check if it's the
    start of a sequence (num - 1 not in set). If so, count how far
    the sequence extends by checking num + 1, num + 2, etc.
    Non-starting numbers are skipped, ensuring each number is visited
    at most twice (once in for loop, once in while loop).

Tech Stack:
    - Hash set for O(1) lookup
    - Sequence start detection (num - 1 not in set)

Complexity:
    - Time: O(n), each number visited at most twice
    - Space: O(n), set stores all numbers
"""


class Solution:
    def longestConsecutive(self, nums):
        # empty array edge case
        if not nums:
            return 0

        # convert to set for O(1) lookup
        all_nums = set(nums)
        max_len = 1

        for n in nums:
            # if n-1 exists, n is not the start of a sequence, skip
            if n - 1 in all_nums:
                continue

            # n is the start of a sequence, count forward
            length = 1
            nxt = n + 1
            while nxt in all_nums:
                length += 1
                nxt += 1

            max_len = max(max_len, length)

        return max_len