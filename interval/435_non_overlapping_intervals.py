"""
435. Non-overlapping Intervals

Description:
    Given an array of intervals, return the minimum number of intervals
    you need to remove to make the rest non-overlapping.
    Intervals that touch at endpoints (e.g. [1,2] and [2,3]) are not overlapping.

Approach:
    Greedy: sort intervals by end time. An interval ending earlier
    leaves more room for future intervals, so we always prefer to keep it.
    Scan left to right, tracking the end of the last kept interval (prev_end):
    - If current start < prev_end: overlap, remove current interval (count += 1).
    - Otherwise: no overlap, keep it and update prev_end.

Tech Stack:
    - Greedy algorithm
    - Sorting by interval end time

Complexity:
    - Time: O(n log n), sorting dominates
    - Space: O(1), only a counter and prev_end variable
"""


class Solution:
    def eraseOverlapIntervals(self, intervals):
        # sort by end time: ending earlier leaves more room
        intervals.sort(key=lambda x: x[1])

        count = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                # overlap: remove this interval (ends later), prev_end stays
                count += 1
            else:
                # no overlap: keep this interval, update prev_end
                prev_end = end

        return count