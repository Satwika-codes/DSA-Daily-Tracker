class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        # Approach:
        # - Iterate through both strings simultaneously.
        # - Count "bulls" when characters match at the same index.
        # - For non-matching positions, store frequency of characters
        #   from secret and guess using hash maps (Counters).
        # - Count "cows" by summing the minimum frequency of each
        #   character present in both Counters.
        # - Format the result as "xAyB".

        from collections import Counter

        bulls = 0
        s_count = Counter()
        g_count = Counter()

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                s_count[secret[i]] += 1
                g_count[guess[i]] += 1

        cows = 0
        for ch in s_count:
            cows += min(s_count[ch], g_count.get(ch, 0))

        return str(bulls) + "A" + str(cows) + "B"
