#!/usr/bin/env python

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        if root is None:
            return True
        if abs(self.height(root.left) - self.height(root.right)) <= 1:
            return self.isBalance(root.left) and self.isBalance(root.right)

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1
