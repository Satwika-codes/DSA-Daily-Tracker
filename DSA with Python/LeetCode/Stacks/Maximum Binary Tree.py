# PROBLEM NUMBER:654
# https://leetcode.com/problems/maximum-binary-tree/
# 654. Maximum Binary Tree
# DIFFICULTY:MEDIUM

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        # Approach:
        # We need to construct a Maximum Binary Tree where:
        # • Root = maximum element in array
        # • Left subtree = built from elements left of max
        # • Right subtree = built from elements right of max
        #
        # Step 1: Base case:
        #         • If array is empty → return None
        #
        # Step 2: Find index of maximum element
        #
        # Step 3: Create root node using that value
        #
        # Step 4: Recursively build:
        #         • Left subtree from nums[:max_idx]
        #         • Right subtree from nums[max_idx+1:]
        #
        # Step 5: Return root

        if not nums:
            return None

        max_idx = nums.index(max(nums))

        root = TreeNode(nums[max_idx])
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])

        return root