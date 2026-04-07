# PROBLEM NUMBER: 24
# https://leetcode.com/problems/swap-nodes-in-pairs/
# 24. Swap Nodes in Pairs
# DIFFICULTY: MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Approach:
        # We need to swap every two adjacent nodes in the linked list.
        #
        # Step 1: Use a dummy node:
        #         • Helps in handling head changes easily
        #
        # Step 2: Maintain a pointer prev:
        #         • Points to node before the current pair
        #
        # Step 3: While there are at least two nodes ahead:
        #         • Let a = prev.next (first node)
        #         • Let b = a.next (second node)
        #
        # Step 4: Perform swap:
        #         • prev.next = b
        #         • a.next = b.next
        #         • b.next = a
        #
        # Step 5: Move prev to next position:
        #         • prev = a (new second node after swap)
        #
        # Step 6: Repeat until no more pairs
        #
        # Step 7: Return dummy.next (new head)

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            a = prev.next
            b = a.next

            # swap
            prev.next = b
            a.next = b.next
            b.next = a

            # move prev
            prev = a

        return dummy.next