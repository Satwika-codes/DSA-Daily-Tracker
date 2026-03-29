# PROBLEM NUMBER:718
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# 718.Maximum Length of Repeated Subarray
# DIFFICULTY:MEDIUM    
class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        # Approach:
        # We need to find the maximum length of a common subarray
        # (continuous elements) between nums1 and nums2.
        #
        # Step 1: Use Dynamic Programming.
        #         Let dp[i][j] represent the length of longest common
        #         subarray ending at nums1[i-1] and nums2[j-1].
        #
        # Step 2: Initialize a DP table of size (n+1) x (m+1) with 0.
        #
        # Step 3: Traverse both arrays:
        #         • If nums1[i-1] == nums2[j-1]:
        #             dp[i][j] = dp[i-1][j-1] + 1
        #         • Else:
        #             dp[i][j] = 0 (because subarray must be continuous)
        #
        # Step 4: Keep track of the maximum value found in dp.
        #
        # Step 5: Return the maximum length.

        n = len(nums1)
        m = len(nums2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        max_len = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = 0

        return max_len