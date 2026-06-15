# PROBLEM NUMBER: 112
# https://leetcode.com/problems/path-sum/
# 112. Path Sum
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        # Approach:
        # We use recursion to explore
        # all root-to-leaf paths in
        # the binary tree.
        #
        # At each node:
        # • Subtract the node's value
        #   from the remaining target sum.
        #
        # • Recursively check the left
        #   and right subtrees with the
        #   updated target value.
        #
        # When a leaf node is reached:
        # • Check whether its value is
        #   equal to the remaining
        #   target sum.
        #
        # If any root-to-leaf path has
        # a sum equal to targetSum,
        # return True.
        #
        # Otherwise, return False after
        # exploring all possible paths.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        if not root:
            return False

        # Leaf node
        if not root.left and not root.right:
            return targetSum == root.val

        targetSum -= root.val

        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))