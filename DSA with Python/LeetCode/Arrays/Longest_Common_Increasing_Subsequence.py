# PROBLEM NUMBER: 674
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# 674. Longest Continuous Increasing Subsequence
# DIFFICULTY: EASY
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach:
        # Step 1: If the array is empty, return 0.
        # Step 2: Initialize max_len and curr_len to 1. 
        #         max_len keeps track of the maximum length of continuous increasing subsequence.
        #         curr_len keeps track of the current length while traversing.
        # Step 3: Traverse the array from the second element:
        #         - If current element > previous element, increment curr_len and update max_len if needed.
        #         - Else, reset curr_len to 1.
        # Step 4: Return max_len after traversing the array.

        if not nums:
            return 0

        max_len = 1
        curr_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 1

        return max_len
