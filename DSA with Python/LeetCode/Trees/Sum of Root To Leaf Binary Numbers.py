# PROBLEM NUMBER: 1022
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# 1022. Sum of Root To Leaf Binary Numbers
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # Approach:
        # We perform a DFS traversal
        # from the root to every leaf.
        #
        # Along each path, we build the
        # binary number represented by
        # the node values.
        #
        # For every node:
        # • Multiply the current value
        #   by 2 (left shift in binary).
        # • Add the current node's value.
        #
        # This appends the node's bit
        # to the binary number formed
        # so far.
        #
        # When a leaf node is reached,
        # the complete binary number
        # is returned.
        #
        # For non-leaf nodes:
        # • Recursively compute the
        #   contribution from the left
        #   subtree.
        # • Recursively compute the
        #   contribution from the right
        #   subtree.
        #
        # The final answer is the sum
        # of all root-to-leaf binary
        # numbers.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        def dfs(node, cur):
            if not node:
                return 0

            cur = cur * 2 + node.val

            if not node.left and not node.right:
                return cur

            return dfs(node.left, cur) + dfs(node.right, cur)

        return dfs(root, 0)