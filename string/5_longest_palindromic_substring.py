"""
Description:
    Given a string s, return the longest palindromic substring in s.
    A palindrome reads the same forward and backward.

Approach:
    Expand Around Center - for each index i, treat it as the center of a palindrome
    and expand outward as long as characters on both sides match.
    Handle odd-length (center = single char) and even-length (center = two chars) separately.
    Track the longest valid palindrome found across all centers.

Tech Stack:
    - Two pointers (l, r) expanding outward from each center
    - String slicing to extract the result

Complexity:
    Time:  O(n^2) - n centers, each expanding at most n/2 times
    Space: O(1)   - only constant extra variables used
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0

        # odd-length: expand around single character center s[i]
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1

        # even-length: expand around gap between s[i] and s[i+1]
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1

        return res