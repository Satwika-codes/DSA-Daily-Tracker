# PROBLEM NUMBER:560
# https://leetcode.com/problems/subarray-sum-equals-k/
# 560. Subarray Sum Equals K
# DIFFICULTY: MEDIUM
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Approach:
        # We use prefix sums with a hashmap.

        # Let prefix_sum be the sum of elements up to the current index.
        # If there exists a previous prefix sum equal to (prefix_sum - k),
        # then the subarray between those indices sums to k.

        # We store how many times each prefix sum has occurred so far.
        # For each new prefix sum, we add the frequency of (prefix_sum - k)
        # to the answer.

        # Initialize the map with {0: 1} to handle subarrays that start
        # from index 0.

        # This gives an O(n) time and O(n) space solution.
        

        from collections import defaultdict

        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num
            count += prefix_count[curr_sum - k]
            prefix_count[curr_sum] += 1

        return count
