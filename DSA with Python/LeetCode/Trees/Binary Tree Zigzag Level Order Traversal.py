# PROBLEM NUMBER: 103
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# 103. Binary Tree Zigzag Level Order Traversal
# DIFFICULTY: MEDIUM

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        # Approach:
        # We use Breadth-First Search
        # (Level Order Traversal) to
        # process the tree one level
        # at a time.
        #
        # A queue stores the nodes
        # waiting to be processed.
        #
        # A boolean flag keeps track
        # of the traversal direction
        # for the current level.
        #
        # For each level:
        # • Remove all nodes belonging
        #   to the current level.
        #
        # • If traversing from left to
        #   right, append node values
        #   to the level list.
        #
        # • Otherwise, insert each value
        #   at the beginning of the
        #   level list to obtain the
        #   reverse order.
        #
        # • Add the left and right
        #   children to the queue for
        #   the next level.
        #
        # After each level, flip the
        # traversal direction so the
        # next level is processed in
        # the opposite order.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(w)
        # where w is the maximum width
        # of the binary tree.

        if not root:
            return []

        ans = []
        q = deque([root])
        left_to_right = True

        while q:
            level = []
            size = len(q)

            for _ in range(size):
                node = q.popleft()

                if left_to_right:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(level)
            left_to_right = not left_to_right

        return ans