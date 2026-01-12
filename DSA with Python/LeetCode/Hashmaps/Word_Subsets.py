# PROBLEM NUMBER: 916
# https://leetcode.com/problems/word-subsets/
# 916.Word Subsets
# DIFFICULTY: MEDIUM
class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        # APPROACH:
        # 1. For all words in words2, compute the maximum frequency required for
        #    each character across all words. This represents the minimum
        #    character requirement a word from words1 must satisfy.
        # 2. For each word in words1, count the frequency of its characters.
        # 3. A word from words1 is considered universal if for every character,
        #    its frequency is greater than or equal to the required maximum
        #    frequency computed from words2.
        # 4. Collect and return all such universal words.

        # Time Complexity:
        # - O(total characters in words2 + total characters in words1)

        # Space Complexity:
        # - O(1), since the alphabet size is fixed (26 lowercase letters)
        
        from collections import Counter

        max_freq = Counter()
        for w in words2:
            freq = Counter(w)
            for c in freq:
                max_freq[c] = max(max_freq[c], freq[c])
                
        res = []
        for w in words1:
            freq = Counter(w)
            ok = True
            for c in max_freq:
                if freq[c] < max_freq[c]:
                    ok = False
                    break
            if ok:
                res.append(w)

        return res
