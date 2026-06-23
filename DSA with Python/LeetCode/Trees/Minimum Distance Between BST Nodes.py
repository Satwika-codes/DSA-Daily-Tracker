# PROBLEM NUMBER: 783
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# 783. Minimum Distance Between BST Nodes
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # Approach:
        # We perform an inorder traversal
        # of the Binary Search Tree.
        #
        # Inorder traversal of a BST
        # visits nodes in sorted order.
        #
        # Therefore, the minimum distance
        # between any two nodes must occur
        # between two consecutive values
        # in this sorted sequence.
        #
        # During traversal:
        # • Keep track of the previously
        #   visited node value.
        #
        # • Compute the difference between
        #   the current value and the
        #   previous value.
        #
        # • Update the minimum difference
        #   whenever a smaller value is
        #   found.
        #
        # Continue until all nodes have
        # been processed.
        #
        # The smallest difference found
        # is returned as the answer.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary search tree.

        self.prev = None
        self.ans = float('inf')

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev is not None:
                self.ans = min(self.ans, node.val - self.prev)

            self.prev = node.val

            inorder(node.right)

        inorder(root)

        return self.ans