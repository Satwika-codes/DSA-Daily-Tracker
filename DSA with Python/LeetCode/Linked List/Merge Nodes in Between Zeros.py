# PROBLEM NUMBER: 2183
# https://leetcode.com/problems/merge-nodes-in-between-zeros/
# 2183. Merge Nodes in Between Zeros
# DIFFICULTY: MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Approach:
        # The list is divided into segments separated by 0s.
        # We need to sum values between every pair of 0s and create a new list.
        #
        # Step 1: Use a dummy node to build result list
        #
        # Step 2: Skip the first node (always 0)
        #
        # Step 3: Traverse the list:
        #         • Maintain a running sum (total)
        #
        # Step 4: If current value is not 0:
        #         • Add it to total
        #
        # Step 5: If current value is 0:
        #         • End of segment reached
        #         • Create a new node with total
        #         • Append to result list
        #         • Reset total = 0
        #
        # Step 6: Continue until end
        #
        # Step 7: Return dummy.next

        dummy = ListNode(0)
        curr_new = dummy

        curr = head.next  # skip first 0
        total = 0

        while curr:
            if curr.val != 0:
                total += curr.val
            else:
                # end of segment
                curr_new.next = ListNode(total)
                curr_new = curr_new.next
                total = 0
            curr = curr.next

        return dummy.next