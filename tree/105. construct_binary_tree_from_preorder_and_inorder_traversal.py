"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Description:
    Given two integer arrays preorder and inorder where preorder is the
    preorder traversal and inorder is the inorder traversal of the same tree,
    construct and return the binary tree.

Approach:
    Key insight: preorder's first element is always the root of the current subtree.
    Finding that root in inorder splits it into left subtree and right subtree.

    1. Build a hashmap (value -> index) for inorder to enable O(1) root lookup.
    2. Use a pointer (pre_nxt_idx) to pick the next root from preorder in order.
    3. Recursively build left subtree first, then right subtree.
       Order matters because preorder visits nodes as root -> left -> right,
       so the pointer must consume all left subtree nodes before right.

Tech Stack:
    - Recursion / Divide and Conquer
    - Hashmap for O(1) index lookup in inorder

Complexity:
    - Time: O(n), each node is created once, hashmap lookup is O(1)
    - Space: O(n), hashmap stores n entries + recursion stack up to O(n)
"""

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # hashmap: value -> index in inorder, for O(1) lookup
        inorder_map = {val: i for i, val in enumerate(inorder)}
        # pointer to the next root candidate in preorder
        self.pre_nxt_idx = 0

        def build(in_left, in_right):
            # base case: no elements in this range
            if in_left > in_right:
                return None

            # pick the next element from preorder as root
            root_val = preorder[self.pre_nxt_idx]
            self.pre_nxt_idx += 1
            root = TreeNode(root_val)

            # find root's position in inorder to split left/right
            mid = inorder_map[root_val]

            # build left subtree first (must be before right, matches preorder order)
            root.left = build(in_left, mid - 1)
            # then build right subtree
            root.right = build(mid + 1, in_right)

            return root

        return build(0, len(inorder) - 1)