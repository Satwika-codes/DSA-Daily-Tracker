# PROBLEM NUMBER :202
# https://leetcode.com/problems/happy-number/
# 202.Happy Number
# DIFFICULTY:202 
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """       
        # APPROACH
        # repeatedly replace the number with the sum of squares of its digits
        # use a set to track numbers already seen to detect a cycle
        # if the number becomes 1, it is a happy number
        # if a number repeats before reaching 1, a cycle exists and it is not happy
        seen = set()                     
        while n != 1:                    
            if n in seen:                
                return False
            seen.add(n)                  
            total = 0                   
            while n > 0:                 
                digit = n % 10           
                total += digit * digit   
                n //= 10                 

            n = total                    

        return True                      






