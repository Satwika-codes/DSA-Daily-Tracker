# PROBLEM NUMBER: 2030
# https://leetcode.com/problems/high-five/
# Smallest K-Length Subsequence With Occurrences of a Letter
# DIFFICULTY: HARD

class Solution(object):
    def smallestSubsequence(self, s, k, letter, repetition):
        """
        :type s: str
        :type k: int
        :type letter: str
        :type repetition: int
        :rtype: str
        """
        # Approach:
        # We need lexicographically smallest subsequence of length k
        # containing at least "repetition" copies of letter.
        #
        # Step 1: Count remaining required letters in string:
        #         • remain_letter = total occurrences of letter left
        #
        # Step 2: Track:
        #         • need = letters still required in subsequence
        #         • stack builds answer (monotonic style)
        #
        # Step 3: Traverse characters one by one
        #
        # Step 4: While possible, pop larger characters to make
        #         subsequence lexicographically smaller if:
        #         • stack top > current char
        #         • enough chars remain to still reach size k
        #         • popping won't violate required letter count
        #
        # Step 5: If a required letter is popped:
        #         • increase need
        #
        # Step 6: Try adding current character:
        #
        #         If current is required letter:
        #         • always take it (if space exists)
        #
        #         Otherwise:
        #         • only take if enough slots remain
        #           for mandatory letters
        #
        # Step 7: Update remain_letter while traversing
        #
        # Step 8: Return stack as final subsequence

        remain_letter = s.count(letter)
        need = repetition
        stack = []

        for i, ch in enumerate(s):

            # Try making lexicographically smaller
            while (stack and
                   stack[-1] > ch and
                   len(stack)-1 + (len(s)-i) >= k and
                   (stack[-1] != letter or remain_letter > need)):

                if stack.pop() == letter:
                    need += 1

            # Can we take current character?
            if len(stack) < k:

                if ch == letter:
                    stack.append(ch)
                    need -= 1

                else:
                    # keep room for required letters
                    if k - len(stack) > need:
                        stack.append(ch)

            if ch == letter:
                remain_letter -= 1

        return "".join(stack)