# PROBLEM NUMBER: 1046
# https://leetcode.com/problems/last-stone-weight/
# Last Stone Weight
# DIFFICULTY: EASY
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        # Approach:
        # Step 1: Convert all stone weights to negative and build a max-heap 
        #         (Python only provides min-heap, so we invert values).
        # Step 2: Repeatedly pop the two heaviest stones (largest negatives).
        # Step 3: If they are not equal, push the difference back into the heap.
        # Step 4: Continue until either one stone or no stone remains.
        # Step 5: Return the remaining stone (convert back to positive), or 0 if none.

        import heapq
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)  # heaviest
            x = -heapq.heappop(stones)  # second heaviest

            if y != x:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0
