#!/usr/bin/env python

#class ListNode(object):
#    self.val = x
#    self.next = None

def Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return head

        pre = head
        cur = head.next
        while cur:
            if pre.val == cur.val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next

        return head
