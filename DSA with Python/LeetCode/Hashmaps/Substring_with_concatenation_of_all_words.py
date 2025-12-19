# PROBLEM NUMBER:30
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# 30.Substring with concatenation of all words
# DIFFICULTY:HARD
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        #APPROACH
        # all words have same length, so store length of one word
        # total length of concatenation is word_length * number_of_words
        # build a hashmap to store required frequency of each word
        # iterate over possible starting offsets based on word length
        # use sliding window with left and right pointers
        # maintain a hashmap for current window word frequencies
        # expand window by moving right pointer word by word
        # if a word frequency exceeds required count, shrink window from left
        # if window size matches total concatenation length, record starting index
        # continue sliding to find all valid starting indices

        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        from collections import defaultdict

        freq = defaultdict(int)
        for w in words:
            freq[w] += 1

        result = []

        for i in range(word_len):
            left = i
            count = 0
            window = defaultdict(int)

            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in freq:
                    window[word] += 1
                    count += 1

                    while window[word] > freq[word]:
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        result.append(left)

                else:
                    window.clear()
                    count = 0
                    left = right + word_len

        return result
