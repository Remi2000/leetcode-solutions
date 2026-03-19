"""
230. Kth Smallest Element in a BST

Description:
    Given the root of a BST and an integer k, return the kth smallest
    value (1-indexed) among all node values in the tree.

Approach:
    BST inorder traversal (left -> root -> right) produces values in
    ascending order. Perform inorder traversal and count nodes visited.
    When count reaches k, we have the answer.

Tech Stack:
    - BST (Binary Search Tree)
    - Inorder Traversal (Recursion)

Complexity:
    Time:  O(k) - traverse until the kth node, worst case O(n)
    Space: O(h) - recursion stack depth = tree height, O(log n) balanced, O(n) skewed
"""


class Solution:
    def kthSmallest(self, root, k):
        self.count = 0
        self.result = 0

        def inorder(node):
            if not node:
                return

            # Go left first (smaller values)
            inorder(node.left)

            # Visit current node, count it
            self.count += 1
            if self.count == k:
                self.result = node.val
                return

            # Go right (larger values)
            inorder(node.right)

        inorder(root)
        return self.result