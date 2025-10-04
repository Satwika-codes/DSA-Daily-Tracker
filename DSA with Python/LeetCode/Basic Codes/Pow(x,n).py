#PROBLEM NUMBER: 50
#https://leetcode.com/problems/powx-n/
#DIFFICULTY:MEDIUM
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        # APPROACH:
        # This solution implements the power function `x^n` handling various edge cases:
        # 1. If the base `x` is 0:
            #- For positive exponent `n`, the result is 0.
            #    - For negative exponent `n`, the result is infinity (division by zero case).
        # 2. If either `x` or `n` is 0, return 1 (since any number to the power 0 is 1).
        # 3. If `n` is negative, invert `x` (x = 1/x) and make `n` positive to compute the result.
        # 4. For positive or negative `x` with positive `n`, the result is calculated using Python's built-in exponentiation operator `**`.
        # This approach directly uses Python's power operator for simplicity while carefully managing edge cases like zero base and negative exponents.
        """
        res=0.0
        if x==0 and n>0:
            return 0
        if x==0 and n<0:
            return "inf"
        if x==0 or n==0:
            return 1
        if  n<0:
            n=-n
            x=1/x
            res=x**n
            return res
        if x>0 and n>0:
            res= x**n
            return res
        if  x<0:
            res= x**n
            return res
            

