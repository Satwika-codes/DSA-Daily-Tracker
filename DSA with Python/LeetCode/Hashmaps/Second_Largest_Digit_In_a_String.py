# PROBLEM NUMBER:1796
# https://leetcode.com/problems/second-largest-digit-in-a-string/
# 1796.Second Largest Digit In a String
# DIFFICULTY: EASY
class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach:
        # Traverse the string and collect all numeric characters.
        # Convert them to integers and store them in a set to keep only unique digits.
        # If the number of unique digits is less than 2, return -1.
        # Otherwise, sort the digits in descending order and return the second element.

        # Time Complexity: O(n)
        # Space Complexity: O(1) (at most 10 digits)


        digits = set()
        for ch in s:
            if ch.isdigit():
                digits.add(int(ch))
        
        if len(digits) < 2:
            return -1
        
        return sorted(digits, reverse=True)[1]
