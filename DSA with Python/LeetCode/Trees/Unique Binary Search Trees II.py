# PROBLEM NUMBER: 95
# https://leetcode.com/problems/unique-binary-search-trees-ii/
# 95. Unique Binary Search Trees II
# DIFFICULTY: MEDIUM

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """

        # Approach:
        # We use recursion to generate
        # all possible Binary Search
        # Trees (BSTs).
        #
        # For every range [left, right]:
        # • Consider each value in the
        #   range as the root of the
        #   current BST.
        #
        # • Recursively generate every
        #   possible left subtree using
        #   values smaller than the root.
        #
        # • Recursively generate every
        #   possible right subtree using
        #   values greater than the root.
        #
        # Every combination of a left
        # subtree and a right subtree
        # forms a unique BST with the
        # chosen root.
        #
        # Create a new root node for
        # each combination and add it
        # to the answer list.
        #
        # The base case occurs when
        # left > right, representing
        # an empty subtree.
        #
        # The recursive process returns
        # all structurally unique BSTs
        # containing values from 1 to n.
        #
        # Time Complexity: O(Cn × n)
        # where Cn is the nth Catalan
        # number (number of unique BSTs).
        #
        # Space Complexity: O(Cn × n)
        # for storing all generated trees.

        if n == 0:
            return []

        def build(left, right):
            if left > right:
                return [None]

            trees = []

            for root_val in range(left, right + 1):
                left_trees = build(left, root_val - 1)
                right_trees = build(root_val + 1, right)

                for left_root in left_trees:
                    for right_root in right_trees:
                        root = TreeNode(root_val)
                        root.left = left_root
                        root.right = right_root
                        trees.append(root)

            return trees

        return build(1, n)