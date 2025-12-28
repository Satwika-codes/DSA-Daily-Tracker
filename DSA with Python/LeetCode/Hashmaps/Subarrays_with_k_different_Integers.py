# PROBLEM NUMBER :992
# https://leetcode.com/problems/subarrays-with-k-different-integers/
# 992.Subarrays with K different Integers
# DIFFICULTY:HARD
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """ 
        :type nums: 
        List[int] :type 
        k: int 
        :rtype: int 
        """
        
        # APPROACH:
        # - The number of subarrays with exactly K distinct elements can be computed as:
        #  atMost(K) - atMost(K - 1).
        # - Use a sliding window technique to count subarrays with at most K distinct elements.
        # - Maintain a frequency hashmap and expand the right pointer.
        # - Shrink the left pointer when the number of distinct elements exceeds K.
        # - Accumulate the number of valid subarrays ending at each position.
        

        from collections import defaultdict

        def atMost(K):
            count = defaultdict(int)
            left = 0
            res = 0

            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    K -= 1
                count[nums[right]] += 1

                while K < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        K += 1
                    left += 1

                res += right - left + 1

            return res

        return atMost(k) - atMost(k - 1)
