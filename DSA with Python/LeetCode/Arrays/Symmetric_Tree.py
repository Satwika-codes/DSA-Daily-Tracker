# PROBLEM NUMBER: 101
# https://leetcode.com/problems/symmetric-tree/
# 101.Symmetric Tree
# DIFFICULTY: EASY
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        # Approach:
        # ----------------------------------------------------------
        # A tree is symmetric if:
        # - The left subtree is a mirror of the right subtree.
        #
        # We use a helper function check(left, right) that verifies:
        # 1. Both nodes are None → symmetric.
        # 2. Only one is None → not symmetric.
        # 3. Values are different → not symmetric.
        # 4. Recursively check:
        #       left.left  ↔ right.right
        #       left.right ↔ right.left
        #
        # This performs a mirror comparison at every node pair.

        if not root:
            return True
        
        return self.check(root.left, root.right)

    def check(self, left, right):
        # Case 1: Both nodes are None → symmetric
        if not left and not right:
            return True

        # Case 2: One is None → asymmetric
        if not left or not right:
            return False

        # Case 3: Values do not match → asymmetric
        if left.val != right.val:
            return False

        # Case 4: Recursively compare mirror children
        return (
            self.check(left.left, right.right) and
            self.check(left.right, right.left)
        )
