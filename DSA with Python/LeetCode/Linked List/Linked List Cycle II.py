# PROBLEM NUMBER: 142
# https://leetcode.com/problems/linked-list-cycle-ii/
# 142. Linked List Cycle II
# DIFFICULTY: MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Approach:
        # We need to detect if a cycle exists and return the node
        # where the cycle begins.
        #
        # Step 1: Use two pointers:
        #         • slow moves 1 step
        #         • fast moves 2 steps
        #
        # Step 2: Detect cycle:
        #         • If slow == fast → cycle exists
        #         • If fast reaches end → no cycle
        #
        # Step 3: Find start of cycle:
        #         • Move slow back to head
        #         • Move both slow and fast one step at a time
        #
        # Step 4: The point where they meet again is the start of cycle
        #
        # Step 5: Return that node

        slow = head
        fast = head

        # Step 1: detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None  # no cycle

        # Step 2: find start of cycle
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow