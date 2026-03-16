# PROBLEM NUMBER: 1247
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
# 1247.Minimum Number of Swaps to Make the String Balanced
# DIFFICULTY: MEDIUM
class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach:
        # We need to find the minimum number of swaps required to make the bracket
        # string balanced. A balanced string means every '[' has a matching ']'
        # in the correct order.
        
        # Step 1: Initialize two variables:
        #         imbalance → tracks the difference between closing and opening brackets.
        #         max_imbalance → keeps track of the maximum imbalance encountered.
        
        # Step 2: Traverse the string character by character.
        
        # Step 3: If the character is '[':
        #         decrease imbalance by 1 because it helps balance previous ']'.
        
        # Step 4: If the character is ']':
        #         increase imbalance by 1 because we have an extra closing bracket.
        
        # Step 5: After each update, record the maximum imbalance seen so far.
        
        # Step 6: The maximum imbalance represents how many unmatched closing
        #         brackets appeared consecutively.
        
        # Step 7: Each swap can fix two misplaced brackets, so the number of swaps
        #         needed is:
        #             (max_imbalance + 1) // 2
        
        # Step 8: Return the computed swaps.
        imbalance = 0
        max_imbalance = 0

        for c in s:
            if c == '[':
                imbalance -= 1
            else:
                imbalance += 1

            max_imbalance = max(max_imbalance, imbalance)

        return (max_imbalance + 1) // 2