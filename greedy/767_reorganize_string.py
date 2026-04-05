"""
Description:
    Given a string s, rearrange its characters so that no two adjacent characters
    are the same. Return any valid rearrangement, or "" if it is not possible.

Approach:
    Greedy with max heap - always place the most frequent remaining character first.
    If the most frequent character conflicts with the last placed character, temporarily
    place the second most frequent character instead, then push the first back onto the heap.
    If no second character exists at that point, the string cannot be reorganized.

Tech Stack:
    - Max heap (simulated via negative frequencies in Python's heapq) to greedily
      pick the most frequent character at each step
    - Counter to build initial character frequencies

Complexity:
    Time:  O(n log k) - n characters placed, each heap operation is O(log k)
                        where k is the number of distinct characters (at most 26)
    Space: O(k)       - heap stores at most k distinct characters
"""

import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        # build max heap using negative frequencies (Python only has min heap)
        max_heap = []
        for char, freq in count.items():
            heapq.heappush(max_heap, (-freq, char))

        res = ""

        while max_heap:
            freq, char = heapq.heappop(max_heap)  # most frequent remaining character

            if not res or res[-1] != char:
                # safe to place: different from last character
                res += char
                if freq + 1 != 0:                 # still has remaining count, push back
                    heapq.heappush(max_heap, (freq + 1, char))
            else:
                # conflict: char matches last placed, must use second most frequent
                if not max_heap:
                    # only one distinct character left but it cannot be placed adjacent - unsolvable
                    return ""
                freq2, char2 = heapq.heappop(max_heap)
                res += char2
                if freq2 + 1 != 0:
                    heapq.heappush(max_heap, (freq2 + 1, char2))
                heapq.heappush(max_heap, (freq, char))  # push char back regardless

        return res