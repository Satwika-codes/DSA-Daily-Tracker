# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# PROBLEM NUMBER: 557
# 557. Reverse Words in a String III
# DIFFICULTY: EASY
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach:
        # Step 1: The goal is to reverse each individual word in the string while keeping the word order the same.
        # Step 2: First split the string `s` into a list of words using the space character as the delimiter, so each word becomes a separate element in the list.
        # Step 3: Then iterate through this list using a list comprehension and reverse each word individually using Python slicing `[::-1]`.
        # Step 4: This creates a new list `reversed_words` where every word from the original list is reversed but their positions remain unchanged.
        # Step 5: Finally join all the reversed words back into a single string using `" ".join()` so that spaces are inserted between the words just like in the original sentence.
        # Step 6: Return the resulting string which contains the same word order but with each word reversed.
        words = s.split(" ")
        reversed_words = [word[::-1] for word in words]
        return " ".join(reversed_words)