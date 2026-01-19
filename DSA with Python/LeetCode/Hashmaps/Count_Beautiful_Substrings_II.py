# PROBLEM NUMBER: 2949
# https://leetcode.com/problems/count-beautiful-substrings-ii/
# 2949Count Beautiful Substrings II
# DIFFICULTY: HARD
class Solution(object):
    def beautifulSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # APPROACH:
        # A substring is considered beautiful if:
        # 1) Number of vowels == number of consonants
        #    → We maintain a running balance:
        #      +1 for vowel, -1 for consonant.
        #    → If the same balance appears again, the substring between
        #      those positions has equal vowels and consonants.

        # 2) (length^2) % k == 0
        #    → Let length = L
        #    → L^2 % k == 0
        #    → We find the smallest integer d such that:
        #      d * d % k == 0
        #    → Any valid substring length must be a multiple of 2*d
        #      (because balance condition requires even length).

        # OPTIMIZATION:
        # -------------
        # We use a hashmap:
        # index_map[balance][index % (2*d)]
        # to count how many times a given (balance, modulo) pair has appeared.

        # When we encounter the same (balance, modulo) again,
        # it means:
        # - Equal vowels and consonants
        # - Valid length condition
        # → Count it as a beautiful substring.

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        vowels = set("aeiou")
        
        # Find smallest d such that d*d % k == 0
        d = 1
        while (d * d) % k != 0:
            d += 1
        
        from collections import defaultdict
        
        balance = 0
        index_map = defaultdict(lambda: defaultdict(int))
        index_map[0][0] = 1
        
        res = 0
        
        for i, ch in enumerate(s, 1):
            if ch in vowels:
                balance += 1
            else:
                balance -= 1
            
            mod = i % (2 * d)
            res += index_map[balance][mod]
            index_map[balance][mod] += 1
        
        return res
