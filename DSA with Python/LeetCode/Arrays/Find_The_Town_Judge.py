# PROBLEM NUMBER: 997
# https://leetcode.com/problems/find-the-town-judge/
# 997. Find the Town Judge
# DIFFICULTY: EASY
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        # Approach (Graph / Trust Score Logic):
        #
        # Goal:
        # The town judge is a person who:
        #   1) Trusts nobody.
        #   2) Is trusted by everyone else → (n - 1) people trust them.
        #
        # Steps:
        # 1. If n == 1 and there is no trust relationship, that single person is the judge.
        #
        # 2. Create a `score` array of size n+1.
        #       - When a trusts b:
        #           * a loses trust score → a is NOT judge → score[a] -= 1
        #           * b gains trust      → score[b] += 1
        #
        # 3. After processing all trust pairs:
        #       - The judge will have score = n - 1
        #         (trusted by everyone else and trusts nobody).
        #
        # 4. Scan the score array and return the index whose score == n - 1.
        #
        # 5. If no such person exists → return -1.

        if n == 1 and not trust:
            return 1
        
        score = [0] * (n + 1)
        
        for a, b in trust:
            score[a] -= 1   # a trusts someone → disqualifies a from being judge
            score[b] += 1   # b is trusted by someone
        
        for i in range(1, n + 1):
            if score[i] == n - 1:
                return i

        return -1
