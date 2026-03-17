# PROBLEM NUMBER: 1508
# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
# 1508. Range Sum of Sorted Subarray Sums
# DIFFICULTY: MEDIUM
class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        # Approach:
        # We need to compute the sums of all possible subarrays of the array nums,
        # sort these sums, and then return the sum of elements from index (left-1)
        # to (right-1) in the sorted list.
        
        # Step 1: Initialize a list "sub_sums" to store the sum of every possible subarray.
        
        # Step 2: Use two nested loops to generate all subarrays:
        #         • Outer loop picks the starting index i.
        #         • Inner loop extends the subarray from i to j.
        
        # Step 3: Maintain a running sum "curr" while extending the subarray,
        #         so we avoid recomputing sums repeatedly.
        
        # Step 4: For each extension, append the current subarray sum to "sub_sums".
        
        # Step 5: After generating all subarray sums, sort the list.
        
        # Step 6: Extract the portion from index (left-1) to (right-1)
        #         because the problem uses 1-based indexing.
        
        # Step 7: Compute the sum of this slice and take modulo (10^9 + 7)
        #         to avoid overflow.
        
        # Step 8: Return the result.
        MOD = 10**9 + 7
        sub_sums = []

        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                sub_sums.append(curr)

        sub_sums.sort()

        return sum(sub_sums[left-1:right]) % MOD