# PROBLEM NUMBER :995
# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
# Minimum Number of K Consecutive Bit Flips
# DIFFICULTY:HARD
class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        isFlipped = [0] * n
        flip = 0
        res = 0

        for i in range(n):

            # remove effect of window
            if i >= k:
                flip ^= isFlipped[i - k]

            # if current bit is 0 after flips
            if nums[i] ^ flip == 0:
                if i + k > n:
                    return -1

                isFlipped[i] = 1
                flip ^= 1
                res += 1

        return res