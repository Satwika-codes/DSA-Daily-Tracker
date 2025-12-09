# PROBLEM NUMBER: 724
# https://leetcode.com/problems/find-pivot-index/
# 724. Find Pivot Index
# DIFFICULTY: EASY
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # Step 1: Compute the total sum of the array.
        # Step 2: Maintain a running "left sum" while iterating through the array.
        #
        # Step 3: At each index i:
        #         • left_sum is the sum of elements to the left.
        #         • right_sum = total_sum - left_sum - nums[i].
        #         • If left_sum == right_sum → this index is the pivot → return i.
        #
        # Step 4: If no index satisfies the condition, return -1.

        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            if left == total - left - nums[i]:
                return i
            left += nums[i]

        return -1
