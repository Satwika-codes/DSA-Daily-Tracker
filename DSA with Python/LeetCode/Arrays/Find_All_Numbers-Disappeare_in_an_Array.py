# PROBLEM NUMBER: 448
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# 448. Find All Numbers Disappeared in an Array
# DIFFICULTY: EASY
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Approach:
        # ----------------------------------------------------------
        # Goal: Find which numbers from 1..n are missing in the array.
        #
        # Idea (Cyclic Sort / Index Placement):
        # -------------------------------------
        # Each number x should ideally be placed at index (x - 1).
        #
        # Steps:
        # 1. Iterate through the list.
        # 2. While nums[i] is NOT at its correct position:
        #        - Swap nums[i] with the element at index nums[i] - 1.
        #    This places every number in its correct spot.
        #
        # 3. After the placement:
        #       - If at index i the value nums[i] != i+1,
        #         then (i+1) is missing → add to result.
        #
        # This works in O(n) time and O(1) extra space.

        n = len(nums)

        # Step 1 & 2: Put each number in its correct index (cyclic sort)
        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Step 3: Collect missing numbers
        res = []
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)

        return res
