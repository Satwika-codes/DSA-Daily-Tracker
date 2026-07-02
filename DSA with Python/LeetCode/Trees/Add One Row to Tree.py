# PROBLEM NUMBER: 623
# https://leetcode.com/problems/add-one-row-to-tree/
# 623. Add One Row to Tree
# DIFFICULTY: MEDIUM

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :type depth: int
        :rtype: Optional[TreeNode]
        """

        # Approach:
        # We use DFS to reach all nodes
        # at depth - 1, since the new
        # row must be inserted directly
        # below them.
        #
        # Special case:
        # • If depth is 1, create a new
        #   root with the given value
        #   and attach the original tree
        #   as its left child.
        #
        # Otherwise:
        # • Recursively traverse the tree
        #   while keeping track of the
        #   current depth.
        #
        # • When a node at depth - 1 is
        #   reached:
        #   - Store its original left
        #     and right children.
        #
        #   - Create two new nodes with
        #     the given value.
        #
        #   - Attach the original left
        #     subtree to the left child
        #     of the new left node.
        #
        #   - Attach the original right
        #     subtree to the right child
        #     of the new right node.
        #
        # Continue until all required
        # insertions are completed.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        def dfs(node, curr_depth):
            if not node:
                return

            if curr_depth == depth - 1:
                left = node.left
                right = node.right

                node.left = TreeNode(val)
                node.right = TreeNode(val)

                node.left.left = left
                node.right.right = right

                return

            dfs(node.left, curr_depth + 1)
            dfs(node.right, curr_depth + 1)

        dfs(root, 1)
        return root