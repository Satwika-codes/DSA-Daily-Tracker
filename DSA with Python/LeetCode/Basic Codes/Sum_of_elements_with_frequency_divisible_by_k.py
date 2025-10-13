# PROBLEM NUMBER:3712
# https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/
# 3712:Sum of elements with frequency divisible by k
# DIFFICULTY:EASY
class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # APPROACH:
        # This solution calculates the sum of all elements in the list `nums` whose frequencies are divisible by `k`.
        # 1. Use `collections.Counter` to compute the frequency of each unique element in `nums`.
        # 2. Initialize `total_sum` to 0.
        # 3. Iterate through each `(num, count)` pair in the frequency dictionary:
        #    - If the frequency (`count`) is divisible by `k`, add `num * count` to `total_sum`.
        # 4. Return `total_sum` as the final result.
        # This approach efficiently groups and counts elements, leveraging hash-based counting from `Counter`, 
        # and runs in O(n) time with O(n) extra space.
        from collections import Counter
        freq = Counter(nums)
        total_sum = 0
        for num, count in freq.items():
            if count % k == 0:
                total_sum += num * count

        return total_sum
        