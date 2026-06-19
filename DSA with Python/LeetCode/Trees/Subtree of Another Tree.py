# PROBLEM NUMBER: 572
# https://leetcode.com/problems/subtree-of-another-tree/
# 572. Subtree of Another Tree
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """

        # Approach:
        # We recursively examine every
        # node in the main tree as a
        # potential starting point for
        # the subtree.
        #
        # For each node:
        # • Check whether the tree rooted
        #   at that node is identical to
        #   subRoot.
        #
        # To compare two trees, use a
        # helper function that verifies:
        # • Both nodes are None.
        # • Both nodes have the same value.
        # • Their left subtrees match.
        # • Their right subtrees match.
        #
        # If an identical tree is found,
        # return True immediately.
        #
        # Otherwise, continue searching
        # in the left and right subtrees
        # of the current node.
        #
        # If no matching subtree exists,
        # return False.
        #
        # Time Complexity: O(n × m)
        # where n = number of nodes in root
        # and m = number of nodes in subRoot.
        #
        # Space Complexity: O(h)
        # where h is the height of the tree.

        def sameTree(a, b):
            if not a and not b:
                return True

            if not a or not b:
                return False

            if a.val != b.val:
                return False

            return (sameTree(a.left, b.left) and
                    sameTree(a.right, b.right))

        if not root:
            return False

        if sameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))