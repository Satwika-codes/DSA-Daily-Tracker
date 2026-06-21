# PROBLEM NUMBER: 637
# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# 637. Average of Levels in Binary Tree
# DIFFICULTY: EASY

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """

        # Approach:
        # We use Breadth-First Search
        # (Level Order Traversal) to
        # process the tree level by level.
        #
        # A queue stores all nodes that
        # belong to the current level.
        #
        # For each level:
        # • Determine the number of nodes
        #   present in that level.
        #
        # • Remove every node from the
        #   queue and accumulate their
        #   values into a level sum.
        #
        # • Add the node's children to
        #   the queue for processing in
        #   the next level.
        #
        # After processing all nodes in
        # the current level, compute:
        # average = level_sum / level_size
        #
        # Store the average in the answer
        # list and continue until all
        # levels have been processed.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(w)
        # where w is the maximum width
        # of the binary tree.

        ans = []
        q = deque([root])

        while q:
            level_size = len(q)
            level_sum = 0

            for _ in range(level_size):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(float(level_sum) / level_size)

        return ans