"""
207. Course Schedule

Description:
    Given numCourses and a list of prerequisites where [a, b] means
    course a requires course b, determine if all courses can be finished.
    Equivalent to detecting if a directed graph has a cycle.

Approach:
    Build an adjacency list from prerequisites, then use DFS to detect cycles.
    Each node has three states: 0 (unvisited), 1 (visiting / in current path),
    2 (done / confirmed safe).
    - If DFS hits a node with state 1, we've looped back → cycle exists.
    - If DFS hits a node with state 2, it was already verified safe → skip.
    If any cycle is found, return False. Otherwise return True.

Tech Stack:
    - Directed graph represented as adjacency list
    - DFS with three-state cycle detection

Complexity:
    - Time: O(V + E), V = numCourses, E = len(prerequisites),
            each node and edge visited once
    - Space: O(V + E), adjacency list + state array + recursion stack
"""


class Solution:
    def canFinish(self, numCourses, prerequisites):
        # build adjacency list: graph[i] stores prerequisites of course i
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # 0 = unvisited, 1 = visiting (in current path), 2 = done (safe)
        state = [0] * numCourses

        def has_cycle(course):
            # currently being visited in this path → cycle detected
            if state[course] == 1:
                return True
            # already fully checked and safe → skip
            if state[course] == 2:
                return False

            # mark as visiting
            state[course] = 1

            # check all prerequisites
            for prereq in graph[course]:
                if has_cycle(prereq):
                    return True

            # all dependencies clear, mark as done
            state[course] = 2
            return False

        # check every course (graph may be disconnected)
        for course in range(numCourses):
            if has_cycle(course):
                return False

        return True