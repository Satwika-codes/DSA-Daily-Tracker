# PROBLEM NUMBER: 437
# https://leetcode.com/problems/path-sum-iii/
# 437. Path Sum III
# DIFFICULTY: MEDIUM

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """

        # Approach:
        # We use DFS along with a
        # prefix sum hashmap to count
        # all valid paths efficiently.
        #
        # The hashmap stores how many
        # times each prefix sum has
        # occurred on the current path
        # from the root.
        #
        # For each node:
        # • Add the current node's value
        #   to the running prefix sum.
        #
        # • If (current_sum - targetSum)
        #   exists in the hashmap, then
        #   those occurrences represent
        #   valid paths ending at the
        #   current node.
        #
        # • Store the current prefix sum
        #   in the hashmap before
        #   exploring the children.
        #
        # • Recursively search the left
        #   and right subtrees.
        #
        # • After returning, remove the
        #   current prefix sum from the
        #   hashmap (backtracking) so it
        #   does not affect other paths.
        #
        # The total count accumulated
        # during DFS is the required
        # answer.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of
        # the binary tree.

        prefix = {0: 1}

        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val

            count = prefix.get(curr_sum - targetSum, 0)

            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            prefix[curr_sum] -= 1

            return count

        return dfs(root, 0)