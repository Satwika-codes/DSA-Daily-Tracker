# PROBLEM NUMBER: 3028
#https://leetcode.com/problems/ant-on-the-boundary
# DIFFICULTY:Easy 
class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Approach:
        - Keep two accumulators: `left_move` and `right_move`.
        - Iterate through nums:
            - If the move is negative, add to left_move.
            - If the move is positive, add to right_move.
            - Whenever abs(left_move) == abs(right_move), it means the ant is back at boundary (position 0),
              so increment the count.
        - Return the final count.

        Time Complexity: O(n)  (looping once over nums)
        Space Complexity: O(1) (using only a few variables)
        """
        left_move=0
        right_move=0
        count=0
        N=len(nums)
        for i in range (N):
            if(nums[i]<0):
                left_move+=nums[i]
            elif(nums[i]>0):
                right_move+=nums[i]
            if(abs(left_move)==abs(right_move)):
                count+=1
        return count