# PROBLEM NUMBER: 23
# https://leetcode.com/problems/merge-k-sorted-lists/
# 23. Merge k Sorted Lists
# DIFFICULTY: HARD

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # Approach:
        # We need to merge k sorted linked lists into one sorted list.
        #
        # Step 1: Use a min heap (priority queue):
        #         • It helps us always get the smallest node among k lists
        #
        # Step 2: Push the first node of each list into the heap:
        #         • Store (node value, list index, node)
        #         • Index is used to avoid comparison issues between nodes
        #
        # Step 3: Create a dummy node to build result list
        #
        # Step 4: While heap is not empty:
        #         • Pop the smallest node from heap
        #         • Attach it to result list
        #
        # Step 5: If the popped node has a next node:
        #         • Push that next node into heap
        #
        # Step 6: Repeat until heap becomes empty
        #
        # Step 7: Return dummy.next (head of merged list)

        heap = []

        # push first node of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next