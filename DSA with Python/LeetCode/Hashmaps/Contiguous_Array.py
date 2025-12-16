# PROBLEM NUMBER: 525
# https://leetcode.com/problems/contiguous-array/
# 525. Contiguous Array
# DIFFICULTY: MEDIUM
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach:
        # - We need the longest contiguous subarray with equal number of 0s and 1s.
        # - Replace 0 with -1 and keep 1 as +1.
        # - Now the problem becomes finding the longest subarray with sum = 0
        # - Use a prefix sum (curr_sum) while traversing the array.
        # - Maintain a hashmap to store the first index where each prefix sum appears.
        # - Initialize hashmap with {0: -1} to handle subarrays starting from index 0.
        # - If the same prefix sum is seen again at index i,
        #   the subarray between previous index + 1 and i has sum = 0.
        # - Update the maximum length using i - first_occurrence[prefix_sum].
        # - If the prefix sum is not present in the map, store its index.
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        prefix_index = {0: -1}
        
        max_len = 0
        curr_sum = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                curr_sum -= 1
            else:
                curr_sum += 1

            if curr_sum in prefix_index:
                max_len = max(max_len, i - prefix_index[curr_sum])
            else:
                prefix_index[curr_sum] = i

        return max_len
