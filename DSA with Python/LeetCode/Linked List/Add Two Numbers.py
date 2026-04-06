# PROBLEM NUMBER:2
# https://leetcode.com/problems/add-two-numbers/
# 2.Add Two Numbers
# DIFFICULTY:EASY


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Approach:
        # We are given two linked lists representing numbers in reverse order.
        # Each node contains a single digit.
        # We need to add the two numbers and return the result as a linked list.
        #
        # Step 1: Use a dummy node to simplify result list construction.
        #         • curr pointer will build the result list
        #
        # Step 2: Maintain a carry variable (initially 0)
        #
        # Step 3: Traverse both lists until all nodes and carry are processed:
        #         • Extract values from l1 and l2 (0 if list is exhausted)
        #
        # Step 4: Compute total:
        #         • total = val1 + val2 + carry
        #
        # Step 5: Update carry:
        #         • carry = total // 10
        #
        # Step 6: Create new node with digit:
        #         • total % 10
        #         • Attach it to result list
        #
        # Step 7: Move pointers of l1, l2, and curr forward
        #
        # Step 8: Continue until l1, l2, and carry are all empty
        #
        # Step 9: Return dummy.next (head of result list)

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next