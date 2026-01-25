# PROBLEM NUMBER: 148
# https://leetcode.com/problems/sort-list/
# 148.Sort List
# DIFFICULTY: MEDIUM
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Approach:
        # - Use Merge Sort on the linked list.
        # - Base case:
        #     If the list is empty or has only one node, it is already sorted.
        # - Split the list into two halves using slow and fast pointers.
        # - Recursively sort both halves.
        # - Merge the two sorted linked lists into one sorted list.
        
        # Why Merge Sort?
        # - Linked lists do not support random access.
        # - Merge sort does not require index access.
        # - Guarantees O(n log n) time complexity.

        # Time Complexity: O(n log n)
        # Space Complexity: O(log n) due to recursion stack
        

        # Base case
        if not head or not head.next:
            return head

        # Step 1: Split the list into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # Step 2: Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Step 3: Merge sorted halves
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next
