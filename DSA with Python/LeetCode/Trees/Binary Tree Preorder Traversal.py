# PROBLEM NUMBER: 144
# https://leetcode.com/problems/binary-tree-preorder-traversal/
# 144. Binary Tree Preorder Traversal
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        # Approach:
        # We perform an iterative
        # preorder traversal using
        # a stack.
        #
        # Preorder traversal visits
        # nodes in the order:
        # Root -> Left -> Right.
        #
        # Initially, push the root
        # node onto the stack.
        #
        # While the stack is not empty:
        # • Pop the top node.
        # • Add its value to the answer.
        # • Push its right child first.
        # • Push its left child next.
        #
        # Since the stack follows the
        # Last-In-First-Out (LIFO)
        # principle, the left child is
        # processed before the right
        # child, producing preorder
        # traversal.
        #
        # Continue until every node has
        # been visited.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        if not root:
            return []

        stack = [root]
        ans = []

        while stack:
            node = stack.pop()
            ans.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return ans