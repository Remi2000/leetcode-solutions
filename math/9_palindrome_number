"""
9. Palindrome Number

Description:
    Given an integer x, return True if x is a palindrome (reads the same
    forwards and backwards), and False otherwise.

Approach:
    Reverse the entire number digit by digit using modulo and integer division,
    then compare the reversed number with the original.
    Negative numbers are never palindromes.

Tech Stack:
    - Math (modulo %, integer division //)

Complexity:
    Time:  O(n) - process each digit once, where n is the number of digits
    Space: O(1) - only a few variables, no extra data structures
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return original == reversed_num