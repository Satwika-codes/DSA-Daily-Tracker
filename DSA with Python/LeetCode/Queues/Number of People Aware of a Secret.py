# PROBLEM NUMBER: 2327
# https://leetcode.com/problems/number-of-people-aware-of-a-secret/
# 2327. Number of People Aware of a Secret
# DIFFICULTY: MEDIUM

class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """

        # Approach:
        # Let dp[i] represent the number
        # of people who learn the secret
        # on day i.
        # A person who learns the secret
        # on a particular day starts
        # sharing it after 'delay' days
        # and forgets it after 'forget'
        # days.
        # We maintain a variable 'share'
        # representing the number of
        # people who can actively share
        # the secret on the current day.
        #
        # For each day:
        # • Add people who become eligible
        #   to share today.
        # • Remove people who forget the
        #   secret today.
        # • The remaining active sharers
        #   determine how many new people
        #   learn the secret today.
        #
        # After filling dp, count all
        # people who still remember the
        # secret on day n.
        #
        # These are the people who learned
        # the secret within the last
        # 'forget - 1' days and have not
        # forgotten it yet.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        MOD = 10**9 + 7

        dp = [0] * (n + 1)
        dp[1] = 1

        share = 0

        for day in range(2, n + 1):

            if day - delay >= 1:
                share = (share + dp[day - delay]) % MOD

            if day - forget >= 1:
                share = (share - dp[day - forget]) % MOD

            dp[day] = share

        ans = 0

        for day in range(n - forget + 1, n + 1):
            if day >= 1:
                ans = (ans + dp[day]) % MOD

        return ans