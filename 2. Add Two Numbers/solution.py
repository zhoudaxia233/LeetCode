# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = l = ListNode(0)
        carry = 0
        
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + carry
            l.next = ListNode(s % 10)
            carry = s // 10
            l = l.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        l.next = ListNode(1) if carry else None
        return dummyHead.next
