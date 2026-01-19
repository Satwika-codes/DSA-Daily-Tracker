# PROBLEM NUMBER:-2190
# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/
# 2190.Most Frequent Number Following Key in an Array
# DIFFICULTY:-EASY
class Solution(object):
    def mostFrequent(self, nums, key):
      """
      :type nums: List[int]
      :type key: int
      :rtype: int
      """
      #   APPROACH:
      #   The task is to find the number that most frequently appears
      #   immediately after the given `key` in the array.

      #   STEPS:
      #   1) Traverse the array from index 0 to len(nums) - 2.
      #      (We stop early to safely access nums[i + 1].)

      #   2) Whenever nums[i] == key:
      #      - Increment the frequency count of nums[i + 1].

      #   3) After processing the array:
      #      - Return the number with the maximum frequency value.

      #   DATA STRUCTURE:
      #   ---------------
      #   - A hashmap (defaultdict) is used to store frequencies of
      #     numbers that follow `key`.

      #   Time Complexity: O(n)
      #   Space Complexity: O(n)
   

      from collections import defaultdict
        
      freq = defaultdict(int)
        
      for i in range(len(nums) - 1):
          if nums[i] == key:
             freq[nums[i + 1]] += 1
        
      return max(freq, key=freq.get)
