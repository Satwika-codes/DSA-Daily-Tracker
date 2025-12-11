# PROBLEM NUMBER: 229
# https://leetcode.com/problems/majority-element-ii/
# 229. Majority Element II
# DIFFICULTY: MEDIUM
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # -------------------------
        # APPROACH
        # -------------------------
        # 1. We want all elements appearing more than n/3 times.
        # 2. Count occurrences of each number using a dictionary.
        # 3. Traverse the dictionary and collect all numbers whose count > n//3.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(n) due to dictionary

        n = len(nums)
        count = {}
        result = []

        # Count occurrences of each number
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Collect numbers with count greater than n/3
        for num in count:
            if count[num] > n // 3:
                result.append(num)

        return result
