# PROBLEM NUMBER: 3823
# https://leetcode.com/problems/reverse-letters-in-a-string-ii/
# 3823.Reverse Letters Then Special Characters in a String
# DIFFICULTY: EASY
class Solution(object):
    def reverseByType(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach:
        # Step 1: The goal is to reverse alphabetic characters and non-alphabetic characters separately while keeping their original positions in terms of type.
        # Step 2: Traverse the string and separate the characters into two lists: one for alphabetic characters (`letters`) and another for non-alphabetic characters (`others`).
        # Step 3: Use the `isalpha()` method to check whether a character is a letter and append it to the corresponding list.
        # Step 4: After collecting the characters, reverse both lists so that when rebuilding the string the characters appear in reversed order within their respective categories.
        # Step 5: Create an empty list `result` to construct the final string and initialize two pointers `l` and `o` to track positions in the reversed `letters` and `others` lists.
        # Step 6: Iterate through the original string again and check each character's type using `isalpha()`.
        # Step 7: If the character is alphabetic, take the next character from the reversed `letters` list and append it to the result, then increment the letter pointer.
        # Step 8: If the character is not alphabetic, take the next character from the reversed `others` list and append it to the result, then increment the other pointer.
        # Step 9: Continue this process until all characters are processed and the result list contains the rebuilt sequence.
        # Step 10: Finally join the result list into a single string using `"".join()` and return it.
        letters = []
        others = []

        # Separate characters
        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                others.append(ch)

        # Reverse both groups
        letters.reverse()
        others.reverse()

        result = []
        l = o = 0

        # Rebuild string
        for ch in s:
            if ch.isalpha():
                result.append(letters[l])
                l += 1
            else:
                result.append(others[o])
                o += 1

        return "".join(result)