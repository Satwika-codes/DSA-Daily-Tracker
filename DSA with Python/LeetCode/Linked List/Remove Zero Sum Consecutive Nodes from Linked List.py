# PROBLEM NUMBER:1171
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
# 1171. Remove Zero Sum Consecutive Nodes from Linked List
# DIFFICULTY:MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Approach:
        # We need to remove all consecutive nodes whose sum = 0.
        #
        # Step 1: Use prefix sum technique:
        #         • If prefix sum repeats → nodes in between sum to 0
        #
        # Step 2: Use a hashmap (seen):
        #         • Maps prefix sum → latest node where it occurs
        #
        # Step 3: Use dummy node:
        #         • Handles cases where removal starts from head
        #
        # Step 4: First pass:
        #         • Traverse list and compute prefix sum
        #         • Store/update seen[prefix] = current node
        #           (store last occurrence to skip full zero-sum range)
        #
        # Step 5: Second pass:
        #         • Reset prefix = 0
        #         • Traverse again
        #         • If prefix seen before:
        #             → skip nodes in between
        #             → curr.next = seen[prefix].next
        #
        # Step 6: This removes all zero-sum sublists
        #
        # Step 7: Return dummy.next

        dummy = ListNode(0)
        dummy.next = head

        prefix = 0
        seen = {}

        # Pass 1: store last occurrence
        curr = dummy
        while curr:
            prefix += curr.val
            seen[prefix] = curr
            curr = curr.next

        # Pass 2: remove zero sum sublists
        prefix = 0
        curr = dummy
        while curr:
            prefix += curr.val
            curr.next = seen[prefix].next
            curr = curr.next

        return dummy.next