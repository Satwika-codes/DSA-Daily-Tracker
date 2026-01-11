class Solution(object):
    def countCompleteSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        n = len(word)
        ans = 0

        # Split word into valid segments
        start = 0
        for i in range(n):
            if i > 0 and abs(ord(word[i]) - ord(word[i - 1])) > 2:
                ans += self.countSegment(word[start:i], k)
                start = i

        ans += self.countSegment(word[start:n], k)
        return ans

    def countSegment(self, s, k):
        res = 0
        m = len(s)

        for x in range(1, 27):  # number of distinct characters
            length = x * k
            if length > m:
                break

            freq = {}
            valid = 0
            left = 0

            for right in range(m):
                freq[s[right]] = freq.get(s[right], 0) + 1
                if freq[s[right]] == k:
                    valid += 1

                if right - left + 1 > length:
                    if freq[s[left]] == k:
                        valid -= 1
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                    left += 1

                if right - left + 1 == length and valid == x:
                    res += 1

        return res
