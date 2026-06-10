# PROBLEM NUMBER: 950
# https://leetcode.com/problems/reveal-cards-in-increasing-order/
# 950. Reveal Cards In Increasing Order
# DIFFICULTY: MEDIUM

from collections import deque

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """

        # Approach:
        # We need to arrange the deck so
        # that revealing cards according
        # to the given process produces
        # cards in increasing order.
        #
        # Instead of simulating the
        # process forward, we simulate
        # it in reverse.
        #
        # First, sort the deck in
        # increasing order.
        #
        # Starting from the largest card:
        # • If the deque is not empty,
        #   move the last card to the front.
        # • Insert the current card
        #   at the front.
        #
        # This reverses the original
        # operations of revealing the
        # top card and moving the next
        # top card to the bottom.
        #
        # After processing all cards,
        # the deque represents the
        # required initial arrangement.
        #
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)

        deck.sort()

        dq = deque()

        for card in reversed(deck):

            if dq:
                dq.appendleft(dq.pop())

            dq.appendleft(card)

        return list(dq)