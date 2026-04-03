"""
125. Valid Palindrome

Description:
    Given a string s, return True if it is a palindrome after converting
    all uppercase letters to lowercase and removing all non-alphanumeric
    characters. Return False otherwise.

Approach 1 - Clean + Reverse (concise):
    Filter out non-alphanumeric chars, convert to lowercase, then
    compare the cleaned string with its reverse.
    Time: O(n), Space: O(n) for the cleaned string.

Approach 2 - Two Pointers (space optimized):
    Left pointer starts from the beginning, right pointer from the end.
    Skip non-alphanumeric characters, compare lowercase chars from both sides.
    Time: O(n), Space: O(1) no extra string created.

Tech Stack:
    - String methods: isalnum(), lower()
    - Two pointers (approach 2)
"""

# ========== Approach 1: Clean + Reverse ==========


class Solution:
    def isPalindrome(self, s):
        # keep only letters and digits, convert to lowercase
        cleaned = "".join([c.lower() for c in s if c.isalnum()])
        # palindrome reads the same forward and backward
        return cleaned == cleaned[::-1]


# ========== Approach 2: Two Pointers ==========


class SolutionTwoPointers:
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            # skip non-alphanumeric from the left
            while left < right and not s[left].isalnum():
                left += 1
            # skip non-alphanumeric from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True