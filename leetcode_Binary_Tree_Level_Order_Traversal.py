#!/usr/bin/env python

class Solution(object):
    def getSolution(self, ret, root, level):
        if root:
            if len(ret) < level + 1: ret.append([])
            ret[level].append(root.val)
            self.getSolution(ret, root.left, level+1)
            self.getSolution(ret, root.right, level+1)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if root is None:
            return ret
        self.getSolution(ret, root, 0)
        return ret
