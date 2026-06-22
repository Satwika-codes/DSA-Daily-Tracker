# PROBLEM NUMBER: 671
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
# 671. Second Minimum Node In a Binary Tree
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # Approach:
        # The root contains the minimum
        # value in the special binary tree.
        #
        # We perform a DFS traversal and
        # search for the smallest value
        # that is strictly greater than
        # the root's value.
        #
        # During traversal:
        # • Let mn be the minimum value
        #   stored at the root.
        #
        # • For each node, check whether
        #   its value is greater than mn
        #   and smaller than the current
        #   second minimum candidate.
        #
        # • If so, update the answer.
        #
        # Continue exploring both left
        # and right subtrees until all
        # nodes have been visited.
        #
        # If no value greater than mn is
        # found, then a second minimum
        # value does not exist, so
        # return -1.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        self.ans = float('inf')
        mn = root.val

        def dfs(node):
            if not node:
                return

            if mn < node.val < self.ans:
                self.ans = node.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return self.ans if self.ans != float('inf') else -1