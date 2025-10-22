# PROBLEM NUMBER: 257
# https://leetcode.com/problems/binary-tree-paths/
# 257.Binary Tree Paths
# Difficulty: Easy
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        # Approach:
        # 1. We need to find all root-to-leaf paths in a binary tree.
        # 2. Use Depth-First Search (DFS) traversal to explore every possible path.
        # 3. Maintain a `path` string that keeps track of the nodes visited so far.
        # 4. Base Case:
        #       - If a node has no left or right child (leaf node), append the completed path to the result list.
        # 5. Recursive Case:
        #       - If the node has a left child → call DFS on left subtree.
        #       - If the node has a right child → call DFS on right subtree.
        # 6. Finally, return the list `res` containing all root-to-leaf paths as strings.
        if not root:
            return []
        res = []

        def dfs(node, path):
            if not node.left and not node.right:
                res.append(path + str(node.val))
                return
            if node.left:
                dfs(node.left, path + str(node.val) + "->")
            if node.right:
                dfs(node.right, path + str(node.val) + "->")

        dfs(root, "")
        return res
        