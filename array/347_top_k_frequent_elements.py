"""
347. Top K Frequent Elements

Description:
    Given an integer array nums and an integer k, return the k most
    frequent elements. You may return the answer in any order.

Approach 1 - Counter.most_common:
    Count frequencies with Counter, use built-in most_common(k)
    to get the k most frequent elements directly. Most concise.
    Time: O(n log n), Space: O(n)

Approach 2 - Counter + Sort:
    Count frequencies with Counter, sort by frequency descending,
    return the top k elements. Same idea as most_common but manual.
    Time: O(n log n), Space: O(n)

Approach 3 - Counter + Heap:
    Count frequencies with Counter, maintain a min-heap of size k.
    For each element, push (freq, num) into the heap. If heap size
    exceeds k, pop the smallest freq. The heap always keeps the
    k most frequent elements.
    Time: O(n log k), Space: O(n)
    Faster when k is much smaller than n.

Tech Stack:
    - Counter for frequency counting
    - Sorting (approach 1) / Min-heap (approach 2)
    - Tuple ordering: heap sorts by first element of tuple (freq)
"""

# ========== Approach 1: Counter.most_common ==========

from collections import Counter


class SolutionMostCommon:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        # most_common(k) returns the k most frequent as [(num, freq), ...]
        return [num for num, freq in count.most_common(k)]


# ========== Approach 2: Counter + Sort ==========

from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        # sort by frequency descending, take top k keys
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]


# ========== Approach 3: Counter + Heap ==========

import heapq
from collections import Counter


class SolutionHeap:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        heap = []

        for num, freq in count.items():
            # push (freq, num): heap sorts by first element (freq)
            heapq.heappush(heap, (freq, num))
            # keep heap size at k, pop the smallest freq
            if len(heap) > k:
                heapq.heappop(heap)

        # heap contains the k most frequent elements
        return [num for freq, num in heap]