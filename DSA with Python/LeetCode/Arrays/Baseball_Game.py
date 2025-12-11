# PROBLEM NUMBER: 682
# https://leetcode.com/problems/baseball-game/
# BASEBALL GAME
# DIFFICULTY: EASY
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """

        # Approach (Stack Simulation):
        #
        # You're given operations describing scores in a baseball game.
        # You must evaluate them following rules:
        #
        # 1. Integer x → Add x to score record.
        # 2. "+"       → Add (last score + second last score).
        # 3. "D"       → Add (2 × last score).
        # 4. "C"       → Remove last score.
        #
        # Use a stack to keep track of valid scores.
        #
        # Steps:
        # • For each op:
        #       - If op is "C": pop last valid score.
        #       - If op is "D": push 2 × last valid score.
        #       - If op is "+": push sum of last two valid scores.
        #       - Else: convert to int and push.
        #
        # Return sum of all values in the stack.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        stack = []
        for op in ops:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))

        return sum(stack)
