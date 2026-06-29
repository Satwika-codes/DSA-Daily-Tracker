# PROBLEM NUMBER: 113
# https://leetcode.com/problems/path-sum-ii/
# 113. Path Sum II
# DIFFICULTY: MEDIUM

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """

        # Approach:
        # We perform a DFS traversal
        # while maintaining:
        # • The current path from the
        #   root to the current node.
        # • The sum of values along
        #   that path.
        #
        # At each node:
        # • Add the node's value to
        #   the current sum.
        #
        # • Append the node's value
        #   to the current path.
        #
        # If the node is a leaf:
        # • Check whether the current
        #   path sum equals targetSum.
        #
        # • If it does, store a copy
        #   of the current path in
        #   the answer list.
        #
        # Otherwise:
        # • Recursively explore the
        #   left subtree.
        #
        # • Recursively explore the
        #   right subtree.
        #
        # After exploring both children,
        # remove the current node from
        # the path (backtracking) so
        # the path can be reused for
        # other branches.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        ans = []

        def dfs(node, curr_sum, path):
            if not node:
                return

            curr_sum += node.val
            path.append(node.val)

            # Leaf node
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    ans.append(path[:])
            else:
                dfs(node.left, curr_sum, path)
                dfs(node.right, curr_sum, path)

            path.pop()

        dfs(root, 0, [])

        return ans