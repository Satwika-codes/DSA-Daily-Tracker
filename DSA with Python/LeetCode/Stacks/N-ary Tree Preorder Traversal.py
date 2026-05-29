# PROBLEM NUMBER: 589
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
# 589. N-ary Tree Preorder Traversal
# DIFFICULTY: EASY

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        # Approach:
        # We perform preorder traversal
        # on an N-ary tree using DFS.
        #
        # Preorder Traversal Order:
        # • Visit root node first
        # • Then recursively visit all children
        #   from left to right
        #
        # Step 1:
        # Create a result list to store traversal.
        #
        # Step 2:
        # Define a recursive DFS function.
        #
        # Step 3:
        # Base Case:
        # • If node is None → return
        #
        # Step 4:
        # Visit current node:
        # • Add node value to result
        #
        # Step 5:
        # Recursively traverse all children.
        #
        # Step 6:
        # Return preorder traversal list.

        res = []

        def dfs(node):

            # Base case
            if not node:
                return

            # Visit root first
            res.append(node.val)

            # Visit all children
            for child in node.children:
                dfs(child)

        dfs(root)

        return res