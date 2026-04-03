"""
261. Graph Valid Tree

Description:
    Given n nodes labeled 0 to n-1 and a list of undirected edges,
    determine if the edges form a valid tree.
    A valid tree must be connected and have no cycles.

Approach:
    A tree with n nodes has exactly n-1 edges. So:
    1. Check edge count == n - 1 (too few → disconnected, too many → cycle).
    2. Build adjacency list (undirected, so add both directions).
    3. DFS from node 0, check if all n nodes are reachable (connected).
    If both conditions met, it's a valid tree.

Tech Stack:
    - Undirected graph represented as adjacency list
    - DFS for connectivity check
    - Edge count check to rule out cycles

Complexity:
    - Time: O(V + E), build graph + DFS visits all nodes and edges once
    - Space: O(V + E), adjacency list + visited set + recursion stack
"""


class Solution:
    def validTree(self, n, edges):
        # a tree with n nodes must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        # build adjacency list (undirected: add both directions)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # DFS from node 0 to check connectivity
        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)

        # all nodes reachable → connected → valid tree
        return len(visited) == n