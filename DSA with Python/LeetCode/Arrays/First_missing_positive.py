# PROBLEM NUMBER: 41
# https://leetcode.com/problems/first-missing-positive/
# 41. First Missing Positive
# DIFFICULTY: HARD
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # Step 1: The missing positive must lie in the range [1, n+1].
        #         Ignore values ≤0 or >n since they cannot be the answer.
        #
        # Step 2: Use index-based placement:
        #         For any value x in range [1, n], place it at index x-1.
        #         Example: value 3 → position index 2.
        #
        # Step 3: Iterate the array and keep swapping a number into its
        #         correct position while:
        #             • it is in the range [1, n], AND
        #             • nums[i] is not already at its correct place.
        #
        # Step 4: After all numbers are placed correctly, scan the array.
        #         The first index i where nums[i] != i+1 gives the answer.
        #
        # Step 5: If all positions are filled correctly, missing number
        #         is n+1 (e.g., nums = [1,2,3] → answer = 4).

        n = len(nums)
        
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
