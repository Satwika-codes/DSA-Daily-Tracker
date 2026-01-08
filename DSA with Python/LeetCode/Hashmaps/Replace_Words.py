# PROBLEM NUMBER:648
# https://leetcode.com/problems/replace-words/
# 648.Replace Words
# DIFFICULTY: HARD
class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        # Approach:
        # We need to replace words in the sentence with the shortest possible
        # root from the dictionary that is a prefix of the word.

        # Steps:
        # 1. Store all roots in a set for fast lookup.
        # 2. For each word in the sentence, check prefixes starting from
        #    length 1 to the full word length.
        # 3. As soon as a prefix exists in the root set, replace the word
        #    with that prefix.
        # 4. If no prefix is found, keep the word unchanged.

        # Since root lengths are small, this approach is efficient and safe.
        

        root_set = set(dictionary)
        result = []

        for word in sentence.split():
            replacement = word
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in root_set:
                    replacement = prefix
                    break
            result.append(replacement)

        return " ".join(result)
