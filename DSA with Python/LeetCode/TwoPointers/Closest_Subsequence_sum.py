# PROBLEM NUMBER: 1775
# https://leetcode.com/problems/closest-subsequence-sum/
# 1775. Closest Subsequence Sum
# DIFFICULTY: HARD
class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        # Approach:
        # - Brute force all subsequences is O(2^n) → TLE for n ~ 40.
        # - Use "meet-in-the-middle":
        #     1. Split nums into two halves: left and right.
        #     2. Compute all possible subset sums for both halves.
        #     3. Sort one half (right sums) to use binary search.
        #     4. For each sum in left_sums, find the closest sum in right_sums
        #        such that abs(left_sum + right_sum - goal) is minimized.
        # - Return the smallest absolute difference found.

        # Time Complexity: O(2^(n/2) * log(2^(n/2))) ~ O(2^(n/2) * n)
        # Space Complexity: O(2^(n/2)) for storing sums
        

        from bisect import bisect_left

        n = len(nums)
        mid = n // 2
        left_nums = nums[:mid]
        right_nums = nums[mid:]
        def subset_sums(arr):
            sums = [0]
            for num in arr:
                sums += [num + s for s in sums]
            return sums

        left_sums = subset_sums(left_nums)
        right_sums = subset_sums(right_nums)
        right_sums.sort()

        ans = abs(goal)  

        for s in left_sums:
            target = goal - s
            idx = bisect_left(right_sums, target)
            if idx < len(right_sums):
                ans = min(ans, abs(s + right_sums[idx] - goal))
            if idx > 0:
                ans = min(ans, abs(s + right_sums[idx - 1] - goal))

        return ans
