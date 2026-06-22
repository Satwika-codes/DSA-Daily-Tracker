# PROBLEM NUMBER: 617
# https://leetcode.com/problems/merge-two-binary-trees/
# 617. Merge Two Binary Trees
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        # Approach:
        # We use recursion to merge the
        # two binary trees node by node.
        #
        # For each pair of nodes:
        # • If one node is None, return
        #   the other node because there
        #   is nothing to merge.
        #
        # • If both nodes exist, add
        #   their values together and
        #   store the result in root1.
        #
        # Then recursively merge:
        # • The left children.
        # • The right children.
        #
        # The merged subtrees are attached
        # back to root1.
        #
        # The process continues until all
        # corresponding nodes have been
        # merged.
        #
        # The final merged tree rooted at
        # root1 is returned as the answer.
        #
        # Time Complexity: O(n)
        # where n is the number of nodes
        # visited across both trees.
        #
        # Space Complexity: O(h)
        # where h is the height of the
        # recursion stack.

        if not root1:
            return root2

        if not root2:
            return root1

        root1.val += root2.val

        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1