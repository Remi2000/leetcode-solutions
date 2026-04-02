"""
55. Jump Game

Description:
    Given an integer array nums where each element represents the maximum
    jump length at that position, determine if you can reach the last index
    starting from index 0.

Approach:
    Greedy: maintain max_reach, the farthest index reachable so far.
    Walk left to right through the array:
    - If current index i > max_reach, we can't reach here, return False.
    - Otherwise, update max_reach = max(max_reach, i + nums[i]).
    If the loop completes without returning False, we can reach the end.

Tech Stack:
    - Greedy algorithm
    - Single pass array traversal

Complexity:
    - Time: O(n), one pass through the array
    - Space: O(1), only one variable max_reach
"""


class Solution:
    def canJump(self, nums):
        max_reach = 0

        for i in range(len(nums)):
            # can't reach this position, impossible to continue
            if i > max_reach:
                return False

            # update the farthest reachable position
            max_reach = max(max_reach, i + nums[i])

        return True