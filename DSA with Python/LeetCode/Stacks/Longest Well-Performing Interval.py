# PROBLEM NUMBER: 1124
# https://leetcode.com/problems/longest-well-performing-interval/
# 1124. Longest Well-Performing Interval
# DIFFICULTY: MEDIUM

class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """

        # Approach:
        # A day is:
        #
        # • Tiring     → hours > 8
        # • Non-tiring → hours <= 8
        #
        # We convert the array into scores:
        #
        # • Tiring day     → +1
        # • Non-tiring day → -1
        #
        # Then the problem becomes:
        #
        # Find the longest subarray whose
        # total score is positive.
        #
        # Step 1:
        # Maintain a running prefix score.
        #
        # score =
        # (# tiring days) - (# non-tiring days)
        #
        # Step 2:
        # If score > 0 at index i:
        #
        # Entire interval [0...i]
        # is well-performing.
        #
        # Length = i + 1
        #
        # Step 3:
        # If score <= 0:
        #
        # We need a previous prefix score
        # equal to (score - 1).
        #
        # Why?
        #
        # If:
        # current_score - previous_score > 0
        #
        # Then:
        # previous_score < current_score
        #
        # The earliest useful score is
        # (score - 1).
        #
        # Step 4:
        # Store only the first occurrence
        # of every prefix score because
        # earlier positions give longer intervals.
        #
        # Step 5:
        # Update answer whenever a longer
        # well-performing interval is found.
        #
        # Step 6:
        # Return maximum length.

        # Stores first occurrence of prefix scores
        first = {}

        score = 0
        ans = 0

        for i, h in enumerate(hours):

            # Tiring day
            if h > 8:
                score += 1

            # Non-tiring day
            else:
                score -= 1

            # Entire prefix is valid
            if score > 0:

                ans = i + 1

            else:

                # Look for earliest score - 1
                if score - 1 in first:

                    ans = max(
                        ans,
                        i - first[score - 1]
                    )

            # Store first occurrence only
            if score not in first:

                first[score] = i

        return ans