# PROBLEM NUMBER: 2460
# https://leetcode.com/problems/apply-operations-to-an-array/
# 2460.Apply Operations to an Array
# DIFFICULTY: EASY
class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)

        # Step 1: Apply operation
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # Step 2: Move non-zero elements forward
        pos = 0
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1

        # Step 3: Fill remaining with 0
        while pos < n:
            nums[pos] = 0
            pos += 1

        return nums