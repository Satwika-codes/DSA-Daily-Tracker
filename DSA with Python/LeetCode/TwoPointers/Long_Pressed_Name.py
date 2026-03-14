# PROBLEM NUMBER: 925
# https://leetcode.com/problems/long-pressed-name/
# LeetCode 925. Long Pressed Name
# DIFFICULTY: EASY
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        # Approach:
        # Step 1: The problem is to check whether the string `typed` could result from long pressing characters while typing the string `name`.
        # Step 2: Use two pointers: `i` to traverse the original `name` and `j` to traverse the `typed` string.
        # Step 3: Traverse through the `typed` string while comparing characters with the corresponding characters in `name`.
        # Step 4: If the current characters match (`name[i] == typed[j]`), it means the character was typed normally, so move both pointers forward.
        # Step 5: If the characters do not match, check whether the current character in `typed` is the same as the previous character in `typed`.
        # Step 6: If it is the same as the previous character, this indicates a long press of that key, so move only the `typed` pointer forward.
        # Step 7: If neither condition is satisfied, it means the `typed` string contains an unexpected character sequence and cannot represent a valid long press, so return False.
        # Step 8: Continue this process until the `typed` string is fully processed.
        # Step 9: Finally check whether all characters of `name` were matched by verifying that pointer `i` has reached the end of `name`; if so return True, otherwise return False.

        i = 0  # pointer for name
        j = 0  # pointer for typed

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        return i == len(name)