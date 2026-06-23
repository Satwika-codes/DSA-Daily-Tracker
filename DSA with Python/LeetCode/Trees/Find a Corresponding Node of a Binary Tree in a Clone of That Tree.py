# PROBLEM NUMBER: 1379
# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """

        # Approach:
        # We traverse both the original
        # and cloned trees simultaneously.
        #
        # Since both trees have identical
        # structure, corresponding nodes
        # will be visited together.
        #
        # For each pair of nodes:
        # • If the current node in the
        #   original tree is the target
        #   node, return the current
        #   node from the cloned tree.
        #
        # • Otherwise, recursively search
        #   the left subtrees.
        #
        # • If the target is found in the
        #   left subtree, return it.
        #
        # • Otherwise, continue searching
        #   the right subtrees.
        #
        # The first matching node found
        # in the cloned tree is the
        # required answer.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        if not original:
            return None

        if original == target:
            return cloned

        left = self.getTargetCopy(
            original.left,
            cloned.left,
            target
        )

        if left:
            return left

        return self.getTargetCopy(
            original.right,
            cloned.right,
            target
        )