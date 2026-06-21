# PROBLEM NUMBER: 230
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# 230. Kth Smallest Element in a BST
# DIFFICULTY: MEDIUM

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        # Approach:
        # We perform an iterative
        # inorder traversal of the
        # Binary Search Tree.
        #
        # In a BST, inorder traversal
        # visits nodes in ascending
        # sorted order.
        #
        # A stack is used to simulate
        # the recursion process.
        #
        # For each step:
        # • Move as far left as possible,
        #   pushing all nodes onto the
        #   stack.
        #
        # • Pop the top node from the
        #   stack. This is the next
        #   smallest element.
        #
        # • Decrement k because one
        #   more element has been
        #   processed.
        #
        # • When k becomes 0, the
        #   current node's value is
        #   the kth smallest element.
        #
        # • Continue traversal by
        #   moving to the right subtree.
        #
        # Time Complexity: O(h + k)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary search tree.

        stack = []
        curr = root

        while True:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val

            curr = curr.right