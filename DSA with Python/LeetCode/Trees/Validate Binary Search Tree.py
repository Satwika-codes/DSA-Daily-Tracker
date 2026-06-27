# PROBLEM NUMBER: 98
# https://leetcode.com/problems/validate-binary-search-tree/
# 98. Validate Binary Search Tree
# DIFFICULTY: MEDIUM

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        # Approach:
        # We use DFS while maintaining
        # the valid range of values
        # for every node.
        #
        # Initially, the root can have
        # any value, so its range is
        # (-∞, +∞).
        #
        # For each node:
        # • Its value must be strictly
        #   greater than the lower bound.
        #
        # • Its value must be strictly
        #   smaller than the upper bound.
        #
        # If the value violates either
        # bound, the tree is not a
        # valid BST.
        #
        # Otherwise:
        # • Recursively validate the
        #   left subtree with the
        #   current node's value as
        #   the new upper bound.
        #
        # • Recursively validate the
        #   right subtree with the
        #   current node's value as
        #   the new lower bound.
        #
        # The tree is a valid BST only
        # if every node satisfies its
        # allowed range.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        def dfs(node, low, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (dfs(node.left, low, node.val) and
                    dfs(node.right, node.val, high))

        return dfs(root, float('-inf'), float('inf'))