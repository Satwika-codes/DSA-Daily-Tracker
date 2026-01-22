# PROBLEM NUMBER: 795
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
# 795. Number of Subarrays with Bounded Maximum
# DIFFICULTY: MEDIUM
class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """   
        # Approach:
        # A subarray is valid if its maximum is between left and right.
        # Instead of checking directly, count:
        # (number of subarrays with max <= right)
        # minus
        # (number of subarrays with max < left).
        # To count subarrays with max <= X, iterate through nums and keep
        # track of the current length of consecutive elements <= X.
        # Each position contributes that length to the total count.
        def count_at_most(x):
            res = 0
            cur = 0
            for num in nums:
                if num <= x:
                    cur += 1
                else:
                    cur = 0
                res += cur
            return res
        
        return count_at_most(right) - count_at_most(left - 1)
