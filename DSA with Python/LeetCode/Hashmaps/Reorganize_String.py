# PROBLEM NUMBER:767
# https://leetcode.com/problems/reorganize-string/
# Reorganize String
# DIFFICULTY: MEDIUM
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach:
        # We want to rearrange characters so that no two adjacent characters
        # are the same.

        # First, count the frequency of each character.
        # If any character appears more than (n + 1) // 2 times, it is
        # impossible to rearrange, so return an empty string.

        # Otherwise, use a max heap based on character frequencies.
        # Repeatedly take the two most frequent characters, append them
        # to the result, decrease their counts, and push them back if
        # they are still available.

        # This greedy approach always avoids placing the same characters
        # next to each other and is guaranteed to work.
        

        from collections import Counter
        import heapq

        freq = Counter(s)
        n = len(s)

        if max(freq.values()) > (n + 1) // 2:
            return ""

        heap = [(-count, ch) for ch, count in freq.items()]
        heapq.heapify(heap)

        res = []

        while len(heap) > 1:
            cnt1, ch1 = heapq.heappop(heap)
            cnt2, ch2 = heapq.heappop(heap)

            res.append(ch1)
            res.append(ch2)

            if cnt1 + 1 < 0:
                heapq.heappush(heap, (cnt1 + 1, ch1))
            if cnt2 + 1 < 0:
                heapq.heappush(heap, (cnt2 + 1, ch2))

        if heap:
            res.append(heap[0][1])

        return "".join(res)
