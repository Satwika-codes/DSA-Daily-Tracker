# PROBLEM NUMBER: 345
# https://leetcode.com/problems/reverse-vowels-of-a-string/
# 345.Reverse Vowels of a string
# Difficulty: Easy
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # APPROACH:  
        # This solution reverses only the vowels in a string using the **two-pointer technique**.  
        # 1. Convert the input string `s` into a list of characters for easy swapping (since strings are immutable).  
        # 2. Define a set of vowels (`aeiouAEIOU`) to check membership efficiently.  
        # 3. Initialize two pointers:  
        #    - `left` starting from the beginning of the list.  
        #    - `right` starting from the end of the list.  
        # 4. While `left < right`:  
        #    - Move `left` forward until a vowel is found.  
        #    - Move `right` backward until a vowel is found.  
        #    - When both pointers point to vowels, swap them and move both pointers inward.  
        # 5. After traversal, join the list back into a string and return it.  
        # This approach ensures that only vowels are reversed while consonants remain in their original positions.  
        # Time Complexity: O(n) — each character is visited at most once.  
        # Space Complexity: O(n) — for converting the string into a list.  
        vowels = set("aeiouAEIOU")
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)