"""
2. Add Two Numbers

Description:
    Given two non-empty linked lists representing two non-negative integers
    stored in reverse order (ones digit first), add the two numbers and
    return the sum as a linked list in the same reverse order.

Approach:
    Simulate elementary addition digit by digit from head to tail.
    Use a carry variable to handle sums >= 10.
    Use a dummy head node to simplify new list construction.

Tech Stack:
    - Linked List
    - Dummy Head Node
    - Math (carry handling)

Complexity:
    Time:  O(max(m, n)) - traverse the longer list once
    Space: O(max(m, n)) - new list has at most max(m, n) + 1 nodes
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Dummy head node to avoid special-casing the first node
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # Keep going while there are digits left or a carry to process
        while l1 or l2 or carry:
            # If a list is exhausted, treat its value as 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add two digits plus carry, just like elementary math
            total = val1 + val2 + carry
            carry = total // 10  # Carry for next position (0 or 1)
            digit = total % 10   # Current digit to store

            # Append new digit node to result list
            curr.next = ListNode(digit)
            curr = curr.next

            # Advance pointers only if the list hasn't ended
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # Skip the dummy node and return the actual head
        return dummy.next