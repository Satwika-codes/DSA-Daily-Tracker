# PROBLEM NUMBER:480
# https://leetcode.com/problems/sliding-window-median/
# 480.Sliding Window Median
# DIFFICULTY:HARD
from collections import defaultdict
import heapq

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """

        # Approach:
        # We need to find the median of every sliding window of size k.
        #
        # Key Idea:
        # Use two heaps:
        #   • small → max heap (store negative values)
        #   • large → min heap
        #
        # Step 1: Maintain balance such that:
        #         • small has equal or one more element than large
        #
        # Step 2: Use a hashmap (delayed) to lazily delete elements
        #         that fall out of the window.
        #
        # Step 3: Define helper functions:
        #
        #   prune(heap):
        #       • Remove elements from heap top if marked in delayed
        #
        #   balance():
        #       • Ensure size property between heaps is maintained
        #
        #   add(num):
        #       • Insert into appropriate heap
        #       • Balance heaps
        #
        #   remove(num):
        #       • Mark element for deletion
        #       • Adjust sizes
        #       • Prune if needed
        #       • Balance heaps
        #
        #   getMedian():
        #       • If k is odd → top of small
        #       • Else → average of tops of both heaps
        #
        # Step 4: Iterate through nums:
        #         • Add current element
        #         • Remove element leaving window
        #         • Once window size reached → record median
        #
        # Step 5: Return list of medians.

        small = []  # max heap (store negatives)
        large = []  # min heap
        delayed = defaultdict(int)

        smallSize = [0]
        largeSize = [0]

        def prune(heap):
            while heap:
                num = heap[0]
                if heap is small:
                    num = -num
                if delayed[num] > 0:
                    delayed[num] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            if smallSize[0] > largeSize[0] + 1:
                val = -heapq.heappop(small)
                heapq.heappush(large, val)
                smallSize[0] -= 1
                largeSize[0] += 1
                prune(small)

            elif smallSize[0] < largeSize[0]:
                val = heapq.heappop(large)
                heapq.heappush(small, -val)
                largeSize[0] -= 1
                smallSize[0] += 1
                prune(large)

        def add(num):
            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                smallSize[0] += 1
            else:
                heapq.heappush(large, num)
                largeSize[0] += 1

            balance()

        def remove(num):
            delayed[num] += 1

            if num <= -small[0]:
                smallSize[0] -= 1
                if num == -small[0]:
                    prune(small)
            else:
                largeSize[0] -= 1
                if large and num == large[0]:
                    prune(large)

            balance()

        def getMedian():
            if k % 2:
                return float(-small[0])
            return (-small[0] + large[0]) / 2.0

        res = []

        for i in range(len(nums)):
            add(nums[i])

            if i >= k:
                remove(nums[i - k])

            if i >= k - 1:
                res.append(getMedian())

        return res