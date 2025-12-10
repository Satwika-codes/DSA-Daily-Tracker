# PROBLEM NUMBER: 90
# https://leetcode.com/problems/subsets-ii/
# 90. Subsets II
# DIFFICULTY: MEDIUM
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Approach:
        # Step 1: Sort the array so duplicates come together.
        #         This helps us skip repeated subsets later.
        #
        # Step 2: Use backtracking to explore two choices for each element:
        #         → Include nums[i]
        #         → Exclude nums[i]
        #
        # Step 3: When excluding, skip all consecutive duplicates:
        #         while nums[i] == nums[i+1], move i forward.
        #
        # Step 4: When i reaches end of list → append current subset.
        #
        # Result: All unique subsets without duplicates.

        nums.sort()
        res = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                res.append(subset[:])
                return

            # Include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # Exclude nums[i]
            subset.pop()

            # Skip all duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtrack(i + 1)

        backtrack(0)
        return res
