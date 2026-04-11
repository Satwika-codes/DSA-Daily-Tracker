# PROBLEM NUMBER: 147
# https://leetcode.com/problems/insertion-sort-list/
# 147. Insertion Sort List
# DIFFICULTY: MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Approach:
        # We need to sort the linked list using Insertion Sort.
        #
        # Step 1: Use a dummy node:
        #         • Represents the start of the sorted list
        #
        # Step 2: Traverse original list using curr pointer
        #
        # Step 3: For each node:
        #         • Find correct position in sorted list
        #         • Start from dummy and move forward
        #         • Stop where next node value is >= curr.val
        #
        # Step 4: Store next node before modifying links
        #
        # Step 5: Insert curr node into sorted list:
        #         • curr.next = prev.next
        #         • prev.next = curr
        #
        # Step 6: Move to next node in original list
        #
        # Step 7: Continue until all nodes are processed
        #
        # Step 8: Return dummy.next (head of sorted list)

        dummy = ListNode(0)  # start of sorted list
        curr = head

        while curr:
            prev = dummy

            # find correct position
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # store next node
            next_node = curr.next

            # insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr

            # move to next node
            curr = next_node

        return dummy.next