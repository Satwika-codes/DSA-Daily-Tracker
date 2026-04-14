# PROBLEM NUMBER:114
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# 114. Flatten Binary Tree to Linked List
# DIFFICULTY: MEDIUM

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # Approach:
        # We need to flatten the binary tree into a linked list (in-place)
        # following preorder traversal:
        # root → left → right
        #
        # Step 1: Use recursion (postorder style):
        #         • First flatten left subtree
        #         • Then flatten right subtree
        #
        # Step 2: Store original right subtree in temp
        #
        # Step 3: Move left subtree to right:
        #         • root.right = root.left
        #         • root.left = None
        #
        # Step 4: Traverse to the end of new right subtree
        #
        # Step 5: Attach original right subtree at the end
        #
        # Step 6: This rearranges tree into a linked list
        #         following preorder sequence

        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        temp = root.right
        root.right = root.left
        root.left = None

        curr = root
        while curr.right:
            curr = curr.right

        curr.right = temp