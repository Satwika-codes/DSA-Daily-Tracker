# PROBLEM NUMBER:696
# https://leetcode.com/problems/count-binary-substrings/
# 696.Count Binary Substrings
# DIFFICULTY: EASY
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach:
        # 1. The goal is to count substrings with equal consecutive 0’s and 1’s 
        #    where all 0’s and 1’s in the substring are grouped together.
        # 2. First, traverse the string to record lengths of consecutive
        #    identical characters (like groups of 0s and 1s) in a list `groups`.
        #       Example: s = "001110" → groups = [2, 3, 1]
        # 3. For each adjacent pair of groups, the number of valid binary substrings
        #    formed between them is the minimum of their lengths.
        #       Example: min(2,3)=2, min(3,1)=1 → total = 3
        # 4. Sum up all these minimum values to get the final result.
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        groups = []
        count = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)
        
        res = 0
        for i in range(1, len(groups)):
            res += min(groups[i - 1], groups[i])
        return res