# PROBLEM NUMBER: 2109
# https://leetcode.com/problems/adding-spaces-to-a-string/
# 2109. Adding Spaces to a String
# DIFFICULTY: MEDIUM
class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        # Approach:
        # Step 1: We are given a string s and a list of indices where spaces must be inserted.
        # Step 2: Traverse the string character by character.
        # Step 3: Maintain a pointer (space_index) to track which position in the spaces list we should check next.
        # Step 4: If the current index i matches spaces[space_index], insert a space before adding the character.
        # Step 5: Append the current character to the result list.
        # Step 6: Continue until all characters are processed.
        # Step 7: Join the list into a string and return it.

        result = []
        space_index = 0
        n = len(spaces)

        for i in range(len(s)):
            # Insert space if current index matches
            if space_index < n and i == spaces[space_index]:
                result.append(" ")
                space_index += 1

            result.append(s[i])

        return "".join(result)