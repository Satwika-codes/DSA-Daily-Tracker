# PROBLEM NUMBER:897
# https://leetcode.com/problems/increasing-order-search-tree/
# 897. Flatten Binary Tree to Linked List
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Approach:
        # We need to rearrange the BST into an increasing order tree
        # such that:
        # • Left child is always None
        # • Right child forms the sorted order (like a linked list)
        #
        # Step 1: Use inorder traversal:
        #         • Inorder of BST gives sorted order
        #
        # Step 2: Use a dummy node:
        #         • Helps build new tree easily
        #
        # Step 3: Maintain a pointer (self.curr):
        #         • Points to last node in new tree
        #
        # Step 4: During inorder traversal:
        #         • Visit left subtree
        #
        # Step 5: Process current node:
        #         • Set node.left = None
        #         • Attach node to curr.right
        #         • Move curr forward
        #
        # Step 6: Visit right subtree
        #
        # Step 7: Return dummy.right (new root)

        dummy = TreeNode(0)
        self.curr = dummy

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            # process node
            node.left = None
            self.curr.right = node
            self.curr = node

            inorder(node.right)

        inorder(root)
        return dummy.right