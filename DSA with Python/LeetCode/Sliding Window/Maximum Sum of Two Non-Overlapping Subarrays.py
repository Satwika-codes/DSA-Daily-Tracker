# PROBLEM NUMBER:1031
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
# 1031.Maximum Sum of Two Non-Overlapping Subarrays
# DIFFICULTY:
class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """

        # Approach:
        # We need to find two non-overlapping subarrays of lengths
        # firstLen and secondLen such that their total sum is maximized.
        #
        # Key Idea:
        # Try both orders:
        #   • firstLen before secondLen
        #   • secondLen before firstLen
        #
        # Step 1: Use prefix sum array to quickly compute subarray sums.
        #
        # Step 2: Define helper(L, M):
        #         • L comes before M
        #
        # Step 3: For helper:
        #         • Maintain maxL = best sum of L-length subarray seen so far
        #           before current M subarray
        #
        # Step 4: Iterate index i representing end of M subarray:
        #         • Update maxL using subarray ending before M starts
        #         • Compute current M subarray sum
        #         • Update result = max(maxL + current M)
        #
        # Step 5: Return result of helper
        #
        # Step 6: Final answer is max of:
        #         • helper(firstLen, secondLen)
        #         • helper(secondLen, firstLen)

        def helper(L, M):
            n = len(nums)
            prefix = [0] * (n + 1)

            # Build prefix sum
            for i in range(n):
                prefix[i + 1] = prefix[i] + nums[i]

            maxL = 0
            res = 0

            for i in range(L + M, n + 1):
                # best L subarray before M
                maxL = max(maxL, prefix[i - M] - prefix[i - M - L])

                # current M subarray
                currM = prefix[i] - prefix[i - M]

                res = max(res, maxL + currM)

            return res

        return max(helper(firstLen, secondLen),
                   helper(secondLen, firstLen))