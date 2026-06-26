# PROBLEM NUMBER: 145
# https://leetcode.com/problems/binary-tree-postorder-traversal/
# 145. Binary Tree Postorder Traversal
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        # Approach:
        # We perform an iterative
        # postorder traversal using
        # a stack.
        #
        # Instead of directly following
        # Left -> Right -> Root order,
        # we first generate the order:
        # Root -> Right -> Left.
        #
        # Initially, push the root node
        # onto the stack.
        #
        # While the stack is not empty:
        # • Pop the top node.
        # • Add its value to the answer.
        # • Push its left child first.
        # • Push its right child next.
        #
        # This produces nodes in the
        # order Root -> Right -> Left.
        #
        # Finally, reverse the answer
        # list to obtain the required
        # postorder traversal:
        # Left -> Right -> Root.
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

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return ans[::-1]
        