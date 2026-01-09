# PROBLEM NUMBER: 692
# https://leetcode.com/problems/top-k-frequent-words/
# LeetCode 692. Top K Frequent Words
# DIFFICULTY: MEDIUM
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        """
        Approach:
        We count the frequency of each word.
        Then we sort the words by:
        1) descending frequency
        2) lexicographical order for ties.

        Finally, we return the first k words from the sorted list.
        This matches the exact ordering required by the problem.
        """

        from collections import Counter

        freq = Counter(words)
        sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], w))

        return sorted_words[:k]
