# PROBLEM NUMBER: 344
# https://leetcode.com/problems/reverse-string/
# 344 Reverse String
# DIFFICULTY: EASY
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # APPROACH:  
        # This solution reverses a list of characters **in-place** using the two-pointer technique.  
        # 1. Initialize two pointers:
        #    - `left` starting at the beginning of the list.
        #    - `right` starting at the end of the list.
        # 2. While `left < right`:
        #    - Swap the elements at `left` and `right`.
        #    - Move `left` one step forward and `right` one step backward.
        # 3. The process continues until the pointers meet or cross, meaning the list is fully reversed.  
        # This approach does not use extra space, satisfying the in-place constraint.  
        # Time Complexity: O(n) — each element is swapped once.  
        # Space Complexity: O(1) — no additional memory is used apart from a few variables.
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        