# PROBLEM NUMBER: 700
# https://leetcode.com/problems/search-in-a-binary-search-tree/
# 700. Search in a Binary Search Tree
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        # Approach:
        # We take advantage of the
        # Binary Search Tree property.
        #
        # For every node:
        # • All values in the left
        #   subtree are smaller than
        #   the current node's value.
        #
        # • All values in the right
        #   subtree are greater than
        #   the current node's value.
        #
        # Starting from the root:
        # • If the current node is None
        #   or its value matches the
        #   target, return the node.
        #
        # • If the target value is
        #   smaller, search in the
        #   left subtree.
        #
        # • If the target value is
        #   greater, search in the
        #   right subtree.
        #
        # Continue recursively until
        # the target is found or the
        # search reaches a None node.
        #
        # Time Complexity: O(h)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary search tree.

        if not root or root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)

        return self.searchBST(root.right, val)