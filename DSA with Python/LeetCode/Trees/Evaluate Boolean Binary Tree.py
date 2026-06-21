# PROBLEM NUMBER: 2331
# https://leetcode.com/problems/evaluate-boolean-binary-tree/
# 2331. Evaluate Boolean Binary Tree
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        # Approach:
        # We use recursion to evaluate
        # the Boolean Binary Tree from
        # the bottom up.
        #
        # Leaf nodes represent Boolean
        # values:
        # • 0 -> False
        # • 1 -> True
        #
        # For a leaf node, simply return
        # its Boolean value.
        #
        # For an internal node:
        # • Recursively evaluate the
        #   left subtree.
        # • Recursively evaluate the
        #   right subtree.
        #
        # The node's value determines
        # the operation:
        # • 2 -> OR operation
        # • 3 -> AND operation
        #
        # Apply the corresponding
        # Boolean operation to the
        # results of the left and
        # right subtrees.
        #
        # The value computed at the
        # root is the final answer.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        # Leaf node
        if not root.left and not root.right:
            return bool(root.val)

        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        if root.val == 2:      # OR
            return left or right
        else:                  # AND (root.val == 3)
            return left and right