# PROBLEM NUMBER: 501
# https://leetcode.com/problems/find-mode-in-binary-search-tree/
# 501. Find Mode in Binary Search Tree
# DIFFICULTY: EASY

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        # Approach:
        # We perform a DFS traversal
        # of the entire tree and count
        # the frequency of each value.
        #
        # For every visited node:
        # • Increment the frequency
        #   count of its value in a
        #   hash map.
        #
        # After the traversal:
        # • Find the maximum frequency
        #   among all values.
        #
        # • Collect every value whose
        #   frequency equals the maximum
        #   frequency.
        #
        # These values represent the
        # mode(s) of the tree.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        freq = {}

        def dfs(node):
            if not node:
                return

            freq[node.val] = freq.get(node.val, 0) + 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        mx = max(freq.values())

        return [x for x in freq if freq[x] == mx]