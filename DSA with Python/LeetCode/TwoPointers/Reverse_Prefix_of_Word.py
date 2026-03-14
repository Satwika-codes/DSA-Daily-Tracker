class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        # Approach:
        # Step 1: The goal is to reverse the prefix of the string up to and including the first occurrence of the character `ch`.
        # Step 2: First find the index of the first occurrence of `ch` in the string using the `find()` method.
        # Step 3: If `find()` returns -1, it means the character `ch` does not exist in the string, so no reversal is needed and the original word is returned.
        # Step 4: If the character is found, take the substring from the start of the string up to `idx + 1` so that the prefix includes the character `ch`.
        # Step 5: Reverse this prefix using Python slicing `[::-1]`.
        # Step 6: Take the remaining part of the string after the prefix (`word[idx + 1:]`) without modifying it.
        # Step 7: Concatenate the reversed prefix with the remaining suffix to form the final string.
        # Step 8: Return the resulting string which contains the reversed prefix and the unchanged suffix.

        idx = word.find(ch)

        if idx == -1:
            return word

        return word[:idx + 1][::-1] + word[idx + 1:]