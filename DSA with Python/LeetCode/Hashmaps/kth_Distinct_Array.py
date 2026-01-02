# PROBLEM NUMBER: 2053
# https://leetcode.com/problems/kth-distinct-string-in-an-array/description/
# 2053.Kth Distinct String in an Array
# DIFFICULTY: EASY
class Solution(object):
    def kthDistinct(self, arr, k):
        """ 
        :type arr: List[str] 
        :type k: int 
        :rtype: str 
        """
        # APPROACH:
        # - A distinct string is one that appears exactly once in the array.
        # - First, count the frequency of each string.
        # - Traverse the array in its original order to preserve sequence.
        # - Decrease k each time a distinct string is found.
        # - When k reaches zero, return that string.
        # - If fewer than k distinct strings exist, return an empty string.
        

        from collections import Counter

        freq = Counter(arr)

        for word in arr:
            if freq[word] == 1:
                k -= 1
                if k == 0:
                    return word

        return ""
