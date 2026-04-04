# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # Approach:
        # We are given a linked list representing a binary number
        # where each node contains either 0 or 1.
        # We need to convert it into its decimal value.
        #
        # Step 1: Initialize a variable num = 0 to store result.
        #
        # Step 2: Traverse the linked list:
        #         • For each node, shift current number left by 1 (num * 2)
        #         • Add current node's value (0 or 1)
        #
        # Step 3: This simulates binary to decimal conversion:
        #         • Example: 101 → ((1*2 + 0)*2 + 1)
        #
        # Step 4: Move to next node until list ends
        #
        # Step 5: Return final number

        num = 0

        while head:
            num = num * 2 + head.val
            head = head.next

        return num