class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        # APPROACH:
        # 1. Count the frequency of each character in string s.
        # 2. Append characters to the result following the order given in
        #    the 'order' string, using their counted frequencies.
        # 3. Append any remaining characters from s that do not appear
        #    in the 'order' string.
        # 4. Join and return the constructed string.

        # Time Complexity:
        # - O(n)

        # Space Complexity:
        # - O(1), since the alphabet size is fixed
        
        from collections import Counter

        freq = Counter(s)
        res = []

        for c in order:
            if c in freq:
                res.append(c * freq[c])
                del freq[c]

        for c in freq:
            res.append(c * freq[c])

        return "".join(res)
