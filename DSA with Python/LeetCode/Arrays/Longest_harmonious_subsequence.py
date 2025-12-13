# PROBLEM NUMBER: 1214
# https://leetcode.com/problems/longest-harmonious-subsequence/
# 1214. Longest Harmonious Subsequence
# DIFFICULTY: EASY
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # APPROACH 
        # Step 1: Count the frequency of each number in the array.
        # Step 2: A harmonious subsequence requires:
        #         - Maximum value - Minimum value = 1
        #         → So we only need to check pairs (x, x+1).
        # Step 3: Iterate through each unique number x.
        #         - If (x + 1) exists, compute the combined frequency:
        #           freq[x] + freq[x + 1].
        # Step 4: Track the maximum combined frequency found.
        # Step 5: Return the maximum length of any harmonious subsequence.

        from collections import Counter
        
        freq = Counter(nums)
        longest = 0
        
        for x in freq:
            if x + 1 in freq:
                longest = max(longest, freq[x] + freq[x + 1])
                
        return longest
