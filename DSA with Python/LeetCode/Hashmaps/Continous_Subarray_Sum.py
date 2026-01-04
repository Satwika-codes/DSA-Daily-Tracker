# PROBLEM NUMBER: 523
# https://leetcode.com/problems/continuous-subarray-sum/
# 523. Continuous Subarray Sum
# DIFFICULTY: MEDIUM
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Approach:
        # We use the prefix sum and modulo property.
        # If two prefix sums have the same remainder when divided by k,
        # then the subarray between them has a sum divisible by k.

        # We store the earliest index for each remainder.
        # If the same remainder appears again and the subarray length
        # is at least 2, we return True.

        # Special case:
        # When k == 0, we check whether there are at least two consecutive
        # zeros in the array.
        

        prefix_mod = {0: -1}
        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num
            if k != 0:
                curr_sum %= k

            if curr_sum in prefix_mod:
                if i - prefix_mod[curr_sum] > 1:
                    return True
            else:
                prefix_mod[curr_sum] = i

        return False
