# PROBLEM NUMBER: 643
# https://leetcode.com/problems/maximum-average-subarray-i/
# 643. Maximum Average Subarray I
# DIFFICULTY: EASY
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Step 1: Compute the sum of the first k elements.
        #         This will be our initial window sum.
        
        # Step 2: Initialize max_sum with this initial sum.
        
        # Step 3: Use a sliding window of size k:
        #         • For each new element entering the window (nums[i]),
        #           add it to the current sum.
        #         • Remove the element leaving the window (nums[i - k]).
        
        # Step 4: After updating the window, compare the current sum
        #         with max_sum and update max_sum if needed.
        
        # Step 5: Continue this process until we reach the end of the array.
        
        # Step 6: The maximum average is max_sum / k.
        
        # Step 7: Return the result as a float.

        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Step 2: Slide the window
        for i in range(k, len(nums)):
            window_sum += nums[i]      # add next element
            window_sum -= nums[i - k]  # remove previous element

            max_sum = max(max_sum, window_sum)

        # Step 3: Return maximum average
        return float(max_sum) / k