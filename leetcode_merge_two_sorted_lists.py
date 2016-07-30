#!/usr/bin/env python

#class ListNode(object):
#    def __init__(self, x):
#        self.val  = x
#        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        newHead = ListNode(0)
        head = newHead

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next

            head = head.next

        if l1 != None:
            head.next = l1
        if l2 != None:
            head.next = l2

        return newHead
