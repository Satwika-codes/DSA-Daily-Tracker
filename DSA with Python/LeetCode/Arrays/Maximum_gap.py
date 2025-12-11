# PROBLEM NUMBER: 164
# https://leetcode.com/problems/maximum-gap/
# 164. Maximum Gap
# DIFFICULTY: MEDIUM
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # Use the "Bucket Sort / Pigeonhole Principle" to find the maximum gap.
        #
        # Key Insight:
        # - If we sort nums, the maximum gap must occur between consecutive elements.
        # - But sorting is O(n log n). We want O(n).
        #
        # Idea:
        # - If we have n numbers, the minimum possible max gap is:
        #       bucket_size = (max - min) // (n - 1)
        #
        # - We create buckets that store:
        #       [min_value_in_bucket, max_value_in_bucket]
        #
        # - We place each number in the correct bucket.
        # - The maximum gap will be:
        #       difference between current bucket's min 
        #       and previous non-empty bucket's max.
        #
        # Why this works:
        # - Within any bucket, numbers are too close to create the max gap.
        # - The gap must occur between buckets.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        if len(nums) < 2:
            return 0
        
        mn, mx = min(nums), max(nums)
        if mn == mx:
            return 0

        n = len(nums)
        size = max(1, (mx - mn) // (n - 1))  # minimum possible bucket size
        
        # Each bucket holds [min_value, max_value]
        buckets = [
            [float('inf'), float('-inf')] 
            for _ in range((mx - mn) // size + 1)
        ]
        
        # Place nums into buckets
        for num in nums:
            idx = (num - mn) // size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)
        
        # Compute max gap between buckets
        prev = mn
        ans = 0
        for b in buckets:
            if b[0] == float('inf'):  # empty bucket
                continue
            ans = max(ans, b[0] - prev)
            prev = b[1]

        return ans
