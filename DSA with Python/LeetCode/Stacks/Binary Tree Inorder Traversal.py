# PROBLEM NUMBER:94
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# 94. Binary Tree Inorder Traversal
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # Approach:
        # In inorder traversal we visit nodes in order:
        # Left → Root → Right
        #
        # Step 1: Create result list to store traversal
        #
        # Step 2: Use recursive helper function
        #
        # Step 3: Base case:
        #         • If node is None → return
        #
        # Step 4: Recursively visit:
        #         • Left subtree
        #
        # Step 5: Process current node:
        #         • Add node value to result
        #
        # Step 6: Recursively visit:
        #         • Right subtree
        #
        # Step 7: Start recursion from root
        #
        # Step 8: Return result list

        res = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res