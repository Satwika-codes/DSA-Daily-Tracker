# PROBLEM NUMBER: 347
# https://leetcode.com/problems/top-k-frequent-elements/
# 347. Top K Frequent Elements
# DIFFICULTY: MEDIUM
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # count frequency of each number using hashmap
        # store number as key and its frequency as value
        # use an array of size len(nums) + 1 where index represents frequency
        # group numbers based on their frequencies
        # iterate from highest frequency to lowest
        # collect elements until k elements are added
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
