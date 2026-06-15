# PROBLEM NUMBER: 543
# https://leetcode.com/problems/diameter-of-binary-tree/
# 543. Diameter of Binary Tree
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # Approach:
        # We use Depth First Search (DFS)
        # to calculate the height of each
        # subtree while simultaneously
        # tracking the tree's diameter.
        #
        # For every node:
        # • Recursively find the height
        #   of the left subtree.
        # • Recursively find the height
        #   of the right subtree.
        #
        # The longest path passing through
        # the current node is equal to
        # left_height + right_height.
        #
        # Update the global diameter with
        # the maximum value encountered.
        #
        # The height of the current node
        # is 1 plus the maximum of the
        # left and right subtree heights.
        #
        # After traversing all nodes,
        # the stored diameter represents
        # the longest path between any
        # two nodes in the tree.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.diameter