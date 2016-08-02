#!/usr/bin/env python

class Solution(object):
    def swapPairs(self, head):
        if head is None:
            return None

        temp = head
        while temp is not None and temp.next is not None:
            temp.val, temp.next.val = temp.next.val, temp.val
            temp = temp.next.next
        return head
