"""
230. Kth Smallest Element in a BST

Description:
    Given the root of a binary search tree and an integer k,
    return the kth smallest value (1-indexed) of all the values
    of the nodes in the tree.

Approach:
    Use iterative inorder traversal (left -> root -> right) with a stack.
    In a BST, inorder traversal visits nodes in ascending order,
    so the kth node visited is the kth smallest.
    Each time we pop a node from the stack, decrement k.
    When k reaches 0, the current node is the answer.

Tech Stack:
    - Iterative inorder traversal with explicit stack
    - BST property: inorder traversal yields sorted order

Complexity:
    - Time: O(H + k), where H is the tree height (go left first) and k is the target
    - Space: O(H), stack holds at most H nodes (height of the tree)
"""


class Solution:
    def kthSmallest(self, root, k):
        stack = []
        curr = root

        while curr or stack:
            # push all left children onto stack (go as small as possible)
            while curr:
                stack.append(curr)
                curr = curr.left

            # pop the smallest unvisited node
            curr = stack.pop()
            k -= 1

            # found the kth smallest
            if k == 0:
                return curr.val

            # move to right subtree for next inorder node
            curr = curr.right