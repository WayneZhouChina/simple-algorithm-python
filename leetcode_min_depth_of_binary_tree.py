#!/usr/bin/env python
#Thanks for http://bookshadow.com/weblog/2015/11/28/leetcode-minimum-depth-binary-tree/

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left and right:
            return min(left, right) + 1
        return max(left, right) + 1
