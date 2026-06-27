# PROBLEM NUMBER: 96
# https://leetcode.com/problems/unique-binary-search-trees/
# 96. Unique Binary Search Trees
# DIFFICULTY: MEDIUM

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Approach:
        # We use Dynamic Programming
        # to count the number of unique
        # Binary Search Trees (BSTs).
        #
        # Let dp[i] represent the number
        # of unique BSTs that can be
        # formed using i nodes.
        #
        # Base cases:
        # • dp[0] = 1 (empty tree)
        # • dp[1] = 1 (single-node tree)
        #
        # For every possible number of
        # nodes:
        # • Consider each node as the
        #   root of the BST.
        #
        # • The nodes on the left of
        #   the root form the left
        #   subtree.
        #
        # • The nodes on the right of
        #   the root form the right
        #   subtree.
        #
        # The number of BSTs for a
        # chosen root is:
        # (number of left subtrees) ×
        # (number of right subtrees).
        #
        # Sum these values over every
        # possible root to obtain
        # dp[nodes].
        #
        # The final answer is dp[n].
        #
        # Time Complexity: O(n²)
        # Space Complexity: O(n)

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                dp[nodes] += dp[root - 1] * dp[nodes - root]

        return dp[n]