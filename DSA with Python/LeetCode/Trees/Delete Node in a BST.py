# PROBLEM NUMBER: 450
# https://leetcode.com/problems/delete-node-in-a-bst/
# 450. Delete Node in a BST
# DIFFICULTY: MEDIUM

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """

        # Approach:
        # We recursively search for the
        # node that contains the given key
        # while using the BST property.
        #
        # If the key is smaller than the
        # current node's value, search in
        # the left subtree.
        #
        # If the key is greater than the
        # current node's value, search in
        # the right subtree.
        #
        # Once the node is found, there
        # are three possible cases:
        #
        # • No left child:
        #   Return the right child.
        #
        # • No right child:
        #   Return the left child.
        #
        # • Two children:
        #   Find the inorder successor,
        #   which is the smallest node
        #   in the right subtree.
        #
        #   Replace the current node's
        #   value with the successor's
        #   value.
        #
        #   Recursively delete the
        #   successor node from the
        #   right subtree.
        #
        # Return the updated subtree
        # after deletion.
        #
        # Time Complexity: O(h)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary search tree.

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # Node with only one child or no child
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            # Node with two children
            temp = root.right
            while temp.left:
                temp = temp.left

            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)

        return root