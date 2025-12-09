# PROBLEM NUMBER: 300
# https://leetcode.com/problems/longest-increasing-subsequence/
# 300. Longest Increasing Subsequence
# DIFFICULTY: MEDIUM
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # Step 1: Use a list called 'tails' where tails[i] stores the smallest possible
        #         ending value of an increasing subsequence of length (i+1).
        #
        # Step 2: For each number x in nums:
        #         • Use binary search (bisect_left) to find the place to insert x in 'tails'.
        #         • If x is greater than all elements in 'tails', append it (LIS grows).
        #         • Otherwise replace the first element in 'tails' >= x with x
        #           (this keeps subsequences optimally small for future extensions).
        #
        # Step 3: The length of 'tails' at the end equals the length of the
        #         Longest Increasing Subsequence (LIS).
        #
        # Time Complexity: O(n log n)

        import bisect
        tails = []

        for x in nums:
            i = bisect.bisect_left(tails, x)
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x

        return len(tails)

