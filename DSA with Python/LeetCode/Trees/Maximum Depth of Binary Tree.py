# PROBLEM NUMBER: 104
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# 104. Maximum Depth of Binary Tree
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # Approach:
        # We use recursion to find the
        # maximum depth of the binary tree.
        #
        # For each node:
        # • Recursively calculate the
        #   depth of the left subtree.
        # • Recursively calculate the
        #   depth of the right subtree.
        #
        # The depth of the current node
        # is 1 plus the maximum of the
        # left and right subtree depths.
        #
        # If the node is None, its depth
        # is 0, which serves as the
        # base case for recursion.
        #
        # The recursion continues until
        # all nodes have been processed,
        # and the depth of the root node
        # becomes the answer.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        if not root:
            return 0

        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )