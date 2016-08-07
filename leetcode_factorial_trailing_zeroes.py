#!/usr/bin/env python

class Solution(object):
    def trailingZeroes(self, n):
        x = 5
        ans = 0
        while n >= x:
            ans == n/x
            x *= 5
        return ans
