# PROBLEM NUMBER: 129
# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# 129. Sum Root to Leaf Numbers
# DIFFICULTY: MEDIUM

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # Approach:
        # We use DFS to traverse every
        # root-to-leaf path in the tree.
        #
        # As we move down a path, we
        # build the number represented
        # by the node values.
        #
        # For each node:
        # • Multiply the current number
        #   by 10.
        #
        # • Add the current node's value.
        #
        # This appends the node's digit
        # to the number formed so far.
        #
        # When a leaf node is reached,
        # the complete number for that
        # root-to-leaf path is returned.
        #
        # For non-leaf nodes:
        # • Recursively compute the sum
        #   from the left subtree.
        #
        # • Recursively compute the sum
        #   from the right subtree.
        #
        # The final answer is the sum
        # of all root-to-leaf numbers.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        def dfs(node, cur):
            if not node:
                return 0

            cur = cur * 10 + node.val

            # Leaf node
            if not node.left and not node.right:
                return cur

            return dfs(node.left, cur) + dfs(node.right, cur)

        return dfs(root, 0)