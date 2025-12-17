# PROBLEM NUMBER: 442
# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# 442. Find All Duplicates in an Array
# DIFFICULTY: MEDIUM
class Solution(object):
    def findDuplicates(self, nums):
        # We use the index mapping property since values are from 1 to n
        # Each number points to index number - 1 in the array
        # We mark a number as visited by making the value at its mapped index negative
        # If we encounter a number whose mapped index is already negative, it means it appeared before
        # We collect such numbers as duplicates
        # This modifies the array in-place and uses constant extra space

        result = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                result.append(abs(nums[i]))
            else:
                nums[index] = -nums[index]

        return result
