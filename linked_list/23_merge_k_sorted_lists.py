"""
23. Merge K Sorted Lists

Description:
    Given an array of k linked lists, each sorted in ascending order,
    merge all lists into one sorted linked list and return it.

Approach:
    Use a min-heap to always pick the smallest node across all k lists.
    1. Push the head of each non-empty list into the heap as (val, i, node),
       where i is the list index to break ties when vals are equal.
    2. Pop the smallest node, attach it to the result linked list.
    3. If the popped node has a next, push next into the heap.
    4. Repeat until the heap is empty.

Tech Stack:
    - Min-heap (heapq) for efficient minimum selection
    - Dummy node for simplified linked list construction
    - In-place: reuses original nodes, only changes next pointers

Complexity:
    - Time: O(N log k), N = total nodes, each push/pop is O(log k)
    - Space: O(k), heap holds at most k nodes at a time
"""

import heapq


class Solution:
    def mergeKLists(self, lists):
        heap = []

        # push head of each non-empty list into heap
        # (val, list_index, node) — list_index breaks ties for equal vals
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        # dummy node to simplify building the result list
        dummy = ListNode()
        curr = dummy

        while heap:
            # pop the smallest node
            val, i, node = heapq.heappop(heap)

            # attach to result list
            curr.next = node
            curr = curr.next

            # if this node has a next, push it into heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next