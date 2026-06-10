# PROBLEM NUMBER: 1823
# https://leetcode.com/problems/find-the-winner-of-the-circular-game/
# 1823. Find the Winner of the Circular Game
# DIFFICULTY: MEDIUM

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        # Approach:
        # This problem is a classic
        # Josephus Problem.
        #
        # Instead of simulating the
        # entire elimination process,
        # we use the recurrence relation
        # for the winner's position.
        #
        # Let f(i) represent the winner's
        # position among i players using
        # 0-based indexing.
        #
        # When a new player is added,
        # the winner's position shifts by
        # k positions in the circle.
        #
        # Therefore:
        # f(i) = (f(i - 1) + k) % i
        #
        # Start with one player where
        # the winner is at position 0.
        #
        # Iteratively compute the winner
        # for 2 to n players.
        #
        # Finally, convert the answer
        # from 0-based indexing to
        # 1-based indexing.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        winner = 0  # f(1)

        for players in range(2, n + 1):
            winner = (winner + k) % players

        return winner + 1