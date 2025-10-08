#PROBLEM NUMBER: 69
#https://leetcode.com/problems/sqrtx/
#Difficulty: Easy
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        # APPROACH:
        # This solution calculates the integer square root of a non-negative integer `x` using binary search.
        # 1. Handle small inputs directly: if `x` is 0 or 1, return `x` immediately.
        # 2. Initialize the search range as `left = 1` and `right = x // 2` since the square root of `x` cannot exceed `x/2` for x > 1.
        # 3. Perform binary search:
        #    - Compute `mid = (left + right) // 2`.
        #    - If `mid * mid == x`, return `mid` (perfect square case).
        #    - If `mid * mid < x`, move the search to the right half (`left = mid + 1`).
        #    - If `mid * mid > x`, move the search to the left half (`right = mid - 1`).
        # 4. When the loop ends, `right` will point to the integer part (floor value) of the square root.
        # This approach efficiently finds the result in O(log x) time and avoids floating-point operations.
        """
        if x < 2:
            return x
        
        left, right = 1, x // 2
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right