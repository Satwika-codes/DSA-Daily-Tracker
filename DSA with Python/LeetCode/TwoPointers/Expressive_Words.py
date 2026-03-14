# PROBLEM NUMBER: 809
# https://leetcode.com/problems/expressive-words/
# 809. Expressive Words
# DIFFICULTY: MEDIUM
class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        # Approach:
        # Step 1: The goal is to count how many words in the given list can become equal to string `s` after applying the "stretchy" rule, meaning groups of characters in `s` can be longer than the corresponding groups in the word if the group in `s` has length at least 3.
        # Step 2: Define a helper function `isStretchy(word)` that checks whether a given word can be stretched to match `s`.
        # Step 3: Use two pointers `i` for string `s` and `j` for the current `word` so we can compare both strings character by character while processing groups of identical characters.
        # Step 4: If characters at the current positions do not match, the word cannot be stretched to form `s`, so return False immediately.
        # Step 5: When characters match, count the length of the current character group in `s` by moving pointer `i` forward while the same character repeats.
        # Step 6: Similarly count the length of the same character group in `word` by moving pointer `j` forward while the character repeats.
        # Step 7: After obtaining both group lengths, check validity: if the group in `s` is smaller than the group in the word, stretching is impossible so return False.
        # Step 8: Also if the group in `s` has length less than 3 and the lengths of the groups are not exactly equal, stretching is not allowed so return False.
        # Step 9: Continue processing all groups until one of the strings finishes; at the end ensure both pointers reached the end of their respective strings.
        # Step 10: In the main function iterate through every word in `words`, call `isStretchy(word)`, and increment the count whenever the word satisfies the stretchy condition.
        # Step 11: Finally return the total count of words that can be stretched to match `s`.
        def isStretchy(word):
            i = j = 0
            n, m = len(s), len(word)

            while i < n and j < m:
                if s[i] != word[j]:
                    return False

                # Count group length in s
                ch = s[i]
                count_s = 0
                while i < n and s[i] == ch:
                    i += 1
                    count_s += 1

                # Count group length in word
                count_w = 0
                while j < m and word[j] == ch:
                    j += 1
                    count_w += 1

                # Check validity
                if count_s < count_w:
                    return False
                if count_s < 3 and count_s != count_w:
                    return False

            return i == n and j == m

        count = 0
        for word in words:
            if isStretchy(word):
                count += 1

        return count