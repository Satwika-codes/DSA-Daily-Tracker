# PROBLEM NUMBER: 1008
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# 1008. Construct Binary Search Tree from Preorder Traversal
# DIFFICULTY: MEDIUM

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """

        # Approach:
        # The first value in preorder is
        # always the root of the BST.
        #
        # We use a stack to keep track of
        # nodes whose right child has not
        # been assigned yet.
        #
        # If the current value is smaller
        # than the stack top, it becomes
        # the left child of the stack top.
        #
        # Otherwise, keep popping until
        # finding the correct parent whose
        # value is smaller than the current
        # value. The current node becomes
        # its right child.
        #
        # Push every newly created node
        # onto the stack and continue
        # building the BST.

        if not preorder:
            return None

        root = TreeNode(preorder[0])

        stack = [root]

        for val in preorder[1:]:

            node = TreeNode(val)

            if val < stack[-1].val:

                stack[-1].left = node

            else:

                while stack and stack[-1].val < val:
                    parent = stack.pop()

                parent.right = node

            stack.append(node)

        return root