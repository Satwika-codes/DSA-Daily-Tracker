#PROBLEM NUMBER: 66
#https://leetcode.com/problems/plus-one/
#Difficulty: Easy
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        # APPROACH:
        # This solution adds one to a number represented as a list of digits.
        # 1. Start iterating from the least significant digit (the end of the list) toward the most significant digit.
        # 2. For each digit:
        #    - If the digit is less than 9, increment it by 1 and return the updated list immediately.
        #    - If the digit is 9, set it to 0 and continue to the next more significant digit (carry over).
        # 3. If all digits were 9, a carry remains after the loop. Return a new list starting with 1 followed by `n` zeros.
        # This approach efficiently handles carries without converting the list to an integer. It works in O(n) time, where n is the number of digits.
        """
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  
            digits[i] = 0  
        return [1] + [0]*n