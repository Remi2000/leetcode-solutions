"""
73. Set Matrix Zeroes

Description:
    Given an m x n integer matrix, if an element is 0,
    set its entire row and column to 0's. Must be done in place.

Approach:
    Two-pass approach with marker arrays:
    1. First pass: scan the matrix, record which rows and columns
       contain at least one 0 using two boolean arrays.
    2. Second pass: for each cell, if its row or column is marked,
       set it to 0.
    Separating scan and update avoids chain reactions where newly
    created zeros incorrectly trigger more rows/columns to be zeroed.

Tech Stack:
    - Matrix traversal (two passes)
    - Boolean marker arrays for rows and columns

Complexity:
    - Time: O(m * n), two full scans of the matrix
    - Space: O(m + n), two marker arrays of size m and n
"""


class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])

        # marker arrays: track which rows/cols need to be zeroed
        row_zero = [False] * m
        col_zero = [False] * n

        # pass 1: scan and mark rows/cols that contain a zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_zero[i] = True
                    col_zero[j] = True

        # pass 2: apply zeros based on markers
        for i in range(m):
            for j in range(n):
                if row_zero[i] or col_zero[j]:
                    matrix[i][j] = 0