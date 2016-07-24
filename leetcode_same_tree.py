#!/usr/bin/env python

#class TreeNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val == q.val:
            if self.isSameTree(p.left, q.left):
                return self.isSameTree(p.right, q.right)
        return False
