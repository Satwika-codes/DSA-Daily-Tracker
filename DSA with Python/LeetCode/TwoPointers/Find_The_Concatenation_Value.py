# PROBLEM NUMBER: 2562
# https://leetcode.com/problems/find-the-array-concatenation-value/
# 2562. Find the Array Concatenation Value
# DIFFICULTY: EASY
class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """   
        # Approach:
        # Use two pointers, one at the start and one at the end of the array.
        # While left <= right, concatenate nums[left] and nums[right] as strings
        # if they are different indices, otherwise add the single middle value.
        # Convert concatenated strings to integers and accumulate the sum.
        l, r = 0, len(nums) - 1
        ans = 0
        
        while l <= r:
            if l == r:
                ans += nums[l]
            else:
                ans += int(str(nums[l]) + str(nums[r]))
            l += 1
            r -= 1
        
        return ans
