# PROBLEM NUMBER: 102
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# 102. Binary Tree Level Order Traversal
# DIFFICULTY: MEDIUM

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        # Approach:
        # We use Breadth-First Search
        # (Level Order Traversal) to
        # visit the tree level by level.
        #
        # A queue stores the nodes
        # waiting to be processed.
        #
        # Initially, the root node is
        # added to the queue.
        #
        # For each level:
        # • Determine the number of
        #   nodes currently in the queue.
        #
        # • Remove exactly those nodes
        #   from the queue and store
        #   their values in a list.
        #
        # • Add each node's left and
        #   right children to the queue
        #   for the next level.
        #
        # After processing all nodes
        # in the current level, append
        # the level's list to the answer.
        #
        # Continue until the queue
        # becomes empty.
        #
        # The final answer contains the
        # values of all nodes grouped
        # by their respective levels.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(w)
        # where w is the maximum width
        # of the binary tree.

        if not root:
            return []

        ans = []
        q = deque([root])

        while q:
            level = []
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(level)

        return ans