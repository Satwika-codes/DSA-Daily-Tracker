# PROBLEM NUMBER: 169
# https://leetcode.com/problems/majority-element/
# 169. Majority Element
# Difficulty: Easy
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach (Boyer-Moore Voting Algorithm):
        # The goal is to find the element that appears more than ⌊n/2⌋ times.
        #We maintain two variables:
        #     - candidate → potential majority element
        #     - count → balance counter
        # Traverse through the list:
        #     - If count == 0, assign current element as the new candidate.
        #     - If the current element equals the candidate, increment count.
        #     - Else, decrement count.
        # By the end, the candidate will be the majority element.
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
        