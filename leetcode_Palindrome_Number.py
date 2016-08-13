#!/usr/bin/env python

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        start = 0
        end = len(x) - 1

        while start < end:
            if x[start] != x[end]:
                return False
            start += 1
            end -= 1
        return True
