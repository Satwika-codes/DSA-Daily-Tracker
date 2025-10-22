# PROBLEM NUMBER: 389
# https://leetcode.com/problems/find-the-difference/
# 389. Find the Difference
# DIFFICULTY: EASY
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # APPROACH:  
        # This solution finds the extra character in string `t` that is not present in string `s` using the **bitwise XOR** approach.  
        # 1. Initialize `res = 0`.  
        # 2. Iterate through all characters in the concatenated string `s + t`.  
        #    - For each character `ch`, compute `res ^= ord(ch)` — the XOR of their ASCII values.  
        # 3. Since XOR cancels out identical values (`x ^ x = 0`),  
        #    all matching characters from `s` and `t` will cancel each other out,  
        #    leaving only the ASCII value of the extra character in `t`.  
        # 4. Convert the final XOR result (`res`) back to a character using `chr(res)` and return it.  
        # This approach is elegant and avoids using extra space for frequency counting.  
        # Time Complexity: O(n) — iterates once over all characters in `s` and `t`.  
        # Space Complexity: O(1) — uses constant extra space.  
        res = 0
        for ch in s + t:
            res ^= ord(ch)
        return chr(res)
        