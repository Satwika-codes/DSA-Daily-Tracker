# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# Difficulty: Medium level
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev=0
        last_digit=0
        sign = -1 if x < 0 else 1 
        if x==0:
            return 0
        x=abs(x)
        while(x>0):
            last_digit=x%10
            rev=rev*10+last_digit
            x=x//10 
        rev *= sign
        if (rev < -2**31 or rev > 2**31-1):
            return 0
        else:
            return rev
        