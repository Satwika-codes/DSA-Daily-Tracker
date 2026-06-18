# PROBLEM NUMBER: 559
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# 559. Maximum Depth of N-ary Tree
# DIFFICULTY: EASY

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        # Approach:
        # We use recursion to find the
        # maximum depth of the N-ary tree.
        #
        # If the current node is None,
        # its depth is 0.
        #
        # If the node has no children,
        # it is a leaf node and its
        # depth is 1.
        #
        # Otherwise:
        # • Recursively compute the
        #   depth of each child.
        #
        # • Take the maximum depth
        #   among all children.
        #
        # • Add 1 for the current node.
        #
        # The final result represents
        # the length of the longest
        # path from the root to any
        # leaf node.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the N-ary tree.

        if not root:
            return 0

        if not root.children:
            return 1

        return 1 + max(self.maxDepth(child) for child in root.children)