# PROBLEM NUMBER:2379
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
# 2379.Minimum Recolors to Get K Consecutive Black Blocks
# DIFFICULTY:
class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
         # Approach:
        # We need to find the minimum number of recolors required to get
        # k consecutive black blocks ('B').
        #
        # Step 1: Use a sliding window of size k.
        #
        # Step 2: Count the number of white blocks ('W') in the first window
        #         of size k. This represents how many recolors are needed
        #         for that window.
        #
        # Step 3: Initialize min_ops with this initial count.
        #
        # Step 4: Slide the window across the string:
        #         • If the new character entering the window is 'W',
        #           increment the white count.
        #         • If the character leaving the window is 'W',
        #           decrement the white count.
        #
        # Step 5: After each shift, update min_ops with the minimum
        #         number of white blocks seen so far.
        #
        # Step 6: Continue until all windows are processed.
        #
        # Step 7: Return min_ops as the answer.
       # count whites in first window
        white = blocks[:k].count('W')
        min_ops = white

        # slide window
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                white += 1
            if blocks[i - k] == 'W':
                white -= 1

            min_ops = min(min_ops, white)

        return min_ops 