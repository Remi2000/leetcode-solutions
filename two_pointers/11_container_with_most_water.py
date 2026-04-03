"""
11. Container With Most Water

Description:
    Given an array of heights where each value represents a vertical line,
    find two lines that together with the x-axis form a container holding
    the most water. Water amount = min(height[left], height[right]) * (right - left).

Approach:
    Two pointers starting from both ends. Calculate area at each step,
    then move the shorter side inward. Moving the shorter side is safe
    because it has already been paired with the widest possible partner.
    Keeping it and moving the taller side can only make things worse
    (width shrinks, height still limited by the short side).

Tech Stack:
    - Two pointers (left and right converging)
    - Greedy: always move the shorter side

Complexity:
    - Time: O(n), each element visited at most once
    - Space: O(1), only two pointers and max_area
"""


class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # calculate current area
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            # move the shorter side inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area