# PROBLEM NUMBER: 3412
# https://leetcode.com/problems/find-mirror-score-of-a-string/
# 3412. Find Mirror Score of a String
# DIFFICULTY: MEDIUM

class Solution(object):
    def calculateScore(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Approach:
        # Every character has a mirror character:
        #
        # • a ↔ z
        # • b ↔ y
        # • c ↔ x
        # ...
        #
        # We process the string from left to right
        # and try to match each character with the
        # closest unmarked mirror character that
        # appeared earlier.
        #
        # Step 1:
        # Maintain a hashmap:
        #
        # stacks[ch]
        #
        # • Stores indices of unmarked occurrences
        #   of character ch.
        #
        # Step 2:
        # For each character:
        #
        # • Compute its mirror character.
        #
        # Example:
        # a → z
        # b → y
        # c → x
        #
        # Step 3:
        # If an unmarked mirror character exists:
        #
        # • Use the most recent occurrence.
        #
        # • Mark both positions by removing
        #   that index from the stack.
        #
        # • Add distance:
        #
        #   current_index - mirror_index
        #
        # to the score.
        #
        # Step 4:
        # Otherwise:
        #
        # • Store the current index
        #   for future matching.
        #
        # Step 5:
        # Return the total mirror score.

        stacks = {}

        score = 0

        for i, ch in enumerate(s):

            # Compute mirror character
            mirror = chr(
                ord('a') +
                (25 - (ord(ch) - ord('a')))
            )

            # Mirror character available
            if mirror in stacks and stacks[mirror]:

                j = stacks[mirror].pop()

                score += i - j

            else:

                # Store current index
                if ch not in stacks:
                    stacks[ch] = []

                stacks[ch].append(i)

        return score