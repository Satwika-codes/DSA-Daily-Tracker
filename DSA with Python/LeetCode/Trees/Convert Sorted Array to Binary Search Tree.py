# PROBLEM NUMBER: 108
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# 108. Convert Sorted Array to Binary Search Tree
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """

        # Approach:
        # We use a divide-and-conquer
        # strategy to construct a
        # height-balanced BST.
        #
        # Since the array is already
        # sorted, the middle element
        # should become the root of
        # the current subtree.
        #
        # For each recursive call:
        # • Select the middle element
        #   as the root node.
        #
        # • Recursively build the left
        #   subtree using elements on
        #   the left side of the middle.
        #
        # • Recursively build the right
        #   subtree using elements on
        #   the right side of the middle.
        #
        # The base case occurs when the
        # subarray becomes empty.
        #
        # Choosing the middle element
        # at every step keeps the tree
        # balanced and satisfies the
        # BST property.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(log n)
        # due to the recursion stack
        # for a balanced tree.

        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)