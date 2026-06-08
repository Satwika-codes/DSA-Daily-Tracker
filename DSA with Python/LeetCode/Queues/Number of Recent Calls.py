# PROBLEM NUMBER: 933
# https://leetcode.com/problems/number-of-recent-calls/
# 933. Number of Recent Calls
# DIFFICULTY: EASY

from collections import deque

class RecentCounter(object):

    def __init__(self):

        # Approach:
        # We maintain a queue containing
        # timestamps of recent requests.
        #
        # For every new ping(t):
        # • Add the current timestamp.
        # • Remove all timestamps that
        #   are older than t - 3000.
        #
        # After removing outdated requests,
        # the queue contains exactly the
        # calls made in the interval
        # [t - 3000, t].
        #
        # The size of the queue is the
        # required answer.

        self.q = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """

        self.q.append(t)

        while self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)