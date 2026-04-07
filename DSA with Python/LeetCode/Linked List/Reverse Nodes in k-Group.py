# PROBLEM NUMBER: 25
# https://leetcode.com/problems/reverse-nodes-in-k-group/
# 25. Reverse Nodes in k-Group
# DIFFICULTY: HARD


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Approach:
        # We need to reverse nodes of the linked list in groups of size k.
        # If remaining nodes are less than k → leave them as it is.
        #
        # Step 1: Handle edge cases:
        #         • If list is empty or k == 1 → return head
        #
        # Step 2: Use a dummy node:
        #         • Helps in handling head changes easily
        #
        # Step 3: Maintain pointer prev_group:
        #         • Points to node before current group
        #
        # Step 4: For each group:
        #         • Find kth node from prev_group
        #         • If less than k nodes → return result
        #
        # Step 5: Store next group start:
        #         • group_next = kth.next
        #
        # Step 6: Reverse current group:
        #         • Use standard linked list reversal
        #         • Reverse nodes from prev_group.next to kth
        #
        # Step 7: Reconnect reversed group:
        #         • prev_group.next → kth (new head of group)
        #         • Old head becomes tail → connect to next group
        #
        # Step 8: Move prev_group to end of reversed group
        #
        # Step 9: Repeat until all groups are processed

        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            # find kth node
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            # reverse group
            prev = group_next
            curr = prev_group.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # connect
            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp