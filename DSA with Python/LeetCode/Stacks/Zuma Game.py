# PROBLEM NUMBER: 488
# https://leetcode.com/problems/zuma-game/
# 488. Zuma Game
# DIFFICULTY: HARD

class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """

        # Approach:
        # We use DFS + Backtracking + Memoization
        # to find the minimum number of insertions
        # needed to clear the board.
        #
        # A helper function repeatedly removes
        # groups of 3 or more consecutive balls,
        # including any chain reactions that occur.
        #
        # For each state, we try inserting every
        # available color at useful positions only.
        #
        # Memoization stores previously computed
        # board and hand states to avoid redundant
        # calculations and speed up the search.
        #
        # Among all valid choices, we return the
        # minimum number of insertions required.

        from collections import Counter

        hand = Counter(hand)
        memo = {}

        def shrink(s):

            changed = True

            while changed:

                changed = False
                i = 0
                new_s = ""

                while i < len(s):

                    j = i

                    while j < len(s) and s[j] == s[i]:
                        j += 1

                    if j - i >= 3:
                        changed = True
                    else:
                        new_s += s[i:j]

                    i = j

                s = new_s

            return s

        def dfs(cur_board, hand_state):

            cur_board = shrink(cur_board)

            if not cur_board:
                return 0

            key = (cur_board, tuple(sorted(hand_state.items())))

            if key in memo:
                return memo[key]

            ans = float('inf')

            for i in range(len(cur_board) + 1):

                for color in hand_state:

                    if hand_state[color] == 0:
                        continue

                    # pruning
                    if i > 0 and cur_board[i - 1] == color:
                        continue

                    # useful insertion only
                    if (
                        (i < len(cur_board) and cur_board[i] == color)
                        or
                        (
                            0 < i < len(cur_board)
                            and cur_board[i - 1] == cur_board[i]
                            and cur_board[i] != color
                        )
                    ):

                        hand_state[color] -= 1

                        nxt = cur_board[:i] + color + cur_board[i:]

                        temp = dfs(nxt, hand_state)

                        if temp != -1:
                            ans = min(ans, 1 + temp)

                        hand_state[color] += 1

            memo[key] = -1 if ans == float('inf') else ans

            return memo[key]

        return dfs(board, hand)