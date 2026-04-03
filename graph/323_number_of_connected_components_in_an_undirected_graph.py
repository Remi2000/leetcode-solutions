"""
323. Number of Connected Components in an Undirected Graph

Description:
    Given n nodes labeled 0 to n-1 and a list of undirected edges,
    return the number of connected components in the graph.

Approach:
    Build an adjacency list (undirected, add both directions).
    Iterate through all nodes. For each unvisited node, run DFS
    to visit all reachable nodes (one connected component) and
    increment the count. Same pattern as 200 Number of Islands
    but on a graph instead of a matrix.

Tech Stack:
    - Undirected graph represented as adjacency list
    - DFS for traversing each connected component
    - Set for tracking visited nodes

Complexity:
    - Time: O(V + E), each node and edge visited once
    - Space: O(V + E), adjacency list + visited set + recursion stack
"""


class Solution:
    def countComponents(self, n, edges):
        # build adjacency list (undirected: add both directions)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        count = 0

        def dfs(node):
            # mark current node as visited
            visited.add(node)
            # visit all unvisited neighbors
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        # each unvisited node starts a new DFS = one connected component
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count