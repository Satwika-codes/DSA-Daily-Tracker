# PROBLEM NUMBER: 226
# https://leetcode.com/problems/invert-binary-tree/
# 226. Invert Binary Tree
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        # Approach:
        # We use recursion to traverse
        # every node in the binary tree.
        #
        # For each node:
        # • Swap its left and right
        #   child pointers.
        #
        # • Recursively invert the
        #   left subtree.
        #
        # • Recursively invert the
        #   right subtree.
        #
        # The base case occurs when
        # the current node is None,
        # in which case there is
        # nothing to invert.
        #
        # After all recursive calls
        # finish, every node in the
        # tree has its children swapped,
        # producing the inverted tree.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root