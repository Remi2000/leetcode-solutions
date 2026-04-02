"""
417. Pacific Atlantic Water Flow

Description:
    Given an m x n matrix of heights, find all cells where water can
    flow to both the Pacific Ocean (top + left borders) and the
    Atlantic Ocean (bottom + right borders). Water flows from higher
    or equal height to lower or equal height in four directions.

Approach:
    Reverse thinking: instead of checking each cell to see if it can
    reach both oceans, start DFS from ocean borders going inward.
    - From Pacific borders (top row + left col): DFS uphill to find
      all cells that can flow to Pacific.
    - From Atlantic borders (bottom row + right col): same DFS.
    - The intersection of both sets is the answer.
    Reverse flow means we move to neighbors with height >= current.

Tech Stack:
    - DFS on a matrix (reverse flow direction)
    - Set intersection to find cells reaching both oceans

Complexity:
    - Time: O(m * n), each cell visited at most twice (once per ocean)
    - Space: O(m * n), two visited sets + recursion stack
"""


class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited):
            # mark current cell as reachable
            visited.add((r, c))
            # explore four directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # in bounds, not visited, and height >= current (reverse flow)
                if (0 <= nr < m and 0 <= nc < n
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)

        # start DFS from Pacific borders (top row + left col)
        for i in range(m):
            dfs(i, 0, pacific)
        for j in range(n):
            dfs(0, j, pacific)

        # start DFS from Atlantic borders (bottom row + right col)
        for i in range(m):
            dfs(i, n - 1, atlantic)
        for j in range(n):
            dfs(m - 1, j, atlantic)

        # cells that can reach both oceans
        return list(pacific & atlantic)