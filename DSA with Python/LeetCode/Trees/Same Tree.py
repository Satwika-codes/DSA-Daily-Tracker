# PROBLEM NUMBER: 100
# https://leetcode.com/problems/same-tree/
# 100. Same Tree
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        # Approach:
        # We use recursion to compare
        # both trees node by node.
        #
        # For each pair of nodes:
        # • If both nodes are None,
        #   they are identical.
        #
        # • If only one node is None,
        #   the trees are different.
        #
        # • If the node values are
        #   different, the trees are
        #   not the same.
        #
        # • Otherwise, recursively
        #   compare the left subtrees
        #   and the right subtrees.
        #
        # The trees are considered
        # identical only if every
        # corresponding node has the
        # same value and structure.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))