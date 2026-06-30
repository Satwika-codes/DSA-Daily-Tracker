# PROBLEM NUMBER: 865
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
# 865. Smallest Subtree with all the Deepest Nodes
# DIFFICULTY: MEDIUM

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        # Approach:
        # We use a postorder DFS
        # traversal.
        #
        # For every subtree, the DFS
        # returns:
        # • The maximum depth of the
        #   subtree.
        # • The node that is the root
        #   of the smallest subtree
        #   containing all deepest nodes.
        #
        # For each node:
        # • Recursively compute the
        #   depth and candidate node
        #   from the left subtree.
        #
        # • Recursively compute the
        #   depth and candidate node
        #   from the right subtree.
        #
        # If one subtree is deeper,
        # propagate its candidate node
        # upward.
        #
        # If both subtrees have the
        # same depth, then the current
        # node is the lowest common
        # ancestor of all deepest nodes,
        # so return the current node.
        #
        # After processing the root,
        # the returned node is the
        # required answer.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        def dfs(node):
            if not node:
                return (0, None)

            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)

            if left_depth > right_depth:
                return (left_depth + 1, left_node)

            if right_depth > left_depth:
                return (right_depth + 1, right_node)

            return (left_depth + 1, node)

        return dfs(root)[1]