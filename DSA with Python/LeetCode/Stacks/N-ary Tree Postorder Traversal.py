# PROBLEM NUMBER: 590
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# 590. N-ary Tree Postorder Traversal
# DIFFICULTY: EASY

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        # Approach:
        # We perform postorder traversal
        # on an N-ary tree using DFS.
        #
        # Postorder Traversal Order:
        # • Visit all children first
        # • Then visit root node
        #
        # Step 1:
        # Create a result list to store traversal.
        #
        # Step 2:
        # Define recursive DFS function.
        #
        # Step 3:
        # Base Case:
        # • If node is None → return
        #
        # Step 4:
        # Recursively traverse all children
        # from left to right.
        #
        # Step 5:
        # After processing children,
        # add current node value to result.
        #
        # Step 6:
        # Return final postorder traversal list.

        res = []

        def dfs(node):

            # Base case
            if not node:
                return

            # Visit all children first
            for child in node.children:
                dfs(child)

            # Visit root node
            res.append(node.val)

        dfs(root)

        return res