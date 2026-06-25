# PROBLEM NUMBER: 110
# https://leetcode.com/problems/balanced-binary-tree/
# 110. Balanced Binary Tree
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        # Approach:
        # We use a postorder DFS traversal
        # to compute subtree heights while
        # simultaneously checking whether
        # the tree is balanced.
        #
        # For each node:
        # • Recursively compute the height
        #   of the left subtree.
        #
        # • Recursively compute the height
        #   of the right subtree.
        #
        # • If either subtree is already
        #   unbalanced, immediately return
        #   -1 to propagate the failure.
        #
        # • If the height difference
        #   between the left and right
        #   subtrees is greater than 1,
        #   return -1.
        #
        # • Otherwise, return the height
        #   of the current subtree.
        #
        # A return value of -1 indicates
        # an unbalanced subtree.
        #
        # After processing the root:
        # • If the result is -1, the tree
        #   is not balanced.
        #
        # • Otherwise, the tree is balanced.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            if left == -1:
                return -1

            right = height(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return height(root) != -1