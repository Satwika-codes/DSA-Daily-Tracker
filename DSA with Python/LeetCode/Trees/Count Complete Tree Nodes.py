# PROBLEM NUMBER: 222
# https://leetcode.com/problems/count-complete-tree-nodes/
# 222. Count Complete Tree Nodes
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # Approach:
        # We use recursion to count
        # the total number of nodes
        # in the binary tree.
        #
        # For each node:
        # • Count the current node.
        # • Recursively count nodes
        #   in the left subtree.
        # • Recursively count nodes
        #   in the right subtree.
        #
        # The total count is the sum
        # of the current node and the
        # counts from both subtrees.
        #
        # The base case occurs when
        # the current node is None,
        # which contributes 0 nodes.
        #
        # By visiting every node once,
        # we obtain the total number
        # of nodes in the tree.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        if not root:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)