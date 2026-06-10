# PROBLEM NUMBER: 2073
# https://leetcode.com/problems/time-needed-to-buy-tickets/
# 2073. Time Needed to Buy Tickets
# DIFFICULTY: EASY

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """

        # Approach:
        # Let the person at index k be
        # the target person.
        #
        # The target person needs
        # tickets[k] purchases to finish.
        #
        # For every person:
        # • If their position is before
        #   or equal to k, they can buy
        #   at most tickets[k] tickets
        #   before the target finishes.
        #
        # • If their position is after k,
        #   they will not get their last
        #   turn once the target person
        #   completes buying tickets.
        #
        # Therefore, they can contribute
        # at most tickets[k] - 1 purchases.
        #
        # Add the contribution of each
        # person to obtain the total
        # time required for the target
        # person to finish buying tickets.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        target = tickets[k]
        ans = 0

        for i in range(len(tickets)):

            if i <= k:
                ans += min(tickets[i], target)
            else:
                ans += min(tickets[i], target - 1)

        return ans