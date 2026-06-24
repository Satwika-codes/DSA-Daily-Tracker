# PROBLEM NUMBER: 993
# https://leetcode.com/problems/cousins-in-binary-tree/
# 993. Cousins in Binary Tree
# DIFFICULTY: EASY

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """

        # Approach:
        # We use Breadth-First Search
        # (Level Order Traversal) to
        # process the tree one level
        # at a time.
        #
        # Along with each node, we store
        # its parent in the queue.
        #
        # For every level:
        # • Search for nodes x and y.
        #
        # • If found, record their
        #   respective parents.
        #
        # After processing the level:
        # • If both nodes are found,
        #   they are cousins only if
        #   their parents are different.
        #
        # • If only one node is found,
        #   they cannot be cousins
        #   because cousins must be
        #   at the same depth.
        #
        # Continue level by level until
        # the answer is determined.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(w)
        # where w is the maximum width
        # of the binary tree.

        q = deque([(root, None)])  # (node, parent)

        while q:
            size = len(q)
            px = py = None

            for _ in range(size):
                node, parent = q.popleft()

                if node.val == x:
                    px = parent

                if node.val == y:
                    py = parent

                if node.left:
                    q.append((node.left, node))

                if node.right:
                    q.append((node.right, node))

            if px and py:
                return px != py

            if px or py:
                return False

        return False