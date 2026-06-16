# PROBLEM NUMBER: 404
# https://leetcode.com/problems/sum-of-left-leaves/
# 404. Sum of Left Leaves
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # Approach:
        # We use recursion to traverse
        # the entire binary tree.
        #
        # For each node:
        # • Check whether its left child
        #   exists and is a leaf node.
        #
        # • If it is a left leaf, add its
        #   value to the answer.
        #
        # • Recursively process the left
        #   subtree to find other left
        #   leaves.
        #
        # • Recursively process the right
        #   subtree to find other left
        #   leaves.
        #
        # The final answer is the sum of
        # all left leaf node values found
        # during the traversal.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        if not root:
            return 0

        ans = 0

        if root.left and not root.left.left and not root.left.right:
            ans += root.left.val

        ans += self.sumOfLeftLeaves(root.left)
        ans += self.sumOfLeftLeaves(root.right)

        return ans