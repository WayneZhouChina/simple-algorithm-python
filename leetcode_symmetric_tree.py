#!/usr/bin/env python

#class TreeNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSymmetricTree(root.left, root.right)

    def isSymmetricTree(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        return (p.val == q.val) and self.isSymmetricTree(p.left, q.right) and self.isSymmetricTree(p.right, q.left)
