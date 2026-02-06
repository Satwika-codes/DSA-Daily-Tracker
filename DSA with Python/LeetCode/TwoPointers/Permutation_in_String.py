# PROBLEM NUMBER:567
# https://leetcode.com/problems/permutation-in-string/
# 567. Permutation in String
# DIFFICULTY: MEDIUM
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Approach:
        # ---------
        # This problem is solved using the Sliding Window technique
        # combined with character frequency counting.

        # 1. If the length of s1 is greater than s2, it is impossible
        #    for s2 to contain a permutation of s1 → return False.
        # 2. Maintain two frequency arrays of size 26:
        #    - cnt1 for characters in s1
        #    - cnt2 for the current window in s2
        # 3. Initialize cnt1 using characters of s1.
        # 4. Slide a window of size len(s1) over s2:
        #    - Add the current character to cnt2.
        #    - Remove the character that goes out of the window.
        # 5. After each update, compare cnt1 and cnt2:
        #    - If they are equal, the current window is a permutation of s1.
        # 6. If no matching window is found, return False.

        # This works efficiently because character frequency comparison
        # takes constant time (26 letters only).
        

        if len(s1) > len(s2):
            return False
        
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        
        for c in s1:
            cnt1[ord(c) - ord('a')] += 1
        
        window = len(s1)
        
        for i in range(len(s2)):
            cnt2[ord(s2[i]) - ord('a')] += 1
            
            if i >= window:
                cnt2[ord(s2[i - window]) - ord('a')] -= 1
            
            if cnt1 == cnt2:
                return True
        
        return False
