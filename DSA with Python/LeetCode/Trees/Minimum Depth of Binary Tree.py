# PROBLEM NUMBER: 111
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# 111. Minimum Depth of Binary Tree
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # Approach:
        # We use recursion to find the
        # minimum depth from the root
        # to any leaf node.
        #
        # If the current node is None,
        # its depth is 0.
        #
        # If the current node is a leaf,
        # the minimum depth is 1.
        #
        # When a node has only one child,
        # we must continue through the
        # existing child because a path
        # ending at a missing child is
        # not a valid root-to-leaf path.
        #
        # When both children exist:
        # • Recursively find the minimum
        #   depth of the left subtree.
        # • Recursively find the minimum
        #   depth of the right subtree.
        # • Take the smaller depth.
        #
        # Add 1 for the current node
        # and return the result.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        if not root:
            return 0

        # Leaf node
        if not root.left and not root.right:
            return 1

        if not root.left:
            return 1 + self.minDepth(root.right)

        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(
            self.minDepth(root.left),
            self.minDepth(root.right)
        )