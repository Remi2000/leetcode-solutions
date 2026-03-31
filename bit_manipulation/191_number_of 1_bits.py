"""
191. Number of 1 Bits

Description:
    Given a positive integer n, return the number of set bits (1s)
    in its binary representation (also known as the Hamming weight).

Approach:
    Check each bit from right to left using bitwise AND:
    - n & 1 extracts the last bit (0 or 1).
    - n >>= 1 right-shifts to move the next bit into the last position.
    Repeat until n becomes 0.

Tech Stack:
    - Bit manipulation: bitwise AND (&), right shift (>>)

Complexity:
    - Time: O(32) = O(1), at most 32 bits to check
    - Space: O(1), only a counter variable
"""


class Solution:
    def hammingWeight(self, n):
        count = 0
        while n:
            # check if the last bit is 1
            if n & 1 == 1:
                count += 1
            # right shift to check the next bit
            n >>= 1
        return count