# PROBLEM NUMBER: 2236
# https://leetcode.com/problems/root-equals-sum-of-children/
# 2236. Root Equals Sum of Children
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        # Approach:
        # The tree consists of a root
        # node and its two children.
        #
        # We simply compare:
        # • The value of the root node.
        # • The sum of the left and
        #   right child values.
        #
        # If the root value equals the
        # sum of its children, return
        # True.
        #
        # Otherwise, return False.
        #
        # Time Complexity: O(1)
        # Space Complexity: O(1)

        return root.val == root.left.val + root.right.val