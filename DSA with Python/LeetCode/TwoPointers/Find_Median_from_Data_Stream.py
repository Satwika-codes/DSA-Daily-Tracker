# PROBLEM NUMBER:295
# https://leetcode.com/problems/find-median-from-data-stream/
# 295.Find Median from Data Stream
# DIFFICULTY:HARD
import heapq

class MedianFinder(object):

    def __init__(self):
        # Approach:
        # ---------
        # We maintain two heaps:
        # 1. Max Heap (left half): stores the smaller half of numbers
        # 2. Min Heap (right half): stores the larger half of numbers

        # Rules:
        # - The size difference between the heaps is at most 1
        # - Max heap always holds the extra element when count is odd

        # Median logic:
        # - If both heaps have equal size → median is average of roots
        # - If sizes differ → median is root of max heap

        # Time Complexity:
        # - addNum(): O(log n)
        # - findMedian(): O(1)

        # Space Complexity:
        # - O(n)
        
        self.maxHeap = []  # Max heap (store negatives)
        self.minHeap = []  # Min heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Step 1: Push to max heap
        heapq.heappush(self.maxHeap, -num)

        # Step 2: Balance: move largest from maxHeap to minHeap
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        # Step 3: Maintain size property
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
