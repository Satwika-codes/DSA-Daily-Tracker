# PROBLEM NUMBER: 948
# https://leetcode.com/problems/bag-of-tokens/
# 948. Bag of Tokens
# DIFFICULTY: MEDIUM
class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        # Approach:
        # Step 1: The goal is to maximize the score by either spending power to gain score or sacrificing score to regain power using tokens.
        # Step 2: First sort the tokens array so that we can always access the smallest token for gaining score and the largest token for regaining power.
        # Step 3: Use two pointers: `left` pointing to the smallest token and `right` pointing to the largest token.
        # Step 4: Initialize `score` to track the current score and `max_score` to record the maximum score achieved during the process.
        # Step 5: While the left pointer has not crossed the right pointer, check if we have enough power to play the smallest token face up.
        # Step 6: If `power >= tokens[left]`, spend that power to gain one score, move the left pointer forward, and update `max_score`.
        # Step 7: If we do not have enough power but still have at least one score, play the largest token face down to regain power, decrease the score by one, and move the right pointer backward.
        # Step 8: If neither action is possible (not enough power and no score to sacrifice), stop the process.
        # Step 9: Continue this greedy process until no more valid moves can be made.
        # Step 10: Finally return `max_score`, which represents the highest score achievable.

        tokens.sort()

        left = 0
        right = len(tokens) - 1

        score = 0
        max_score = 0

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)

            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1

            else:
                break

        return max_score
        