"""
Description:
    Given a string s and numRows, write s in a zigzag pattern across numRows rows,
    then read off each row left to right to produce the result.

Approach:
    Simulate the zigzag traversal using a direction variable and numRows buckets.
    Each character is placed into the current row bucket, then the direction flips
    whenever the top or bottom row is reached.
    Initialize direction as -1 so that the first flip (triggered immediately at row 0)
    sets it to 1, allowing the pointer to correctly move downward from the start.

Tech Stack:
    - List of strings as row buckets to collect characters
    - Direction variable (+1/-1) to simulate up/down movement

Complexity:
    Time:  O(n) - each character is visited once
    Space: O(n) - row buckets store all n characters
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = ["" for _ in range(numRows)]
        curr_row = 0
        # initialize as -1: first character lands on row 0, triggers a flip to +1,
        # so the pointer correctly starts moving downward
        directions = -1

        for c in s:
            rows[curr_row] += c
            # flip direction when top or bottom row is reached
            if curr_row == 0 or curr_row == numRows - 1:
                directions *= -1
            curr_row += directions

        return "".join(rows)