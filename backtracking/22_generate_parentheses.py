"""
22. Generate Parentheses

Description:
    Given n pairs of parentheses, generate all combinations
    of well-formed (valid) parentheses.

Approach:
    Use backtracking to build strings character by character.
    At each step, decide whether to add '(' or ')' based on two rules:
    - Can add '(' if open_count < n
    - Can add ')' if close_count < open_count
    This ensures every generated string is always valid.

Tech Stack:
    - Backtracking / Recursion

Complexity:
    Time:  O(4^n / sqrt(n)) - the nth Catalan number (number of valid combinations)
    Space: O(n) - recursion depth is at most 2n, not counting result storage
"""


class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(curr, open_count, close_count):
            # Base case: string is complete, collect result
            if len(curr) == 2 * n:
                result.append(curr)
                return

            # Choice 1: add '(' if we haven't used all n
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            # Choice 2: add ')' if there are unmatched '(' to close
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result