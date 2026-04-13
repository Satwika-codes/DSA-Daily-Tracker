# PROBLEM NUMBER: 2058
# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
# DIFFICULTY: MEDIUM


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        # Approach:
        # We need to find distances between critical points in the linked list.
        # A node is critical if:
        # • It is a local maxima (greater than both neighbors)
        # • Or a local minima (smaller than both neighbors)
        #
        # Step 1: Traverse the list using three pointers:
        #         • prev → previous node
        #         • curr → current node
        #         • curr.next → next node
        #
        # Step 2: Maintain an index counter for positions
        #
        # Step 3: For each node (excluding first and last):
        #         • Check if it is a critical point
        #         • If yes → store its index in a list
        #
        # Step 4: If less than 2 critical points:
        #         • Return [-1, -1]
        #
        # Step 5: Compute minimum distance:
        #         • Difference between consecutive critical points
        #
        # Step 6: Compute maximum distance:
        #         • Difference between first and last critical points
        #
        # Step 7: Return [min_dist, max_dist]

        prev = head
        curr = head.next
        index = 1

        critical = []

        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                critical.append(index)

            prev = curr
            curr = curr.next
            index += 1

        if len(critical) < 2:
            return [-1, -1]

        # min distance
        min_dist = float('inf')
        for i in range(1, len(critical)):
            min_dist = min(min_dist, critical[i] - critical[i - 1])

        # max distance
        max_dist = critical[-1] - critical[0]

        return [min_dist, max_dist]