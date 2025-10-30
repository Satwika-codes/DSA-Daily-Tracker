# PROBLEM NUMBER: 179
# https://leetcode.com/problems/largest-number/
# 179. Largest Number
# DIFFICULTY: MEDIUM
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Approach:
        # The goal is to arrange a list of non-negative integers such that 
        # they form the largest possible number when concatenated.
        # Idea:
        # 1. Convert all integers in `nums` to strings for easy concatenation.
        # 2. Use a custom sorting logic:
        #       - For any two numbers `a` and `b`, compare `a+b` and `b+a`.
        #       - If `b+a` is greater, swap them to ensure the larger 
        #         combined value comes first.
        # 3. Join the sorted list into a single string.
        # 4. Handle edge case where the result starts with '0' 
        nums = list(map(str, nums))
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        res = "".join(nums)
        return "0" if res[0] == "0" else res
        