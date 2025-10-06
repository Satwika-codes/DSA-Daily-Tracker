#PROBLEM NUMBER : 3701
#https://leetcode.com/problems/compute-alternating-sum/
#DIFFICULTY: Easy
class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # APPROACH:
        # This solution calculates the alternating sum of elements in a list `nums`.
        # 1. Initialize a variable `sum` to 0.
        # 2. If the list is empty, return 0 immediately.
        # 3. Iterate over the indices of the list:
        #    - Add the element to `sum` if the index is even.
#    - Subtract the element from `sum` if the index is odd.
        # 4. Return `sum` as the final alternating sum.
        # This approach ensures that elements at even positions are added and elements at odd positions are subtracted, providing a straightforward implementation of alternating sum.
        """
        sum=0
        if(len(nums)==0):
            return 0
        for i in range(len(nums)):
            if (i%2==0):
                sum+=nums[i]
            if(i%2!=0):
                sum-=nums[i]
        return sum
                
                