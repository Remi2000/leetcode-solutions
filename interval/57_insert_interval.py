"""
57. Insert Interval

Description:
    Given an array of non-overlapping intervals sorted by start time,
    insert a new interval and merge if necessary.
    Return the resulting array of non-overlapping intervals.

Approach:
    Three-phase linear scan sharing a single index i:
    1. Add all intervals that end before newInterval starts (no overlap).
    2. Merge all overlapping intervals with newInterval by taking
       min of starts and max of ends, then add the merged interval.
    3. Add all remaining intervals that start after newInterval ends.

Tech Stack:
    - Linear scan with shared index across three while loops
    - Interval merging with min/max

Complexity:
    - Time: O(n), each interval is visited exactly once across all phases
    - Space: O(n), result array stores all intervals
"""


class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)

        # phase 1: add all intervals that end before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # phase 2: merge all overlapping intervals with newInterval
        start = newInterval[0]
        end = newInterval[1]
        while i < n and intervals[i][0] <= end:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i += 1
        result.append([start, end])

        # phase 3: add all remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result